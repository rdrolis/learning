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
# Wrong positional arguments
dp('garfield', 'cat')

# Keyword Arguments in a function
dp(at='rabbit', pn='Bugs Bunny')

# Default Value in function argument


def dp(pn, at="dog"):
    """Display information about a pet"""
    print(f"\nI have a {at}.")
    print(f"My {at}'s name is {pn.title()}.")


dp('happy')
dp(pn='tweety', at='canary')
