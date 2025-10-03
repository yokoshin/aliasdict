# Contributing to aliasdict

This guide provides newcomers with an overview of the repository and tips for getting started.

## Project Structure

```
aliasdict/
├── aliasdict/          # Package with the implementation
│   ├── __init__.py
│   └── aliasdict.py
├── tests/              # Unit tests
│   └── test_aliasdict.py
├── setup.py            # Packaging script (generates version file)
├── setup.cfg
├── README.md           # Short README
└── README.rst          # Main documentation
```

### Key Modules

- **`aliasdict/aliasdict.py`**
  - `GZDict` implements a dictionary wrapper that optionally gzip-compresses
    stored values.
  - `AliasDict` extends `GZDict` to allow multiple keys (aliases) to refer to
    a single value.
- **`tests/test_aliasdict.py`**
  - Contains unit tests covering alias creation, deletion, persistence,
    iteration and compression.

## Getting Started

1. **Run the tests** using `python -m unittest` or `pytest` to verify your
   environment before and after making changes.
2. **Review `aliasdict/aliasdict.py`** to understand how aliases are stored and
   how compressed values are handled.
3. **Check `setup.py`** if you plan to adjust packaging or versioning.
4. **Refer to `README.rst`** for usage examples such as saving/loading data or
   disabling compression.

## Next Steps

- Experiment with the test suite to explore edge cases.
- Look into Python packaging if you wish to publish a new release.
- Contributions should include updates to the tests when adding new features.

We hope this helps you get started with `aliasdict`.
