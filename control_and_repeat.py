##################################################
# Control and repeat
# -------------------
# Learn how to control the flow
# of execution of statements in a program by
# using if, else, and elif statements.
# Learn how to repeat code blocks by using
# iteration tools in python such as for and
# while loops
#
# If new to python read the accompanying powerpoint
# to learn more about the theory: [insert link]
#
#
# To run file, type: python control_and_repeat.py
#
# By Doug Purcell
#
###################################################


# BOOLEAN ALGEBRA: True or False
# ----------------------------------------
# Must understand truth tables
# Used to determine control flow: if/elif/else statements
# Describe boolean type by asking true or false questions


is_the_sky_blue = True
do_cats_bark = False

print(is_the_sky_blue)
print(do_cats_bark)

# The 'and' truth table
# 'and' evaluates to false unless both operands are False

print(True and True)
print(True and False)
print(False and False)
print(False and True)
print()

# or evaluates to true with at least one true operand
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print()

# xor evaluates to true
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)
print()

# compound statements or combining them
print(True or False or False)
print(True and False or True)
print(True or False and True)
print(not False & (True and True) or False)
print()

# CONTROL FLOW IN PYTHON
# -----------------------
# if/else statement

x, y, z = 5, 10, 15
if x < y and z > y:
    print(x)
else:
    print(y)

# The above could also be rewritten as follows

x, y, z = 5, 10, 15
if x < z > y:
    print(x)
else:
    print(y)


# nested if statement
# is the below logically equivalent to the above?
if x < y:
    if z > y:
        print(x)
else:
    print(y)

# what's the output and why does it happen?

if x < y:
    if z < y:
        print(x)
else:
    print(y)


if x < y:
    if z > y:
        print(x)
    print(y, '\n')

if not x > y:
    print('inverse!', '\n')

# elif statements
# can change multiple conditionals together

var = 10
if var == 1:
    print(var + 10)
elif var == 3:
    print(var + 20)
elif var == 5:
    print(var + 30)
elif var == 7:
    print(var + 50)
elif var == 9:
    print(var + 70)
elif var == 10:
    print(var + 100)
else:
    print('I think it\'s not in here')
print()


# ternary statement
# allows for assignment of variable based on expression evaluation
test_variable = 1
result = 10 if test_variable else ''
print(result, '\n')

# There's many comparison operators such as <=, >=, !=, etc.
# micro programming sessions
# write a program that reads in input, in miles and converts it
# to feet and kilometers. Here are the conversion units:

miles = float(input('Enter the miles '))
feet = miles * 5280
inches = miles * 63360
kilometers = miles * 1.60934
meters = miles * 1609.34
print(miles, 'miles', '=', feet, 'ft', inches, 'in', kilometers, 'km', meters, 'm')
print()

# write a program that takes input which represents the miles ran
# and then states if the user ran more than a marathon
# marathon equals 26.22 miles


miles_ran = float(input('Enter the miles ran '))
if miles_ran >= 26.22:
    print('Ran a marathon')
elif miles_ran < 0:
    print('Can\'t run negative miles!')
else:
    miles_to_go = 26.22 - miles
    print(miles_to_go, 'miles to go')
print()

# Iteration in python
# -------------------
# Computers are perfect for this, humans not so much!
# Two main ways to do this is while and for loops


# -- WHILE LOOP --
# while something is true do this...

i = 0
while i < 10:
    i += 1
    print(i)
print()

# decrementing with a while loop
j = 50
while j > 0:
    print(j, end=' ')
    j -= 1
print('\n\n')

# fibonacci sequence
# prints the first 10
i, j, count = 0, 1, 0
while count < 10:
    print(i)
    i, j = j, j + i
    count += 1
print()

# simple sequence

scale = int(input('Enter number to scale the loop by: '))
i, j = 0, 1
while i < 10:
    j *= scale
    print('j =', j, end=' ')
    i += 1
print()

# infinite loop
# while True:
#     pass

# infinite loops have their place
# can be used to make simple games

sum = 0
while True:
    nums = float(input('Enter a number '))
    sum += nums
    print('sum ', '=', sum)
    if sum > 100:
        exit()

# if you want to exit out of a program you could use
# the break statement

i = 1
while i < 100000000000000000:
    print(i, end=' ')
    i += 1
    if i % 7 == 0:
        print(i)
        break
print()


# continue statement
# passes over the

i = 0
while i <= 20:
    i += 1
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')
print()

# nesting loops
# a loop inside a loop

i, j = 0, 1
while i < 5:
    while j < 5:
        print('i =', i, 'j =', j, end=' ')
        j += 1
    i += 1
    j = 1  # resets the inner loop
print()

# for loop
# --------
# popular choice for iterating over data structures
# different from for loops in C style languages like Java
# range() function helps generate a sequence of numbers

for x in range(10):
    print(x, end=' ')
print()

# nesting for loops to print multiplication tables
# of 1 - 12

for x in range(1, 13):
    for y in range(1, 13):
        print(x, 'x', y, '=', x * y)
    print('--------------')


# a fun way to learn nested loops
# create patterns with them

# 4 x 4 star square
for x in range(4):
    for y in range(4):
        print('*', end=' ')
    print()
print()

# right triangle
for x in range(6):
    for y in range(x):
        print('*', end=' ')
    print()
print()

# money rectangle
for x in range(3):
    for y in range(10):
        print('$', end=' ')
    print()


# generating prime numbers within the the range 1-1000
# known as the sieve's algorithm
# sieve of eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# why is this implementation poor? Hint, change range(3, 1000) to (3, 1000000)
# research algorithmic complexity: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Algorithmic%20Complexity/complexity.html

for x in range(3, 1000):
    for y in range(2, x):
        if x % y == 0:
            break
    if x == y + 1:
        print(x, end=' ')
print()


# calculating factorials of a number n

n = int(input('Enter a number n '))
count = n-1
while count >= 1:
    n *= count
    count -= 1
print('n =', n)

# read in a list of numbers and print the mean
summation, n = 0, 0
try:
    while True:
        list_of_numbers = float(input('Enter numbers. Terminate by hitting Ctrl + C (keyboard interrupt): '))
        summation += list_of_numbers
        n += 1
except KeyboardInterrupt:
    print()
    print('Program existing...')
    print('-------------------')
    print('summation = ', summation)
    print('count =', n)
    print('average = ', summation / n)










