#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 05:58:39 2020

@author: rrolison
"""


def gfn(fi, ln, mn=''):
    """Return a full name, neatly formatted"""
    if mn:
        fn = f"{fi} {mn} {ln}"
    else:
        fn = f"{fi} {ln}"
    return fn.title()


m = gfn('jimi', 'hendrix')
print(m)
m = gfn('john', 'hooker', 'lee')
print(m)
