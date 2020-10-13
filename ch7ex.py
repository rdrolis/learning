#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:20:49 2020

@author: rrolison
"""

# Exercise 7-1 Rental Car
c = input("What make of car would you like to rent? ")
print(f"Let me see if we have any {c.title()}s available.\n")
# Exercise 7-2 Restaurant Seating
g = input("How many guests are in your party? ")
g = int(g)
if g > 8:
    n = input("What is your first name? ")
    print(f"{n.title()}, please wait while for an available table.")
else:
    print("Your table is ready.")
# Exercise 7-3 Multples of Ten
n = input("Enter a number and I will tell you if it is a multiple of 10: ")
n = int(n)
if n % 10 == 0:
    print(f"The number {n} is a multiple of 10.")
else:
    print(f"The number {n} is not a multiple of ten.")
