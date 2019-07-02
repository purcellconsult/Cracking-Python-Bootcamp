########################################
# Unit testing in python
# ----------------------
# Learn the various ways to unit test
# in python. Accompanying Google Doc:
# https://docs.google.com/presentation/d/1K8SN0TzK52700sM5QAhQii_a7KbutCwRA0wJQY8l6Z4/edit?usp=sharing
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###########################################

# Software testing is a profession in itself!
# UNITTEST
# PYTEST
# NOSE
# DOCTEST
# PYLINT
# HYPOTHESIS

# UNIT TEST MODULE
# ----------------
# A unit testing framework inspired by JUnit
# Built into the python core
# Supports test automation, sharing of setup and shutdown of code tests
# Aggregation of tests into collections and independence of tests from reporting framework


# UNIT TEST DEMO
# --------------

import unittest


class TestListMethods(unittest.TestCase):
    """
    Python list methods:
    https://docs.python.org/3/tutorial/datastructures.html
    """
    def test_append(self):
        x = [1, 2, 3]
        x.append(10)
        self.assertTrue(x, [1, 2, 3, 10])

    def test_count(self):
        cars = ['Mercedes', 'Lexus', 'Ford', 'BMW', 'Ferrari', 'Honda', 'Toyota', 'Ford']
        self.assertEqual(cars.count('Ford'), 2)

    def test_pop(self):
        fruits = ['apple', 'orange', 'tangerine', 'pineapple']
        self.assertEqual(fruits.pop(), 'pineapple')

    def test_reverse(self):
        music = ['jazz', 'r and b', 'rock and roll', 'edm']
        self.assertNotEqual(music.reverse(), music)

    def test_is_not(self):
        x = []
        y = [1]
        self.assertIsNot(x, y)

    def test_count_equal(self):
        a = [2, 4, 6]
        b = [6, 2, 4]
        self.assertCountEqual(a, b)

    # Running tests via command line
    # ------------------------------
    # The unittest module can be used from the command line
    # to run tests from modules, classes, or individual methods.

    # python -m unittest test_module1 test_module2
    # python -m unittest test_module.TestClass
    # python -m unittest test_module.TestClass.test_method

    # Common assert methods in unittest
    # ---------------------------------
    # Learn about them here: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
    # assertEqual(a, b)
    # assertNotEqual(a, b)
    # assertTrue(x)
    # assertFalse(x)
    # assertIs(a, b)
    # assertIsNot(a, b)
    # assertIsNone(x)
    # assertIsNotNone(x)
    # assertIn(a, b)
    # assertNotIn(a, b)
    # assertIsInstance(a, b)
    # assertNotIsInstance(a, b)

    # Pytest module
    # --------------
    # pytest is a framework that makes it easy to write small tests.
    # Compared to unittest it has detailed info on failing assert statements.
    #   * No need to remember self.assert *
    # Autodiscovery of test modules and functions
    # Can run unittest and nose test suites out of the box
    # Strong plugin architecture. Has 315+ external plugins.

    # Installing pytest
    # ------------------
    # in the command line run the following:
    #   $ pip3 install -U pytest
    # Test that you've installed the correct version
    #   $ pytest --version
    # In PyCharm - File -> Settings -> Tools -> Python Integration Tools -> Default test runner -> pytest

