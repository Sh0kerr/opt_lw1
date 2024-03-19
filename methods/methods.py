import pandas as pd

import exceptions

IntOrFloat = int | float
PHI = (5 ** 0.5 - 1) / 2    # PHI ~= 0.618


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a


def get_report(f, a, b, iters) -> dict[str: IntOrFloat]:
    optimum = (a + b) / 2
    f_optimum = f(optimum)

    report = {
        'Оптимум': optimum,
        'Функция в оптимуме': f_optimum,
        'Количество итераций': iters,
    }

    return report


def rename(new_name: str):
    def wrapper(f):
        f.__name__ = new_name
        return f
    return wrapper


@rename('Дихотомия')
def dichotomy(f: callable, 
              a: IntOrFloat, b: IntOrFloat, 
              l: IntOrFloat=0.1, eps: IntOrFloat=1e-6, 
              maximization: bool=False) -> tuple[dict[str: IntOrFloat], pd.DataFrame]:
    if l <= 2 * eps:
        raise exceptions.WrongIntervalRange(l, eps)

    data = pd.DataFrame(columns=['a', 'b', 
                               'lambda', 'mu', 
                               f'{f.__name__}(lambda)', f'{f.__name__}(mu)'])

    while abs(b - a) > l:
        lambd = (a + b) / 2 - eps
        mu = (a + b) / 2 + eps

        f_lambd = f(lambd)
        f_mu = f(mu)

        if f_lambd < f_mu:
            b = b if maximization else mu
            a = lambd if maximization else a
        else:
            a = a if maximization else lambd
            b = mu if maximization else b
        
        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]
    
    data.index += 1
    data.index.name = 'k'

    res = get_report(f, a, b, len(data.index))

    return res, data


@rename('Золотое сечение')
def golden_section(f: callable, 
                   a: IntOrFloat, b: IntOrFloat, 
                   l: IntOrFloat=0.1, eps: IntOrFloat=1e-6, 
                   maximization: bool=False) -> tuple[dict[str: IntOrFloat], pd.DataFrame]:
    lambd = a + (1 - PHI) * (b - a)
    mu = a + PHI * (b - a)

    f_lambd = f(lambd)
    f_mu = f(mu)

    data = pd.DataFrame({'a': [a], 'b': [b], 
                       'lambda': [lambd], 'mu': [mu], 
                       f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})
    
    while abs(b - a) > l:
        if f_lambd < f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu

            temp = mu

            mu = a + PHI * (b - a) if maximization else lambd
            lambd = temp if maximization else a + (1 - PHI) * (b - a)

            temp = f_mu

            f_mu = f(mu) if maximization else f_lambd
            f_lambd = temp if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b

            temp = lambd

            lambd = a + (1 - PHI) * (b - a) if maximization else mu
            mu = temp if maximization else a + PHI * (b - a)
            
            temp = f_lambd

            f_lambd = f(lambd) if maximization else f_mu
            f_mu = temp if maximization else f(mu)

        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]
    
    data.index += 1
    data.index.name = 'k'
    
    res = get_report(f, a, b, len(data.index))

    return res, data


@rename('Фибоначчи')
def fibonacci(f: callable, 
              a: IntOrFloat, b: IntOrFloat, 
              l: IntOrFloat=0.1, eps: IntOrFloat=1e-6,
              maximization: bool=False) -> tuple[dict[str: IntOrFloat], pd.DataFrame]:
    n = 0
    while fib(n) < (b - a) / l:
        n += 1

    lambd = a + fib(n - 2) * (b - a) / fib(n)
    mu = a + fib(n - 1) * (b - a) / fib(n)
    k = 0

    f_lambd = f(lambd)
    f_mu = f(mu)

    data = pd.DataFrame({'a': [a], 'b': [b], 
                       'lambda': [lambd], 'mu': [mu], 
                       f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})
    
    while k < n - 3:
        if f_lambd <= f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu

            temp = mu

            mu = a + fib(n - k - 2) * (b - a) / fib(n - k - 1) if maximization else lambd
            lambd = temp if maximization else a + fib(n - k - 3) * (b - a) / fib(n - k - 1)
            
            temp = f_mu

            f_mu = f(mu) if maximization else f_lambd
            f_lambd = temp if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b

            temp = lambd

            lambd = a + fib(n - k - 3) * (b - a) / fib(n - k - 1) if maximization else mu
            mu = temp if maximization else a + fib(n - k - 2) * (b - a) / fib(n - k - 1)

            temp = f_lambd

            f_lambd = f(lambd) if maximization else f_mu
            f_mu = temp if maximization else f(mu)

        k += 1

        data.loc[len(data.index)] = [a, b, lambd, mu, f_lambd, f_mu]
    
    data.index += 1
    data.index.name = 'k'
    
    res = get_report(f, a, b, len(data.index))

    return res, data
