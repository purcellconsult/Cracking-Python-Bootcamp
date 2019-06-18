#######################################
# Learn the basics of data structures
# in python.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#######################################


# What's a data structure? A way for computers
# to store and retrieve data.
# A data structure may be selected or designed to store data
# for the purpose of working on it with various algorithms.
# Data structures are popular interview questions during
# technical exams at software companies.
# It's important to pick the proper data structure for the the
# particular problem you're working on. An ill suited data structure
# could lead to poor performing programs.
# python has 4 builtin data structures, and many more that can
# be imported to use in your various programs.

# lists
# ------
# a data structure that stores data in a linear fashion
# the elements, or 'data' inside of a list is typically homogeneous
# similar to an array in other languages
# like with other languages

empty = []

# use the append method to add data into a list
# you can only add one element at a time.
empty.append(10)
empty.append(100)
empty.append(50)
print(empty)

# accessing elements in lists with the index
# python is a 0th indexed based language, meaning the 0th index
# maps to the first element.

evens = [2, 4, 6, 8, 10, 12, 14]
print(evens[0])      # 2
print(evens[2])      # 6
print(len(evens)-1)  # 6
print()

# in python you can also use negative indices
print(evens[-1])    # 14
print(evens[-3])    # 10

# you can slice lists or take a range of numbers
print(evens[0:3])   # 2, 4, 6
print(evens[::])    # returns everything
print(evens[::2])   # returns everything with a skip of 2
print(evens[-7:-3]) # 2, 4, 6, 8
print(evens[::-1])  # reverses the list
print()


# common functions and methods associated with lists
# len() gets the size

size = len(evens) # 7
evens.extend([13, 17, 19, 23])    # adds another list the the current one
print(evens)
evens.reverse()                   # reverses the list
print(evens)
print(evens.count(13))             # 1
print(evens.pop())                 # 2
evens.insert(0, 29)
print(evens)

# iterating or walking through lists
# you can use a for or while loop to iterate over a list
primes = [2, 3, 5, 7, 11, 13, 17, 19]
for x in primes:
    print(x, end=' ')

print()
# if you use a while loop you must access the elements
# using subscript notation
i = 0
while i < len(primes):
    print(primes[i], end=' ')
    i += 1


print()

# nested lists
# a list within a list is a 2D or two dimensional list

grid_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# better formatted
print(grid_1)

grid_2 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

print(grid_2[0][0])     # 1
print(grid_2[0][1])     # 2
print(grid_2[1][1])     # 5
print(grid_2[2][0] * grid_2[2][2])  # 63
print()

# to iterate through all of the rows and columns of a 2D list
# you'll need a nested loop

for row in range(len(grid_2)):
    for col in range(len(grid_2)):
        print(grid_2[row][col], end=' ')
    print()


# list comprehensions
# a shorthand version for creating lists

a = []
for x in range(10):
    a.append(x)
print(a)

# instead do the following
b = [x for x in range(10)]
print(b)

# build list of even integers from 0 .. 100
c = [x for x in range(100) if x % 2 == 0]
print(c)

# nested list comprehensions
d = [x for x in range(1, 3) for y in range(1, 7)]
print(d)

# tuples
# ------
# tuples are very similar to lists with the exception that
# tuples are immutable. Meaning that the object is immutable.

point = (1, 5)
print(point)            # 2
print(point.count(1))   # 1
print(point.index(5))   # 1
print(len(point))       # 2
print(point[::])        # (1, 5)
print(point[1])         # 5

# iterating over tuples
for x in point:
    print(x, end=' ')
print()

# dictionaries
# ------------
# also known as hash tables, hash maps, or associative arrays in other languages.
# contains key/value mappings.
# a very ubiquitous data structure. Used for database indexing.
# create them using curly braces.

vowels_1 = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

# could also change format

vowels_2 = {
    'a': 0,
    'e': 1,
    'i': 2,
    'o': 3,
    'u': 4
}

# accessing elements in dictionaries
# can use subscript notation to get the value

print(vowels_1['a'])
print(vowels_1.items()) # returns all key/value mappings
print(vowels_1.pop('o'))
print(vowels_1.keys())      # returns all of the keys
print(vowels_1.values())    # gets all of the values
print(vowels_1.get('a'))


# sets
# ----
# similar to sets in mathematics. It can't hold no duplicates.
# internally implements a dictionary
# also uses curly braces
# order is not preserved

letters = {'a', 'A', 'a', 'b', 'b', 'c', 'd', 'e', 'e', 'f'}
print(letters)
# common set functions
# set operations like in mathematics

constants = {'a', 'b', 'c'}
print(letters.union(constants))                 # returns first set combined with elements of second
print(letters.difference(constants))            # returns a set that subtracts the second from the first
print(letters.intersection(constants))          # returns elements common
print(letters.symmetric_difference(constants))  # (A-B) U (B-A)

# like with the other data structures, they can also be
# iterated over.

for x in letters:
    print(x, end=' ')
