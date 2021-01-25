#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:37:57 2020

@author: rdrolis
"""

# Exercise 9-1 Restaurant
# Exercise 9-4 add methods for number of customers served

"""
Chapter exercises after 9-9 are in modules. See /ch9mod subdirectory
for these exercises.
"""


class Restaurant:
    """Define a restaurant"""

    def __init__(self, n, c):
        """Initialize name and type"""
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


r1 = Restaurant('applebees', 'casual')
r1.desc()
r1.open()
r1.cust()
r1.set_cust(1500)
r1.cust()
r1.inc_cust(2500)
r1.cust()

# Exercise 9-2 Three Restaurants

r2 = Restaurant('whataburger', 'fast')
r3 = Restaurant('olive garden', 'italian casual')
r4 = Restaurant('pappadeaux', 'Louisiana coast')
print()
r2.desc()
r2.open()
print()
r3.desc()
r3.open()
print()
r4.desc()
r4.open()

# Exercise 9-3 Users
# Exercise 9-5 Add methods for number of login attempts.


class User:
    """ Define user information"""

    def __init__(self, first, last, email, uname):
        """Initialize user attributes"""
        self.first = first.title()
        self.last = last.title()
        self.email = email
        self.uname = uname
        self.logins = 0

    def info(self):
        """Provide user info"""
        print(f"\n{self.first} {self.last}")
        print(f"Username: {self.uname}")
        print(f"Email address: {self.email}")

    def greet(self):
        print(f"\nHello {self.first.title()} {self.last.title()}, thank you \
for logging in.")

    def incr_login(self):
        """Increment the number of login attempts."""
        self.logins += 1
        print(f"You have logged in {self.logins} times.")

    def reset_login(self):
        self.logins = 0
        print(f"You have logged in {self.logins} times.")


u1 = User('john', 'kelly', 'jkelly@cia.gov', 'jkelly')
u2 = User('santa', 'clause', 'santa@northpole.com', 'sclause')
u3 = User('jack', 'ryan', 'dci@cia.gov', 'jryan')

u1.info()
u1.greet()
u2.info()
u2.greet()
u3.info()
u3.greet()
u1.greet()
u1.incr_login()
u1.greet()
u1.incr_login()
u1.greet()
u1.reset_login()

# Exercise 9-6 Ice Cream Stand


class IceCreamStand(Restaurant):
    """Represents attributes specific to ice cream stands"""

    def __init__(self, n, c):
        """
        Initialize the attributes of the parent class
        Then initialize the attributes specific to an ice cream stand
        """
        super().__init__(n, c)
        self.flavors = ['vanilla', 'chocolate', 'rocky road', 'butter pecan']

    def print_flavors(self):
        print(f"{self.n.title()} offers the following ice cream flavors:")
        for f in self.flavors:
            print(f.title())


stand = IceCreamStand('baskin robbins', 'ice cream')
stand.desc()
stand.open()
stand.print_flavors()

# Exercise 9-7 Admin user


class Admin(User):
    """Attributes specific to an administrative user."""

    def __init__(self, first, last, email, uname):
        """
        Initialize the attributes of the parent class
        Then initialize the the attributes specific to an admin user.
        """
        super().__init__(first, last, email, uname)
        self.privileges = [
            'can add posts',
            'can delete posts',
            'can ban user'
            ]

    def show_privilege(self):
        print("You have the following privileges:")
        for p in self.privileges:
            print(f"\t-{p}")


u1 = Admin('jack', 'ryan', 'dci@cia.gov', 'jryan')
u1.greet()
u1.show_privilege()

# Exercise 9-9 Privileges


class Privileges:
    """Initialize the privileges for an admin user"""

    def __init__(self, privileges=[]):
        """Initialize the privileges"""
        self.privileges = privileges

    def show_privilege(self):
        print("You have the following privileges:")
        if self.privileges:
            for pr in self.privileges:
                print(f"-{pr}")
        else:
            print("This user has no privileges.")


class Admin(User):
    """Attributes specific to an administrative user."""

    def __init__(self, first, last, email, uname):
        """
        Initialize the attributes of the parent class
        Then initialize the the attributes specific to an admin user.
        """
        super().__init__(first, last, email, uname)
        self.privileges = Privileges()


u1 = Admin('jack', 'ryan', 'dci@cia.gov', 'jryan')
u1.greet()
u1.privileges.show_privilege()
print("Adding admin privileges...")
u1_privileges = [
    'can add users',
    'can delete users',
    'can moderate discussions',
    ]
u1.privileges.privileges = u1_privileges
u1.privileges.show_privilege()

# Exercise 9-9 Battery Upgrade


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


tesla = ElectricCar('tesla', '75D', 2020)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.battery_size = 100
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
