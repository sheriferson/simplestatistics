"""
Implements product() function.
"""

def product(x, y):
    """
    This function calculates the product of two vectors or lists of numerical objects, like so:

    .. math::
        [x_1, x_2, x_3, x_4] \\times [y_1, y_2, y_3, y_4] = [x_1y_1, x_2y_2, x_3y_3, x_4y_4]


    Args:
        x: An int or a float, or a list or tuple of numerical objects.
        y: An int or a float, or a list or tuple of numerical objects. If a\
                list or tuple, must have the same length as x.

    Returns:
        A list of numerical objects of the same length as x and y.

    Examples:

        >>> product([1, 2, 3], [1, 2, 3])
        [1, 4, 9]
        >>> product((2, 3), (3, -1))
        [6, -3]
        >>> product([1.25, 2.75], [2.5, 3.40])
        [3.125, 9.35]
        >>> product(2, [1, 2, 3])
        [2, 4, 6]
        >>> product([-3, -2, -1], 3)
        [-9, -6, -3]
        >>> product(5.5, 6.4)
        35.2

        >>> product('a', [2, 4])
        Traceback (most recent call last):
            ...
        TypeError: product() expects ints, floats, lists, or tuples of numbers.
        >>> product([1, 2], [3, 4, 5])
        Traceback (most recent call last):
            ...
        ValueError: The two lists or tuples have to have equal lengths
    """
    # product can work with two list, two tuples, two ints,
    # or an int and one of the others
    if type(x) not in [int, float, list, tuple] or type(y) not in [int, float, list, tuple]:
        raise TypeError('product() expects ints, floats, lists, or tuples of numbers.')

    # if you provide lists or tuples, they have to have the same length
    # for now
    if type(x) in [list, tuple] and type(y) in [list, tuple] and len(x) != len(y):
        raise ValueError('The two lists or tuples have to have equal lengths')

    product_vector = []

    # I'm not very happy with this if-else heavy implementation
    # but can't think of how to do this in a smarter more dynamic way

    # if both are ints, return their product
    if type(x) in [int, float] and type(y) in [int, float]:
        return(x * y)

    # if x is int, y must be a float, list, or tuple
    elif type(x) in [int, float]:
        for ii, _ in enumerate(y):
            product_vector.append(x * y[ii])

    # if y is int, x must be a float, list, or tuple
    elif type(y) in [int, float]:
        for ii, _ in enumerate(x):
            product_vector.append(x[ii] * y)

    # else, both are lists or tuples
    else:
        for ii, _ in enumerate(x):
            product_vector.append(x[ii] * y[ii])

    return(product_vector)
