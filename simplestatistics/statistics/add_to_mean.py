"""
Implements add_to_mean() function.
"""

from .sum import sum # pylint: disable=redefined-builtin

def add_to_mean(current_mean, n, new_value, decimals=2):
    """
    This function can be used when wanting to know the new mean of a list
    after adding one or more values to it.

    One could use this function instead of recalculating the new mean by
    adding all the old values with the new one and dividing by n (where n is
    the new total number of items in the list).

    Args:
        current_mean: Mean of the list pre-new value.
        n: Number of items in the list pre-new value.
        new_value: An int, float, or list of ints and/or flots of the new value(s)
        decimals: (optional) number of decimal points (default is 2)

    Returns:
        A float object denoting the new mean.

    Examples:
        >>> add_to_mean(20, 4, 10)
        18.0
        >>> add_to_mean(40, 4, (10, 12))
        30.33
        >>> add_to_mean(0, 3, (10, -10, 0))
        0.0
        >>> add_to_mean(50, 0, 5)
        Traceback (most recent call last):
            ...
        ValueError: Current n must be an integer greater than 0.
        >>> add_to_mean(16, 8, ('5')) # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        TypeError: add_to_mean() requires the new value(s) ... ints and/or floats.
    """

    old_sum = current_mean * n

    # sanity check the provided n
    if n <= 0 or not isinstance(n, int):
        raise ValueError('Current n must be an integer greater than 0.')

    if isinstance(new_value, (int, float)):
        new_sum = old_sum + new_value

        return(round(new_sum / (n + 1), decimals))


    elif type(new_value) in [list, tuple]:
        new_sum = old_sum + sum(new_value)

        return(round(new_sum / (n + len(new_value)), decimals))

    else:
        raise TypeError('add_to_mean() requires the new value(s) to be an int, '
                        'float, or a list or tuple of ints and/or floats.')
