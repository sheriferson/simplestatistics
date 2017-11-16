"""
Importing all functions into simplestatistics namespace
"""
# descriptive statistics
from .statistics.min import min # pylint: disable=redefined-builtin
from .statistics.max import max # pylint: disable=redefined-builtin
from .statistics.sum import sum # pylint: disable=redefined-builtin
from .statistics.quantile import quantile
from .statistics.product import product

# measures of central tendency
from .statistics.mean import mean
from .statistics.median import median
from .statistics.mode import mode
from .statistics.geometric_mean import geometric_mean
from .statistics.harmonic_mean import harmonic_mean
from .statistics.root_mean_square import root_mean_square
from .statistics.add_to_mean import add_to_mean
from .statistics.skew import skew
from .statistics.kurtosis import kurtosis

# measures of dispersion
from .statistics.variance import variance
from .statistics.standard_deviation import standard_deviation
from .statistics.coefficient_of_variation import coefficient_of_variation
from .statistics.interquartile_range import interquartile_range
from .statistics.sum_nth_power_deviations import sum_nth_power_deviations
from .statistics.z_scores import z_scores

# similarity
from .statistics.correlate import correlate
from .statistics.covariance import covariance

# linear regression
from .statistics.linear_regression import linear_regression
from .statistics.linear_regression_line import linear_regression_line

# distributions
from .statistics.factorial import factorial
from .statistics.choose import choose
from .statistics.normal import normal
from .statistics.binomial import binomial
from .statistics.bernoulli import bernoulli
from .statistics.poisson import poisson
from .statistics.gamma_function import gamma_function
from .statistics.beta import beta
from .statistics.t_test import t_test
from .statistics.chi_squared_dist_table import chi_squared_dist_table

# classifiers
from .statistics.bayesian_classifier import bayesian_classifier
from .statistics.perceptron import perceptron

# errors
from .statistics.error_function import error_function

# hyperbolic functions
from .statistics.sinh import sinh
from .statistics.cosh import cosh
from .statistics.tanh import tanh
