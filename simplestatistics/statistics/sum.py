from .decimalize import decimalize

def sum(data):
    """
    This function returns the sum of numerical values in a data set.

    To reduce floating-point errors, I am using an implementation of the `Kahan summation algorithm`_.

    .. _`Kahan summation algorithm`: https://en.wikipedia.org/wiki/Kahan_summation_algorithm

    The implementation is modeled after that of `simple-statistics`_.

    .. _`simple-statistics`: https://github.com/simple-statistics/simple-statistics/blob/master/src/sum.js

    Args:
        data: A numeric built-in object or list of numeric objects.

    Returns:
        A numeric object.

    Examples:
        >>> sum([1, 2, 3])
        6.0
        >>> sum([-1, 0, 1])
        0.0
        >>> sum([2.3, 0, -1.1])
        1.2
        >>> sum(4)
        4
        >>> sum((3, 2.5))
        5.5
        >>> sum('abc')
        Traceback (most recent call last):
            ...
        TypeError: sum() expects an int, list, or tuple.
    """
    current_sum = 0

    error_compensation = 0
    corrected_current_value = 0
    next_sum = 0

    if type(data) in [int, float]:
        return(data)
    elif type(data) in [list, tuple]:
        for ii in range(len(data)):
            corrected_current_value = data[ii] - error_compensation

            next_sum = current_sum + corrected_current_value

            error_compensation = next_sum - current_sum - corrected_current_value

            current_sum = next_sum

        # floating-point errors are unavoidable
        # with all measures taken above, we will still need
        # to round to 3 decimal points sometimes
        return(round(current_sum, 3))
    else:
        raise TypeError("sum() expects an int, list, or tuple.")

