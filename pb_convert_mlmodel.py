from __future__ import print_function
import sys
sys.path.insert(0, 'src')
import tfcoreml as tf_converter
from argparse import ArgumentParser
from utils import exists

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--pb-output', type=str,
                        dest='pb_output',
                        help='pb output name',
                        metavar='PB_OUTPUT', required=True)

    return parser

##def check_opts(opts):

def main():
    parser = build_parser()
    opts = parser.parse_args()
    #check_opts(opts)

    tf_converter.convert(tf_model_path = '../models/pb/' + opts.pb_output + '.pb',
                     mlmodel_path = '../models/mlmodel/temp.mlmodel',
                     output_feature_names = ['add_37:0'],
                     ## Note found this after running a conversion the first time
                     image_input_names = ['outputImage'])

if __name__ == '__main__':
    main()
