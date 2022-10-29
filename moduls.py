# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:49:28 2022

@author: VICTUS
"""

# import math
# print(math.sqrt(9))
# print(int(math.pow(5, 4)))
# print(math.pi)
# print(math.log2(8))


# import random as r
# # # .randint()
# number = r.randint(1, 100)
# print(number)

# # # .choice()
# names = ['elbek','jamal','xuseyn','jake','hagvart','arnold']
# name = r.choice(names)
# print(name.title())


# # # .shuffle()
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)


# import math
# length = lambda pi, r : 2*pi*r
# print(length(math.pi, 10))

# square = lambda x,y: x**y
# print(square(5, 3))


# import math
# def degree(n):
#     return lambda x: x**n
# square = degree(2)
# cube = degree(3)
# print(f"""The square of 2 is equal to {square(2)}
# and the cube of 3 is equal to {cube(3)}""")


# from math import sqrt
# numbers = list(range(10))
# square_root = list(map(sqrt,numbers))
# print(numbers)
# print(square_root)


# =============================================================================
# numbers = list(range(10))
# def degree(x):
#     """Function that returns square of number"""
#     return x*x
# print(numbers)
# print(list(map(degree, numbers)))
# # # EASEAST WAY
# squares = list(map(lambda x:x*x, numbers))
# print(squares)
# =============================================================================


# a = [4,5,6]
# b = [7,8,9]
# a_plus_b = list(map(lambda x,y: x+y, a,b))
# print(a)
# print(b)
# print(a_plus_b)


# import random as r
# numbers = r.sample(range(100),10)
# print(numbers)
# def is_even(x):
#     """If x is even it will return True,else False"""
#     return x%2==0
# =============================================================================
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)
# 
# even_numbers = list(filter(lambda x: x%2==0,numbers))
# print(even_numbers)
# =============================================================================
