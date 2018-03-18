# -*- coding:utf-8 -*-
# Filename: __init__.py.py
# Author：hankcs
# Date: 2018-02-21 12:54
__version__ = '0.1.0'
from iparser.iparser import IParser
from iparser.tagger.segmenter import Segmenter
from iparser.tagger.pos_tagger import POSTagger
from iparser.parser.dep_parser import DepParser
from iparser.static import PTB_POS, PTB_DEP, CTB_SEG, CTB_POS, CTB_DEP
