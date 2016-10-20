#!/usr/local/bin/python3
import html
import requests
import re

class LibError(Exception):
    pass

proxy = None

fake_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'UTF-8,*;q=0.5',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0'
}

def r0(pattern, text):
    _r = re.findall(pattern, text)
    return _r

def r1(pattern, text):
    _r = re.search(pattern, text)
    return _r

def escape_file_path(path):
    path = path.replace('/', '-')
    path = path.replace('\\', '-')
    path = path.replace('*', '-')
    path = path.replace('?', '-')
    return path

def r_get(link, **kwargs):
    proxy = kwargs.get('proxy',None)
    res = requests.get(link, proxies=proxy, headers=fake_headers)
    return res

def to_url(u):
    u = u.replace('http','')
    u = u.replace('https','')
    u = u.replace('://','')
    return u

def downloader(dic, **kwargs):
    proxy = kwargs.get('proxy',None)
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
    _d = list(set(dic['pics']))
    for i in _d:
        j += 1
        print('downloading {}/{}'.format(j,len(_d)))
        url = i.split('/')[-1]
        path = '{a} - {b} - {c}'.format(a=dic['author'], b=dic['title'], c=url)
        path = escape_file_path(path)
        content = r_get(i,proxy=proxy).content
        with open(path, 'wb') as f:
            f.write(content)
    return 0
