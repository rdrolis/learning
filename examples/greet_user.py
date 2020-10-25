#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:25:08 2020

@author: rrolison
"""


def gu(names):
    """Print a simple greeting to each user in a list."""
    for n in names:
        m = f"Hello, {n.title()}."
        print(m)


unames = ['hannah', 'ty', 'margot']
gu(unames)
