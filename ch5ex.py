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
    
#Exercise 5-2 More Conditional Tests
wx = 'rainy'
if wx.lower() != 'hot':
    wx = 'not hot'
    print(f"\nThe weather is {wx.lower()}.")
else:
    print("\nThe weather is too hot.")

n1 = 50
if n1 == 50:
    print("\nThe number is 50.")
else:
    if n1 != 50:
        print("\nThe number is not 50.")

wx = ['hot', 'rainy', 'cold']
w = 'snow'
if w not in wx:
    wx.append(w.lower())
    print(f"\n{w.title()} has been added to the list")
    print(wx)
else:
    print(f"\n{w.title()} is already in the list.")
if w not in wx:
    wx.append(w.lower())
    print(f"\n{w.title()} has been added to the list")
    print(wx)
else:
    print(f"\n{w.title()} is already in the list.")    
w = 'stormy'
if w not in wx:
    wx.append(w.lower())
    print(f"\n{w.title()} has been added to the list")
    print(wx)
else:
    print(f"\n{w.title()} is already in the list.") 
w = 'cold'
if w not in wx:
    wx.append(w.lower())
    print(f"\n{w.title()} has been added to the list")
    print(wx)
else:
    print(f"\n{w.title()} is  'already in the list.")
#Exercise 5-3 Alien Colors #1
al_c = 'green'
if al_c =='green':
    print("\nYou just scored 5 points.")
al_c = 'orange'
if al_c =='green':
    print("\nYou just scored 5 points.")
#Exercise 5-4 Alien Colors #2
al_c = 'green'
if al_c =='green':
    print("\nYou just scored 5 points.")
if al_c != 'green':
    print("\nYou just scored 10 points.")
al_c = 'green'
if al_c =='green':
    print("\nYou just scored 5 points.")
if al_c != 'green':
    print("\nYou just scored 10 points.")



    