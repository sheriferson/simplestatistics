"""
Implements tanh() function.
"""

from .sinh import sinh
from .cosh import cosh

def tanh(x, decimals=5):
    """
    The hyperbolic tan, analogous to the trigonometric tan.

    Hyperbolic functions are defined on a parabola whereas trigonometric
    functions are defined on a circle.

    There are -- at least -- two different equations that produce
    the same results when calculating :math:`tanh`. One found on the Wikipedia
    page for hyperbolic functions:

        .. math::
            \\text{tanh}(x) = \\frac{1 - e^{-2x}}{1 + e^{-2x}}

    And a simpler equation found on this reference_ page by Erik Max Francis:

    .. _reference: http://www.alcyone.com/max/reference/maths/hyperbolic.html

        .. math::
            \\text{tanh}(x) = \\frac{sinh(x)}{cosh(x)}

    Args:
        x: int or float

    Returns:
        A float object denoting the hyperbolic tan of input.

    Examples:
        >>> tanh(3)
        0.99505
        >>> tanh(0.2)
        0.19738
        >>> tanh('c')
        Traceback (most recent call last):
            ...
        TypeError: tanh expects an integer or float.
    """

    if type(x) not in [int, float]:
        raise TypeError('tanh expects an integer or float.')

    return(round(sinh(x) / cosh(x), ndigits=decimals))
