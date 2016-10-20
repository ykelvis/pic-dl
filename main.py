#!/usr/bin/env python3

import sys
import getopt
import logging
from importlib import import_module
from known_sites import SITES
from utils import *

def main(url):
    global proxy
    if 'http' not in url:
        url = 'http://' + url
    for k in SITES.keys():
        if k in url:
            lib_path = 'dl-lib.' + SITES[k]
            m = import_module(lib_path)
            web_page = r_get(url, proxies=proxy).text
            ret = m.return_dic(web_page)
            try:
                assert ret['pics'] != []
                downloader(ret, proxies=proxy)
            except AssertionError:
                log.error('No Link Found, {}'.format(url))
                raise LibError('No link found.')
            finally:
                return 0
    log.warning('Not supported site. {}'.format(url))
    return 0

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

    for k, v in opts:
        if k == '-x' or k == '--proxy':
            proxy = v
        elif k == '-h' or k == '--help':
            print(help_message)
            sys.exit(0)
        elif k == '-v' or k == '--verbose':
            log.setLevel('DEBUG')

    for i in args:
        main(i)
