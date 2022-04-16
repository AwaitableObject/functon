from functon import defun, fn, IF

def factorial(N: int) -> defun((IF, ("=", "N", 1), 1, ("*", "N", ("factorial", ("-", "N", 1))))):
    """Compute the factorial of N."""

fn(factorial, 5)