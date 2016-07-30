simplestatistics
----------------

|Circle CI| |codecov| |Documentation Status| |PyPI version|

`simple-statistics <https://github.com/tmcw/simple-statistics>`__ for
Python.

``simplestatistics`` is compatible with Python 2 & 3. ### Installation

.. code:: bash

    pip install simplestatistics

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

+-------------+----------------------------------------------------------------------+
| Function    | Example                                                              |
+=============+======================================================================+
| Min         | ``min([-3, 0, 3])``                                                  |
+-------------+----------------------------------------------------------------------+
| Max         | ``max([1, 2, 3])``                                                   |
+-------------+----------------------------------------------------------------------+
| Sum         | ``sum([1, 2, 3.5])``                                                 |
+-------------+----------------------------------------------------------------------+
| Quantiles   | ``quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], [0.25, 0.75])``   |
+-------------+----------------------------------------------------------------------+
| Product     | ``product([1.25, 2.75], [2.5, 3.40])``                               |
+-------------+----------------------------------------------------------------------+

Measures of central tendency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------------+---------------------------------+
| Function         | Example                         |
+==================+=================================+
| Mean             | ``mean([1, 2, 3])``             |
+------------------+---------------------------------+
| Median           | ``median([10, 2, -5, -1])``     |
+------------------+---------------------------------+
| Mode             | ``mode([2, 1, 3, 2, 1])``       |
+------------------+---------------------------------+
| Geometric mean   | ``geometric_mean([1, 10])``     |
+------------------+---------------------------------+
| Kurtosis         | ``kurtosis([1, 2, 3, 4, 5])``   |
+------------------+---------------------------------+
| Skew             | ``skew([1, 2, 5])``             |
+------------------+---------------------------------+

Measures of dispersion
^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------+------------------------------------------+
| Function                         | Example                                  |
+==================================+==========================================+
| Sample and population variance   | ``variance([1, 2, 3], sample = True)``   |
+----------------------------------+------------------------------------------+
| Standard deviation               | ``standard_deviation([1, 2, 3])``        |
+----------------------------------+------------------------------------------+
| Standard scores (z-scores)       | ``z_scores([-2, -1, 0, 1, 2])``          |
+----------------------------------+------------------------------------------+

Linear regression
^^^^^^^^^^^^^^^^^

+-----------------------+----------------------------------------------------+
| Function              | Example                                            |
+=======================+====================================================+
| Simple linear         | ``linear_regression([1, 2, 3, 4, 5], [4, 4.5, 5.5, |
| regression            |  5.3, 6])``                                        |
+-----------------------+----------------------------------------------------+

Similarity
^^^^^^^^^^

+------------------------+---------------------------------------------------+
| Function               | Example                                           |
+========================+===================================================+
| Correlate              | ``correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, |
|                        |  1, 2, 3, 2, 4, 5])``                             |
+------------------------+---------------------------------------------------+

Distributions
^^^^^^^^^^^^^

+-------------------------+--------------------------------------------------------------+
| Function                | Example                                                      |
+=========================+==============================================================+
| Factorial               | ``factorial(20)`` or ``factorial([1, 5, 20])``               |
+-------------------------+--------------------------------------------------------------+
| Choose                  | ``choose(5, 3)``                                             |
+-------------------------+--------------------------------------------------------------+
| Normal distribution     | ``normal(4, 8, 2)`` or ``normal([1, 4], 8, 2)``              |
+-------------------------+--------------------------------------------------------------+
| Binomial distribution   | ``binomial(4, 12, 0.2)`` or ``binomial([3,4,5], 12, 0.5)``   |
+-------------------------+--------------------------------------------------------------+
| One-sample t-test       | ``t_test([1, 2, 3, 4, 5, 6], 3.385)``                        |
+-------------------------+--------------------------------------------------------------+

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

.. |Circle CI| image:: https://circleci.com/gh/sheriferson/simplestatistics.svg?style=svg
   :target: https://circleci.com/gh/sheriferson/simplestatistics
.. |codecov| image:: https://codecov.io/gh/sheriferson/simplestatistics/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sheriferson/simplestatistics
.. |Documentation Status| image:: https://readthedocs.org/projects/simplestatistics/badge/?version=latest
   :target: http://simplestatistics.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/simplestatistics.svg
   :target: https://badge.fury.io/py/simplestatistics
