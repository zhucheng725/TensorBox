import os
import json
import subprocess

from model_lift import TensorBox

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', required=True)
    parser.add_argument('--expname', default='')
    val_json = '/media/kirito/1T/procedure/TensorBox/data/testdata/val_boxes_ratation.json'
    parser.add_argument('--gpu', default=0)
    parser.add_argument('--logdir', default='output')
    parser.add_argument('--iou_threshold', default=0.9, type=float)
    parser.add_argument('--tau', default=0.1, type=float)
    parser.add_argument('--min_conf', default=0.98, type=float)
    parser.add_argument('--show_suppressed', default=False, type=bool)
    args = parser.parse_args()
    os.environ['CUDA_VISIBLE_DEVICES'] = str(args.gpu)
    hypes_file = '%s/hypes.json' % os.path.dirname(args.weights)
    with open(hypes_file, 'r') as f:
        H = json.load(f)
    expname = args.expname + '_' if args.expname else ''

    tensorbox = TensorBox(H)
    rect_count = tensorbox.eval(args.weights,
                                                  val_json,
                                                  args.min_conf,
                                                  args.tau,
                                                  args.show_suppressed,
                                                  expname)

    print('-----------------------------finished----------------------------------')

if __name__ == '__main__':
    main()
