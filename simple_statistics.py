# I need sane division that returns a float not int
from __future__ import division

from decimal import *
import math
import sys

# Are you trying to use python3?
# if yes, reduce is now in functools
# ref: http://stackoverflow.com/questions/8689184/python-name-reduce-is-not-defined
if sys.version_info >= (3,0):
    from functools import reduce

# To avoid errors resulting from floating point arithmetic
# I will use the Decimal function to convert all numbers
# to type decimal before calculating variance
def decimalize(data):
    # if asked to decimalize one number
    if type(data) is float:
        return(Decimal(data))
    # if asked to decimalize a list/vector
    else:
        for ii in range(len(data)):
            data[ii] = Decimal(data[ii])

        return(data)


def mean(data):
    """
    >>> mean([1])
    1.0
    >>> mean([1, 2])
    1.5
    >>> mean([1, 2, 3])
    2.0
    >>> mean([-1, 0, 1, 2, 3])
    1.0
    """
    return sum(data) / len(data)

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
    return pow(reduce(lambda v, mem: v * mem, x, 1.0), 1 / float(len(x)))

# [variance](http://en.wikipedia.org/wiki/Variance)
#
# is the sum of squared deviations from the mean
def variance(data, sample = True):
    """
    >>> variance([1]) # variance of one value is not defined
    >>> variance([4]) # variance of one value is not defined
    >>> variance([1, 2, 3, 4])
    1.6666666666666667
    >>> variance([1, 2, 3, 4], sample = False)
    1.25
    >>> variance([1, 2, 3, 4, 5, 6])
    3.5
    >>> variance([-2, -1, 0, 1, 2])
    2.5
    """
    if len(data) < 2:
        return(None)

    data = decimalize(data)
    m = mean(data)
    if sample:
        return(float(sum([pow(x -m, 2) for x in data]) / (len(data) - 1)))
    else:
        return float(mean([pow(x - m, 2) for x in data]))

def standard_deviation(data):
    """
    >>> standard_deviation([1, 2, 3])
    1.0
    >>> standard_deviation([1, 2, 3, 4])
    1.2909944487358056
    >>> standard_deviation([-1, 0, 1, 2, 3, 4])
    1.8708286933869707
    """
    return math.sqrt(variance(data))

def min(data):
    """
    >>> min([1, 2, 3])
    1
    >>> min([-3, 0, 3])
    -3
    >>> min([-2])
    -2
    >>> min(-3)
    -3
    """

    if type(data) is list:
        min_value = data[0]
        for ii in data:
            if ii < min_value:
                min_value = ii
    elif type(data) is int or type(data) is float:
        min_value = data

    return(min_value)


def max(data):
    """
    >>> max([1, 2, 3])
    3
    >>> max([-3, 0, 3])
    3
    >>> max([-2])
    -2
    >>> max(-3)
    -3
    """

    if type(data) is list:
        max_value = data[0]
        for ii in data:
            if ii > max_value:
                max_value = ii
    elif type(data) is int or type(data) is float:
        max_value = data

    return(max_value)

def median(data):
    """
    >>> median([1, 2, 3])
    2.0
    >>> median([1, 2, 3, 4])
    2.5
    >>> median([10, 2, -5, -1])
    0.5
    >>> median([-2])
    -2.0
    >>> median(-3)
    -3.0
    >>> median("90")
    Traceback (most recent call last):
        ...
    TypeError: median() expects an int or a list.
    """
    
    if type(data) is int:
        return(float(data))
    elif type(data) is list:
        data.sort()

        if len(data) == 1:
            return(float(data[0]))
        elif len(data) % 2 == 1:
            return(float(data[int(len(data) / 2)]))
        else:
            middleIndex = len(data) / 2
            return((data[int(middleIndex - .5)] + data[int(middleIndex + .5)]) / 2)
    else:
        raise TypeError("median() expects an int or a list.")

def mode(data):
    """
    >>> mode([1, 2, 3, 1])
    [1]
    >>> mode([2, 3, 1, 1, 2])
    [1, 2]
    >>> mode([-1, 1, 0])
    [-1, 0, 1]
    >>> mode(4)
    4
    >>> mode([])
    """
    max_count = 0
    modes = []
    number_counter = {}

    if type(data) is int:
        return(data)
    elif type(data) is list and len(data) > 0:
        data.sort()

        for ii in data:
            if ii in number_counter.keys():
                number_counter[ii] = number_counter[ii] + 1
            else:
                number_counter[ii] = 1

            if number_counter[ii] == max_count:
                modes.append(ii)
            elif number_counter[ii] > max_count:
                modes = [ii]
                max_count = number_counter[ii]

        modes.sort()
        return(modes)

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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
