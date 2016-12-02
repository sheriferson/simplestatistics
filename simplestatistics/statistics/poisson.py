import math # to use math.e to get Euler's number
from .factorial import factorial

def poisson(lam, k = list(range(0, 21)), decimals = 4):
    """
    The `Poisson distribution`_ is, quoting from the Wikipedia page:

        ... a discrete probability distribution that expresses the probability of a given
        number of events occurring in a fixed interval of time and/or space if these events
        occur with a known average rate and independently of the time since the last event.

    .. _`Poisson distribution`: https://en.wikipedia.org/wiki/Poisson_distribution

    This function calculates the probability of events for a Poisson distribution.

    An event can occur 0, 1, 2,... times in an interval.
    The average number of events in an interval is designated :math:`\\lambda` (lambda).
    Lambda is the event rate, also called the rate parameter. The probability of observing
    :math:`k` events in an interval is given by the equation:

        .. math::
            P(k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}

    :math:`\\lambda` is the average number of events per interval

    :math:`e` is the number 2.71828... (Euler's number)

    :math:`k` is the number of events, takes values 0, 1, 2...

    If provided with a :math:`k` value or list of values, the function will return
    the probabilities for those values. Otherwise, the function will return
    the probabilities for k = [0, 1, 2... 20].

    Args:
        lam: Value for *lambda*. Has to be a positive value
        k: Value for *k*. Default is [0, 1, 2... 20]
        decimals: (optional) number of decimal points (default is 4)

    Returns:
        A value or list of values for the probability(ies) of observing the one
        or more provided *k* values given provided *lamda*.

    Examples:
        >>> poisson(3, 3)
        0.224
        >>> poisson(3, [0, 1, 2, 3])
        [0.0498, 0.1494, 0.224, 0.224]
        >>> poisson(5.5, 7)
        0.1234

        >>> poisson(-3)
        Traceback (most recent call last):
            ...
        ValueError: lambda has to be a positive value.

    """
    if lam <= 0:
        raise ValueError('lambda has to be a positive value.')

    if type(k) is int:
        p = (pow(math.e, -lam) * pow(lam, k)) / factorial(k)
        return(round(p, decimals))

    elif type(k) is list:
        ps = []
        for kx in k:
            p = (pow(math.e, -lam) * pow(lam, kx)) / factorial(kx)
            ps.append(round(p, decimals))

        return(ps)
