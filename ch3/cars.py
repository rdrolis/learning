# -*- coding: utf-8 -*-

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw','audi','toyota','subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the orginal list again:")
print(cars)
cars.reverse()
print(cars)