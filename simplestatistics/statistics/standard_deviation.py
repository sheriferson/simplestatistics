import math
from .variance import variance

def standard_deviation(data):
    """
    The `standard deviation`_ is the square root of variance_ (the sum of squared deviations
    from the mean).
    The standard deviation is a commonly used measure of the variation and distance of
    a set of values in a sample from the mean of the sample.

    .. _`standard deviation`: https://en.wikipedia.org/wiki/Standard_deviation
    .. _variance: http://en.wikipedia.org/wiki/Variance

    Equation:

        .. math::
            \\sigma = \\sqrt{\\frac{\\sum (x - \\mu)^2}{N - 1}}

        In English:
            - Obtain the difference between each value and the mean.
            - Square those values.
            - Sum the squared values.
            - Divide by the number of values - 1 (to correct for the sampling).
            - Obtain the square root of the result.

    Args:
        data: A list of numerical objects.

    Returns:
        A float object.

    Examples:

        >>> standard_deviation([1, 2, 3])
        1.0
        >>> standard_deviation([1, 2, 3, 4])
        1.2909944487358056
        >>> standard_deviation([-1, 0, 1, 2, 3, 4])
        1.8708286933869707
    """
    return math.sqrt(variance(data))


