#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:02:32 2020

@author: rrolison
"""

# Write a pizza order taking program
import time


def mp(pizza, toppings):
    sauce = pizza[3]
    crust = pizza[2]
    size = pizza[1]
    cust = pizza[0]
    print(f"\n{cust.title()}, you have ordered a {size} pizza with \
{crust} crust and {sauce} sauce and the following toppings:\n")
    for to in toppings:
        print(f"-{to}")


pizza = []
cr = ['pan', 'thick', 'thin']
sa = ['tomato', 'pesto', 'alfredo']
si = ['medium', 'large']
toppings = []

c = input("Please give me your name for the order. \
           Type 'q' at anytime to quit: ")
if c == 'q':
    raise Exception("Thank you. Please visit us again soon.")
else:
    print(f"\nThank you {c.title()}. Please continue with your order: ")
pizza.append(c)
cu = pizza[0]
# Find out pizza size

print("\nWhat size pizza would you like? You may choose from the following: ")
for sz in si:
    print(f"-{sz}")
size = input("Size:  ")
if size == 'q':
    raise Exception(f"\nThank you {cu.title()}, please visit us again.")
else:
    print(f"You have chosen a {size} pizza. Please continue.")
pizza.append(size)

# Ask type of crust

print("\nWhat type of crust would you like? \
You may choose from the following: ")
for c in cr:
    print(f"-{c}")
crust = input("Crust: ")
if crust == 'q':
    raise Exception(f"\nThank you {cu.title()}, please visit us again.")
else:
    print(f"You have chosen a {crust} crust pizza. Please continue:")
pizza.append(crust)

# Type of sauce

print("\nWhat type of sauce would you like? \
You may choose from the following: ")
for s in sa:
    print(f"-{s}")
sauce = input("Sauce: ")
if sauce == 'q':
    raise Exception(f"\nThank you {cu.title()}, please visit us again.")
else:
    print(f"You have chosen {sauce} sauce. Please continue:")
pizza.append(sauce)

# Get toppings
active = True
while active:
    t = input("Please enter your toppings. Type 'q' when finished: ")
    if t == 'q':
        active = False
    else:
        toppings.append(t)
# Summarize and print order

print("\nPlease wait while we summarize your order...")
time.sleep(5)

mp(pizza[:], toppings)

summ = input("Is your order correct? (y/n) ")

if summ == 'n':
    raise Exception(f"Thank you {cu.title()}, please reenter your order.")
else:
    print("\nThank you for your order. We will have it ready shortly.")
