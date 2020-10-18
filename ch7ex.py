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
    print(f"{n.title()}, please wait for an available table.")
else:
    print("Your table is ready.")

# Exercise 7-3 Multples of Ten
n = input("Enter a number and I will tell you if it is a multiple of 10: ")
n = int(n)
if n % 10 == 0:
    print(f"The number {n} is a multiple of 10.")
else:
    print(f"The number {n} is not a multiple of ten.")

# Exercise 7-4 Pizza Toppings
pr = "\nPlease enter your topping choices"
pr += "\n When finished adding toppings, type 'quit': "
t = ""
act = True
while act:
    t = input(pr)
    if t == "quit":
        act = False
    else:
        print(f"Adding {t} to your pizza.")

# Exercise 7-5 Movie Tickets
pr = "\nWelcome to Kabuki Theater. Please enter the ages of guests."
pr += "\nTo exit, type 'quit': "
while True:
    a = input(pr)
    if a == 'quit':
        break
    a = int(a)
    if a < 3:
        print(" Your ticket is free.")
    elif a < 13:
        print(" Your ticket is $10.")
    else:
        print(" Your ticket is $15.")

# Exercise 7-6 Three Exits
    # Exit 1: active variable
pr = "\nPlease enter your topping choices"
pr += "\n When finished adding toppings, type 'quit': "
t = ""
act = True
while act:
    t = input(pr)
    if t == "quit":
        act = False
    else:
        print(f"Adding {t} to your pizza.")

        # Exit 2: conditional test in while statement
pr = "\nPlease enter your topping choices"
pr += "\n When finished adding toppings, type 'quit': "
t = ""
while t != 'quit':
    t = input(pr)
    if t != 'quit':
        print(f"Adding {t} to your pizza.")

    # Exit 3 Using a 'break' statement
pr = "\nPlease enter your topping choices"
pr += "\n When finished adding toppings, type 'quit': "
while True:
    t = input(pr)
    if t == 'quit':
        break
    else:
        print(f"Adding {t} to your pizza.")

# Exercise 7-7 Infinite loop
pr = "\nPlease enter your topping choices"
pr += "\n When finished adding toppings, type 'quit': "
t = input(pr)
while t != 'quit':
    print(f"Adding {t} to your pizza.")

# Exercise 7-8 Deli
orders = ['blt', 'bologna', 'pastrami', 'rueben', 'club', 'pastrami',
          'roast beef', 'corned beef', 'pastrami']
finish = []
while orders:
    s = orders.pop()
    print(f"Currently making a {s} sandwich.")
    finish.append(s)
# Confirm finished orders
print("\nThe following sandwich orders are ready:")
for fs in finish:
    print(fs.title())

# Exercise 7-9 No Pastrami
orders = ['blt', 'bologna', 'pastrami', 'rueben', 'club', 'pastrami',
          'roast beef', 'corned beef', 'pastrami']
finish = []
print("Sorry, we have run out of pastrami")
while 'pastrami' in orders:
    orders.remove('pastrami')
while orders:
    s = orders.pop()
    print(f"Currently making a {s} sandwich.")
    finish.append(s)
# Confirm finished orders
print("\nThe following sandwich orders are ready:")
for fs in finish:
    print(fs.title())
# Exercise 7-10 Dream Vacation
v = {}
poll_act = True
while poll_act:
    n = input("\nWhat is your name? ")
    p = input("\nIf you could visit one place in the world, where would you \
              go? ")
    v[n] = p
    r = input("Would you like to let another person respond? (y/n) ")
    if r == 'n':
        poll_act = False
print("\n--- Poll Results ---")
for n, p in v.items():
    print(f"{n.title()} would like to visit {p.title()}.")
