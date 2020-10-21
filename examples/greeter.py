#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:02:25 2020

@author: rrolison
"""

n = input("Please enter your name: ")
print(f"\n Hello, {n.title()}.")
print()
pr = "If you tell us who you are, we can peronalize the messages you see."
pr += "\nWhat is your first name? "
n = input(pr)
print(f"Hello, {n.title()}.")
print()
# Chapter 8 using functions


def greet_user():
    """Display a simple greeting"""
    print("Hello.")


greet_user()


def gr_u(username):
    """Greeting using a name"""
    print(f"\nHello, {username.title()}!")


gr_u('george')


def gfn(fi, ln):
    """Return a full name, neatly formatted"""
    fn = f"{fi} {ln}"
    return fn.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    first = input("First name: ")
    if first == 'q':
        break
    last = input("Last name: ")
    if last == 'q':
        break

    form = gfn(first, last)
    print(f"Hello, {form}!")
