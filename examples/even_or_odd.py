#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:15:40 2020

@author: rrolison
"""

n = input("Enter a number and I will tell you if it is even or odd: ")
n = int(n)
if n % 2 == 0:
    print(f"The number {n} is even.")
else:
    print(f"The number {n} is odd.")
