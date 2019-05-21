#########################################
# Text based calculator coding project:
# Due: 05/21/2019 at 10:30 am
#
# Write a simple text based calculator
# that prompts the user for two input,
# and prints out the correct calculations.
#
# The operations to model are:
# addition
# subtraction
# multiplication
# division
# modulus
# square root
# exponential
# basic trigonometry: sin(), cos(), tan()
# shows results both in radians and degrees
# logarithm
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#########################################

from math import sin, cos, tan
from math import radians
from math import log
from math import sqrt

'''
addition operation
'''

a1 = float(input('Addition. Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 + a2
print(a1, '+', a2, '=', a3)

'''
subtraction operation
'''
a1 = float(input('Subtraction: Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 - a2
print(a1, '-', a2, '=', a3)

'''
multiplication operation
'''

a1 = float(input('Multiplication: Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 * a2
print(a1, 'x', a2, '=', a3)

'''
division operation
'''

a1 = float(input('Division: Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 / a2
print(a1, '/', a2, '=', a3)

'''
modulus operation
'''

a1 = float(input('Modulus: Enter first number '))
a2 = float(input('Enter second number '))
a3 = a1 % a2
print(a1, '%', a2, '=', a3)

'''
square root operation
'''

a1 = float(input('Square root: Enter number to take square root of '))
print('√', a1, '=', sqrt(a1))

'''
Exponentiation
'''

b = float(input("Exponentiation. Enter a number for the 'base' "))
n = int(input('Enter the power '))
result = b ** n
print(b, '^', n, '=', result)

'''
basic trigonometry: sin(), cos(), trig:
in both radians and degrees
'''


a = float(input('Enter number to compute, sin, cos, and tan of '))

# calculate degrees

sine_degs = sin(radians(a))
cosine_degs= cos(radians(a))
tangent_degs = tan(radians(a))

# calculate radians
sine_rads = sin(a)
cosine_rads = cos(a)
tangent_rads = tan(a)

print(sine_degs, '° sine')
print(sine_rads, 'r sine')

print(cosine_degs, '° cosine')
print(cosine_rads, 'r cosine')

print(tangent_degs, '° tangent')
print(tangent_rads, 'r tangent')

'''
Implement the logarithm. In mathematics the
logarithm is the inverse function of
exponentiation.
'''

x = float(input('Logarithm. Enter the value of x '))
base = float(input('Enter the base '))
logarithm = log(x, base)
print('log base', base, 'of', x, '=', logarithm)


