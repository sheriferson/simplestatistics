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
def geometric_mean(x):
    """
    >>> geometric_mean([1])
    1.0
    >>> geometric_mean([1, 10])
    3.1622776601683795
    """
    return pow(reduce(lambda v, mem: v * mem, x, 1.0), 1 / float(len(x)))

