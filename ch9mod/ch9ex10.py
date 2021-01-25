#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:55:12 2021

@author: rdrolis
"""

from restaurant import Restaurant

r1 = Restaurant('applebees', 'casual')
r1.desc()
r1.open()
r1.cust()
r1.set_cust(1500)
r1.cust()
r1.inc_cust(2500)
r1.cust()
print()
r2 = Restaurant('whataburger', 'fast')
r3 = Restaurant('olive garden', 'italian casual')
r4 = Restaurant('pappadeaux', 'Louisiana coast')
print()
r2.desc()
r2.open()
r2.cust()
r2.set_cust(800)
r2.cust()
r2.inc_cust(600)
r2.cust()
print()
r3.desc()
r3.open()
print()
r4.desc()
r4.open()
