"""
Implements gamma_function().
"""

from .factorial import factorial

def gamma_function(x):
    """
    The gamma function is an extension of the factorial function for all
    positive integers. It is a common component in many probability
    distributions (e.g., the beta distribution).

    .. math::
        \\gamma = (n - 1)!

    Examples:
        >>> gamma_function(6)
        120
        >>> gamma_function([6, 8, 10, 12])
        [120, 5040, 362880, 39916800]
        >>> gamma_function((3, 4))
        [2, 6]
        >>> gamma_function([3, .5])
        Traceback (most recent call last):
            ...
        TypeError: factorial() expects a positive integer or list of positive integers.

    """

    if type(x) in [list, tuple]:
        results = []
        for value in x:
            results.append(factorial(value - 1))

        return(results)
    elif type(x) is int:
        return(factorial(x - 1))
