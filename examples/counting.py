#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:11:57 2020

@author: rrolison
"""
cn = 1
while cn <= 5:
    print(cn)
    cn += 1
print()
# using continue in a loop
cn = 0
while cn < 10:
    cn += 1
    if cn % 2 == 0:
        continue
    print(cn)
