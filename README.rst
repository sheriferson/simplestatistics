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

+---------------+------------------------------------------------------------+
| Function      | Example                                                    |
+===============+============================================================+
| `Min <http:// | ``min([-3, 0, 3])``                                        |
| simplestatist |                                                            |
| ics.readthedo |                                                            |
| cs.io/en/late |                                                            |
| st/#min>`__   |                                                            |
+---------------+------------------------------------------------------------+
| `Max <http:// | ``max([1, 2, 3])``                                         |
| simplestatist |                                                            |
| ics.readthedo |                                                            |
| cs.io/en/late |                                                            |
| st/#max>`__   |                                                            |
+---------------+------------------------------------------------------------+
| `Sum <http:// | ``sum([1, 2, 3.5])``                                       |
| simplestatist |                                                            |
| ics.readthedo |                                                            |
| cs.io/en/late |                                                            |
| st/#sum>`__   |                                                            |
+---------------+------------------------------------------------------------+
| `Quantiles <h | ``quantile([3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20], [0.25,  |
| ttp://simples | 0.75])``                                                   |
| tatistics.rea |                                                            |
| dthedocs.io/e |                                                            |
| n/latest/#qua |                                                            |
| ntiles>`__    |                                                            |
+---------------+------------------------------------------------------------+
| `Product <htt | ``product([1.25, 2.75], [2.5, 3.40])``                     |
| p://simplesta |                                                            |
| tistics.readt |                                                            |
| hedocs.io/en/ |                                                            |
| latest/#produ |                                                            |
| ct>`__        |                                                            |
+---------------+------------------------------------------------------------+

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
| `Root mean square <http://simplestatistics.readthedocs.io/en/latest/#root-mean-square>`__   | ``root_mean_square([1, -1, 1, -1])``   |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Skewness <http://simplestatistics.readthedocs.io/en/latest/#skewness>`__                   | ``skew([1, 2, 5])``                    |
+---------------------------------------------------------------------------------------------+----------------------------------------+
| `Kurtosis <http://simplestatistics.readthedocs.io/en/latest/#kurtosis>`__                   | ``kurtosis([1, 2, 3, 4, 5])``          |
+---------------------------------------------------------------------------------------------+----------------------------------------+

Measures of dispersion
^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------+-----------------------------------+
| Function                               | Example                           |
+========================================+===================================+
| `Sample and population                 | ``variance([1, 2, 3], sample = Tr |
| variance <http://simplestatistics.read | ue)``                             |
| thedocs.io/en/latest/#variance>`__     |                                   |
+----------------------------------------+-----------------------------------+
| `Standard                              | ``standard_deviation([1, 2, 3])`` |
| deviation <http://simplestatistics.rea |                                   |
| dthedocs.io/en/latest/#standard-deviat |                                   |
| ion>`__                                |                                   |
+----------------------------------------+-----------------------------------+
| `Standard scores                       | ``z_scores([-2, -1, 0, 1, 2])``   |
| (z-scores) <http://simplestatistics.re |                                   |
| adthedocs.io/en/latest/#standard-score |                                   |
| s-z-scores>`__                         |                                   |
+----------------------------------------+-----------------------------------+

Linear regression
^^^^^^^^^^^^^^^^^

+------------------------------------+---------------------------------------+
| Function                           | Example                               |
+====================================+=======================================+
| `Simple linear                     | ``linear_regression([1, 2, 3, 4, 5],  |
| regression <http://simplestatistic | [4, 4.5, 5.5, 5.3, 6])``              |
| s.readthedocs.io/en/latest/#linear |                                       |
| -regression>`__                    |                                       |
+------------------------------------+---------------------------------------+
| `Linear regression line function   | ``linear_regression_line([.5, 9.5])([ |
| generator <http://simplestatistics | 1, 2, 3])``                           |
| .readthedocs.io/en/latest/#linear- |                                       |
| regression-line-function>`__       |                                       |
+------------------------------------+---------------------------------------+

Similarity
^^^^^^^^^^

+----------------+-----------------------------------------------------------+
| Function       | Example                                                   |
+================+===========================================================+
| `Correlation < | ``correlate([2, 1, 0, -1, -2, -3, -4, -5], [0, 1, 1, 2, 3 |
| http://simples | , 2, 4, 5])``                                             |
| tatistics.read |                                                           |
| thedocs.io/en/ |                                                           |
| latest/#correl |                                                           |
| ation>`__      |                                                           |
+----------------+-----------------------------------------------------------+

Distributions
^^^^^^^^^^^^^

+-------------------------+--------------------------------------------------+
| Function                | Example                                          |
+=========================+==================================================+
| `Factorial <http://simp | ``factorial(20)`` or ``factorial([1, 5, 20])``   |
| lestatistics.readthedoc |                                                  |
| s.io/en/latest/#factori |                                                  |
| al>`__                  |                                                  |
+-------------------------+--------------------------------------------------+
| `Choose <http://simples | ``choose(5, 3)``                                 |
| tatistics.readthedocs.i |                                                  |
| o/en/latest/#choose>`__ |                                                  |
+-------------------------+--------------------------------------------------+
| `Normal                 | ``normal(4, 8, 2)`` or ``normal([1, 4], 8, 2)``  |
| distribution <http://si |                                                  |
| mplestatistics.readthed |                                                  |
| ocs.io/en/latest/#norma |                                                  |
| l-distribution>`__      |                                                  |
+-------------------------+--------------------------------------------------+
| `Binomial               | ``binomial(4, 12, 0.2)`` or                      |
| distribution <http://si | ``binomial([3,4,5], 12, 0.5)``                   |
| mplestatistics.readthed |                                                  |
| ocs.io/en/latest/#binom |                                                  |
| ial-distribution>`__    |                                                  |
+-------------------------+--------------------------------------------------+
| `One-sample             | ``t_test([1, 2, 3, 4, 5, 6], 3.385)``            |
| t-test <http://simplest |                                                  |
| atistics.readthedocs.io |                                                  |
| /en/latest/#one-sample- |                                                  |
| t-test>`__              |                                                  |
+-------------------------+--------------------------------------------------+

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
