# I need sane division that returns a float not int
from __future__ import division

from .decimalize import decimalize
from .mean import mean
from .standard_deviation import standard_deviation

# [t-test](http://en.wikipedia.org/wiki/Student's_t-test)
#
# This is to compute a one-sample t-test, comparing the mean
# of a sample to a known value, x.
#
# in this case, we're trying to determine whether the
# population mean is equal to the value that we know, which is `x`
# here. usually the results here are used to look up a
# [p-value](http://en.wikipedia.org/wiki/P-value), which, for
# a certain level of significance, will let you determine that the
# null hypothesis can or cannot be rejected.
def t_test(sample, x):
    """
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
