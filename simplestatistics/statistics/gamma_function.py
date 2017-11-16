"""
Implements gamma_function().
"""

import math
from .factorial import factorial

def calculate_gamma_pdf(x):
    """
    Helper function to calculate Gamma PDF for value x.
    """
    first_part = math.sqrt(2 * math.pi / x)
    second_part = pow((1 / math.e) * (x + (1 / ((12*x) - (1/10*x)))), x)

    return(first_part * second_part)

def gamma_function(x, decimals=6):
    """
    The gamma function is an extension of the factorial function for all
    positive integers. It is a common component in many probability
    distributions (e.g., the beta distribution).

    The probability density function (PDF) for integers is defined as:

    .. math::
        \\Gamma(n) = (n - 1)!

    Whereas for decimals/fractions we use Stirling's approximation:

    .. math::
         \\Gamma(x) \\approx \\sqrt{\\frac{2\\pi}{x}} \\bigg{(}\\frac{1}{e}
         \\bigg{(}x + \\frac{1}{12z - \\frac{1}{10z}} \\bigg{)}\\bigg{)}^x

    Args:
        x: Non-negative int or float or list of ints or floats representing
           values for which the Gamma function probability density function
           values are desired.
        decimals: (optional) number of decimal points (default is 6)

    Returns:
       Int or float (or list of ints or floats) representing the Gamma function
       probability density function values for x or each value in x.

    Examples:
        >>> gamma_function(6)
        120
        >>> gamma_function(1.2, decimals=2)
        0.92
        >>> gamma_function([6, 8, 10, 12])
        [120, 5040, 362880, 39916800]
        >>> gamma_function((3, 4))
        [2, 6]
        >>> gamma_function([3, .5], decimals=2)
        [2, 1.76]
        >>> gamma_function(-.5)
        Traceback (most recent call last):
            ...
        ValueError: gamma_function is only defined for non-negative values.
    """

    if type(x) in [list, tuple]:
        results = []
        for value in x:
            results.append(gamma_function(value, decimals=decimals))

        return(results)
    elif type(x) is float:
        if x < 0:
            raise ValueError('gamma_function is only defined for non-negative values.')

        return(round(calculate_gamma_pdf(x), decimals))
    elif type(x) is int:
        return(factorial(x - 1))
