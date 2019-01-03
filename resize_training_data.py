import sys, os
sys.path.insert(0, 'src')
from argparse import ArgumentParser
from utils import save_img, get_img, exists, list_files

TRAIN_PATH = 'data/bin/train2014/train2014'
RESULT_PATH = 'data/train2014'

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--train-path', type=str,
                        dest='train_path', help='path to training images folder',
                        metavar='TRAIN_PATH', default=TRAIN_PATH)

    parser.add_argument('--result-path', type=str,
                        dest='result_path', help='path to saved training images folder',
                        metavar='RESULT_PATH', default=RESULT_PATH)

    return parser

def check_opts(opts):
    exists(opts.train_path, "train path not found!")
    exists(opts.result_path, "result path not found!")

def main():
    parser = build_parser()
    options = parser.parse_args()
    check_opts(options)

    files = list_files(options.train_path) 
    print('hihi')
    for x in files:
        in_path = os.path.join(options.train_path, x)
        out_path = os.path.join(options.result_path, x)
        img = get_img(in_path, (256,256,3))
        save_img(out_path, img)

if __name__ == '__main__':
    main()