from .choose import choose
from .decimalize import decimalize

def binom_single_calculation(k, n, p):
    # break the binomial distribution into three components
    # 1. n choose k
    component_1 = choose(n, k)

    # 2. p to the power k
    component_2 = pow(p, k)

    # 3. (1 - p) to the power (n - k)
    component_3 = pow((1 - p), (n - k))

    # return the product of the three components
    return(float(component_1 * component_2 * component_3))

def binomial(k, n, p):
    """
    The `Binomial Distribution`_ is, quoting from the Wikipedia
    page:

        In probability theory and statistics, the binomial distribution 
        with parameters n and p is the discrete probability distribution 
        of the number of successes in a sequence of n independent 
        yes/no experiments, each of which yields success with 
        probability p.

    .. _`binomial distribution`: https://en.wikipedia.org/wiki/Binomial_distribution

    Probability mass function equation:
        .. math::
           f(k; n, p) = Pr(X = k) = \\binom{n}{k} p^k (1 - p)^{n-k}


    Args:
        k: Int or list of ints representing number of choices or successes.
        n: Int representing total number of trials.
        p: Float representing probability of success per trial.

    Returns:
        Float (or list of floats, if provided k was a list) 
        representing probabilities of obtaining each k according to 
        the binomial distribution.

    Examples:

        >>> binomial(4, 12, 0.2)
        0.13287555072
        >>> binomial([1, 2, 3], 10, 0.5)
        [0.009765625, 0.0439453125, 0.1171875]

        >>> binomial(4, 10, 1.5)
        Traceback (most recent call last):
            ...
        ValueError: probability cannot be greater than 1 or smaller than 0
    """

    # probability has to be between 0 and 1
    if p > 1 or p < 0:
        raise ValueError('probability cannot be greater than 1 or smaller than 0')

    # decimalize probability to get
    # better precision
    p = decimalize(p)

    if type(k) in [int, float]:
        return(binom_single_calculation(k, n, p))
    elif type(k) in [list, tuple]:
        binom_distribution_list = [binom_single_calculation(value, n, p) for value in k]

        return(binom_distribution_list)
