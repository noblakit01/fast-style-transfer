import tensorflow as tf
from argparse import ArgumentParser

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--name', type = str, dest='name',
                        help='name of meta file to load checkpoint from',
                        metavar='NAME', required=True)
    return parser

def main():
    parser = build_parser()
    opts = parser.parse_args()

    meta_path = 'checkpoint/' + opts.name + '.ckpt.meta'
    output_node_names = ['add_37']

    with tf.Session() as sess:
        # Restore the graph
        saver = tf.train.import_meta_graph(meta_path)
        
        # Load weights
        saver.restore(sess, tf.train.latest_checkpoint('checkpoint/'))
        
        # Freeze the graph
        frozen_graph_def = tf.graph_util.convert_variables_to_constants(
            sess,
            sess.graph_def,
            output_node_names)
            
        # Save the frozen graph
        with open('../style-transfer-models/pb/' + opts.name + '.pb', 'wb') as f:
            f.write(frozen_graph_def.SerializeToString())

if __name__ == '__main__':
    main()

