#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 18:09:18 2020

@author: rrolison
"""
p = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(p)
while 'cat' in p:
    p.remove('cat')
print(p)
