#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:27:13 2020

@author: rrolison
"""
# Using break to exit a loop
pr = "\nPlease enter the name of a city you have visited:"
pr += "\n(Enter 'quit' when you are finished.) "

while True:
    c = input(pr)
    if c == 'quit':
        break
    else:
        print(f"I would live to go to {c.title()}.")
