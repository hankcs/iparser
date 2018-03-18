# -*- coding:utf-8 -*-
# Filename: iparser.py
# Author：hankcs
# Date: 2018-03-01 21:47
from iparser.parser.common import eprint, ConllSentence
from iparser.parser.dep_parser import DepParser
from iparser.tagger.pos_tagger import POSTagger
from iparser.tagger.segmenter import Segmenter


class IParser(object):
    def __init__(self, seg_config_file=None, pos_config_file=None, dep_config_file=None) -> None:
        super().__init__()
        if seg_config_file:
            self._segmenter = Segmenter(seg_config_file).load()
        else:
            try:
                from segtok.tokenizer import word_tokenizer
                class EnglishSegmenter(object):
                    def segment(self, sentence):
                        return word_tokenizer(sentence)

                self._segmenter = EnglishSegmenter()
            except ImportError:
                class BlankSegmenter(object):
                    def segment(self, sentence: str):
                        return sentence.split()

                self._segmenter = BlankSegmenter()

                eprint('No segmenter available, fallback to str.split. You can try a better segmenter like:\n'
                       'pip3 install segtok')
        self._postagger = POSTagger(pos_config_file).load() if pos_config_file else None
        self._depparser = DepParser(dep_config_file).load() if dep_config_file else None

    def segment(self, sentence: str) -> list:
        return self._segmenter.segment(sentence)

    def tag(self, sentence: str or list) -> list:
        if type(sentence) is str:
            sentence = self._segmenter.segment(sentence)
        return self._postagger.tag(sentence)

    def parse(self, sentence: str or list) -> ConllSentence:
        if type(sentence) is str:
            words = self._segmenter.segment(sentence)
            tags = self._postagger.tag(words, ret_tulple=False)
            sentence = [(word, tag) for word, tag in zip(words, tags)]
        return self._depparser.parse(sentence)
