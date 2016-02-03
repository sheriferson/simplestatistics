## simple-statistics-py

[simple-statistics](https://github.com/tmcw/simple-statistics)
for Python.

### Tests

    python simple_statistics.py

or

    python3 simple_statistics.py


## Spirit and rules

- Everything should be implemented in raw, organic, locally sourced python.
- Use libraries only if you have to and only when unrelated to the math/statistics. For example, `from functools import reduce` to make `reduce` available for those using python3. That's okay, because it's about making python work and not about making the stats easier.
- It's okay to use operators and functions if they correspond to regular calculator buttons. For example, all calculators have a built-in square root function, so there is no need to implement that ourselves, we can use `math.sqrt()`.
Anything beyond that, like `mean`, `median`, we have to write ourselves.
