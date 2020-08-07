# -*- coding: utf-8 -*-
#Exercise 4-1 Pizzas
pizzas = ['pepperoni','combination','cheese','sausage']
for pizza in pizzas:
    print(pizza)
print()
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("Pizza is one of my favorites.\n")
#Exercise 4-2 Animals
reptiles = ['snake', 'lizard', 'alligator']
for reptile in reptiles:
    print(f"A {reptile} is a reptile.")
print("These are all examples of reptiles.")
#Exercise 4-3 Counting to Twenty
count = list(range(1, 21))
print(count)
#Exercise 4-4 Million
mil=list(range(1,1000001))
#for m in mil:
    #print(m) 
#Exercise 4-5 Summing a million
print(max(mil))
print(min(mil))
print(sum(mil))
print()
#Exercise 4-6 Odd numbers
for odd in range(1, 20, 2):
    print(odd)
print()
#Exercise 4-7 Threes
for t in range(3, 31 ,3):
    print(t)
print()
#Exercise 4-8 Cubes
cu = []
for c in range(1, 11):
    cu.append(c**3)
print(cu)
cu = []
print()
#Exercise 4-9 Cubes List Comprehension
cu = [c**3 for c in range(1,11)]
print(cu)

