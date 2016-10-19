#!/usr/local/bin/python3

__all__ = ['lofter_download']

import sys
sys.path.append('../')

from dler import r0

def return_dic(p):
    title = r0(r'<meta name=\"Description\" content=\"(.*)\"\/>',p)
    title = ''.join(title)
    author = r0(r'<a href=\"\/\">(.*)<\/a>',p)
    author = ''.join(author)
    pics = r0(r'bigimgsrc=\"(http:\/\/img\w+\d?[^"]*)\"',p)
    _pics = []
    for i in pics:
        if "?" in i:
            _pics.append(i.split("?")[0])
    if _pics != []:
        pics = _pics[:]
    return {'title': title, 'author': author, 'pics': pics}
