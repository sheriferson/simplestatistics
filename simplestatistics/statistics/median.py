# I need sane division that returns a float not int
from __future__ import division

def median(data):
    """
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

