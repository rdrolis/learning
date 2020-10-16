#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:59:36 2020

@author: rrolison
"""
# while loop
pr = "\nTell me something and I will repeat it back to you."
pr += "\nEnter 'quit' to exit the program. "
m = ""
while m != 'quit':
    m = input(pr)
    if m != 'quit':
        print(m)
# quit test using a flag
a = True
while a:
    m = input(pr)
    if m == 'quit':
        a = False
    else:
        print(m)
