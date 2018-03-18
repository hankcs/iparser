# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 13:34
import argparse

import sys

import re

from iparser import *
from iparser.iparser import IParser
from iparser.parser.common import eprint
from iparser.tagger.segmenter import Segmenter


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    arg_parser = argparse.ArgumentParser(description='A Prototype of Industrial Strength Dependency Parsing System')
    task_parser = arg_parser.add_subparsers(dest="task", help='which task to perform?')
    segment_parser = task_parser.add_parser(name='segment', help='word segmentation')
    tag_parser = task_parser.add_parser(name='tag', help='part-of-speech tagging')
    parse_parser = task_parser.add_parser(name='parse', help='dependency parsing')
    server_parser = task_parser.add_parser(name='serve', help='http server', description='A http server for IParser')
    server_parser.add_argument('--port', type=int, default=8666)

    def add_args(p, config=None, lang=True):
        p.add_argument("--config", default=config, required=config is None,
                       help='path to config file')
        p.add_argument("--action", dest="action", default='predict',
                       help='Which action (train, test, predict)?')
        if lang:
            p.add_argument("--language", dest="language", default='en',
                           help='Which language (en, cn)? Use en for English, cn for Chinese')

    add_args(segment_parser, CTB_SEG, False)
    add_args(tag_parser, config=PTB_POS)
    add_args(parse_parser, config=PTB_POS + ';' + PTB_DEP)
    args = arg_parser.parse_args()

    def die(msg):
        eprint(msg)
        exit(1)

    if args.task == 'segment':
        segmenter = Segmenter(args.config)
        if args.action == 'train':
            segmenter.train()
            segmenter.load()
            segmenter.evaluate()
        elif args.action == 'test':
            segmenter.load()
            segmenter.evaluate()
        elif args.action == 'predict':
            segmenter.load()
            for line in sys.stdin:
                line = line.strip()
                print(' '.join(segmenter.segment(line)))
        else:
            die('Invalid action: ' + args.action)
    elif args.task == 'tag':
        if args.action == 'train':
            postagger = POSTagger(args.config)
            postagger.train()
            postagger.load()
            postagger.evaluate()
        elif args.action == 'test':
            postagger = POSTagger(args.config)
            postagger.load()
            postagger.evaluate()
        elif args.action == 'predict':
            if args.language == 'en':
                parser = IParser(pos_config_file=args.config)
            elif args.language == 'cn':
                configs = re.split('[;:]', args.config)
                if len(configs) == 1:
                    seg_config = CTB_SEG
                    pos_config = configs[0]
                elif len(configs) == 2:
                    seg_config, pos_config = configs[0], configs[1]
                else:
                    die('Expected only 1 or 2 configs')
                parser = IParser(seg_config_file=seg_config, pos_config_file=pos_config)
            for line in sys.stdin:
                line = line.strip()
                print(' '.join(word + '/' + tag for (word, tag) in parser.tag(line)))
    elif args.task == 'parse':
        if args.action == 'train':
            parser = DepParser(args.config)
            parser.train()
            parser.load()
            parser.evaluate()
        elif args.action == 'test':
            parser = DepParser(args.config)
            parser.load()
            parser.evaluate()
        elif args.action == 'predict':
            configs = re.split('[;:]', args.config)
            if len(configs) == 1:
                seg_config = CTB_SEG if args.language == 'cn' else None
                pos_config = CTB_POS if args.language == 'cn' else PTB_POS
                dep_config = configs[0]
            elif len(configs) == 2:
                seg_config = CTB_SEG if args.language == 'cn' else None
                pos_config = configs[0]
                dep_config = configs[1]
            elif len(configs) == 3:
                seg_config = configs[0]
                pos_config = configs[1]
                dep_config = configs[2]
            else:
                die('Expected only 1~3 configs')

            parser = IParser(seg_config_file=seg_config, pos_config_file=pos_config, dep_config_file=dep_config)
            for line in sys.stdin:
                line = line.strip()
                print(parser.parse(line))
    elif args.task == 'serve':
        from iparser import server
        server.run(port=args.port)


if __name__ == '__main__':
    main()
