"""
Implements sinh() function.
"""

from math import e # 2.718...

def sinh(x, decimals=5):
    """
    The hyperbolic sin, analogous to the trigonometric sin.

    Hyperbolic functions are defined on a parabola whereas trigonometric
    functions are defined on a circle.

    One of the uses of :math:`sinh` is in calculating
    `Stirling's approximation`_ for factorials, which in turn is useful for
    calculating the gamma function and the beta distribution probability
    density function.

    .. _`Stirling's approximation`: https://en.wikipedia.org/wiki/Stirling%27s_approximation

    I've come across two different equations that produce
    the same results when calculating :math:`sinh`. One found on
    the Wikipedia page for hyperbolic functions:

        .. math::
            \\text{sinh}(x) = \\frac{1 - e^{-2x}}{2e^{-x}}

    And a simpler equation found on this reference_ page by
    Erik Max Francis:

    .. _reference: http://www.alcyone.com/max/reference/maths/hyperbolic.html

        .. math::
            \\text{sinh}(x) = \\frac{e^x - e^{-x}}{2}

    I implemented the second version for simplicity.

    Args:
        x: int or float

    Returns:
        A float object denoting the hyperbolic sin of input

    Examples:
        >>> sinh(2)
        3.62686
        >>> sinh(2.2)
        4.45711
        >>> sinh('3')
        Traceback (most recent call last):
            ...
        TypeError: sinh expects an integer or float.

    """
    # Another unimplemented version that gives the same results
    # result = (pow(e, x) - pow(e, -x)) / 2

    if not isinstance(x, (int, float)):
        raise TypeError('sinh expects an integer or float.')

    result = (1 - pow(e, -2 * x)) / (2 * pow(e, -x))

    return(round(result, decimals))
