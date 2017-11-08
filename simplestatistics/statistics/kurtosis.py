"""
Implements kurtosis() function.
"""

# I need sane division that returns a float not int
from __future__ import division

from .decimalize import decimalize
from .mean import mean
from .sum import sum # pylint: disable=redefined-builtin

def kurtosis(x):
    """
    `Kurtosis`_ is a descriptor of the shape of a probability distribution.
    It is a measure of the "tailedness" of the probability distribution of a variable.

    .. _`Kurtosis`: https://en.wikipedia.org/wiki/Kurtosis

    There are several ways of calculating kurtosis. See `this page`_ for a reference.

    .. _`this page`: http://www.ats.ucla.edu/stat/mult_pkg/faq/general/kurtosis.htm

    This function is an implementation of the formula found in Sheskin (2000), which is the one
    used by SPSS and SAS by default.

    Sheskin, D.J. (2000) *Handbook of Parametric and Nonparametric Statistical
    Procedures, Second Edition*. Boca Raton, Florida: Chapman & Hall/CRC.

    Equation:
        .. math::
            \\frac{n(n+1)}{(n-1)(n-2)(n-3)}\\bigg{(}\\frac{s4}{V(x)^2}\\bigg{)}
            - 3 \\frac{(n-1)^2}{(n-2)(n-3)}

        Where

        :math:`s2 = \\sum(X-\\bar{X})^2`

        :math:`s4 = \\sum(X-\\bar{X})^4`

        :math:`V(x) = \\frac{s2}{n - 1}`

    Args:
        x: A list of numerical objects. This calculation requires **at least 4 observations**.

    Returns:
        A numerical object.

    Examples:

        >>> kurtosis([1, 2, 3, 4, 5])
        -1.1999999999999993
        >>> kurtosis([1987, 1987, 1991, 1992, 1992, 1992, 1992, 1993, 1994, 1994, 1995])
        0.4466257157411544
        >>> kurtosis(2) # no kurtosis for a single number/value
        >>> kurtosis([1, 2, 3]) # this kurtosis calculation requires at least 4 observations
    """

    if type(x) in [int, float]:
        return(None)
    elif type(x) in [list, tuple] and len(x) < 5:
        return(None)

    n = len(x)
    mean_x = decimalize(mean(x))

    s2 = sum([pow((value - mean_x), 2) for value in x])
    s4 = sum([pow((value - mean_x), 4) for value in x])
    vx = s2 / (n - 1)

    component1 = ((n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3)))

    component2 = (s4 / pow(vx, 2))

    component3 = (pow((n - 1), 2) / ((n - 2) * (n - 3)))

    return((component1 * component2) - (3 * component3))
