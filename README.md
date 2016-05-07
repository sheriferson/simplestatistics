## simple-statistics-py

[simple-statistics](https://github.com/tmcw/simple-statistics)
for Python.

### Tests

    python simple_statistics.py

or

    python3 simple_statistics.py


### Functions

| Function                       | Example                              |
|--------------------------------|--------------------------------------|
| Mean                           | `mean([1, 2, 3])`                    |
| Geometric mean                 | `geometric_mean([1, 10])`            |
| Sample and population variance | `variance([1, 2, 3], sample = True)` |
| Standard deviation             | `standard_deviation([1, 2, 3])`      |
| One-sample t-test              | `t_test([1, 2, 3, 4, 5, 6], 3.385)`  |
| Min                            | `min([-3, 0, 3])`                    |
| Max                            | `max([1, 2, 3])`                     |

#### Coming soon

- `median([1, 2, 3])`
- `mode([1, 2, 1, 3, 3, 5])`
- Proper documentation.

And more.

### Spirit and rules

- Everything should be implemented in raw, organic, locally sourced python.
- Use libraries only if you have to and only when unrelated to the math/statistics. For example, `from functools import reduce` to make `reduce` available for those using python3. That's okay, because it's about making python work and not about making the stats easier.
- It's okay to use operators and functions if they correspond to regular calculator buttons. For example, all calculators have a built-in square root function, so there is no need to implement that ourselves, we can use `math.sqrt()`.
Anything beyond that, like `mean`, `median`, we have to write ourselves.
