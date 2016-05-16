def mode(data):
    """
    The mode_ is "the value that appears most often in a set of data."

    .. _mode: https://en.wikipedia.org/wiki/Mode_(statistics)

    If more than one value appear equally frequently more than the rest of the values,
    then the mode is not unique and includes all the values that appear the same maximum
    number of times.

    In the most extreme of cases, of each value in the dataset appears the same number of times,
    then the mode is all the values.

    Args:
        data: A numeric built-in object, a tuple, or list of numeric objects.

    Returns:
        A list containing one or more modes if the function received a list as input.
        Or, a numeric object if the function received a numeric object.


    Examples:
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

