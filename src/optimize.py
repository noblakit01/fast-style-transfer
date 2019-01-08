from __future__ import print_function
import functools
import vgg, pdb, time
import tensorflow as tf, numpy as np, os
import transform
from utils import get_img

STYLE_LAYERS = ('relu1_1', 'relu2_1', 'relu3_1', 'relu4_1', 'relu5_1')
CONTENT_LAYER = 'relu4_2'
DEVICES = 'CUDA_VISIBLE_DEVICES'

# np arr, np arr
def optimize(content_targets, style_target, content_weight, style_weight,
             tv_weight, vgg_path, epochs=2, print_iterations=1000,
             batch_size=4, save_path='saver/fns.ckpt', log_dir='logdirs', slow=False,
             learning_rate=1e-3,
             last_epoch=False, last_iterations=False):
    debug = False         
    if slow:
        batch_size = 1
    mod = len(content_targets) % batch_size
    if mod > 0:
        print("Train set has been trimmed slightly.. %d %d" % (len(content_targets), mod))
        content_targets = content_targets[:-mod] 

    style_features = {}

    batch_shape = (batch_size,256,256,3)
    style_shape = (1,) + style_target.shape
    print(style_shape)
    
    # precompute style features
    with tf.Graph().as_default(), tf.device('/cpu:0'), tf.Session() as sess:
        style_image = tf.placeholder(tf.float32, shape=style_shape, name='style_image')
        style_image_pre = vgg.preprocess(style_image)
        net = vgg.net(vgg_path, style_image_pre)
        style_pre = np.array([style_target])
        for layer in STYLE_LAYERS:
            features = net[layer].eval(feed_dict={style_image:style_pre})
            features = np.reshape(features, (-1, features.shape[3]))
            gram = np.matmul(features.T, features) / features.size
            style_features[layer] = gram

    with tf.Graph().as_default(), tf.Session() as sess:
        X_content = tf.placeholder(tf.float32, shape=batch_shape, name="X_content")
        X_pre = vgg.preprocess(X_content)

        # precompute content features
        content_features = {}
        content_net = vgg.net(vgg_path, X_pre)
        content_features[CONTENT_LAYER] = content_net[CONTENT_LAYER]

        if slow:
            preds = tf.Variable(
                tf.random_normal(X_content.get_shape()) * 0.256
            )
            preds_pre = preds
        else:
            preds = transform.net(X_content/255.0)
            preds_pre = vgg.preprocess(preds)

        net = vgg.net(vgg_path, preds_pre)

        content_size = _tensor_size(content_features[CONTENT_LAYER])*batch_size
        assert _tensor_size(content_features[CONTENT_LAYER]) == _tensor_size(net[CONTENT_LAYER])
        content_loss = content_weight * (2 * tf.nn.l2_loss(
            net[CONTENT_LAYER] - content_features[CONTENT_LAYER]) / content_size
        )

        style_losses = []
        for style_layer in STYLE_LAYERS:
            layer = net[style_layer]
            bs, height, width, filters = map(lambda i:i.value,layer.get_shape())
            size = height * width * filters
            feats = tf.reshape(layer, (bs, height * width, filters))
            feats_T = tf.transpose(feats, perm=[0,2,1])
            grams = tf.matmul(feats_T, feats) / size
            style_gram = style_features[style_layer]
            style_losses.append(2 * tf.nn.l2_loss(grams - style_gram)/style_gram.size)

        style_loss = style_weight * functools.reduce(tf.add, style_losses) / batch_size

        # total variation denoising
        tv_y_size = _tensor_size(preds[:,1:,:,:])
        tv_x_size = _tensor_size(preds[:,:,1:,:])
        y_tv = tf.nn.l2_loss(preds[:,1:,:,:] - preds[:,:batch_shape[1]-1,:,:])
        x_tv = tf.nn.l2_loss(preds[:,:,1:,:] - preds[:,:,:batch_shape[2]-1,:])
        tv_loss = tv_weight*2*(x_tv/tv_x_size + y_tv/tv_y_size)/batch_size
        
        # overall loss
        loss = content_loss + style_loss + tv_loss

        # add summary for each loss
        tf.summary.scalar('content_loss', content_loss)
        tf.summary.scalar('style_loss', style_loss)
        tf.summary.scalar('tv_loss', tv_loss)
        tf.summary.scalar('total_loss', loss)

        global_step = tf.train.get_or_create_global_step()
        trainable_variables = tf.trainable_variables()
        grads = tf.gradients(loss, trainable_variables)

        optimizer = tf.train.AdamOptimizer(learning_rate)
        train_op = optimizer.apply_gradients(zip(grads, trainable_variables), global_step=global_step, name='train_step')

        merged_summary_op = tf.summary.merge_all()
        summary_writer = tf.summary.FileWriter(log_dir, graph=tf.get_default_graph())

        sess.run(tf.global_variables_initializer())
        
        saver = tf.train.Saver()
        checkpoint_exists = True

        try:
            ckpt_state = tf.train.get_checkpoint_state(save_path)
        except tf.errors.OutOfRangeError as e:
            print('Cannot restore checkpoint: %s' % e)
            checkpoint_exists = False
        if not (ckpt_state and ckpt_state.model_checkpoint_path):
            print('No model to restore at %s' % save_path)
            checkpoint_exists = False

        if checkpoint_exists:
            print('Loading checkpoint %s' % ckpt_state.model_checkpoint_path)
            tf.logging.info('Loading checkpoint %s' % ckpt_state.model_checkpoint_path)
            saver.restore(sess, ckpt_state.model_checkpoint_path)

        num_examples = len(content_targets)

        if checkpoint_exists:
            iterations = sess.run(global_step)
            epoch = (iterations * batch_size) // num_examples
            iterations = iterations - epoch * (num_examples // batch_size)
        else:
            epoch = 0
            iterations = 0

        import random
        uid = random.randint(1, 100)

        print('UID: %s' % uid)
        print('EPOCH: %s / %s' % (epoch, epochs))
        print('content_weight : %g, style_weight : %g, tv_weight: %g'
              % (content_weight, style_weight, tv_weight))

        while epoch < epochs:
            print('Start Epoch: %d iterations: %d' % (epoch, iterations))
            while iterations * batch_size < num_examples:
                start_time = time.time()
                curr = iterations * batch_size
                step = curr + batch_size
                
                X_batch = np.zeros(batch_shape, dtype=np.float32)
                #print('epoch: %d cur: %d step %d' % (epoch, curr, step))
                for j, img_p in enumerate(content_targets[curr:step]):
                   X_batch[j] = get_img(img_p).astype(np.float32)

                iterations += 1
                assert X_batch.shape[0] == batch_size

                train_feed_dict = {
                   X_content:X_batch
                }

                _, summary, L_total, L_content, L_style, L_tv, step = sess.run(
                    [train_op, merged_summary_op, loss, content_loss, style_loss, tv_loss, global_step],
                    feed_dict=train_feed_dict)
                print('epoch : %d, iter : %4d,' % (epoch, step),
                      'L_total : %g, L_content : %g, L_style : %g, L_tv : %g'
                      % (L_total, L_content, L_style, L_tv))

                summary_writer.add_summary(summary, iterations)
                
                end_time = time.time()
                delta_time = end_time - start_time

                if debug:
                    print("UID: %s, batch time: %s" % (uid, delta_time))
                
                is_last_iteration = iterations * batch_size >= num_examples
                is_print_iter = int(iterations) % print_iterations == 0 or is_last_iteration
                if slow:
                    is_print_iter = epoch % print_iterations == 0
                is_last = epoch == epochs - 1 and is_last_iteration
                should_print = is_print_iter or is_last
                if should_print:
                    to_get = [style_loss, content_loss, tv_loss, loss, preds]
                    test_feed_dict = {
                       X_content:X_batch
                    }

                    tup = sess.run(to_get, feed_dict = test_feed_dict)
                    _style_loss,_content_loss,_tv_loss,_loss,_preds = tup
                    losses = (_style_loss, _content_loss, _tv_loss, _loss)
                    if slow:
                       _preds = vgg.unprocess(_preds)
                    else:
                       if is_last:
                           saver = tf.train.Saver(write_version=tf.train.SaverDef.V1)
                           saver.save(sess, save_path + '/fns.ckpt')
                           print('saved path %s' % save_path)
                       # New version tf.train.Saver will not save physical file .ckpt anymore, instead
                       # it will save a checkpoint files.
                       # we can saved and restore 
                       # https://www.tensorflow.org/guide/saved_model
                       # or convert to pb:
                       # https://github.com/lengstrom/fast-style-transfer/issues/96
                       #
                       # If you want one, use 
                       # saver = tf.train.Saver(write_version=tf.train.SaverDef.V1)
                       # 
                       saver.save(sess, save_path + '/fns.ckpt')
                       print('saved epoch: %d iterations: %d step: %d' % (epoch, iterations, step))
                    yield(_preds, losses, iterations, epoch)

            iterations = 0
            epoch += 1

def _tensor_size(tensor):
    from operator import mul
    return functools.reduce(mul, (d.value for d in tensor.get_shape()[1:]), 1)
