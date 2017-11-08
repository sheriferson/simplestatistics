"""
Implements covariance() function.
"""

from .mean import mean

def covariance(x, y):
    """
    (Sample) Covariance_ is a measure of how two random variables vary together.
    When the greater values of one variable correspond to the greater values of
    the other variable, this is a positive covariance. Whereas when the greater values
    of one variable correspond to the lesser values of the other variable, this is
    negative covariance.

    .. _Covariance: https://en.wikipedia.org/wiki/Covariance

    This `Cross Validated answer`_ provides a good explanation of the difference
    between covariance and correlation. Covariance is understood in the context
    of the units and scales involved.  You cannot compare covariances across those
    contexts. A correlation is a "normalized" covariance that will always be a value
    between -1 and 1 and takes into account the scale of the variables.

    .. _`Cross Validated answer`: http://stats.stackexchange.com/a/18089

    Equation:
        .. math::
            q_{jk} = \\frac{1}{N - 1} \\sum\\limits_{i=1}^N (X_{ij}
            - \\bar{X_j}) (X_{ik} - \\bar{X_k})

    Args:
        x: A list of numerical objects.
        y: A list of numerical objects that has the same length as x.

    Returns:
        A numerical object.

    Examples:
        >>> covariance([1,2,3,4,5,6], [6,5,4,3,2,1])
        -3.5
        >>> covariance([1,2,3], [4, 4.5, 5])
        0.5

        >>> covariance(2, 3) # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: To calculate covariance you need lists or tuples of equal length...
        >>> covariance([2, 4], [6, 6.5, 7]) # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: To calculate covariance you need lists or tuples of equal length...
        >>> covariance([1], [-1])
        Traceback (most recent call last):
            ...
        ValueError: covariance requires lists of equal length where length is > 1.
    """

    if type(x) not in [list, tuple] or type(y) not in [list, tuple]:
        raise ValueError("To calculate covariance you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) != len(y):
        raise ValueError("To calculate covariance you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) <= 1 or len(y) <= 1:
        raise ValueError("covariance requires lists of equal length where length is > 1.")

    xmean = mean(x[:])
    ymean = mean(y[:])

    covsum = 0
    n = len(x)

    for ii in list(range(n)):
        covsum += (x[ii] - xmean) * (y[ii] - ymean)

    bessels_correction = n - 1

    return(covsum / bessels_correction)
