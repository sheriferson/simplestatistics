"""
Implements harmonic_mean() function.
"""

from .mean import mean

def harmonic_mean(x):
    """
    The `harmonic mean`_ is a kind of average that is calculated as
    the reciprocal_ of the arithmetic mean of the reciprocals.
    It is appropriate when calculating averages of rates_.

    .. _`harmonic mean`: https://en.wikipedia.org/wiki/Harmonic_mean
    .. _reciprocal: https://en.wikipedia.org/wiki/Multiplicative_inverse
    .. _rates: https://en.wikipedia.org/wiki/Rate_(mathematics)

    Equation:
        .. math::
            H = \\frac{n}{\\frac{1}{x_1}+\\frac{1}{x_2}+\\ldots+\\frac{1}{x_n}} =
            \\frac{n}{\\sum\\limits_{i=1}^n \\frac{1}{x_i}}

    Args:
        x: A list or tuple of numerical objects.

    Returns:
        A numerical object.

    Raises:
        TypeError: If the user passes something other than list or tuple.

    Examples:
        >>> harmonic_mean([1, 2, 4])
        1.7142857142857142
        >>> harmonic_mean(7)
        Traceback (most recent call last):
            ...
        TypeError: harmonic_mean() expects a list or a tuple.
    """

    if type(x) not in [list, tuple]:
        raise TypeError('harmonic_mean() expects a list or a tuple.')

    reciprocals = [1 / float(num) for num in x]
    # sum_of_reciprocals = sum(reciprocals[:])

    return(1 / mean(reciprocals))
