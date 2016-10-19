#!/usr/local/bin/python3
import sys
import html
import re
import requests
from importlib import import_module

SITES = {
        'tuchong': 'tuchong',
        'lofter': 'lofter'
        }

fake_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0'
}

def escape_file_path(path):
    path = path.replace('/', '-')
    path = path.replace('\\', '-')
    path = path.replace('*', '-')
    path = path.replace('?', '-')
    return path

def downloader(dic):
    dic['author'] = html.unescape(dic['author'])
    dic['title'] = html.unescape(dic['title'])
    '''
        {
            author:
            title:
            pics:[]
                }
    '''
    j = 0
    for i in dic['pics']:
        j += 1
        print('downloading {}/{}'.format(j,len(dic['pics'])))
        url = i.split('/')[-1]
        path = '{a} - {b} - {c}'.format(a=dic['author'], b=dic['title'], c=url)
        path = escape_file_path(path)
        content = requests.get(i,headers=fake_headers).content
        with open(path, 'wb') as f:
            f.write(content)
    return 0

def get_source(link):
    res = requests.get(link,headers=fake_headers).text
    return res

def to_url(u):
    u = u.replace('http','')
    u = u.replace('https','')
    u = u.replace('://','')
    return u

def r1(pattern, text):
    _r = re.search(pattern, text)
    return _r

def r0(pattern, text):
    _r = re.findall(pattern, text)
    return _r

def main(l):
    if 'http' not in l:
        l = 'http://' + l
    for k in SITES.keys():
        if k in l:
            lib_path = 'dl-lib.' + SITES[k]
            m = import_module(lib_path)
            a = get_source(l)
            print(m.return_dic(a))
            downloader(m.return_dic(a))

if __name__ == '__main__':
    main(sys.argv[1])
