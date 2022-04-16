import builtins
from typing import Any, Callable


def defun(body: tuple) -> Callable:
    # print(dir(inspect.getmodule(func))) get function for recursion, or internal usage
    def result() -> tuple:
        return body

    return result


def fn(func: Callable, *args: Any) -> Callable:
    if hasattr(builtins, func.__name__):
        return func(*args)
    return func.__annotations__["return"](args)
