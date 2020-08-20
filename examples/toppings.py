#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:43:23 2020

@author: rdrolis
"""

r_top = 'mushrooms'
if r_top != 'anchovies':
    print("Hold the Anchovies!")

# Doesn't test all conditions (when condition is met routine stops)
r_top = ['mushrooms', 'extra cheese']
if 'mushrooms' in r_top:
    print("\nAdding mushrooms.")
elif 'pepperoni' in r_top:
    print("Adding pepperoni.")
elif 'extra cheese' in r_top:
    print("Adding extra cheese.")
print("Finished making your pizza.")

#Tests all conditions (if condition is not met, contiunes through routine)
if 'mushrooms' in r_top:
    print("\nAdding mushrooms.")
if 'pepperoni' in r_top:
    print("Adding pepperoni.")
if 'extra cheese' in r_top:
    print("Adding extra cheese.")
print("Finished making your pizza.\n")
# requested topping using for loop
r_tops = ['sausage', 'mushrooms', 'pepperoni','green peppers', 'extra cheese']
for rtop in r_tops:
    if rtop == 'green peppers':
        print("Sorry, green peppers are not available right now.")
    else:
        print(f"Adding {rtop}.")
print("Finished making your pizza.\n")
# empty requested topping list
rtops = []
for rtop in rtops:
    print(f"Adding {rtop}.")
else:
    print("Are you sure you want a plain pizza?\n")

#Making a pizza with multiple lists.
a_top = ['sausage', 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
r_top = ['sausage', 'extra cheese', 'black olives', 'pepperoni']
for r in r_top:
    if r in a_top:
        print(f"Adding {r}.")
    else:
        print(f"Sorry, we don't have {r}.")
print("Your pizza is ready.\n")
print()
#Pizza order
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
#Summarize order
print(f"You ordered a {pizza['crust']}-crust pizza \
with the following toppings:")
for t in pizza['toppings']:
    print(t)
