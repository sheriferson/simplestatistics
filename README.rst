simplestatistics
----------------

|Circle CI| |codecov| |Documentation Status| |PyPI version|

`simple-statistics <https://github.com/tmcw/simple-statistics>`__ for
Python.

``simplestatistics`` is compatible with Python 2 & 3. ### Installation

Install the `current PyPI
release <https://pypi.python.org/pypi/simplestatistics>`__:

.. code:: bash

    pip install simplestatistics

Or install the development version from GitHub:

.. code:: bash

    pip install git+https://github.com/sheriferson/simplestatistics

Usage
~~~~~

.. code:: python

    >>> import simplestatistics as ss
    >>> ss.mean([1, 2, 3])
    2.0
    >>> ss.t_test([1, 2, 2.4, 3, 0.9], 2)
    -0.3461277235039042

Documentation
~~~~~~~~~~~~~

You can `read the documentation
online <http://simplestatistics.readthedocs.io/en/latest/>`__.

Or you can generate it yourself:

Inside ``simplestatistics/``.

.. code:: bash

    make html

Documentation will be generated in ``_build/html/``.

Tests
~~~~~

If you want coverage reports, you need to have
```coverage`` <https://pypi.python.org/pypi/coverage>`__ installed:

.. code:: bash

    pip install coverage
    nosetests --with-coverage --cover-package=simplestatistics --with-doctest

Otherwise, to just run the tests:

.. code:: bash

    nosetests --with-doctest

Functions and examples
~~~~~~~~~~~~~~~~~~~~~~

Descriptive statistics
^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Function                                                                      | Example                                                              |
+===============================================================================+======================================================================+
| `Min <http://simplestatistics.readthedocs.io/en/latest/#min>`__               | ``min([-3, 0, 3])``                                                  |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `Max <http://simplestatistics.readthedocs.io/en/latest/#max>`__               | ``max([1, 2, 3])``                                                   |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `Sum <http://simplestatistics.readthedocs.io/en/latest/#sum>`__               | ``sum([1, 2, 3.5])``                                                 |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `Quantiles <http://simplestatistics.readthedocs.io/en/latest/#quantiles>`__   | ``quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], [0.25, 0.75])``   |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `Product <http://simplestatistics.readthedocs.io/en/latest/#product>`__       | ``product([1.25, 2.75], [2.5, 3.40])``                               |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------+

Measures of central tendency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+---------------------------------------------------------------------------------------------+----------------------------------------+
| Function                                                                                    | Example                                |
+=============================================================================================+========================================+
| `Mean <http://simplestatistics.readthedocs.io/en/latest/#mean>`__                           | ``mean([1, 2, 3])``                    |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Median <http://simplestatistics.readthedocs.io/en/latest/#median>`__                       | ``median([10, 2, -5, -1])``            |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Mode <http://simplestatistics.readthedocs.io/en/latest/#mode>`__                           | ``mode([2, 1, 3, 2, 1])``              |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Geometric mean <http://simplestatistics.readthedocs.io/en/latest/#geometric-mean>`__       | ``geometric_mean([1, 10])``            |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Harmonic mean <http://simplestatistics.readthedocs.io/en/latest/#harmonic-mean>`__         | ``harmonic_mean([1, 2, 4])``           |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Root mean square <http://simplestatistics.readthedocs.io/en/latest/#root-mean-square>`__   | ``root_mean_square([1, -1, 1, -1])``   |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Skewness <http://simplestatistics.readthedocs.io/en/latest/#skewness>`__                   | ``skew([1, 2, 5])``                    |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Kurtosis <http://simplestatistics.readthedocs.io/en/latest/#kurtosis>`__                   | ``kurtosis([1, 2, 3, 4, 5])``          |
+---------------------------------------------------------------------------------------------+----------------------------------------+

Measures of dispersion
^^^^^^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Function                                                                                                          | Example                                          |
+===================================================================================================================+==================================================+
| `Sample and population variance <http://simplestatistics.readthedocs.io/en/latest/#variance>`__                   | ``variance([1, 2, 3], sample = True)``           |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| `Standard deviation <http://simplestatistics.readthedocs.io/en/latest/#standard-deviation>`__                     | ``standard_deviation([1, 2, 3])``                |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| `Coefficient of variation <http://simplestatistics.readthedocs.io/en/latest/#coefficient_of_variation>`__         | ``coefficient_of_variation([1, 2, 3])``          |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| `Interquartile range <http://simplestatistics.readthedocs.io/en/latest/#interquartile-range>`__                   | ``interquartile_range([1, 3, 5, 7])``            |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| `Sum of Nth power deviations <http://simplestatistics.readthedocs.io/en/latest/#sum-of-nth-power-deviations>`__   | ``sum_nth_power_deviations([-1, 0, 2, 4], 3)``   |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| `Standard scores (z-scores) <http://simplestatistics.readthedocs.io/en/latest/#standard-scores-z-scores>`__       | ``z_scores([-2, -1, 0, 1, 2])``                  |
+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+

Linear regression
^^^^^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| Function                                                                                                                            | Example                                                         |
+=====================================================================================================================================+=================================================================+
| `Simple linear regression <http://simplestatistics.readthedocs.io/en/latest/#linear-regression>`__                                  | ``linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5.5, 5.3, 6])``   |
+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| `Linear regression line function generator <http://simplestatistics.readthedocs.io/en/latest/#linear-regression-line-function>`__   | ``linear_regression_line([.5, 9.5])([1, 2, 3])``                |
+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

Similarity
^^^^^^^^^^

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| Function                                                                          | Example                                                                  |
+===================================================================================+==========================================================================+
| `Correlation <http://simplestatistics.readthedocs.io/en/latest/#correlation>`__   | ``correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, 1, 2, 3, 2, 4, 5])``   |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Distributions
^^^^^^^^^^^^^

+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Function                                                                                              | Example                                                      |
+=======================================================================================================+==============================================================+
| `Factorial <http://simplestatistics.readthedocs.io/en/latest/#factorial>`__                           | ``factorial(20)`` or ``factorial([1, 5, 20])``               |
+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| `Choose <http://simplestatistics.readthedocs.io/en/latest/#choose>`__                                 | ``choose(5, 3)``                                             |
+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| `Normal distribution <http://simplestatistics.readthedocs.io/en/latest/#normal-distribution>`__       | ``normal(4, 8, 2)`` or ``normal([1, 4], 8, 2)``              |
+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| `Binomial distribution <http://simplestatistics.readthedocs.io/en/latest/#binomial-distribution>`__   | ``binomial(4, 12, 0.2)`` or ``binomial([3,4,5], 12, 0.5)``   |
+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| `One-sample t-test <http://simplestatistics.readthedocs.io/en/latest/#one-sample-t-test>`__           | ``t_test([1, 2, 3, 4, 5, 6], 3.385)``                        |
+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Classifiers
^^^^^^^^^^^

+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| Function                                                                                                | Example                                                        |
+=========================================================================================================+================================================================+
| `Naive Bayesian classifier <http://simplestatistics.readthedocs.io/en/latest/#bayesian-classifier>`__   | See documentation for examples of how to train and classify.   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| `Perceptron <http://simplestatistics.readthedocs.io/en/latest/#perceptron>`__                           | See documentation for examples of how to train and classify.   |
+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Spirit and rules
~~~~~~~~~~~~~~~~

-  Everything should be implemented in raw, organic, locally sourced
   Python.
-  Use libraries only if you have to and only when unrelated to the
   math/statistics. For example, ``from functools import reduce`` to
   make ``reduce`` available for those using python3. That's okay,
   because it's about making Python work and not about making the stats
   easier.
-  It's okay to use operators and functions if they correspond to
   regular calculator buttons. For example, all calculators have a
   built-in square root function, so there is no need to implement that
   ourselves, we can use ``math.sqrt()``. Anything beyond that, like
   ``mean``, ``median``, we have to write ourselves.

Pull requests are welcome!

Contributors
~~~~~~~~~~~~

-  Jim Anderson
   (`jhowardanderson <https://github.com/jhowardanderson>`__)
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
