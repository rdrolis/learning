#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:02:32 2020

@author: rrolison
"""

# Write a pizza order taking program

import time
import sys

restart = True


def exit():
    print(f"Thank you {cu.title()}, please visit is again soon.")
    sys.exit()


print("Welcome to Ray's Pizza Den. Please enter your order using our \
automated system and we will be happy to serve you.")
c = input("\nPlease give us your name for your order. \
Type 'q' at anytime to quit: ")
if c == 'q':
    print("Thank you. Please visit us again soon.")
    sys.exit()
else:
    print(f"\nThank you {c.title()}. Please continue with your order: ")

while restart:
    toppings = []
    pizza = []
    uatop = ['anchovy', 'anchovies', 'pineapple', 'artichoke hearts',
             'artichoke heart']
    sa = ['ragu', 'pesto', 'alfredo']
    cr = ['pan', 'thin', 'hand tossed']

    def mp(pizza, toppings):
        sauce = pizza[3]
        crust = pizza[2]
        size = pizza[1]
        cust = pizza[0]
        print(f"\n{cust.title()}, you have ordered a {size} pizza with \
{crust} crust and {sauce} sauce and the following toppings:\n")
        for to in toppings:
            print(f"-{to}")

    pizza.append(c)
    cu = pizza[0]

# Find out pizza size

    si = ['medium', 'large']

    print("\nWhat size pizza would you like? You may choose from the \
following: ")
    for sz in si:
        print(f"-{sz}")
    while True:
        size = input("Size:  ")
        if size == 'q':
            exit()
        elif size in si:
            print(f"You have chosen a {size} pizza. Please continue.")
            break
        else:
            print(f"We're sorry. {size.title()} pizzas are not available. \
Please select from the available options.")

    pizza.append(size)

# Ask type of crust

    print("\nWhat type of crust would you like? \
You may choose from the following: ")
    for c in cr:
        print(f"-{c}")
    while True:
        crust = input("Crust: ")
        if crust == 'q':
            exit()
        elif crust in cr:
            print(f"You have chosen a {crust} crust pizza. Please continue:")
            break
        else:
            print(f"We're sorry. {crust.title()} crust is currently not \
available. Please select from the available options.")
    pizza.append(crust)

# Type of sauce

    print("\nWhat type of sauce would you like? \
You may choose from the following: ")
    for s in sa:
        print(f"-{s}")
    while True:
        sauce = input("Sauce: ")
        if sauce == 'q':
            exit()
        elif sauce in sa:
            print(f"You have chosen {sauce} sauce. Please continue:")
            break
        else:
            print(f"We're sorry. {sauce} sauce is currently not available. \
Please select from the available options.")

    pizza.append(sauce)

# Get toppings
    active = True
    while active:
        t = input("Please enter your toppings. Type 'q' when finished: ")
        if t == 'q':
            active = False
        elif t in uatop:
            print(f"Oops. We are currently out of {t}.")
        else:
            toppings.append(t)
# Summarize and print order

    print("\nPlease wait while we summarize your order...")
    time.sleep(3)

    mp(pizza[:], toppings)

    summ = input("Is your order correct? (y/n) ")

    if summ == 'n':
        print(f"No problem {cu.title()}, please reenter your order.")
    else:
        print("\nThank you {cu.title()} for your order. We will have it ready\
shortly.")
        restart = False
