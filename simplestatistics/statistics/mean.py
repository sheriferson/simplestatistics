# I need sane division that returns a float not int
from __future__ import division

def mean(data):
    """
    >>> mean([1])
    1.0
    >>> mean([1, 2])
    1.5
    >>> mean([1, 2, 3])
    2.0
    >>> mean([-1, 0, 1, 2, 3])
    1.0
    """
    return sum(data) / len(data)

