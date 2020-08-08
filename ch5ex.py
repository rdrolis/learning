#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:54:31 2020

@author: rdrolis
"""
#Exercise 5-1 Conditional Tests
#conditional tests 1 & 2
p = 'Springfield XD'
print("\nIs p == 'springfield xd'? I predict false.")
print(p == 'springfield xd')
print("Does p.lower() == 'springfield xd'? I predict true.")
print(p.lower() == 'springfield xd')

#conditional tests 3-10
a_0 = 25
a_1 = 18
print("\n Are both ages over 21? I predict false.")
if a_0 > 21 and a_1 > 21:
    print("true")
else:
    print("false")
print("\n Is at least one age over 21? I predict true.")
if a_0 > 21 or a_1 > 21:
    print("true")
else:
    print("false")
print("\nAre both ages at least 18? I predict true.")
if a_0 >= 18 and a_1 >= 18:
    print('true')
else:
    print("false")
print("\nDoes one age equal 22? I predict false.")
if a_0 == 22 or a_1 == 22:
    print("true")
else:
    print("false")
a_0 = 22
print("\nDoes one age equal 22? I predict true.")
if a_0 == 22 or a_1 == 22:
    print("true")
else:
    print("false")
a_0 = 25
a_1 = 27
print("\nAre both ages over 25? I predict false.")
if a_0 > 25 and a_1 > 25:
    print("true")
else:
    print("false")
print("\nAre both ages at least 25? I predict true.")
if a_0 >= 25 or a_1 >= 25:
    print("true")
else:
    print('false')
print("\n Is one age 30? I predict false.")
if a_0 == 30 or a_1 == 30:
    print("true")
else:
    print("false")
    