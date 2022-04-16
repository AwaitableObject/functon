[![Actions Status](https://github.com/zhivykh/functon/workflows/CI/badge.svg)](https://github.com/zhivykh/functon/actions/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Stable Version](https://img.shields.io/pypi/v/functon?color=blue)](https://pypi.org/project/functon/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

# Functon λ [EXPERIMENTAL]

## Installation

```
python3 -m pip install functon
```

## Usage
Hello world:

```python
>>> from functon import fn
>>> fn(print, "Hello world!")
'Hello world!'
```


Triple the value of a number:

```python
>>> from functon import defun, fn
>>> def triple(x: int) -> defun(("*", 3, "x")):
...     """Compute three times X."""
>>> fn(triple, 3)
9
```

Compute factorials using recursion:

```python
>>> from functon import defun, fn, IF
>>> def factorial(N: int) -> defun((IF, ("=", "N", 1), 1, ("*", "N", ("factorial", ("-", "N", 1))))):
...     """Compute the factorial of N."""
>>> fn(factorial, 5) 
120
```