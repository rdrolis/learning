#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:51:44 2020

@author: rrolison
"""

# Arbitrary number of arguments


def make_pizza(*toppings):
    """ Print the list of toppings that have been requested. """
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Add a for loop and print statement


def make_pizza(*toppings):
    """Summarize the pizza order. """
    print("Making a pizza with the following toppings:")
    for t in toppings:
        print(f" -{t}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary argument (arbitrary must go last)


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for t in toppings:
        print(f"-{t}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
