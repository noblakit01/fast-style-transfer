# Convert ckpt models to pb models

## Requirements

* Python:
   * 2.7.10 (verified on MacOS 10.14.2)
* Tensorflow: 
   * 1.5.0 (verified on MacOS 10.14.2)
* Pillow:
   * 3.4.2 (verified on MacOS 10.14.2)
* scipy:
   * 0.18.1 (verified on MacOS 10.14.2)
* numpy:
   * 1.15.4 (verified on MacOS 10.14.2)
* moviepy:
   * 0.2.3.5 (verified on MacOS 10.14.2)

## Conversion

Simple run
```
python ckpt_to_pb.py --checkpoint path/to/ckpt --in-path "path/to/test/input.jpg" --out-path "path/to/test/output.jpg" --device "/cpu:0" --batch-size 1
```

## Source code

Main source code used to convert ckpt to pb in [ckpt_to_pb.py](./ckpt_to_pb.py)

## Explanation

**Step 1:** The first step is to figure out the name of the output node for our graph; TensorFlow auto-generates this when not explicitly set. We can get it by printing the net in the `ckpt_to_pb.py` script.
```python
# function ffwd,line 93
preds = transform.net(img_placeholder)
preds_name = preds.name
b = preds_name.index(':')
param_name = preds_name[:b]
```

**Step 2** We can save the graph to disk. Note that if you’re using your own models that you’ll need to add the code to satisfy the checkpoints directory condition vs. a single checkpoint file.
```python
# function ffwd, line 98
if os.path.isdir(checkpoint_dir):
    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
        ########## add this for pre-trained models ###########
        a = ckpt.model_checkpoint_path.index('.ckpt')
        pb_name = ckpt.model_checkpoint_path[:a].replace('/ckpt/', '/pb/') + '.pb'
        frozen_graph_def = tf.graph_util.convert_variables_to_constants(sess,sess.graph_def,[param_name])
        with open(pb_name, 'wb') as f:
            f.write(frozen_graph_def.SerializeToString())
        #####################################################
    else:
        raise Exception("No checkpoint found...")
else:
    saver.restore(sess, checkpoint_dir)
    ########## add this for custom models ###########
    a = checkpoint_dir.index('.ckpt')
    pb_name = checkpoint_dir[:a].replace('/ckpt/', '/pb/') + '.pb'
    frozen_graph_def = tf.graph_util.convert_variables_to_constants(sess,sess.graph_def,[param_name])
    with open(pb_name, 'wb') as f:
        f.write(frozen_graph_def.SerializeToString())
    #####################################################
```

