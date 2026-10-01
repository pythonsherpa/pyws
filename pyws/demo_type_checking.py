from typing import Optional, List, Dict

a: int = 42
b: float = 3.14
c: bool = True
d: str = "hello world"


def multiply(x: int, y: int) -> int:
    return x * y


print(multiply(4, 5))


def greet(name: str | None = None) -> str:
    if name is None:
        name = "stranger"
    return "Hello " + name

print(greet())

e: list[int] = [1,2,3]
f: dict[str, str]
g: int | str = "1"
h: list[int | str] = [1, "2"]


class MyClass:
    value: int = 42

    def __init__(self) -> None:
        ...

    def multiply(self, x: int, y: int) -> int:
        return x * y


