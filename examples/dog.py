#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 06:20:58 2020

@author: rdrolis
"""
# Introduction to classes


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attribues."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting on command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over on command"""
        print(f"{self.name} rolled over!")


md = Dog('Willie', 6)
yd = Dog('Lucy', 3)
print(f"My dog's name is {md.name}.")
print(f"Your dog's name is {yd.name}")
print(f"{md.name} is {md.age} years old.")
print(f"{yd.name} is {yd.age} years old.")
md.sit()
yd.sit()
md.roll_over()
yd.roll_over()
