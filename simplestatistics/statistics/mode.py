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

