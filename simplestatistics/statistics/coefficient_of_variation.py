"""
Implements coefficient_of_variation() function.
"""

from .standard_deviation import standard_deviation
from .mean import mean

def coefficient_of_variation(data, sample=True):
    """
    The `coefficient of variation`_ is the ratio of the standard deviation to the mean.

    .. _`coefficient of variation`: https://en.wikipedia.org/wiki/Coefficient_of_variation

    Args:
        data: A list of numerical objects.
        sample: A boolean value. If True, calculates coefficient of variation for
          sample. If False, calculates coefficient of variation for population.

    Returns:
        A float object.
    Examples:
        >>> coefficient_of_variation([1, 2, 3])
        0.5
        >>> coefficient_of_variation([1, 2, 3], False)
        0.408248290463863
        >>> coefficient_of_variation([1, 2, 3, 4])
        0.5163977794943222
        >>> coefficient_of_variation([-1, 0, 1, 2, 3, 4])
        1.247219128924647
    """

    return standard_deviation(data, sample) / mean(data)
