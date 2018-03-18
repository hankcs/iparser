# -*- coding:utf-8 -*-
# Filename: train_parser.py
# Author：hankcs
# Date: 2018-02-28 12:04
import argparse
from os.path import isfile

import numpy as np

from iparser.parser.dep_parser import DepParser
from iparser.parser.common import eprint

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config_file', default='data/ctb/dep/config-subword.ini')
    args, extra_args = arg_parser.parse_known_args()
    if not isfile(args.config_file):
        eprint('%s not exist' % args.config_file)
        exit(1)
    parser = DepParser(args.config_file, extra_args).train()
    parser.evaluate()
    # parser._parser.save(parser._config.save_model_path)
