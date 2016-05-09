def max(data):
    """
    >>> max([1, 2, 3])
    3
    >>> max([-3, 0, 3])
    3
    >>> max([-2])
    -2
    >>> max(-3)
    -3
    """

    if type(data) is list:
        max_value = data[0]
        for ii in data:
            if ii > max_value:
                max_value = ii
    elif type(data) is int or type(data) is float:
        max_value = data

    return(max_value)

