# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 21:14
import argparse

__requires__ = 'iparser==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='A http server for IParser')
    arg_parser.add_argument('--port', type=int, default=8666)
    args = arg_parser.parse_args()
