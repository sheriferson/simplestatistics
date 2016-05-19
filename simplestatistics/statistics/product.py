def product(x, y):
    """
    This function calculates the product of two vectors or lists of numerical objects, like so:

    .. math::
        [x_1, x_2, x_3, x_4] \\times [y_1, y_2, y_3, y_4] = [x_1y_1, x_2y_2, x_3y_3, x_4y_4]


    Args:
        x: A list or tuple of numerical objects.
        y: A list or tuple (same type as x) of numerical objects. Must have the same length as x.

    Returns:
        A list of numerical objects of the same length as x and y.

    Examples:

        >>> product([1, 2, 3], [1, 2, 3])
        [1, 4, 9]
        >>> product((2, 3), (3, -1))
        [6, -3]
        >>> product([1.25, 2.75], [2.5, 3.40])
        [3.125, 9.35]
    """
    if type(x) not in [list, tuple] or type(y) not in [list, tuple]:
        raise TypeError("product() expects lists or tuples of equal length")

    if len(x) != len(y):
        raise ValueError("The two lists or tuples have to have equal lengths.")

    product_vector = []

    for ii in range(len(x)):
        product_vector.append(x[ii] * y[ii])

    return(product_vector)
