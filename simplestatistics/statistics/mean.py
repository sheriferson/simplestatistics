# I need sane division that returns a float not int
from __future__ import division

def mean(data):
    """
    The mean_, or *average*, is "the sum of values divided by the number of values".

    .. _mean: https://en.wikipedia.org/wiki/Mean

    Equation:
        .. math::
            \\bar{X} = \\frac{\sum X}{n}

    Args:
        data: A numeric built-in object, a tuple,
            or list of numeric objects.

    Returns:
        A float object.

    Examples:

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

