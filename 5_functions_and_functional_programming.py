#######################################
# Functions and functional programming
# ------------------------------------
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################

# what's a function in mathematics
# A relation between the mapping of a set of inputs to a set of outputs
# Examples are x^2, x^3, or sqrt(x + 3)

# why use functions?
# ------------------
# 1. Makes code more modular
# 2. Allows code reuse
# 3. Abstraction. You don't need to know the complex underlining
# details of a program just to use it. Kind of like you don't need
# to be an engineer to drive a car, you just need to know thins
# such as accelerate, decelerate, brake, etc.
# Research more uses of functions in your free time.

# -- How to create functions in python -- #

"""
def f():
    pass
"""

# def is a reserved keyword in python.
# f is the name of the function
# The open ( and close ) parentheses must follow the function name
# A function could have variables inside called parameters
# The colon must follow the closing parentheses
# 'underneath' the function name is called the body. The details of the function goes here.
# The body of a function must be indented four spaces.
# A function could optionally return a value.

# What's the difference between parameters and arguments?
# A parameter is a variable which goes inside the parentheses of a function
# An argument is an expression within parentheses


# -- A function declaration in python --

def sum_nums(x, y):
    return x + y


# to call or use the function do the following
result = sum_nums(5, 10)    # 15

# the return statement
# it allows you to store the result for later reuse


# A function that sums three numbers
def summation(x, y, z):
    return x + y + z


a = summation(5, 10, 15)
b = summation(10, 20, 30)
c = a + b
print(c)


# summing an arbitrary amount of numbers
def summation(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


x = summation(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(x)

# keyword arguments
# -----------------
# Use these when you want your arguments to have default values
# When your arguments don't have default values this is know as positional keyword arguments


def f(x=10, y=20):
    return (x + y) * 3

print(f(x=20, y=100)) # 360

# passing in an arbitrary number of keyword arguments
# you can also pass in an arbitrary number of keyword arguments

def func(**kwargs):
    for x, y in kwargs.items():
        print('x={}, y={}'.format(x, y))

func(a=1, b=5, c=10)


# Functional programming in python
# --------------------------------
# Functional programming is a paradigm. A coding paradigm is a style to programming. 
# There's various styles to programming like they're various style to fashion.
# There's languages dedicated to various styles: Java, object oriented, Haskell function
# python is mixed: it supports various paradigms such as imperative, oop, and functional
# functional aspects in python: lambdas, map, filter, reduce


# lambdas: aka anonymous functions
# -------------------------------
x1 = lambda x, y: x + y
print(x1(20, 20))   # 30

# filter: allows you to filter the result
items = [x for x in range(1, 1001)]
x2 = filter(lambda x: x % 3 == 0, items)
print(list(x2))

# map: returns a list of results after applying the function
# to each item in the list

nums = [x for x in range(1, 11)]
mapped = map(lambda x : x** 2, nums)
print(list(mapped))

# reduce: apply a function passed in the argument to all of
# the elements in a list.

first_1000 = [x for x in range(1001)]
import functools
print('The summation is:',  functools.reduce(lambda x, y: x + y, first_1000))

