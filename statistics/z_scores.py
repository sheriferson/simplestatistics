from .mean import mean
from .standard_deviation import standard_deviation

def z_scores(data):
    """
    >>> z_scores([-2, -1, 0, 1, 2])
    [1.2649110640673518, 0.6324555320336759, 0.0, -0.6324555320336759, -1.2649110640673518]
    >>> z_scores([1, 2])
    [0.7071067811865475, -0.7071067811865475]
    >>> z_scores([90])
    >>> z_scores(4)
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

