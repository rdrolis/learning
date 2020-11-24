#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:05:31 2020

@author: rdrolis
"""

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for t in toppings:
        print(f"-{t}")