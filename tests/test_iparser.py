# -*- coding:utf-8 -*-
# Filename: test_iparser.py
# Author：hankcs
# Date: 2018-03-01 22:27
from iparser import *

iparser = IParser(seg_config_file=CTB_SEG, pos_config_file=CTB_POS, dep_config_file=CTB_DEP)
print(iparser.parse('咬死猎人的狗'))
