#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 07:53:53 2020

@author: rdrolis
"""

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }
for u, ui in users.items():
    print(f"\nUsername: {u}")
    fn = f"{ui['first']} {ui['last']}"
    lo = ui['location']
    print(f"\tFull name: {fn.title()}")
    print(f"\tLocation: {lo.title()}")
