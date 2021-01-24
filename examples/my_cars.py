#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:50:06 2021

@author: rdrolis
"""

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
my_tesla = car.ElectricCar('telsa', 'model s', 2019)
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())
