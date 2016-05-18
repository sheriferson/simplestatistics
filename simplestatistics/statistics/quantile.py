def get_q_value(data, p):
    q = len(data) * p

    for index in range(len(data)):
        if (index + 1) >= q:
            return(data[index])

def quantile(data, p = [0, .25, .5, .75, 1]):
    """
    Quantiles_ are "are cutpoints dividing the range of a probability distribution 
    into contiguous intervals with equal probabilities, or dividing the observations 
    in a sample in the same way".
    This function assumes the data provided is a statistical population, not sample.

    Consider the first example below:

        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], .25)
        7

    Given the probability 0.25, 7 is the value below which you can find 25%
    of the values after the data is sorted.

    .. _Quantiles: https://en.wikipedia.org/wiki/Quantile

    Args:
        data: The sample. A list of numerical objects.
        p: Can be a numerical object (int or float) indicating one quantile, or a list of
            numerical objects indicating several quantiles.
            p is `[0, 0.25, 0.5, 0.75, 1]` by default.

    Returns:
        A numerical object if provided p was a single value, or a list of quantiles
        if provided p was a list.
        The list will be returned in the order of quantiles provided.

    Examples:

        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], .25)
        7
        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], .5)
        9
        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], .75)
        15
        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], 1)
        20
        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20])
        [3, 7, 9, 15, 20]
        >>> quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], [.75, .25])
        [15, 7]
    """
    # this function needs a list
    if type(data) is not list:
        raise TypeError("quantile expects a list of numerical objects.")
    
    data.sort()

    n = len(data)

    if type(p) in [int, float]:
        return(get_q_value(data, p))
    elif type(p) is list:
        quantiles = []
        for prob in p:
            quantiles.append(get_q_value(data, prob))

        return(quantiles)
