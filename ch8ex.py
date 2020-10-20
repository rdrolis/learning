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
