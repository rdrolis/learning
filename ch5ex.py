#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:54:31 2020

@author: rdrolis
"""
# Exercise 5-1 Conditional Tests
# conditional tests 1 & 2
p = 'Springfield XD'
print("\nIs p == 'springfield xd'? I predict false.")
print(p == 'springfield xd')
print("Does p.lower() == 'springfield xd'? I predict true.")
print(p.lower() == 'springfield xd')

# conditional tests 3-10
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

# Exercise 5-2 More Conditional Tests
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

# Exercise 5-3 Alien Colors #1
al_c = 'green'
if al_c == 'green':
    print("\nYou just scored 5 points.")
al_c = 'orange'
if al_c == 'green':
    print("\nYou just scored 5 points.")

# Exercise 5-4 Alien Colors #2
al_c = 'green'
if al_c == 'green':
    print("\nYou just scored 5 points.")
if al_c != 'green':
    print("\nYou just scored 10 points.")
al_c = 'red'
if al_c == 'green':
    print("\nYou just scored 5 points.")
if al_c != 'green':
    print("\nYou just scored 10 points.")

# Exercise 5-5 Alien Colors #3
al_c = 'green'
if al_c == 'green':
    sc = 5
if al_c == 'yellow':
    sc = 10
if al_c == 'red':
    sc = 15
print(f"\nYou scored {sc} points.")

al_c = 'yellow'
if al_c == 'green':
    sc = 5
if al_c == 'yellow':
    sc = 10
if al_c == 'red':
    sc = 15
print(f"\nYou scored {sc} points.")

al_c = 'red'
if al_c == 'green':
    sc = 5
if al_c == 'yellow':
    sc = 10
if al_c == 'red':
    sc = 15
print(f"\nYou scored {sc} points.")

# Exercise 5-6 Stages of life
a = 2
if a < 2:
    st = 'a baby'
elif a >= 2 and a < 4:
    st = 'a toddler'
elif a >= 4 and a < 13:
    st = 'a kid'
elif a >= 13 and a < 20:
    st = 'a teenager'
elif a >= 20 and a < 65:
    st = 'an adult'
elif a > 65:
    st = 'a senior citizen'
print(f"\nThat person is {st}.")

# Exercise 5-7 Favorite Fruits
f = 'apples'
ff = ['peaches', 'watermelon', 'oranges']
if f in ff:
    print(f"\nYou really like {f}.")
else:
    print(f"\nI guess you don't like {f} that much.\n")
# Exercise 5-8 Hello Admin
users = ['robert', 'jessica', 'admin', 'amy']
if users:
    for u in users:
        if u == 'admin':
            print(f"Hello, {u}, would you like to see a report?")
        else:
            print(f"Hello {u.title()}, welcome to the system.")
print()

# Exercise 5-9 No Users
users = []
if users:
    for u in users:
        if u == 'admin':
            print(f"Hello, {u}, would you like to see a report?")
        else:
            print(f"Hello {u.title()}, welcome to the system.")
else:
    print("user list is empty\n")

# Exercise 5-10 Checking Usernames
cusers = ['robert', 'jessica', 'james', 'amy', 'starr']
nusers = ['amy', 'troy', 'keith', 'james', 'billy']
for n in nusers:
    if n in cusers:
        print(f"Username {n.title()} is not available.")
    else:
        print(f"Username {n.title()} is available.")
print()
# Exercise 5-11 Ordinal Numbers
num = range(1, 10)
if num:
    for n in num:
        if n == 1:
            print(f"{n}st")
        elif n == 2:
            print(f"{n}nd")
        elif n == 3:
            print(f"{n}rd")
        else:
            print(f"{n}th")
else:
    print("End of list.")
