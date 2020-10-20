#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:14:36 2020

@author: rrolison
"""

# Exercise 8-1 Display Message


def m():
    """Define Message"""
    print("Python is not really hard to learn.")


m()

# Exercise 8-2 Favorite Book


def b(book):
    """Function message using parameter"""
    print(f"\n{book.title()} is one of my favorite books.")


b('treasure island')
b('without remorse')
b('hunt for red october')

# Exercise 8-3 T-Shirt/ 8-4 Large Shirt


def ts(m, s='large'):
    """T-Shirt Orders"""
    print(f"A {s} t-shirt was ordered with the following slogan \
          '{m.title()}'.")


ts('trump 2020')
ts('I love Python', 'medium')
ts('I love Python')
print()

# Exercise 8-5 Cities


def dc(c, co='united states'):
    """Describe a city"""
    print(f"{c.title()} is located in {co.title()}.")


dc('houston')
dc('nashville')
dc('busan', 'south korea')
