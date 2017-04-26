#!/usr/bin/env python3

__all__ = ['poco_download']

import sys
sys.path.append('../')

from ..utils import r0

def return_dic(p):
    title = r0(r'<title>(.*)<\/title>' ,p)
    title = ''.join(title)
    author = r0(r'<a href=\"\/\">(.*)<\/a>' ,p)
    author = ''.join(author)
    pics = r0(r'originPhoto:\'(http[^\']+)\'',p)
    _pics = []
    for i in pics:
        _pics.append((i.split("?")[0], i.split("?")[0].split("/")[-1]))
    if _pics != []:
        pics = _pics[:]
    return {'title': title, 'author': author, 'pics': pics}

