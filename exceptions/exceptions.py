class WrongIntervalRange(Exception):
    """Неправильно задана конечная длина интервала неопределенности."""
    
    def __init__(self, l: int | float, eps: int | float):
        super().__init__(f"Заданная конечная длина интервала неопределенности {l=} должна быть больше {2 * eps=}")
        self.l = l
        self.eps = eps
