# I need sane division that returns a float not int
from __future__ import division

def median(data):
    """
    The median_ is "the number separating the higher half of a data sample... from the lower half."

    .. _median: https://en.wikipedia.org/wiki/Median

    If the sample has an odd number of values, the median is the value in the middle. 
    If the sample has an even number of values, the median is the mean of the two middle values.

    Args:
        data: A numeric built-in object or list of numeric objects.

    Returns:
        A float object.

    Examples:
        >>> median([1, 2, 3])
        2.0
        >>> median([1, 2, 3, 4])
        2.5
        >>> median([10, 2, -5, -1])
        0.5
        >>> median([-2])
        -2.0
        >>> median(-3)
        -3.0
        >>> median("90")
        Traceback (most recent call last):
            ...
        TypeError: median() expects an int or a list.
    """
    
    if type(data) is int:
        return(float(data))
    elif type(data) is list:
        data.sort()

        if len(data) == 1:
            return(float(data[0]))
        elif len(data) % 2 == 1:
            return(float(data[int(len(data) / 2)]))
        else:
            middleIndex = len(data) / 2
            return((data[int(middleIndex - .5)] + data[int(middleIndex + .5)]) / 2)
    else:
        raise TypeError("median() expects an int or a list.")

