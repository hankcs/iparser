# -*- coding:utf-8 -*-
# Filename: train_segmenter.py
# Author：hankcs
# Date: 2018-03-01 22:28
from iparser.tagger.segmenter import Segmenter

segmenter = Segmenter('data/pku/seg/config.ini')
segmenter.train()
segmenter.load()
segmenter.evaluate()
print(segmenter.segment('商品和服务'))