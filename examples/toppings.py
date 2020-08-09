#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:43:23 2020

@author: rdrolis
"""

r_top = 'mushrooms'
if r_top != 'anchovies':
    print("Hold the Anchovies!")
# Doesn't work doesn't test all conditions
r_top = ['mushrooms', 'extra cheese']
if 'mushrooms' in r_top:
    print("\nAdding mushrooms.")
elif 'pepperoni' in r_top:
    print("Adding pepperoni.")
elif 'extra cheese' in r_top:
    print("Adding extra cheese.")
print("Finished making your pizza.")
#Tests all conditions
if 'mushrooms' in r_top:
    print("\nAdding mushrooms.")
if 'pepperoni' in r_top:
    print("Adding pepperoni.")
if 'extra cheese' in r_top:
    print("Adding extra cheese.")
print("Finished making your pizza.")