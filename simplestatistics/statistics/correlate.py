# I need sane division that returns a float not int
from __future__ import division

from .z_scores import z_scores
from .product import product
from .sum import sum

def correlate(x, y):
    """
    Correlation_ refers to "the extent to which two variables have a linear
    relationship with each other".

    .. _Correlation: https://en.wikipedia.org/wiki/Correlation_and_dependence

    A correlation (usually denoted as :math:`r`) can range from 1.0 to -1.0.
    :math:`r` of 1.0 is the strongest positive correlation between two
    variables, and an :math:`r` of -1.0 is the strongest negative correlation.

    Equation:
        .. math::
            r_x,_y = \\frac{\\sum\\limits_{i=1}^n (x_i - \\bar{x})(y_i - \\bar{y})}{ns_x s_y}

    In English:
        - Get the :math:`z` (standardized) scores of x.
        - Get the :math:`z` (standardized) scores of y.
        - Get the product of the two lists of standardized scores.
        - Sum the product of standardized scores.
        - Divide by the length of x or y :math:`-` 1 (to correct for sampling).

    Args:
        x: A list of numerical objects.
        y: A list of numerical objects that has the same length as x.

    Returns:
        A numerical object.

    Examples:
        >>> correlate([1, 2, 3, 4], [1, 3, 3, 5])
        0.9486666666666667
        >>> correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, 1, 2, 3, 2, 4, 5])
        -0.9434285714285714
    """

    x = z_scores(x)
    y = z_scores(y)

    z_products = product(x, y)
    z_sum = sum(z_products)

    r = z_sum / (len(x) - 1)

    return(r)
