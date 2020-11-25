#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:29:10 2020

@author: rrolison
"""

from printing_functions import *

# Start with some designs that need to be printed.
up = ['phone case', 'robot pendant', 'dodecahedron']
co = []
# Simulate printing each design
# Move each design to co when finished.

while up:
    cu = up.pop()
    print(f"Printing model: {cu}")
    co.append(cu)

# Display all completed models
print("\nThe following models have been printed:")
for c in co:
    print(c)
print()

# Same routine using functions


ud = ['phone case', 'robot pendant', 'dodecahedron', 'bushing']
cm = []
pm(ud, cm)
scm(cm)
print()

# Do not modify original list
print("Do not modify original list:")
ud = ['phone case', 'robot pendant', 'dodecahedron', 'bushing']
cm = []
pm(ud[:], cm)
scm(cm)
print(ud)
