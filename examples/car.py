#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 04:07:54 2021

@author: rdrolis
"""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to identify a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
    
    def read_odometer(self):
        """Print a statement showing a car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add a given amount to odeometer reading."""
        self.odometer_reading += miles
        

my_new_car = Car('audi', 'a4', 2019)
my_new_car.odometer_reading = 23
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(21)
new_car = Car('subaru', 'outback', 2015)
print(new_car.get_descriptive_name())
new_car.update_odometer(12000)
new_car.read_odometer()
new_car.increment_odometer(100)
new_car.read_odometer()
