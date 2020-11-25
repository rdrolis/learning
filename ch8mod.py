#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:41:59 2020

@author: rrolison
"""


def pr_car(car):
    """ Print car in particular order"""
    for k, v in reversed(car.items()):
        if k == 'make':
            print(f"{k.title()}: {v.title()}")
        elif k == 'model':
            print(f"{k.title()}: {v.title()}")
        else:
            print(f"{k.title()}: {v.title()}")


def make_car(model, make, **feature):
    """Build a dictionary with information about cars"""
    feature['model'] = model
    feature['make'] = make
    return feature


def build_profile(first, last, **user_info):
    """Build a dictionary containing every thing we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def sand(*items):
    """Summarize sandwich order"""
    print("\nMaking a sandwich with the following ingredients:")
    for i in items:
        print(f"-{i}")
