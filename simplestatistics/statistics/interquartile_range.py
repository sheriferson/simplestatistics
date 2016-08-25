from .quantile import quantile

def interquartile_range(x):
    """
    The `interquartile range`_ is the difference between the third
    and first quartiles of a numerical list. It is a measure of
    dispersion, or the spread of a distribution.

    .. _`interquartile range`: https://en.wikipedia.org/wiki/Interquartile_range

    Args:
        x: A list or tuple of numerical objects.

    Returns:
        An int or float of the difference between third and first quartiles.

    Examples:
        >>> interquartile_range([1, 2, 3, 4])
        2
        >>> interquartile_range([1, 3, 5, 7])
        4
        >>> interquartile_range(4)
        Traceback (most recent call last):
            ...
        TypeError: interquartile_range() expects a list or tuple.
    """

    if type(x) not in [list, tuple]:
        raise TypeError('interquartile_range() expects a list or tuple.')

    x.sort()

    q1 = quantile(x, .25)
    q3 = quantile(x, .75)

    return(q3 - q1)
