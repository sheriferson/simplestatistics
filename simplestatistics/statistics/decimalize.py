"""
Implements unexposed helper function decimalize() used by other exposed
functions to arrive at better numerical accuracy and avoid floating point errors.
"""

import decimal

def decimalize(data):
    """
    Utility function converting all inputs to Decimal,
    streamlines input types for other statistics functions.

    Args:
        data: A numeric built-in object, a tuple or list of numeric objects.

    Returns:
        A Decimal object in the case of a single numeric built-in, or a list of
        Decimal objects when supplied a list or tuple of built-in numerics.

    Raises:
        TypeError: An object other than a built-in numeric or a list or tuple
        of numerics was supplied as data.

    Examples:

        >>> decimalize(1)
        Decimal('1')
        >>> decimalize([1,2,3])
        [Decimal('1'), Decimal('2'), Decimal('3')]
        >>> decimalize((1,2,3))
        [Decimal('1'), Decimal('2'), Decimal('3')]

        >>> decimalize('abc')
        Sorry, the decimalize function accepts lists or tuples of numerics
    """
    try:
        if type(data) in [int, float]:
            return(decimal.Decimal(data))
        elif type(data) == list:
            for ii, _ in enumerate(data):
                data[ii] = decimal.Decimal(data[ii])
            return data
        elif type(data) == tuple:
            data = list(data)
            for ii, _ in enumerate(data):
                data[ii] = decimal.Decimal(data[ii])
            return data
        else:
            raise TypeError
    except TypeError:
        print("Sorry, the decimalize function accepts lists or tuples of numerics")
    return
