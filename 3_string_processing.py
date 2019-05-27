#########################################
# String processing in python.
# Learn how to create, manipulate,
# format, and harness strings in python.
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
##########################################

# creating strings in python

e = 'Hello'
f = 'Bonjour'
s = 'Jambo'
h = 'Namaste'
a = 'Selami'
i = 'Ciao'

# view output with print() statement

print(e)
print(f)
print(s)
print(h)
print(a)
print(i)
print()

# manipulating strings in python
# strings can be indexed and manipulated
# this is known as subscript notation
# strings indexes start at 0

print(e[0]) # H
print(f[1]) # o
print(s[2]) # m
print(h[6]) # e

# get ranges in strings by slicing them
# you can use the following syntax to slice strings
# string_name[start:end:skip]
# start is inclusive, the end is exclusive

print(a[0:2])   # Se
print(i[0:3])   # Cia
print(s[::2])   # Jmo

# strings can have negative indexes

print(f[-7:-4])     # Bon
print(a[-6:-3])     # Sel
print(i[-1::-1])    # reverses a string

# ways to manipulate strings in python

a = 'Hello'
b = 'friend'
c = a + b
print(c)            # Hellofriend
print(a + ' ' + b)  # Hello friend
d = '9'
print(10 * int(d))

print(a * 5)

# common methods for the string class

text = 'This is a small world'
print(text.count('i'))
print(text.lower())
print(text.upper())
print(' '.join(text))
print(text.split(' '))
print(text.islower())
print(text.isupper())
print(text.isalnum())
print(len(text))
print()


# converts character to decimal
print(ord('A'))
# converts decimal back to character
print(chr(65))
print()

# iterating with a for loop
text = 'what a wonderful world'
for letter in text:
    print(letter)
print()

# iterating with a while loop
i = 0
while i < len(text):
    print(text[i])
    i += 1

# differences between single, double, and triple quotes.

# single quote
print('What\'s up?')    # the backslash is needed to escape the apostrophe.
print("What's up?")     # the apostrophe is not needed in this case.
print("\"What's up?\"") # the apostrophe is needed to add on the quotes to the text
print("""What's up? Does the "" need an escape?""") # triple quotes can escape single, double, and a lot more.


def triple_quote_docs():
    """
    You know, triple quotes
    can also be used for what's
    knows as a docstring. This let's
    you describe some functionality of the
    method/function, class, etc.
    """
    return


print(triple_quote_docs.__doc__)    # prints the content in triple quotes


# Dig into the string module in python
# Learn about the string module in the python docs: https://docs.python.org/3/library/string.html
# The various ways to format strings in python: commas, %, format(),
# f-strings and template strings

# formatting strings using commas

print('Mixing numbers like ', 8, 'with text')

# the following is allowed
print('9' + '0')

# the following is not allowed
# print('9' + 0)

# the following is allowed
print(float('9') + float('0'))

# using the % sign
# similar to the printf()function in c
print('Hello World For the %dth time' % 100)
print('%s %s %d %d %f %f' % ('Mercedes', 'Apple', 100, 20, 3.2, 1))
print('This is a +%d integer' % 10)
print('This is a negative -%d integer' % 250)
print('This is a confused -%d integer' % 300)

# The format string syntax was introduced in python3
# Read about it here: https://docs.python.org/3/library/string.html#formatstrings

var_1 = 'test'
var_2, var_3 = 'move it move it', 'MOVE IT!'
dog = 'Lassie'
print('This is a {}'.format(var_1))
print('I like to {}, you like to {}!'.format(var_2, var_3))
print('This is {}, and this is B'.format('A', 'B'))
print('Number {1} and number {0}'.format(100, 200))  # keyword position
# accessing arguments by name
print('Mount Whitney is located at {latitude}°N, and {longitude}°W'.format(latitude='35.5785', longitude='118.2923'))

temp = {'day_one': 90, 'day_two': 100}
print('It is {day_one}° F today and tomorrow it will be {day_two}° F'.format(**temp))


# accessing arguments' items:
point = (5, 10)
print('The point values are {0[0]} and {0[1]}'.format(point))

# accessing an argument's attributes


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return 'Rectangle({self.length}, {self.width})'.format(self=self)

rect = Rectangle(10, 5.5)
print(rect.__str__())


# aligning text

print('{:<10}'.format('X')) # left align
print('{:>10}'.format('X')) # right align
print('{:^10}'.format('X')) # center
print('{:?^10}'.format('X')) # add a fill character

# formatting binary, octal, and hexadecimals
print('Binary number: {0:b}'.format(50))
print('Octal number: {0:o}'.format(100))
print('Hexadecimal number: {0:x}'.format(2555))

# using commas as a delimiter
print('{:,}'.format(2783727282727)) # 2,783,727,282,727
print('{:.2%}'.format(90.60/100))   # 90.60%


# formatted string literals also known as f strings
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

item_1, item_2, item_3 = 'computer', 'mouse', 'browser'
print(f"He uses a {item_1}.")
print(f"He uses a {item_2} and a {item_3}.")
print(f"He uses a {item_1} 3 times a day.")


# Templates
# Learn about them more in the python docs: https://docs.python.org/3/library/string.html#template-strings


from string import Template
poem = Template('$x are red and $y are blue')
print(poem.substitute(x='roses', y='violets'))




