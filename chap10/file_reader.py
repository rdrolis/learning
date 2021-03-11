#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:48:34 2021

@author: rrolison
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

fn = 'pi_digits.txt'

with open(fn) as fo:
    for li in fo:
        print(li.rstrip())

with open(fn) as fo:
    lines = fo.readlines()

for ln in lines:
    print(ln.rstrip())
