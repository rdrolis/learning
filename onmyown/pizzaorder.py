#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:02:32 2020

@author: rrolison
"""

# Write a pizza order taking program

import time
import sys
from pizzamodule import mp
from pizzamodule import start

restart = True


def exit():
    print(f"Thank you {cu.title()}, please visit is again soon.")
    sys.exit()


start()

cu = input("\nPlease give us your name for your order. \
Type 'q' at anytime to quit: ")
if cu == 'q':
    print("Thank you. Please visit us again soon.")
    sys.exit()
else:
    print(f"\nThank you {cu.title()}. Please continue with your order: ")


while restart:
    toppings = []
    pizza = []
    uatop = ['anchovy', 'anchovies', 'pineapple', 'artichoke hearts',
             'artichoke heart']
    sa = ['ragu', 'pesto', 'alfredo']
    cr = ['pan', 'thin', 'hand tossed']

    pizza.append(cu)

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
    for r in cr:
        print(f"-{r}")
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
            print(f"We're sorry. {sauce.title()} sauce is currently not \
available. Please select from the available options.")

    pizza.append(sauce)

# Get toppings
    active = True
    while active:
        t = input("Please enter a topping and hit 'Enter'. Type 'q' when \
finished: ")
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
        print(f"\nThank you {cu.title()} for your order. We will have it ready\
 shortly.")
        restart = False
