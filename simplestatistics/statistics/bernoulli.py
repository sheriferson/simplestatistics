from .binomial import binomial

def bernoulli(p, decimals = 2):
    """
    The `Bernoulli Distribution`_ is, quoting from the Wikipedia page:

        The Bernoulli distribution is the probability discrete distribution of a random
        variable which takes value 1 with success probability p and value 0 with failure
        probability q = 1 - p. It can be used, for example, to represent the toss of a coin,
        where "1" is defined to mean "heads" and "0" is defined to mean "tails" (or vice versa).
        It is a special case of a Binomial Distribution where n = 1.

    .. _ `bernoulli distribution`: https://en.wikipedia.org/wiki/Bernoulli_distribution

    Args:
        p: Int or float representing *p* (probability)
        decimals: (optional) number of decimal points (default is 2)

    Returns:
        List of the distribution values for the variable taking values 0, 1.

    Examples:
        >>> bernoulli(0.5)
        [0.5, 0.5]
        >>> bernoulli(0.25)
        [0.75, 0.25]
        >>> bernoulli(0.3)
        [0.7, 0.3]
        >>> bernoulli(1.1)
        Traceback (most recent call last):
            ...
        ValueError: Probability (p) must be between 0 and 1.
    """

    if p < 0 or p > 1:
        raise ValueError('Probability (p) must be between 0 and 1.')

    probabilities = binomial([0, 1], 1, p)
    probabilities = [round(x, decimals) for x in probabilities]

    return(probabilities)

