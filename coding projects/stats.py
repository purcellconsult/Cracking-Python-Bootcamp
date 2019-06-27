##################################
# Stat-tastic!
# ------------
#
# This exercise helps you practice functions
# and rediscover statistics by coding common
# statistical formulas in python.
# Note, can't use the built in statistics module: https://docs.python.org/3/library/statistics.html
# You can't use the max, min, or sorted functions from the python library: https://docs.python.org/3/library/functions.html
#
# Stats formulas: https://www.statisticssolutions.com/common-statistical-formulas
#
# Functions to code:
# ------------------
#
# Total: The total elements in the file
# Summation: The sum of all of the elements in a file
# Sample Mean: The average
# Sample Standard Deviation: Measures the spread of a data distribution
# Sample Variance: How far a set of numbers are spread out from the average value
# min: The smallest number in the file
# max: The largest number in the file
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################

from math import sqrt


# DATA is a constant
DATA = 'sample_dataset'


def total():
    """
    represents the total number n
    of observations in the sample.
    """
    i = 0
    with open(DATA) as file:
        for line in file:
            i += 1
    return i


def summation():
    """
    sums all of the numbers
    in a dataset.
    """
    sum = 0
    with open(DATA) as file:
        for line in file:
            sum += int(line)
        return sum


def sample_mean():
    """
    calculates the 'average'
    """
    n = total()
    sum = 0
    with open(DATA) as file:
        for x in file:
            sum += int(x)
    return sum / n


def sample_variance():
    """
    a measure of the spread(variability) of
    the scores in the sample on a given variable.
    s = sqrt [ Σ ( xi – x_bar )2 / ( n – 1 ) ]
    """

    n = total()
    with open(DATA) as file:
        for x in file:
            sum = (int(x) - n)**2
        return sum / (n - 1)


def sample_standard_dev():
    """
    The average of the squared differences
    from the mean.
    """
    std_dev = sample_variance()
    return sqrt(std_dev)


def median():
    """
    calculates the median for a dataset.
    """
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
        ordered = sorted(items)
        size = total()
        if size % 2 == 0:
            middle = int(size / 2)
            return ordered[middle]
        else:
            middle = size // 2
            return ordered[middle]


def min():
    """
    one way to compute the minimum
    number in the dataset.
    """
    DATA = 'sample_dataset'
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
    i = 0
    min = items[0]
    while i < len(items):
        if items[i] < min:
            min = items[i]
        i += 1
    return min


def max():
    """
    one way to compute the max
    number in the dataset.
    """
    DATA = 'sample_dataset'
    items = []
    with open(DATA) as file:
        for x in file:
            items.append(int(x))
    max = items[0]
    i = 0
    while i < len(items):
        if items[i] > max:
            max = items[i]
        i += 1
    return max


print(total())
print(summation())
print(sample_mean())
print(sample_variance())
print(sample_standard_dev())
print(median())
print(min())
print(max())