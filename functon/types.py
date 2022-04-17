from types import ModuleType
from typing import Any, Callable, Optional

Expr = tuple | Callable


class FunctonFunction:
    def __init__(
        self,
        func_name: str,
        func_code: tuple,
        func_module: Optional[ModuleType],
    ):
        self.func_name = func_name
        self.func_code = func_code
        self.func_module = func_module

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(self.func_name)
        print("Hello world")
        return 9
