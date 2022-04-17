from collections.abc import Iterable
from typing import Any, Callable

from functon.types import Expr


def RETURN(expr: Expr) -> Any:
    """Return function."""

    return expr


def IF(cond: bool, true_expr: Expr, false_expr: Expr) -> Expr:
    """If function."""

    if cond:
        return true_expr
    return false_expr


def FOR(it: Iterable, body: Callable) -> None:
    """For function."""
    for i in it:
        body(i)
