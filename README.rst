simplestatistics
================

|Circle CI| |codecov| |Documentation Status| |PyPI version|

`simple-statistics <https://github.com/tmcw/simple-statistics>`__ for Python.

``simplestatistics`` is compatible with Python 2 & 3.

.. raw:: html

   <!-- TOC -->

Installation
------------

Install the `current PyPI release <https://pypi.python.org/pypi/simplestatistics>`__:

.. code:: bash

    pip install simplestatistics

Or install the development version from GitHub:

.. code:: bash

    pip install git+https://github.com/sheriferson/simplestatistics

Usage
-----

.. code:: python

    >>> import simplestatistics as ss
    >>> ss.mean([1, 2, 3])
    2.0
    >>> ss.t_test([1, 2, 2.4, 3, 0.9], 2)
    -0.3461277235039039

Documentation
-------------

You can `read the documentation online <http://simplestatistics.readthedocs.io/en/latest/>`__.

Or you can generate it yourself:

Inside ``simplestatistics/``.

.. code:: bash

    make html

Documentation will be generated in ``_build/html/``.

Tests
-----

To run all doctests and see test coverage:

.. code:: bash

    pip3 install -r requirements.txt
    pytest simplestatistics --doctest-modules --cov=simplestatistics

The code adheres to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ guidelines except for the
following checkers:

-  ``invalid-name``
-  ``len-as-condition``
-  ``superfluous-parens``
-  ``unidiomatic-typecheck``

To `lint <https://en.wikipedia.org/wiki/Lint_%28software%29>`__ the code, make sure you have
[``pylint``] installed (``pip install pylint``), ``cd`` into the ``simplestatistics/statistics``
directory, then run:

.. code:: bash

    pylint -d 'invalid-name, len-as-condition, superfluous-parens, unidiomatic-typecheck' *.py

Functions and examples
----------------------

Descriptive statistics
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Min <http://simplestatistics.readthedocs.io/en | ``min([-3, 0, 3])``                             |
| /latest/#min>`__                                |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Max <http://simplestatistics.readthedocs.io/en | ``max([1, 2, 3])``                              |
| /latest/#max>`__                                |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Sum <http://simplestatistics.readthedocs.io/en | ``sum([1, 2, 3.5])``                            |
| /latest/#sum>`__                                |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Quantiles <http://simplestatistics.readthedocs | ``quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 2 |
| .io/en/latest/#quantiles>`__                    | 0], [0.25, 0.75])``                             |
+-------------------------------------------------+-------------------------------------------------+
| `Product <http://simplestatistics.readthedocs.i | ``product([1.25, 2.75], [2.5, 3.40])``          |
| o/en/latest/#product>`__                        |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Measures of central tendency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Mean <http://simplestatistics.readthedocs.io/e | ``mean([1, 2, 3])``                             |
| n/latest/#mean>`__                              |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Median <http://simplestatistics.readthedocs.io | ``median([10, 2, -5, -1])``                     |
| /en/latest/#median>`__                          |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Mode <http://simplestatistics.readthedocs.io/e | ``mode([2, 1, 3, 2, 1])``                       |
| n/latest/#mode>`__                              |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Geometric                                      | ``geometric_mean([1, 10])``                     |
| mean <http://simplestatistics.readthedocs.io/en |                                                 |
| /latest/#geometric-mean>`__                     |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Harmonic                                       | ``harmonic_mean([1, 2, 4])``                    |
| mean <http://simplestatistics.readthedocs.io/en |                                                 |
| /latest/#harmonic-mean>`__                      |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Root mean                                      | ``root_mean_square([1, -1, 1, -1])``            |
| square <http://simplestatistics.readthedocs.io/ |                                                 |
| en/latest/#root-mean-square>`__                 |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Add to                                         | ``add_to_mean(40, 4, (10, 12))``                |
| mean <http://simplestatistics.readthedocs.io/en |                                                 |
| /latest/#add-to-mean>`__                        |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Skewness <http://simplestatistics.readthedocs. | ``skew([1, 2, 5])``                             |
| io/en/latest/#skewness>`__                      |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Kurtosis <http://simplestatistics.readthedocs. | ``kurtosis([1, 2, 3, 4, 5])``                   |
| io/en/latest/#kurtosis>`__                      |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Measures of dispersion
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+----------------------------------------------+
| Function                                          | Example                                      |
+===================================================+==============================================+
| `Sample and population                            | ``variance([1, 2, 3], sample = True)``       |
| variance <http://simplestatistics.readthedocs.io/ |                                              |
| en/latest/#variance>`__                           |                                              |
+---------------------------------------------------+----------------------------------------------+
| `Sample and population Standard                   | ``standard_deviation([1, 2, 3], sample = Tru |
| deviation <http://simplestatistics.readthedocs.io | e)``                                         |
| /en/latest/#standard-deviation>`__                |                                              |
+---------------------------------------------------+----------------------------------------------+
| `Sample and population Coefficient of             | ``coefficient_of_variation([1, 2, 3], sample |
| variation <http://simplestatistics.readthedocs.io |  = True)``                                   |
| /en/latest/#coefficient-of-variation>`__          |                                              |
+---------------------------------------------------+----------------------------------------------+
| `Interquartile                                    | ``interquartile_range([1, 3, 5, 7])``        |
| range <http://simplestatistics.readthedocs.io/en/ |                                              |
| latest/#interquartile-range>`__                   |                                              |
+---------------------------------------------------+----------------------------------------------+
| `Sum of Nth power                                 | ``sum_nth_power_deviations([-1, 0, 2, 4], 3) |
| deviations <http://simplestatistics.readthedocs.i | ``                                           |
| o/en/latest/#sum-of-nth-power-deviations>`__      |                                              |
+---------------------------------------------------+----------------------------------------------+
| `Sample and population Standard scores            | ``z_scores([-2, -1, 0, 1, 2], sample = True) |
| (z-scores) <http://simplestatistics.readthedocs.i | ``                                           |
| o/en/latest/#standard-scores-z-scores>`__         |                                              |
+---------------------------------------------------+----------------------------------------------+

Linear regression
~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Simple linear                                  | ``linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5 |
| regression <http://simplestatistics.readthedocs | .5, 5.3, 6])``                                  |
| .io/en/latest/#linear-regression>`__            |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Linear regression line function                | ``linear_regression_line([.5, 9.5])([1, 2, 3])` |
| generator <http://simplestatistics.readthedocs. | `                                               |
| io/en/latest/#linear-regression-line-function>` |                                                 |
| __                                              |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Similarity
~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Correlation <http://simplestatistics.readthedo | ``correlate([2, 1, 0, -1, -2, -3, -4, -5], [0,  |
| cs.io/en/latest/#correlation>`__                | 1, 1, 2, 3, 2, 4, 5])``                         |
+-------------------------------------------------+-------------------------------------------------+
| `Covariance <http://simplestatistics.readthedoc | ``covariance([1,2,3,4,5,6], [6,5,4,3,2,1])``    |
| s.io/en/latest/#covariance>`__                  |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Distributions
~~~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Factorial <http://simplestatistics.readthedocs | ``factorial(20)`` or ``factorial([1, 5, 20])``  |
| .io/en/latest/#factorial>`__                    |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Choose <http://simplestatistics.readthedocs.io | ``choose(5, 3)``                                |
| /en/latest/#choose>`__                          |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Normal                                         | ``normal(4, 8, 2)`` or ``normal([1, 4], 8, 2)`` |
| distribution <http://simplestatistics.readthedo |                                                 |
| cs.io/en/latest/#normal-distribution>`__        |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Binomial                                       | ``binomial(4, 12, 0.2)`` or                     |
| distribution <http://simplestatistics.readthedo | ``binomial([3,4,5], 12, 0.5)``                  |
| cs.io/en/latest/#binomial-distribution>`__      |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Bernoulli                                      | ``bernoulli(0.25)``                             |
| distribution <http://simplestatistics.readthedo |                                                 |
| cs.io/en/latest/#bernoulli-distribution>`__     |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Poisson                                        | ``poisson(3, [0, 1, 2, 3])``                    |
| distribution <http://simplestatistics.readthedo |                                                 |
| cs.io/en/latest/#poisson-distribution>`__       |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Gamma                                          | ``gamma_function([1, 2, 3, 4, 5])``             |
| function <http://simplestatistics.readthedocs.i |                                                 |
| o/en/latest/#gamma-function>`__                 |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Beta                                           | ``beta([.1, .2, .3], 5, 2)``                    |
| distribution <http://simplestatistics.readthedo |                                                 |
| cs.io/en/latest/#beta-distribution>`__          |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `One-sample                                     | ``t_test([1, 2, 3, 4, 5, 6], 3.385)``           |
| t-test <http://simplestatistics.readthedocs.io/ |                                                 |
| en/latest/#one-sample-t-test>`__                |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Chi Squared Distribution                       | ``chi_squared_dist_table(k = 10, p = .01)``     |
| Table <http://simplestatistics.readthedocs.io/e |                                                 |
| n/latest/#chi-squared-distribution-table>`__    |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Classifiers
~~~~~~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Naive Bayesian                                 | See documentation for examples of how to train  |
| classifier <http://simplestatistics.readthedocs | and classify.                                   |
| .io/en/latest/#bayesian-classifier>`__          |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| `Perceptron <http://simplestatistics.readthedoc | See documentation for examples of how to train  |
| s.io/en/latest/#perceptron>`__                  | and classify.                                   |
+-------------------------------------------------+-------------------------------------------------+

Errors
~~~~~~

+-------------------------------------------------+-------------------------------------------------+
| Function                                        | Example                                         |
+=================================================+=================================================+
| `Gauss error                                    | ``error_function(1)``                           |
| function <http://simplestatistics.readthedocs.i |                                                 |
| o/en/latest/#error-function>`__                 |                                                 |
+-------------------------------------------------+-------------------------------------------------+

Hyperbolic functions
~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+---------------+
| Function                                                                       | Example       |
+================================================================================+===============+
| `sinh <https://en.wikipedia.org/wiki/Hyperbolic_function#Other_definitions>`__ | ``sinh(2)``   |
+--------------------------------------------------------------------------------+---------------+
| `cosh <https://en.wikipedia.org/wiki/Hyperbolic_function#Other_definitions>`__ | ``cosh(2.5)`` |
+--------------------------------------------------------------------------------+---------------+
| `tanh <https://en.wikipedia.org/wiki/Hyperbolic_function#Other_definitions>`__ | ``tanh(.2)``  |
+--------------------------------------------------------------------------------+---------------+

Spirit and rules
----------------

-  Everything should be implemented in raw, organic, locally sourced Python.
-  Use libraries only if you have to and only when unrelated to the math/statistics. For example,
   ``from functools import reduce`` to make ``reduce`` available for those using python3. That’s
   okay, because it’s about making Python work and not about making the stats easier.
-  It’s okay to use operators and functions if they correspond to regular calculator buttons. For
   example, all calculators have a built-in square root function, so there is no need to implement
   that ourselves, we can use ``math.sqrt()``. Anything beyond that, like ``mean``, ``median``, we
   have to write ourselves.

Pull requests are welcome!

Contributors
------------

-  Jim Anderson (`jhowardanderson <https://github.com/jhowardanderson>`__)
-  Lidiane Taquehara (`lidimayra <https://github.com/lidimayra>`__)
-  Pierre-Selim (`PierreSelim <https://github.com/PierreSelim>`__)
-  Tom MacWright (`tmcw <https://github.com/tmcw>`__)

.. |Circle CI| image:: https://circleci.com/gh/sheriferson/simplestatistics.svg?style=svg
   :target: https://circleci.com/gh/sheriferson/simplestatistics
.. |codecov| image:: https://codecov.io/gh/sheriferson/simplestatistics/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sheriferson/simplestatistics
.. |Documentation Status| image:: https://readthedocs.org/projects/simplestatistics/badge/?version=latest
   :target: http://simplestatistics.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/simplestatistics.svg
   :target: https://badge.fury.io/py/simplestatistics
