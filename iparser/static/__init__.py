# -*- coding:utf-8 -*-
# Filename: __init__.py.py
# Author：hankcs
# Date: 2018-03-04 下午4:08
from iparsermodels import *

STATIC_PACKAGE = 'iparser/static'
STATIC_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(STATIC_ROOT))
INDEX_HTML = os.path.join(STATIC_ROOT, 'index.html')


if __name__ == '__main__':
    print(PROJECT_ROOT)
    print(STATIC_ROOT)
    print(PTB_POS)
