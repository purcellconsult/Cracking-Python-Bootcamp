
import pytest

# Pytest Demo
# -----------


def add_nums(x, y):
    return x + y


def test_add_nums():
    assert add_nums(5, 15) == 20


# Output when ran:
# -----------------
# platform linux -- Python 3.6.7, pytest-5.0.0, py-1.8.0, pluggy-0.12.0
# rootdir: /home/doug/PycharmProjects/master_python_coursecollected 1 item
#
# 6_py_test_demo.py .                                                      [100%]

# uses raises helper to assert that some code raises an exception

def x():
    raise SyntaxError(1)


def test_x():
    with pytest.raises(SyntaxError):
        x()

# Group multiple tests in a class
# -------------------------------
# More examples of the assert statement in pytest


class TestClass(object):
    def test_one(self):
        greet = 'Hello World!'
        assert '!' in greet

    def test_two(self):
        x, y = 5, 10
        assert x < y

    def test_three(self):
        x, y, z = 5, 10, 15
        assert (x * y) != z

    def test_four(self):
        statement = True
        assert statement is True

    def test_five(self):
        money = []
        assert money is not None

