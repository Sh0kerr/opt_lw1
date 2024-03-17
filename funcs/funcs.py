def f1(x: int | float) -> int | float:
    return 3 * x - x ** 3 - 1


def f2(x: int | float) -> int | float:
    return (4 - x ** 2) / (x * (x ** 2 + 3))
