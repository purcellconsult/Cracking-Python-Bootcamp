##########################################
# Generators in python
# ----------------------
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
##########################################

from random import choice
from string import ascii_letters, digits

symbols = '★☺⁂♬ϟ⌚'
# option 1
option_1 = []
for x in symbols:
    option_1.append(ord(x))

# option 2
option_2 = [ord(x) for x in symbols]

# option 3 generator expression

genexpr = (ord(x) for x in symbols)
print(option_1)
print(option_2)
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))

# Option 2 is still easy to understand plus only contains one line of code compared to 3 lines in option 1.
# Also, a list comprehensions intent is clear. It only builds a list. A for loop can do a ton of stuff, compute values, count items, etc.

# list comprehensions vs map and filter
# list comprehensions can emulate the logic of maps and filter

message = 'python is a fine language'
output_1 = [ord(x) for x in message if ord(x) > 110]

# maps and filter
output_2 = list(filter(lambda x: x > 110, map(ord, message)))
print(output_1)
print(output_2)

print()
symbols = '★☺⁂♬ϟ⌚'
list_comp = [ord(x) for x in symbols]
genexpr = (ord(x) for x in symbols if ord(x) > 110)

print(list_comp)
print(genexpr)
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))


def forever(start=1, step=5.5):
    while True:
        start = (start * step)**3
        yield start


forever()

# simple generator example

message = 'hello'
for char in message:
    print(char)

# if we had to implement this with a while loop, it looks something like..

it = iter(message)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


def gen_12345():
    for x in range(5):
        yield x


print(next(gen_12345()))
print(next(gen_12345()))


class Password:

    def __init__(self, length=8):
        self.password = ''
        i = 0
        if length >= 8 and length < 21:
            chars = ascii_letters + digits
            while i < length:
                self.password += choice(chars)
                i += 1

    def __iter__(self):
        return self

    def __next__(self):
        for ch in self.password:
            yield ch


secret = Password()
print(secret.password)

it = iter(secret)
print(it)
print(next(it))
print(next(it))


# iterators in python
class SimpleNumber:
    def __init__(self, start=0):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        for x in range(self.start):
            yield x


simple = SimpleNumber()


it = iter(simple)
print(it.__next__())

print(next(it))
print(next(it))
