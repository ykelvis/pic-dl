#!/usr/local/bin/python3
import sys
from importlib import import_module
from known_sites import SITES
from utils import *

def main(l):
    if 'http' not in l:
        l = 'http://' + l
    for k in SITES.keys():
        if k in l:
            lib_path = 'dl-lib.' + SITES[k]
            m = import_module(lib_path)
            a = r_get(l).text
            print(m.return_dic(a))
            d = m.return_dic(a)
            try:
                assert d['pics'] != []
                downloader(d)
            except AssertionError:
                raise LibError('No link found.')

if __name__ == '__main__':
    main(sys.argv[1])
