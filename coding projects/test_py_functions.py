###############################################
# Testing lab in python
# ----------------------
# Learn how to test various functions
# and methods in python using the unittest,
# pytest, nose, doctest, mock, and hypothesis.
#
# Goal. Get it to work in unittest.
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###############################################

import unittest


"""
using unittest in python:
https://docs.python.org/3/library/unittest.html
"""


class TestPythonFunctions(unittest.TestCase):
    """
    This class is used to test some of the functions
    in the builtin python library:
    https://docs.python.org/3/library/functions.html
    """

    def test_abs(self):
      self.assertEqual(1010, abs(-1010))

    def test_abs_not_equal(self):
        self.assertNotEqual(-1100, abs(-1100))

    def test_bin(self):
        self.assertEqual('0b1010', bin(10))

    def test_bool(self):
        self.assertEqual(True, 5 > 3)

    def test_callable(self):
        def fun():
            return 'YEAH BOI!!!'
            self.assertEqual(True, callable(self.fun))

    def test_chr(self):
        self.assertEqual(chr(91) + chr(93), '[]')

    def test_dict(self):
        self.assertEqual(dict(a=10, b=10, c=30, d=40, e=50), {'a': 10, 'b': 10, 'c': 30, 'd': 40, 'e': 50})

    def test_divmod(self):
        self.assertEqual(divmod(5.0, 3.0), (1.0, 2.0))

    def test_enumerate(self):
        evens = [x for x in range(1, 11) if x % 2 == 0]
        self.assertEqual(list(enumerate(evens, start=1)), [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)])

    def test_exec(self):
        self.assertEqual(eval('5 + 15'), 20)

    def test_float(self):
        self.assertEqual(float(5), 5.0)

    def test_format(self):
        self.assertEqual('Hello World', '{0} {1}'.format('Hello', 'World'))

    def test_hex(self):
        self.assertEqual(hex(65535), '0xffff')

    def test_int(self):
        self.assertEqual(int(6.65), 6)

    def test_len(self):
        self.assertEqual(5, len([1, 2, 3, 4, 5]))

    def test_list(self):
        self.assertEqual(list(range(10)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_max(self):
        self.assertEqual(100, max([1, 20, 100, 50, 75, 90]))

    def test_min(self):
        self.assertEqual(3, min(10, 20, 30, 3, 40, 50, 60))

    def test_next(self):
        x = iter([y for y in range(1, 10)])
        self.assertEqual(1, next(x))

    def test_oct(self):
        self.assertEqual('0o764', oct(500))

    def test_round(self):
        self.assertEqual(round(5.3527822, 3), 5.353)

    def test_sorted(self):
        items = [9, 5, 3, 2, 1, 0, .2329, -929, 832, 25, 8, 4, 8]
        self.assertEqual(sorted(items), [-929, 0, 0.2329, 1, 2, 3, 4, 5, 8, 8, 9, 25, 832])

    def test_sum(self):
        nums = [5, 10, 15, 20]
        self.assertEqual(sum(nums), 50)

    def test_sum_true(self):
        self.assertTrue(sum([1, 2, 3]) < 10)


if __name__ == '__main__':
    unittest.main()