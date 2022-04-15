[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Functon λ [EXPERIMENTAL]

## Installation

```
python3 -m pip install functon
```

## Usage
Hello world:

```python
>> from functon import fn
>> fn(print, "Hello world!")
Hello world!
```


Triple the value of a number:

```python
>> from functon import defun, fn
>> triple = defun(("X"),
    "Compute three times X.",
    ("*", 3, "X"))
>> res = fn(triple, 3)
>> res
9
```

Compute factorials using recursion:

```python
>> from functon import defun, fn
>> factorial = defun(("N"),
    "Compute the factorial of N.",
    ("if", ("=", "N", 1),
        1,
    ("*", "N", ("factorial", ("-", "N", 1)))))
>> fn(factorial, 5) 
120
```