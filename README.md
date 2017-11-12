# simplestatistics

[![Circle CI](https://circleci.com/gh/sheriferson/simplestatistics.svg?style=svg)](https://circleci.com/gh/sheriferson/simplestatistics)
[![codecov](https://codecov.io/gh/sheriferson/simplestatistics/branch/master/graph/badge.svg)](https://codecov.io/gh/sheriferson/simplestatistics)
[![Documentation Status](https://readthedocs.org/projects/simplestatistics/badge/?version=latest)](http://simplestatistics.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/simplestatistics.svg)](https://badge.fury.io/py/simplestatistics)

[simple-statistics](https://github.com/tmcw/simple-statistics)
for Python.

`simplestatistics` is compatible with Python 2 & 3.

<!-- TOC -->

## Installation

Install the [current PyPI release](https://pypi.python.org/pypi/simplestatistics):

```bash
pip install simplestatistics
```

Or install the development version from GitHub:

```bash
pip install git+https://github.com/sheriferson/simplestatistics
```

## Usage

```python
>>> import simplestatistics as ss
>>> ss.mean([1, 2, 3])
2.0
>>> ss.t_test([1, 2, 2.4, 3, 0.9], 2)
-0.3461277235039042
```

## Documentation

You can [read the documentation online](http://simplestatistics.readthedocs.io/en/latest/).

Or you can generate it yourself:

Inside `simplestatistics/`.

```bash
make html
```

Documentation will be generated in `_build/html/`.

## Tests

If you want coverage reports, you need to have [`coverage`](https://pypi.python.org/pypi/coverage) installed:

```bash
pip install coverage
nosetests --with-coverage --cover-package=simplestatistics --with-doctest
```

Otherwise, to just run the tests:

```bash
nosetests --with-doctest
```

The code adheres to [PEP8] guidelines except for the following checkers:

- `invalid-name`
- `len-as-condition`
- `superfluous-parens`
- `unidiomatic-typecheck`

[PEP8]: https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code"

To [lint] the code, make sure you have [`pylint`] installed (`pip install pylint`), `cd` into the `simplestatistics/statistics` directory, then run:

```bash
pylint -d 'invalid-name, len-as-condition, superfluous-parens, unidiomatic-typecheck' *.py
```

[lint]: https://en.wikipedia.org/wiki/Lint_%28software%29 "Linting Wikipedia page"
[pylint]: https://pylint.org "Pylint website"

## Functions and examples

### Descriptive statistics

| Function      | Example                                                          |
|---------------|------------------------------------------------------------------|
| [Min][]       | `min([-3, 0, 3])`                                                |
| [Max][]       | `max([1, 2, 3])`                                                 |
| [Sum][]       | `sum([1, 2, 3.5])`                                               |
| [Quantiles][] | `quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], [0.25, 0.75])` |
| [Product][]   | `product([1.25, 2.75], [2.5, 3.40])`                             |

[Min]: http://simplestatistics.readthedocs.io/en/latest/#min
[Max]: http://simplestatistics.readthedocs.io/en/latest/#max
[Sum]: http://simplestatistics.readthedocs.io/en/latest/#sum
[Quantiles]: http://simplestatistics.readthedocs.io/en/latest/#quantiles
[Product]: http://simplestatistics.readthedocs.io/en/latest/#product

### Measures of central tendency

| Function             | Example                            |
|----------------------|------------------------------------|
| [Mean][]             | `mean([1, 2, 3])`                  |
| [Median][]           | `median([10, 2, -5, -1])`          |
| [Mode][]             | `mode([2, 1, 3, 2, 1])`            |
| [Geometric mean][]   | `geometric_mean([1, 10])`          |
| [Harmonic mean][]    | `harmonic_mean([1, 2, 4])`         |
| [Root mean square][] | `root_mean_square([1, -1, 1, -1])` |
| [Add to mean][]      | `add_to_mean(40, 4, (10, 12))`     |
| [Skewness][]         | `skew([1, 2, 5])`                  |
| [Kurtosis][]         | `kurtosis([1, 2, 3, 4, 5])`        |

[Mean]: http://simplestatistics.readthedocs.io/en/latest/#mean
[Median]: http://simplestatistics.readthedocs.io/en/latest/#median
[Mode]: http://simplestatistics.readthedocs.io/en/latest/#mode
[Geometric mean]: http://simplestatistics.readthedocs.io/en/latest/#geometric-mean
[Harmonic mean]: http://simplestatistics.readthedocs.io/en/latest/#harmonic-mean
[Root mean square]: http://simplestatistics.readthedocs.io/en/latest/#root-mean-square
[Add to mean]: http://simplestatistics.readthedocs.io/en/latest/#add-to-mean
[Skewness]: http://simplestatistics.readthedocs.io/en/latest/#skewness
[Kurtosis]: http://simplestatistics.readthedocs.io/en/latest/#kurtosis

### Measures of dispersion

| Function                                                    | Example                                               |
|-------------------------------------------------------------|-------------------------------------------------------|
| [Sample and population variance][variance]                  | `variance([1, 2, 3], sample = True)`                  |
| [Sample and population Standard deviation][sd]              | `standard_deviation([1, 2, 3], sample = True)`        |
| [Sample and population Coefficient of variation][cv]        | `coefficient_of_variation([1, 2, 3], sample = True)`  |
| [Interquartile range][]                                     | `interquartile_range([1, 3, 5, 7])`                   |
| [Sum of Nth power deviations][sumndevs]                     | `sum_nth_power_deviations([-1, 0, 2, 4], 3)`          |
| [Sample and population Standard scores (z-scores)][zscores] | `z_scores([-2, -1, 0, 1, 2], sample = True)`          |

[variance]: http://simplestatistics.readthedocs.io/en/latest/#variance
[sd]: http://simplestatistics.readthedocs.io/en/latest/#standard-deviation
[cv]: http://simplestatistics.readthedocs.io/en/latest/#coefficient-of-variation
[Interquartile range]: http://simplestatistics.readthedocs.io/en/latest/#interquartile-range
[sumndevs]: http://simplestatistics.readthedocs.io/en/latest/#sum-of-nth-power-deviations
[zscores]: http://simplestatistics.readthedocs.io/en/latest/#standard-scores-z-scores

### Linear regression

| Function                                                | Example                                                     |
|---------------------------------------------------------|-------------------------------------------------------------|
| [Simple linear regression][linreg]                      | `linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5.5, 5.3, 6])` |
| [Linear regression line function generator][linregline] | `linear_regression_line([.5, 9.5])([1, 2, 3])`              |

[linreg]: http://simplestatistics.readthedocs.io/en/latest/#linear-regression
[linregline]: http://simplestatistics.readthedocs.io/en/latest/#linear-regression-line-function

### Similarity

| Function        | Example                                                              |
|-----------------|----------------------------------------------------------------------|
| [Correlation][] | `correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, 1, 2, 3, 2, 4, 5])` |
| [Covariance][]  | `covariance([1,2,3,4,5,6], [6,5,4,3,2,1])`                           |

[Correlation]: http://simplestatistics.readthedocs.io/en/latest/#correlation
[Covariance]: http://simplestatistics.readthedocs.io/en/latest/#covariance

### Distributions

| Function                           | Example                                                |
|------------------------------------|--------------------------------------------------------|
| [Factorial][]                      | `factorial(20)` or `factorial([1, 5, 20])`             |
| [Choose][]                         | `choose(5, 3)`                                         |
| [Normal distribution][]            | `normal(4, 8, 2)` or `normal([1, 4], 8, 2)`            |
| [Binomial distribution][]          | `binomial(4, 12, 0.2)` or `binomial([3,4,5], 12, 0.5)` |
| [Bernoulli distribution][]         | `bernoulli(0.25)`                                      |
| [Poisson distribution][]           | `poisson(3, [0, 1, 2, 3])`                             |
| [One-sample t-test][]              | `t_test([1, 2, 3, 4, 5, 6], 3.385)`                    |
| [Chi Squared Distribution Table][] | `chi_squared_dist_table(k = 10, p = .01)`              |
| [Gamma function][]                 | `gamma_function([1, 2, 3, 4, 5])`                      |

[Factorial]: http://simplestatistics.readthedocs.io/en/latest/#factorial
[Choose]: http://simplestatistics.readthedocs.io/en/latest/#choose
[Normal distribution]: http://simplestatistics.readthedocs.io/en/latest/#normal-distribution
[Binomial distribution]: http://simplestatistics.readthedocs.io/en/latest/#binomial-distribution
[Bernoulli distribution]: http://simplestatistics.readthedocs.io/en/latest/#bernoulli-distribution
[Poisson distribution]: http://simplestatistics.readthedocs.io/en/latest/#poisson-distribution
[One-sample t-test]: http://simplestatistics.readthedocs.io/en/latest/#one-sample-t-test
[Chi Squared Distribution Table]: http://simplestatistics.readthedocs.io/en/latest/#chi-squared-distribution-table
[Gamma function]: http://simplestatistics.readthedocs.io/en/latest/#gamma-function

### Classifiers

| Function                         | Example                                                      |
|----------------------------------|--------------------------------------------------------------|
| [Naive Bayesian classifier][nbc] | See documentation for examples of how to train and classify. |
| [Perceptron][]                   | See documentation for examples of how to train and classify. |

[nbc]: http://simplestatistics.readthedocs.io/en/latest/#bayesian-classifier
[Perceptron]: http://simplestatistics.readthedocs.io/en/latest/#perceptron

### Errors

| Function                    | Example             |
|-----------------------------|---------------------|
| [Gauss error function][gef] | `error_function(1)` |

[gef]: http://simplestatistics.readthedocs.io/en/latest/#error-function

### Hyperbolic functions

| Function      | Example     |
|---------------|-------------|
| [sinh][hyper] | `sinh(2)`   |
| [cosh][hyper] | `cosh(2.5)` |
| [tanh][hyper] | `tanh(.2)`  |

[hyper]: https://en.wikipedia.org/wiki/Hyperbolic_function#Other_definitions

## Spirit and rules

- Everything should be implemented in raw, organic, locally sourced Python.
- Use libraries only if you have to and only when unrelated to the math/statistics. For example, `from functools import reduce` to make `reduce` available for those using python3. That's okay, because it's about making Python work and not about making the stats easier.
- It's okay to use operators and functions if they correspond to regular calculator buttons. For example, all calculators have a built-in square root function, so there is no need to implement that ourselves, we can use `math.sqrt()`.
Anything beyond that, like `mean`, `median`, we have to write ourselves.

Pull requests are welcome!

## Contributors

- Jim Anderson ([jhowardanderson](https://github.com/jhowardanderson))
- Lidiane Taquehara ([lidimayra](https://github.com/lidimayra))
- Pierre-Selim ([PierreSelim](https://github.com/PierreSelim))
- Tom MacWright ([tmcw](https://github.com/tmcw))
