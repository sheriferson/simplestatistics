"""
Implements factorial() function.
"""

from .factorial import factorial

def choose(n, k):
    """
    The choose function calculates the `binomial coefficient`_
    as used in combinatorics and other counting problems.

    .. _`binomial coefficient`: https://en.wikipedia.org/wiki/Binomial_coefficient

    The binomical coefficient, written as :math:`n \\choose k`
    and often read aloud as ':math:`n` choose :math:`k`'
    is the answer to the question "how many ways are there to choose
    :math:`k` elements, regardless of their order, from a set of :math:`n`
    elements?".

    Equation:
        .. math::
            \\frac{n!}{k! (n - k)!}

    Args:
        n: An integer.
        k: An integer.

    Returns:
        An integer.

    Examples:

        >>> choose(5, 3)
        10

        >>> choose(2.1, 5)
        Traceback (most recent call last):
            ...
        TypeError: choose() expects both n and k to be integers
    """

    # choose works with integers
    if type(n) is float or type(k) is float:
        raise TypeError('choose() expects both n and k to be integers')

    numerator = factorial(n)
    denomerator = factorial(k) * factorial(n - k)

    return(int(numerator / denomerator))
