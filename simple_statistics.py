import math
import sys

# Are you trying to use python3?
# if yes, reduce is now in functools
# ref: http://stackoverflow.com/questions/8689184/python-name-reduce-is-not-defined
if sys.version_info >= (3,0):
    from functools import reduce


"""
>>> mean([1])
1.0
>>> mean([1, 2])
1.5
>>> mean([1, 2, 3])
2.0
"""
mean = lambda data: sum(data) / float(len(data))

# geometric mean
#
# a mean function that is more useful for numbers in different
# ranges.
#
# this is the nth root of the input numbers multipled by each other
#
# This runs on `O(n)`, linear time in respect to the array
def geometric_mean(x):
    """
    >>> geometric_mean([1])
    1.0
    >>> geometric_mean([1, 10])
    3.1622776601683795
    """
    return pow(reduce(lambda v, mem: v * mem, x, 1.0), 1 / float(len(x)));

# [variance](http://en.wikipedia.org/wiki/Variance)
#
# is the sum of squared deviations from the mean
def variance(data):
    """
    >>> variance([1, 2, 3, 4, 5, 6])
    2.9166666666666665
    >>> variance([1])
    0.0
    """
    m = mean(data)
    return mean([pow(x - m, 2) for x in data]);

standard_deviation = lambda data: math.sqrt(variance(data))

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
  >>> t_test([1, 2, 3, 4, 5, 6], 3.385);
  0.1649415480881466
  """
  # Square root the length of the sample
  rootN = pow(len(sample), 0.5)
  # Compute the known value against the sample,
  # returning the t value
  return (mean(sample) - x) / (standard_deviation(sample) / rootN)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
