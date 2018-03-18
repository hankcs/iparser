# -*- coding:utf-8 -*-
# Filename: test_tagger.py
# Author：hankcs
# Date: 2018-03-03 下午8:43
from iparser.tagger.pos_tagger import POSTagger

postagger = POSTagger('data/ctb/pos/config.ini')
postagger.train()
postagger.load()
postagger.evaluate()
print(postagger.tag('教授 在 教授 自然 语言 处理'.split()))
