# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 14:09
from iparser import *

postagger = POSTagger(PTB_POS)
postagger.load()
# postagger.evaluate()
print(postagger.tag('I looove languages'.split()))