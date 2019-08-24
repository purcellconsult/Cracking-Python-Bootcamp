###########################################
# Code from python
# Features python variables, numbers, and
# builtin data types
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
############################################


###############################
# creating variables in python
###############################

a = 5
b = 10
c = a
d = a**2
e = d + 10

#############################################
# to view the output use the print() function
#############################################

print(a)
print(b)
print(c)
print(d)
print(e)
# prints text
print('Hello World')
# prints numbers and text, is really a tuple.
print(5, 'birds')
# prints empty space
print()


###############################
# using python as a calculator
# learn the operators:
# + & -
# * & /
# % & //
# ** and ()
###############################

print(10 + 10)
print(20 - 5)
print(9 * 9)
print(5 / 2)
# floor functionality
print(5 // 2)
print(10 % 3)
print(5 ** 3)
# the parentheses changes order of execution
print(10 - 3 / (5 % 3))
print()


#######################################
# two main types of numbers in python:
# int and float.
########################################

a1 = 5
print(type(a))
# euler's number
b1 = 2.7182818284590452353602874713527
print(type(b1))

# 7.718281828459045
c1 = a1 + b1
print(c1)
# 7.Truncates the mantissa
print(int(c1))
print(float(c1))
print()

##################################################
# reading in text and numbers in python!
# the input() function allows
# you to create interactive and fun programs :-)!
##################################################

# reading in text
# your_message = input('What\'s your message? ')
# print('The message is: ', your_message)


################################################
# reading in numbers. Pass the input() function
# to the int() function.
################################################

your_int = int(input('Enter any number '))
print('Your number is: ', your_int)
print()


###########################################
# importing modules
# Gain more functionality by importing
# modules like math
###########################################

import math
from math import degrees
print(math.sin(90))
print(math.cos(180))
print(math.tan(45))
# converts to degrees
print(degrees(math.pi/2))

print(math.pi)
print(math.factorial(4))
print(math.gcd(75, 1000))
print(math.isclose(10, 10.00000000000000000000000000000001))
print(math.exp(3))
print(math.log(16, 2))
print(math.floor(5.5242))
print(math.sqrt(9))


#################################
# Microprogramming session
#
# calculate change for groceries
# area of a triangle
# quadratic equation
#
################################

milk = 2.90
loaf_of_bread = 1.89
pack_of_ham = 4.99
grocery_cost = milk + loaf_of_bread + pack_of_ham
change = int(input('Enter the amount of change you have in $10, $20, or '
                   '$50 portions. '))

your_change = change - grocery_cost
print(round(your_change, 2))


# area of a triangle is 1/2 * b * h
base = float(input('Enter base of a triangle '))
height = float(input('Enter height of triangle '))
area = 1/2 * base * height
print('Area of a triangle with base', base, 'and height ', height, 'is', area)

# quadratic formula
# Has two roots:
# x = -b + sqrt(b^2 - 4ac) / 2a
# x = -b - sqrt(b^2 - 4ac) / 2a
# write a program that accepts a, b, and c, then
# returns correct answer

from math import sqrt
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

x1 = 0
x1 = -b + sqrt(b**2 - (4 * a * c))
x1 = x1 / (2 * a)

x2 = -b - sqrt(b**2 - (4 * a * c))
x2 = x2 / (2 * a)
print('x1 =', x1)
print('x2 =', x2)

