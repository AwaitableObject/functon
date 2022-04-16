from collections.abc import Iterable
from typing import Any, Sequence

from functon.exceptions import NotIterable


def INC(arg: Any) -> Any:
    return arg + 1


def QUOTE(arg: Any) -> Any:
    return arg


def CAR(arg: Sequence | None) -> Any:
    if arg is None:
        return None

    if isinstance(arg, Iterable):
        return arg[0] if len(arg) else arg

    raise NotIterable()
