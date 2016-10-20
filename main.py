#!/usr/local/bin/python3
import sys
import getopt
import logging
from importlib import import_module
from known_sites import SITES
from utils import *

def main(l):
    global proxy
    if 'http' not in l:
        l = 'http://' + l
    for k in SITES.keys():
        if k in l:
            lib_path = 'dl-lib.' + SITES[k]
            m = import_module(lib_path)
            a = r_get(l,proxies=proxy).text
            print(m.return_dic(a))
            d = m.return_dic(a)
            try:
                assert d['pics'] != []
                downloader(d,proxies=proxy)
            except AssertionError:
                log.error('No Link Found')
                raise LibError('No link found.')

help_message = '''Supported sites: {}
Usage:
\t-x|--proxy scheme://host:port
\t-h|--help
'''.format('\n\t' + '\n\t'.join(list(SITES.keys())))

if __name__ == '__main__':
    proxy = None

    logging.basicConfig(format='[%(levelname)s] %(message)s')
    log = logging.getLogger()
    log.setLevel('WARNING')

    short_opts = "Vvhx:"
    opts = ['version', 'proxy=', 'help', 'verbose']

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, opts)
    except getopt.GetoptError as err:
        log.error(err)
        print(help_message)
        sys.exit(2)

    for k,v in opts:
        if k == '-x' or k == '--proxy':
            proxy = v
        elif k == '-h' or k == '--help':
            print(help_message)
            sys.exit(0)
        elif k == '-v' or k == '--verbose':
            log.setLevel('DEBUG')

    for i in args:
        main(i)
