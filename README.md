## simplestatistics

[![Circle CI](https://circleci.com/gh/sheriferson/simplestatistics.svg?style=svg)](https://circleci.com/gh/sheriferson/simplestatistics)
[![codecov](https://codecov.io/gh/sheriferson/simplestatistics/branch/master/graph/badge.svg)](https://codecov.io/gh/sheriferson/simplestatistics)
[![Documentation Status](https://readthedocs.org/projects/simplestatistics/badge/?version=latest)](http://simplestatistics.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/simplestatistics.svg)](https://badge.fury.io/py/simplestatistics)

[simple-statistics](https://github.com/tmcw/simple-statistics)
for Python.

`simplestatistics` is compatible with Python 2 & 3.
### Installation

```bash
pip install simplestatistics
```

### Usage

```python
>>> import simplestatistics as ss
>>> ss.mean([1, 2, 3])
2.0
>>> ss.t_test([1, 2, 2.4, 3, 0.9], 2)
-0.3461277235039042
```

### Documentation

You can [read the documentation online](http://simplestatistics.readthedocs.io/en/latest/).

Or you can generate it yourself:

Inside `simplestatistics/`.

```bash
make html
```

Documentation will be generated in `_build/html/`.

### Tests

If you want coverage reports, you need to have [`coverage`](https://pypi.python.org/pypi/coverage) installed:

```bash
pip install coverage
nosetests --with-coverage --cover-package=simplestatistics --with-doctest
```

Otherwise, to just run the tests:

```bash
nosetests --with-doctest
```

### Functions and examples

#### Descriptive statistics

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

#### Measures of central tendency

| Function           | Example                     |
|--------------------|-----------------------------|
| [Mean][]           | `mean([1, 2, 3])`           |
| [Median][]         | `median([10, 2, -5, -1])`   |
| [Mode][]           | `mode([2, 1, 3, 2, 1])`     |
| [Geometric mean][] | `geometric_mean([1, 10])`   |
| [Skewness][]       | `skew([1, 2, 5])`           |
| [Kurtosis][]       | `kurtosis([1, 2, 3, 4, 5])` |

[Mean]: http://simplestatistics.readthedocs.io/en/latest/#mean
[Median]: http://simplestatistics.readthedocs.io/en/latest/#median
[Mode]: http://simplestatistics.readthedocs.io/en/latest/#mode
[Geometric mean]: http://simplestatistics.readthedocs.io/en/latest/#geometric-mean
[Skewness]: http://simplestatistics.readthedocs.io/en/latest/#skewness
[Kurtosis]: http://simplestatistics.readthedocs.io/en/latest/#kurtosis

#### Measures of dispersion

| Function                                   | Example                              |
|--------------------------------------------|--------------------------------------|
| [Sample and population variance][variance] | `variance([1, 2, 3], sample = True)` |
| [Standard deviation][sd]                   | `standard_deviation([1, 2, 3])`      |
| [Standard scores (z-scores)][zscores]      | `z_scores([-2, -1, 0, 1, 2])`        |

[variance]: http://simplestatistics.readthedocs.io/en/latest/#variance
[sd]: http://simplestatistics.readthedocs.io/en/latest/#standard-deviation
[zscores]: http://simplestatistics.readthedocs.io/en/latest/#standard-scores-z-scores 

#### Linear regression

| Function                                                | Example                                                     |
|---------------------------------------------------------|-------------------------------------------------------------|
| [Simple linear regression][linreg]                      | `linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5.5, 5.3, 6])` |
| [Linear regression line function generator][linregline] | `linear_regression_line([.5, 9.5])([1, 2, 3])`              |

[linreg]: http://simplestatistics.readthedocs.io/en/latest/#linear-regression
[linregline]: http://simplestatistics.readthedocs.io/en/latest/#linear-regression-line-function

#### Similarity

| Function        | Example                                                              |
|-----------------|----------------------------------------------------------------------|
| [Correlation][] | `correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, 1, 2, 3, 2, 4, 5])` |

[Correlation]: http://simplestatistics.readthedocs.io/en/latest/#correlation

#### Distributions

| Function                  | Example                                                |
|---------------------------|--------------------------------------------------------|
| [Factorial][]             | `factorial(20)` or `factorial([1, 5, 20])`             |
| [Choose][]                | `choose(5, 3)`                                         |
| [Normal distribution][]   | `normal(4, 8, 2)` or `normal([1, 4], 8, 2)`            |
| [Binomial distribution][] | `binomial(4, 12, 0.2)` or `binomial([3,4,5], 12, 0.5)` |
| [One-sample t-test][]     | `t_test([1, 2, 3, 4, 5, 6], 3.385)`                    |

[Factorial]: http://simplestatistics.readthedocs.io/en/latest/#factorial
[Choose]: http://simplestatistics.readthedocs.io/en/latest/#choose
[Normal distribution]: http://simplestatistics.readthedocs.io/en/latest/#normal-distribution
[Binomial distribution]: http://simplestatistics.readthedocs.io/en/latest/#binomial-distribution
[One-sample t-test]: http://simplestatistics.readthedocs.io/en/latest/#one-sample-t-test

### Spirit and rules

- Everything should be implemented in raw, organic, locally sourced Python.
- Use libraries only if you have to and only when unrelated to the math/statistics. For example, `from functools import reduce` to make `reduce` available for those using python3. That's okay, because it's about making Python work and not about making the stats easier.
- It's okay to use operators and functions if they correspond to regular calculator buttons. For example, all calculators have a built-in square root function, so there is no need to implement that ourselves, we can use `math.sqrt()`.
Anything beyond that, like `mean`, `median`, we have to write ourselves.

Pull requests are welcome!

### Contributors

- Jim Anderson ([jhowardanderson](https://github.com/jhowardanderson))
- Pierre-Selim ([PierreSelim](https://github.com/PierreSelim))
- Tom MacWright ([tmcw](https://github.com/tmcw))
