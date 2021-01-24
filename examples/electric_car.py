#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:35:04 2021

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


class Battery:
    """Model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize a battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement about the battry's size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the battery's range."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attibutes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


tesla = ElectricCar('tesla', 'model s', 2019)
tesla2 = ElectricCar('tesla', '75D', 2020)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla2.battery.battery_size = 100
print(tesla2.get_descriptive_name())
tesla2.battery.describe_battery()
tesla2.battery.get_range()
