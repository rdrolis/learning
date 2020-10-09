#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:05:14 2020

@author: rrolison
"""
a = 3
if a < 4:
    print("\nYour admission cost is $0.")
elif a < 18:
    print("\n Your admission cost is $25.")
else:
    print("You admission cost is $40.")
print("\nNew ticket price routine:")
a = 64
if a < 4:
    price = 0
elif a < 18:
    price = 25
elif a < 65:
    price = 40
elif a >= 65:
    price = 20
print(f"\nYour ticket price is ${price}.")
