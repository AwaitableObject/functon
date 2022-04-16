from functon import defun, IF, fn

def fib(n: int) -> defun(
    (IF, ("<", "n", 2),
        "n",
        ("+", ("fib", ("-", "n", 1), ("fib", ("-", "n", 2))))
    )
):
    """Compute the N'th Fibonacci number."""

fn(fib, 5)
