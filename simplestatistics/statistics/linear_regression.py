"""
Implements linear_regression() function.
"""

# I need sane division that returns a float not int
# from __future__ import division

from .mean import mean
from .product import product

def linear_regression(x, y, decimals=2):
    """
    This is a `simple linear regression`_ that finds the line of best fit based on
    a set of points. It uses the least sum of squares to find the slope (:math:`m`)
    and y-intercept (:math:`b`). Maximum number of decimals can be set with optional
    argument decimals.

    .. _`simple linear regression`: https://en.wikipedia.org/wiki/Linear_regression

    Equation:
        .. math::
            m = \\frac{\\bar{X}\\bar{Y} - \\bar{XY}}{(\\bar{X})^2 - \\bar{X^2}}

            b = \\bar{Y} - m\\bar{X}

    Where:
        - :math:`m` is the slope.
        - :math:`b` is the y intercept.

    Returns:
        A tuple of two values: (m, b), where m is the slope and b is the y intercept.

    Examples:

        >>> linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5.5, 5.3, 6])
        (0.48, 3.62)
        >>> linear_regression([1, 2, 3, 4, 5], [2, 2.9, 3.95, 5.1, 5.9])
        (1.0, 0.97)
        >>> linear_regression([0, 1, 2, 3, 4], [1.429, 4.554, 7.679, 1.804, 13.929], decimals=3)
        (2.225, 1.429)
        >>> linear_regression((1, 2), (3, 3.5))
        (0.5, 2.5)
        >>> linear_regression([1], [2])
        (None, 2)
        >>> linear_regression(4, 5)
        >>> linear_regression([1, 2], [5])
        Traceback (most recent call last):
            ...
        ValueError: The two variables have to have the same length.
    """

    if type(x) not in [list, tuple] or type(y) not in [list, tuple]:
        return(None)
    elif len(x) != len(y):
        raise ValueError('The two variables have to have the same length.')
    elif len(x) == 1 or len(y) == 1:
        return((None, y[0]))

    mean_x = mean(x)
    mean_y = mean(y)
    mean_xy = mean(product(x, y))

    x2 = [pow(xi, 2) for xi in x]
    mean_x2 = mean(x2)

    # calculate slope
    numerator = (mean_x * mean_y) - mean_xy
    denomerator = pow(mean_x, 2) - mean_x2

    m = numerator / denomerator # slope

    # calculate y intercept
    b = mean_y - (m * mean_x)

    return(round(m, decimals), round(b, decimals))
