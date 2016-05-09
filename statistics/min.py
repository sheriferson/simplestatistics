def min(data):
    """
    >>> min([1, 2, 3])
    1
    >>> min([-3, 0, 3])
    -3
    >>> min([0, 1, 3, -5, 6])
    -5
    >>> min([-2])
    -2
    >>> min(-3)
    -3
    """

    if type(data) is list:
        min_value = data[0]
        for ii in data:
            if ii < min_value:
                min_value = ii
    elif type(data) is int or type(data) is float:
        min_value = data

    return(min_value)

