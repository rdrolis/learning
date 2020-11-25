#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:34:24 2020

@author: rrolison
"""

# Function for printing models


def pm(ud, cm):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing.
    """
    while ud:
        cd = ud.pop()
        print(f"Printing model: {cd}")
        cm.append(cd)


def scm(cm):
    """ Show all the models that were printed. """
    print("The following models have been printed:")
    for c in cm:
        print(c)
