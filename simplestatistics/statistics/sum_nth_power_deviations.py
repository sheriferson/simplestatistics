"""
Implements sum_nth_power_deviations(x, n), which gives the sum of each value
in x (from the mean) to the Nth power.
"""

from .mean import mean
from .sum import sum # pylint: disable=redefined-builtin

def sum_nth_power_deviations(x, n):
    """
    The sum of the deviations of each value (from the mean) to the Nth
    power.

    Args:
        x: List or tuple of numerical objects.
        n: Power to raise each deviation from the mean.

    Returns:
        Float of the sum of the deviations from the mean raised to Nth power.

    Examples:
        >>> sum_nth_power_deviations([1, 2, 3], 2)
        2.0
        >>> sum_nth_power_deviations([-1, 0, 2, 4], 3)
        7.875
        >>> sum_nth_power_deviations(4, 3)
        Traceback (most recent call last):
            ...
        TypeError: sum_nth_power_deviations() expects the data to be a list or tuple.
    """

    if type(x) not in [list, tuple]:
        raise TypeError('sum_nth_power_deviations() expects the data to be a list or tuple.')

    m = mean(x[:])

    n_deviations = [pow(num - m, n) for num in x]

    return(sum(n_deviations))
