.. simplestatistics documentation master file, created by
   sphinx-quickstart on Tue May 10 18:58:12 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction to simplestatistics
================================

Goal and rules
--------------

The goal of simplestatistics is to provide statistical methods that are implemented in readable Python.

simplestatistics is compatible with Python 2 & 3.


- Everything should be implemented in raw, organic, locally sourced python.

- Use libraries only if you have to and only when unrelated to the math/statistics. For example, ``from functools import reduce`` to make ``reduce`` available for those using python3. That's okay, because it's about making python work and not about making the stats easier.

- It's okay to use operators and functions if they correspond to regular calculator buttons. For example, all calculators have a built-in square root function, so there is no need to implement that ourselves, we can use ``math.sqrt()``. Anything beyond that, like ``mean``, ``median``, we have to write ourselves.

Pull requests are welcome! Please visit the `project on GitHub`_.

.. _`project on GitHub`: https://github.com/sheriferson/simplestatistics

Installation
------------

.. code-block:: bash

    pip install simplestatistics

Usage
-----

.. code-block:: python

    >>> import simplestatistics as ss
    >>> ss.mean([1, 2, 3])
    2.0
    >>> ss.t_test([1, 2, 2.4, 3, 0.9], 2)
    -0.3461277235039042

Tests
-----

To get coverage reports with tests:

.. code-block:: bash

    pip install coverage
    nosetests --with-coverage --cover-package=simplestatistics --with-doctest

Otherwise, to just run the tests:

.. code-block:: bash

    nosetests --with-doctest

.. toctree::
    :maxdepth: 2

Functions
=========

Descriptive statistics
----------------------

Min
^^^

.. autofunction:: simplestatistics.min

Max
^^^

.. autofunction:: simplestatistics.max

Sum
^^^

.. autofunction:: simplestatistics.sum

Quantiles
^^^^^^^^^

.. autofunction:: simplestatistics.quantile

Product
^^^^^^^

.. autofunction:: simplestatistics.product

Measures of central tendency
----------------------------

Mean
^^^^

.. autofunction:: simplestatistics.mean

Median
^^^^^^

.. autofunction:: simplestatistics.median

Mode
^^^^

.. autofunction:: simplestatistics.mode

Geometric mean
^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.geometric_mean

Harmonic mean
^^^^^^^^^^^^^

.. autofunction:: simplestatistics.harmonic_mean

Root mean square
^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.root_mean_square

Skewness
^^^^^^^^

.. autofunction:: simplestatistics.skew

Kurtosis
^^^^^^^^

.. autofunction:: simplestatistics.kurtosis

Measures of dispersion
----------------------

Coefficient of variation
^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.coefficient_of_variation

Variance
^^^^^^^^

.. autofunction:: simplestatistics.variance

Standard deviation
^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.standard_deviation

Interquartile range
^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.interquartile_range

Sum of Nth power deviations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.sum_nth_power_deviations

Standard scores (z scores)
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.z_scores

Linear regression
-----------------

Linear regression
^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.linear_regression

Linear regression line function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.linear_regression_line

Similarity
----------

Correlation
^^^^^^^^^^^

.. autofunction:: simplestatistics.correlate

Covariance
^^^^^^^^^^

.. autofunction:: simplestatistics.covariance

Distributions
-------------

Factorial
^^^^^^^^^

.. autofunction:: simplestatistics.factorial

Choose
^^^^^^

.. autofunction:: simplestatistics.choose

Normal distribution
^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.normal

Binomial distribution
^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.binomial

Bernoulli distribution
^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.bernoulli

Poisson distribution
^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.poisson

One-sample t test
^^^^^^^^^^^^^^^^^
.. autofunction:: simplestatistics.t_test
    
Chi Squared Distribution Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: simplestatistics.chi_squared_dist_table

Utilities
---------

Decimalize
^^^^^^^^^^

.. automodule:: simplestatistics.statistics.decimalize
    :members:

Classifiers
-----------

Bayesian classifier
^^^^^^^^^^^^^^^^^^^

.. autoclass:: simplestatistics.bayesian_classifier
    :members:

Perceptron
^^^^^^^^^^

.. autoclass:: simplestatistics.perceptron
    :members:

Errors
------

Error function
^^^^^^^^^^^^^^

.. autoclass:: simplestatistics.error_function
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`

