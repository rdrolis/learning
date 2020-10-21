#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 06:14:52 2020

@author: rrolison
"""


def bp(fn, ln, a=None):
    """Return a dictionary of information about a person"""
    p = {'first': fn, 'last': ln}
    if a:
        p['age'] = a
    return p


m = bp('jimi', 'hendrix', a=27)
print(m)
