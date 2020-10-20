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

# Pets Function call


def dp(at, pn):
    """Display information about a pet"""
    print(f"\nI have a {at}.")
    print(f"My {at}'s name is {pn.title()}.")


dp('python', 'kaa')
dp('dog', 'snoopy')
