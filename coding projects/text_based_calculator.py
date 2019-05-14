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

'''
addition operation
'''

a1 = float(input('Addition. Enter first number '))
a2 = float(input('Addition. Enter second number '))
a3 = a1 + a2
print('The sum of ', a1, 'and ', a2, '=', a3)