"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.
"""

from math import sqrt

def find_next_square(sq):

    def is_square(n):
        if n >= 0:
            square_root = sqrt(n)
            if square_root % 1 == 0:
                return True

        return False

    if is_square(sq):
        next_square_root = sqrt(sq) + 1
        next_square = int(next_square_root ** 2)

    else:
        next_square = -1

    return next_square

print(find_next_square(155))
