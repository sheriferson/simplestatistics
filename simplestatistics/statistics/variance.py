# I need sane division that returns a float not int
from __future__ import division

from .mean import mean
from .decimalize import decimalize

# [variance](http://en.wikipedia.org/wiki/Variance)
#
# is the sum of squared deviations from the mean
def variance(data, sample = True):
    """
    >>> variance([1]) # variance of one value is not defined
    >>> variance([4]) # variance of one value is not defined
    >>> variance([1, 2, 3, 4])
    1.6666666666666667
    >>> variance([1, 2, 3, 4], sample = False)
    1.25
    >>> variance([1, 2, 3, 4, 5, 6])
    3.5
    >>> variance([-2, -1, 0, 1, 2])
    2.5
    """
    if len(data) < 2:
        return(None)

    data = decimalize(data)
    m = mean(data)
    if sample:
        return(float(sum([pow(x -m, 2) for x in data]) / (len(data) - 1)))
    else:
        return(float(mean([pow(x - m, 2) for x in data])))

