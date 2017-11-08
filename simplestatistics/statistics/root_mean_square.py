"""
Implement root_mean_square() function.
"""

import math
from .sum import sum # pylint: disable=redefined-builtin

def root_mean_square(x):
    """
    Root mean square (RMS) is the square root of the sum of the squares of values in a list
    divided by the length of the list. It is a mean function that measures the magnitude
    of values in the list regardless of their sign.

    Args:
        x: A list or tuple of numerical objects.

    Returns:
        A float of the root mean square of the list.

    Examples:
        >>> root_mean_square([-1, 1, -1, 1])
        1.0
        >>> root_mean_square((9, 4))
        6.96419413859206
        >>> root_mean_square(9)
        Traceback (most recent call last):
            ...
        TypeError: root_mean_square() expects a list or a tuple.
    """

    if type(x) not in [list, tuple]:
        raise TypeError('root_mean_square() expects a list or a tuple.')

    squares = []

    squares = [pow(num, 2) for num in x]
    sum_of_squares = sum(squares)
    ms = sum_of_squares / len(x)
    rms = math.sqrt(ms)

    return(rms)
