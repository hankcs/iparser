# -*- coding:utf-8 -*-
# Filename: server.py
# Author：hankcs
# Date: 2018-03-03 下午9:47

"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse, quote

import argparse

from iparser.iparser import IParser
from iparser.static import INDEX_HTML, PTB_POS, PTB_DEP, CTB_DEP, CTB_POS, CTB_SEG

SENTENCE = 'sentence'
TEMPLATE = 'Error'
with open(INDEX_HTML) as src:
    TEMPLATE = src.read()
print('Loading PTB models...')
en_parser = IParser(pos_config_file=PTB_POS, dep_config_file=PTB_DEP)
print('Loading CTB models...')
cn_parser = IParser(seg_config_file=CTB_SEG, pos_config_file=CTB_POS, dep_config_file=CTB_DEP)


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def write(self, text: str):
        self.wfile.write(text.encode())

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        self._set_headers()
        # {'text': ['I looove iparser!']}
        sentence = 'I looove iparser!'
        if SENTENCE in params:
            s = params[SENTENCE]
            if len(s):
                sentence = s[0].strip()
        MAX_LENGTH = 200
        if len(sentence) > MAX_LENGTH:
            sentence = sentence[:MAX_LENGTH]
        parser = cn_parser if len(re.findall('[\u4e00-\u9fff]+', sentence)) > 0 else en_parser
        conll = quote(parser.parse(sentence).__str__())
        self.write(TEMPLATE.replace('{SENTENCE}', sentence).replace('{CONLL}', conll))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.write("<html><body><h1>POST!</h1></body></html>")


def run(server_class=HTTPServer, handler_class=S, port=8666):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Serving http://localhost:{}?sentence=I+looove+iparser%21'.format(port))
    httpd.serve_forever()