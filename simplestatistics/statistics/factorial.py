"""
Implements factorial() function, and helper function obtain_factorial().
"""

def obtain_factorial(x):
    """
    Helper function obtain_factorial() for the factorial() function.
    Given value x, it returns the factorial of that value.
    """
    product = 1
    for ii in list(range(x)):
        product = product * (ii + 1)

    return(product)

def factorial(x):
    """
    The factorial_ (denoted :math:`n!`) is the product of all positive
    integers less than or equal to a positive integer (:math:`n`).

    .. _factorial: https://en.wikipedia.org/wiki/Factorial

    Equation:
        .. math::
            n! = \\prod_{k=1}^n k

    Args:
        x: A numeric built-in object, or a list of numeric built-in objects for :math:`n`

    Returns:
        A numerical (int) object.

    Examples:

        >>> factorial(5)
        120
        >>> factorial(1)
        1
        >>> factorial(20)
        2432902008176640000
        >>> factorial([1, 5, 20])
        [1, 120, 2432902008176640000]

        >>> factorial(-2)
        Traceback (most recent call last):
            ...
        ValueError: factorial() expects a positive integer.
        >>> factorial(4.5)
        Traceback (most recent call last):
            ...
        TypeError: factorial() expects a positive integer or list of positive integers.
        >>> factorial([2, 3, 'a'])
        Traceback (most recent call last):
            ...
        ValueError: Perhaps you provided a list that contains non-integers.
    """

    if type(x) is int:
        if x < 0:
            raise ValueError('factorial() expects a positive integer.')

        return(obtain_factorial(x))
    elif type(x) is list:
        try:
            products = []
            for element in x:
                products.append(obtain_factorial(element))

            return(products)
        except:
            raise ValueError('Perhaps you provided a list that contains non-integers.')
    else:
        raise TypeError('factorial() expects a positive integer or list of positive integers.')
