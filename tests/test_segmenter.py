# -*- coding:utf-8 -*-
# Filename: train_segmenter.py
# Author：hankcs
# Date: 2018-03-01 22:28
from iparser import *

segmenter = Segmenter(CTB_SEG)
segmenter.load()
# segmenter.evaluate()
print(segmenter.segment('下雨天地面积水'))
