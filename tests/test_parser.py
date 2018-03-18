# -*- coding:utf-8 -*-
# Filename: train_parser.py
# Author：hankcs
# Date: 2018-02-28 12:04
import argparse
from os.path import isfile

from iparser import PTB_DEP, CTB_DEP
from iparser.parser.common import eprint
from iparser.parser.dep_parser import DepParser

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config_file', default='result/ctb/dep/config.ini')
    args, extra_args = arg_parser.parse_known_args()
    parser = DepParser(args.config_file, extra_args)
    parser.load()
    parser.evaluate()
    # sentence = [('Is', 'VBZ'), ('this', 'DT'), ('the', 'DT'), ('future', 'NN'), ('of', 'IN'), ('chamber', 'NN'),
    #             ('music', 'NN'), ('?', '.')]
    # print(parser.parse(sentence))
