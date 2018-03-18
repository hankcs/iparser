# -*- coding:utf-8 -*-
# Filename: test_tagger.py
# Author：hankcs
# Date: 2018-03-03 下午8:43
from iparser import *

postagger = POSTagger(CTB_POS)
postagger.load()
# postagger.evaluate()
print(postagger.tag('教授 在 教授 自然 语言 处理'.split()))
