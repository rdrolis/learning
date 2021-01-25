#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:50:35 2021

@author: rdrolis
"""

"""
Module that tries to model the characteristics of a restaurant.
"""


class Restaurant:
    """Define a restaurant"""

    def __init__(self, n, c):
        """Initialize name and type of restaurant"""
        self.n = n
        self.c = c
        self.nc = 0

    def desc(self):
        """Provide restaurant information"""
        print(f"{self.n.title()} serves {self.c} food.")

    def open(self):
        "State the restaurant is open"
        print(f"{self.n.title()} is open.")

    def cust(self):
        """Print a statement show number of customers served"""
        print(f"{self.n.title()} has served {self.nc} customers.")

    def set_cust(self, cu):
        """Set the number of customers served."""
        self.nc = cu

    def inc_cust(self, add):
        """Increment the number of customers served."""
        self.nc += add
