from .mean import mean
from .standard_deviation import standard_deviation

def z_scores(data):
    """
    Standardizing a variable or set of data is transforming the data such that it
    has a mean of 0 and standard deviation of 1.

    Each converted value equals how many standard deviations the value is above or below the mean.
    These converted values are known as "z scores".

    Equation:
        .. math::
            z_i = \\frac{X_i - \\bar{X}}{s_X}

    In English:
        - Subract the value from the mean.
        - Divide the result by the standard deviation.

    Args:
        data: A list of numerical objects.

    Returns:
        A list of float objects.

    Examples:
        >>> z_scores([-2, -1, 0, 1, 2])
        [1.2649110640673518, 0.6324555320336759, 0.0, -0.6324555320336759, -1.2649110640673518]
        >>> z_scores([1, 2])
        [0.7071067811865475, -0.7071067811865475]
        >>> z_scores([90]) # a z score for one value is not defined
        >>> z_scores(4) # a z score for one value is not defined
    """
    # You can't get z scores for one number
    if type(data) is int:
        return(None)
    elif type(data) is list:
        # You can't get z scores for one number
        if len(data) < 2:
            return(None)

        mean_of_data = mean(data)
        sd_of_data = standard_deviation(data)

        z_scores = [((mean_of_data - float(ii)) / sd_of_data) for ii in data]
        return(z_scores)

