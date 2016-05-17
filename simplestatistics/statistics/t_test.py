# I need sane division that returns a float not int
from __future__ import division

from .decimalize import decimalize
from .mean import mean
from .standard_deviation import standard_deviation

def t_test(sample, x):
    """
    A one-sample `t-test`_ is a test that compares the mean of a sample to a known value, x.

    In this case, we're trying to determine whether the sample mean is equal to the value
    that we know, which is `x`. Usually the results are used to look up a `p-value`_, which,
    for a certain level of significance, will let you determine whether the null hypothesis
    (that there is no real difference between the mean of the sample and provided `x`) can
    be rejected or not.

    .. _`t-test`: http://en.wikipedia.org/wiki/Student's_t-test
    .. _`p-value`: http://en.wikipedia.org/wiki/P-value

    Equation:
        .. math::
            t = \\frac{\\bar{X} - \\mu}{sd_X}

    :math:`\\bar{X}` is the sample mean

    :math:`\\mu` is the provided value

    :math:`sd_X` is the sample standard deviation

    Args:
        sample: A list of numerical objects (the sample)
        x: The provided value to compare the mean of the sample to.

    Returns:
        A numerical object.

    Example:

        >>> t_test([1, 2, 3, 4, 5, 6], 3.385)
        0.150570344262835
    """

    sample = decimalize(sample)
    x = decimalize(x)

    # Square root the length of the sample
    rootN = pow(len(sample), 0.5)
    rootN = decimalize(rootN)

    # get standard deviation of sample
    sample_sd = decimalize(standard_deviation(sample))

    # Compute the known value against the sample,
    # returning the t value
    t_statistic = ((mean(sample) - x) / sample_sd) * rootN
    return(float(t_statistic))
