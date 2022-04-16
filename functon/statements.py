from collections.abc import Iterable
from typing import Callable

from functon.types import Expr


def IF(cond: bool, true_expr: Expr, false_expr: Expr) -> Expr:
    if cond:
        return true_expr
    return false_expr


def FOR(it: Iterable, body: Callable) -> None:
    for i in it:
        body(i)
