import math
from .variance import variance

def standard_deviation(data):
    """
    >>> standard_deviation([1, 2, 3])
    1.0
    >>> standard_deviation([1, 2, 3, 4])
    1.2909944487358056
    >>> standard_deviation([-1, 0, 1, 2, 3, 4])
    1.8708286933869707
    """
    return math.sqrt(variance(data))


