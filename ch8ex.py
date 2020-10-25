#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:14:36 2020

@author: rrolison
"""

# Exercise 8-1 Display Message


def m():
    """Define Message"""
    print("Python is not really hard to learn.")


m()

# Exercise 8-2 Favorite Book


def b(book):
    """Function message using parameter"""
    print(f"\n{book.title()} is one of my favorite books.")


b('treasure island')
b('without remorse')
b('hunt for red october')

# Exercise 8-3 T-Shirt/ 8-4 Large Shirt


def ts(m, s='large'):
    """T-Shirt Orders"""
    print(f"A {s} t-shirt was ordered with the following slogan \
          '{m.title()}'.")


ts('trump 2020')
ts('I love Python', 'medium')
ts('I love Python')
print()

# Exercise 8-5 Cities


def dc(c, co='united states'):
    """Describe a city"""
    print(f"{c.title()} is located in {co.title()}.")


dc('houston')
dc('nashville')
dc('busan', 'south korea')

# Exercise 8-6 Cities


def cc(c, co):
    """Return a city and country neatly formatted"""
    cf = f"{c}, {co}"
   print return cf.title()


while True:
    print("\nGive me the name of a city and its country")
    print("enter 'q' at any time to quit:")
    city = input("Name of city: ")
    if city == 'q':
        break
    country = input("Country name: ")
    if country == 'q':
        break

    form = cc(city, country)
    print(form)

# Exercise 8-7 Albums


def make_album(t, a, s=None):
    """Return a dictionary of album information"""
    al = {'title': t, 'artist': a}
    if s:
        al['songs'] = s
    return al


album = make_album('van halen', 'van halen')
print(album)
album = make_album('ou812', 'van halen')
print(album)
album = make_album('land of make believe', 'chuck mangione', 12)
print(album)

# Exercise 8-8 User Albums

while True:
    print("\nEnter the name of an artist and album")
    print("enter 'q' at any time to quit:")
    art = input("Artist's name: ")
    if art == 'q':
        break
    tit = input("Album title: ")
    if tit == 'q':
        break
    album = make_album(tit, art)
    print(album)
  
# Exercise 8-9 Messages


def shm(ms):
    """ Print a list of messages. """
    for m in ms:
        t = f"Here is your message: {m}."
        print(t)


texts = ['brb', 'ok', 'cu soon']
shm(texts)

# Exercise 8-10 Sending Messages

def sm(t, st):
    """Simulate sending each message """
    while t:
        m = t.pop()
        print(f"Sending message: {m}")
        st.append(m)


def stm(st):
    """ Show the sent messages """
    print("The following text messages have been sent:")
    for mt in st:
        print(mt)

texts = ['brb', 'ok', 'cu soon']
sm(texts, st)
print()
stm(st)

# Exercise 8-11 Archived Messages

def sm(t, st):
    """Simulate sending each message """
    while t:
        m = t.pop()
        print(f"Sending message: {m}")
        st.append(m)


def stm(st):
    """ Show the sent messages """
    print("The following text messages have been sent:")
    for mt in st:
        print(mt)
st = []
texts = ['brb', 'ok', 'cu soon']
sm(texts[:], st)
print()
stm(st)
print()
print(texts)
print(st)
