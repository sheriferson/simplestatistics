"""
Implements normal() function with norm_single_calculation() helper function.
"""

import math

def norm_single_calculation(x, mean, standard_deviation):
    """
    Helper function that calculates normal density function for a particular
    x with a given mean and stadard deviation.
    """
    # break the normal distribution probability density function
    # into two components

    # component 1
    #   1 / (sqrt(2 * sd^2 * pi))

    # component 2
    #   e ^ (- (x - mean) ^ 2 / 2 sd^2)

    # x = decimalize(x)
    # mean = decimalize(mean)
    # standard_deviation = decimalize(standard_deviation)

    # before we do a lot of math, let's check if sd is 0
    if standard_deviation == 0:
        return(0)

    # component 1
    comp1 = 1 / (math.sqrt(2 * pow(standard_deviation, 2) * math.pi))

    # component 2
    comp2 = pow(math.e, (-1 * (pow(x - mean, 2)) / (2 * pow(standard_deviation, 2))))

    # return the product of the two components
    return(comp1 * comp2)

def normal(x, mean, standard_deviation):
    """
    The `Normal Distribution`_ is, quoting from the Wikipedia page:

        A very common continuous probability distribution. Normal distributions
        are important in statistics and are often used in the natural and social
        sciences to represent real-valued random variables whose distributions are not known.

        The normal distribution is useful because of the central limit theorem.
        In its most general form, under some conditions (which include finite variance),
        it states that averages of random variables independently drawn from independent
        distributions converge in distribution to the normal, that is, become normally
        distributed when the number of random variables is sufficiently large. Physical
        quantities that are expected to be the sum of many independent processes (such
        as measurement errors) often have distributions that are nearly normal. Moreover,
        many results and methods (such as propagation of uncertainty and least squares
        parameter fitting) can be derived analytically in explicit form when the
        relevant variables are normally distributed.

    .. _`Normal Distribution`: https://en.wikipedia.org/wiki/Normal_distribution

    Probability density function equation:
        .. math::
            f(x \\mid \\mu, \\sigma^2) = \\frac{1}{\\sqrt{2 \\sigma^2 \\pi}}
            e^{-\\frac{(x - \\mu)^2}{2\\sigma^2}}

    Args:
        x: Int or float or list of ints or floats representing values for which
        the normal distribution density is desired.
        mean: Mean of the sample or population.
        standard_deviation: Standard deviation of the sample or population.

    Returns:
        Float or (or list of floats if provided x was a list)
        representing the normal distribution density function for x
        or each value in x.

    Examples:
        >>> normal(4, 8, 2)
        0.02699548325659403
        >>> normal([1, 4], 8, 2)
        [0.00043634134752288024, 0.02699548325659403]
        >>> normal(4, 8, 0)
        0
    """

    if type(x) in [int, float]:
        return(norm_single_calculation(x, mean, standard_deviation))
    elif type(x) in [list, tuple]:
        norm_distribution_list = [norm_single_calculation(value, mean, standard_deviation)
                                  for value in x]

        return(norm_distribution_list)
