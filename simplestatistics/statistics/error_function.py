from .standard_deviation import standard_deviation
import math

def error_function(x, decimals = 2):
    """
    The error function, or `Gauss error function`_.

    .. _`Gauss error function`: https://en.wikipedia.org/wiki/Error_function

    The function returns the probability that a value in a normal distribution is between :math:`\\frac{x}{sd\\sqrt{2}}`
    and :math:`\\frac{-x}{sd\\sqrt{2}}`.

    This implementation is closely modeled after the impementation in `simple-statistics <https://github.com/simple-statistics/simple-statistics>`_,
    and returns a numerical approximation of the exact value.

    Args:
        x: A numerical object denoting sd
        decimals: number of decimal points (default is 2)

    Returns:
        Probability between 0 and 1.

    Examples:
        >>> error_function(1)
        0.84
        >>> error_function(.8, decimals = 1)
        0.7
        >>> error_function(1.01)
        0.85
        >>> error_function(-0.4)
        -0.43
        >>> error_function('.75')
        Traceback (most recent call last):
            ...
        ValueError: error_function() only accepts values of type int or float.
    """

    if type(x) not in [int, float]:
        raise ValueError('error_function() only accepts values of type int or float.')
    t = 1 / (1 + (0.5 * abs(x)))

    tau = t * math.exp( (math.pow(x, 2) * - 1) - \
        1.26551223 + \
        1.00002368 * t + \
        0.37409196 * math.pow(t, 2) + \
        0.09678418 * math.pow(t, 3) - \
        0.18628806 * math.pow(t, 4) + \
        0.27886807 * math.pow(t, 5) - \
        1.13520398 * math.pow(t, 6) + \
        1.48851587 * math.pow(t, 7) - \
        0.82215223 * math.pow(t, 8) + \
        0.17087277 * math.pow(t, 9))

    if x >= 0:
        return(round(1 - tau, decimals))
    else:
        return(round(tau - 1, decimals))

