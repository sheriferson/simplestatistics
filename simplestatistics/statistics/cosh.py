"""
Implements cosh() function.
"""

from math import e # 2.718...

def cosh(x, decimals=5):
    """
    The hyperbolic cos, analogous to the trigonometric cos.

    Hyperbolic functions are defined on a parabola whereas trigonometric
    functions are defined on a circle.

    There are -- at least -- two different equations that produce
    the same results when calculating :math:`cosh`. One found on
    the Wikipedia page for hyperbolic functions:

        .. math::
            \\text{cosh}(x) = \\frac{1 + e^{-2x}}{2e^{-x}}

    And a simpler equation found on this reference_ page by
    Erik Max Francis:

    .. _reference: http://www.alcyone.com/max/reference/maths/hyperbolic.html

        .. math::
            \\text{cosh}(x) = \\frac{e^x + e^{-x}}{2}

    I implemented the second version for simplicity.

    Args:
        x: int or float

    Returns:
        A float object denoting the hyperbolic cos of input.

    Examples:
        >>> cosh(2)
        3.7622
        >>> cosh(2.5)
        6.13229
        >>> cosh('c')
        Traceback (most recent call last):
            ...
        TypeError: cosh expects an integer or float.

    """
    if type(x) not in [int, float]:
        raise TypeError('cosh expects an integer or float.')

    result = (1 + pow(e, -2 * x)) / (2 * pow(e, -x))

    return(round(result, decimals))
