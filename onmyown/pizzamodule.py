#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:00:55 2020

@author: rrolison
"""


def start():
    print("Welcome to Ray's Pizza Den. Please enter your order using our \
automated system and we will be happy to serve you.")


def mp(pizza, toppings):
    sauce = pizza[3]
    crust = pizza[2]
    size = pizza[1]
    cust = pizza[0]
    print(f"\n{cust.title()}, you have ordered a {size} pizza with \
{crust} crust and {sauce} sauce and the following toppings:\n")
    for to in toppings:
        print(f"-{to}")
