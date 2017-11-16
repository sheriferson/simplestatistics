"""
Implements beta() distribution function.
"""

# I need sane division that returns a float not int
from __future__ import division

from .gamma_function import gamma_function

def calculate_beta_pdf(x, _alpha, _beta):
    """
    Helper function to calculate Beta PDF for value x.
    """

    numerator = (pow(x, _alpha - 1) * pow(1 - x, _beta - 1))

    denominator = (gamma_function(_alpha, decimals=9) *
                   gamma_function(_beta, decimals=9)) / gamma_function(_alpha + _beta, decimals=9)

    return(numerator / denominator)

def beta(x, _alpha, _beta, decimals=6):
    """
    Returns probability density function for beta distribution

    .. math::
        \\text{PDF} = \\frac{x^{\\alpha - 1}(1 - x)^{\\beta - 1}}{\\text{B}(\\alpha, \\beta)}

    .. math::
        \\text{where  } \\text{B}(\\alpha, \\beta) =
        \\frac{\\Gamma(\\alpha)\\Gamma(\\beta)}{\\Gamma(\\alpha + \\beta)}

    Args:
        x: Float or list of floats between 0 and 1 representing values
            for which the Beta distribution probability density function is desired.
        _alpha: Int or float representing :math:`\\alpha`
        _beta: Int of float representing :math:`\\beta`
        decimals: (optional) number of decimal points (default is 6)

    Returns:
        Float or list of floats representing Beta distribution probability
        density function values fo x or each value in x.

    Examples:
        >>> beta(.5, 1, 3)
        0.75
	>>> beta([.01, .02, .03], 2, 5)
	[0.288179, 0.553421, 0.796764]
        >>> beta(-.5, 3, 3)
        Traceback (most recent call last):
            ...
        ValueError: The beta distribution is only defined for non-negative values.
    """

    if type(x) in [list, tuple]:
        results = []
        for value in x:
            results.append(beta(value, _alpha, _beta))
        return(results)
    elif type(x) in [int, float]:
        if x < 0:
            raise ValueError('The beta distribution is only defined for non-negative values.')
        return(round(calculate_beta_pdf(x, _alpha, _beta), decimals))
