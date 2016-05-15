from decimal import *

def decimalize(data):
    """Utility function converting all inputs to Decimal,
    streamlines input types for other statistics functions.

    Args:
        data: A numeric built-in object, a tuple or 
            list of numeric objects.

    Returns:
        A Decimal object in the case of a single numeric
        built-in, or a list of Decimal objects when supplied
        a list or tuple of built-in numerics.

    Raises:
        TypeError: An object other than a built-in numeric or
            a list or tuple of numerics was supplied as data.
        
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
            return(Decimal(data))
        elif type(data) == list:
            for ii in range(len(data)):
                data[ii] = Decimal(data[ii])
            return data
        elif type(data) == tuple:
            data = list(data)
            for ii in range(len(data)):
                data[ii] = Decimal(data[ii])
            return data
        else:
            raise TypeError
    except TypeError:
        print("Sorry, the decimalize function accepts lists or tuples of numerics")    
    return
