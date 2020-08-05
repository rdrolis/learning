#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 05:45:12 2020

@author: rdrolis
"""
#Establishing a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#Inster at beginning of list
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[0] = 'honda'
#Append a list
motorcycles.append('ducati')
print(motorcycles)
#Delete item from list
del motorcycles[-1]
motorcycles.insert(0, 'ducati')
print(motorcycles)
#Popping item from list
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}")
#Popping item from any position
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}")
#Remove item by value
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
