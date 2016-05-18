# I need sane division that returns a float not int
from __future__ import division
import sys

# Are you trying to use python3?
# if yes, reduce is now in functools
# ref: http://stackoverflow.com/questions/8689184/python-name-reduce-is-not-defined
# instead of using an if statement, I'll just import reduce from functools anyway
from functools import reduce

# geometric mean
#
# a mean function that is more useful for numbers in different
# ranges.
#
# this is the nth root of the input numbers multipled by each other
#
# This runs on `O(n)`, linear time in respect to the array
def geometric_mean(data):
    """
    The `geometric mean`_ uses the product of a set of numbers to determine their central tendency,
    as opposed to the regular arithmetic mean which uses their sum.

    .. _`geometric mean`: https://en.wikipedia.org/wiki/Geometric_mean

    Equation:
        .. math::
            \\sqrt[n]{x_1 x_2 \\dotso x_n}

    Args:
        data: A list of numeric objects.

    Returns:
        A float object.

    Examples:
        >>> geometric_mean([1])
        1.0
        >>> geometric_mean([1, 10])
        3.1622776601683795
    """
    return pow(reduce(lambda v, mem: v * mem, data, 1.0), 1 / float(len(data)))

