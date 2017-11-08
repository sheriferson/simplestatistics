"""
Implements skew() function to calculate skewness of a variable
"""

# I need sane division that returns a float not int
from __future__ import division

from .decimalize import decimalize
from .mean import mean
from .sum import sum # pylint: disable=redefined-builtin

def skew(x):
    """
    Skew or `Skewness`_ is a measure of the asymmetry of the probability distribution of
    a variable around its mean.

    .. _`Skewness`: https://en.wikipedia.org/wiki/Skewness

    A positive (+ve) skewness value indicates a long tail to the **right** of the mean.

    A negative (-ve) skewness value indicates a long tail to the **left** of the mean.

    There are several equations to calculate skewness. The one used in this function is
    `Pearson's moment coefficient of skewness`_.

    .. _`Pearson's moment coefficient of skewness`: \
            https://en.wikipedia.org/wiki/Skewness#Pearson.27s_moment_coefficient_of_skewness

    Equation:
        .. math::
            \\gamma_1 = E\\Bigg[\\bigg(\\frac{(X-\\mu)^3}{\\sigma}\\bigg)\\Bigg]
            = \\frac{\\mu^3}{\\sigma^3} =
            \\frac{E[(X - \\mu)^3]}{(E[(X - \\mu)^3])^{3/2}} = \\frac{\\kappa_3}{\\kappa_2^{3/2}}

        which can be rewritten as

        .. math::
            \\gamma_1 = \\frac{\\frac{1}{n} \\sum(X - \\mu)^3}{\\frac{1}{n}
            (\\sum(X - \\mu)^2)^{3/2}}

    Args:
        x: A list of numerical objects.

    Returns:
        A numerical object.

    Examples:

        >>> skew([1, 2, 3])
        0.0
        >>> skew([1, 2, 5])
        0.5279896038431618
        >>> skew([20, 30]) # skew of a variable that contains two observations is always 0
        0.0
        >>> skew(9) # no skew for a single number/value
    """

    if type(x) in [int, float]:
        return(None)

    mean_x = decimalize(mean(x))
    n = len(x)

    m2 = sum([pow((value - mean_x), 2) for value in x]) * (1/n)
    m3 = sum([pow((value - mean_x), 3) for value in x]) * (1/n)

    m2_32 = pow(m2, 1.5)

    return(m3/m2_32)
