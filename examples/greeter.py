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
