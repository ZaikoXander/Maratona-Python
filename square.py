""" * Task *

Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. """

from math import sqrt

def is_square(n):
    if n >= 0:
        square_root = sqrt(n)
        if square_root % 1 == 0:
            return True

    return False

print(is_square(25))
