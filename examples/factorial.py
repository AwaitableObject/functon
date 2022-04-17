from functon import defun, fn, IF

def factorial(n: int) -> defun(
    (IF, ("=", "n", 1), 
    1, 
    ("*", "n", ("factorial", ("-", "n", 1))))
):
    """Compute the factorial of n."""

fn(factorial, 5)