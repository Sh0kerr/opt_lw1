import pandas as pd

PHI = (5 ** 0.5 - 1) / 2    # PHI ~= 0.618


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a


def dichotomy(f: callable, 
              a: int | float, b: int | float, 
              l: int | float=0.1, eps: int | float=1e-6, 
              maximization: bool=False) -> pd.DataFrame:
    assert l > 2 * eps

    df = pd.DataFrame(columns=['a', 'b', 
                               'lambda', 'mu', 
                               f'{f.__name__}(lambda)', f'{f.__name__}(mu)'])

    while abs(b - a) > l:
        a_k = a
        b_k = b

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

        data = pd.DataFrame({'a': [a_k], 'b': [b_k], 
                'lambda': [lambd], 'mu': [mu], 
                f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})
        
        df = pd.concat([df, data], ignore_index=True)
    
    df.index += 1
    df.index.name = 'k'

    return df


def golden_section(f: callable, 
                   a: int | float, b: int | float, 
                   l: int | float, 
                   maximization: bool=False) -> pd.DataFrame:
    """
    @TODO: походу некорректно работает для f2 хз почему хзхзхзхз
    лох
    """
    lambd = a + (1 - PHI) * (b - a)
    mu = a + PHI * (b - a)

    f_lambd = f(lambd)
    f_mu = f(mu)

    df = pd.DataFrame({'a': [a], 'b': [b], 
                       'lambda': [lambd], 'mu': [mu], 
                       f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})
    
    while abs(b - a) > l:
        if f_lambd < f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu
            mu = a + PHI * (b - a) if maximization else lambd
            lambd = mu if maximization else a + (1 - PHI) * (b - a)
            f_mu = f(mu) if maximization else f_lambd
            f_lambd = f_mu if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b
            lambd = a + (1 - PHI) * (b - a) if maximization else mu
            mu = lambd if maximization else a + PHI * (b - a)
            f_lambd = f(lambd) if maximization else f_mu
            f_mu = f_lambd if maximization else f(mu)

        data = pd.DataFrame({'a': [a], 'b': [b], 
                             'lambda': [lambd], 'mu': [mu], 
                             f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})

        df = pd.concat([df, data], ignore_index=True)
    
    df.index += 1
    df.index.name = 'k'

    return df


def fibonacci(f: callable, 
              a: int | float, b: int | float, l: int | float, 
              maximization: bool=False) -> pd.DataFrame:
    n = 0
    while fib(n) < (b - a) / l:
        n += 1

    lambd = a + fib(n - 2) * (b - a) / fib(n)
    mu = a + fib(n - 1) * (b - a) / fib(n)
    k = 0

    f_lambd = f(lambd)
    f_mu = f(mu)

    df = pd.DataFrame({'a': [a], 'b': [b], 
                       'lambda': [lambd], 'mu': [mu], 
                       f'{f.__name__}(lambda)': [f_lambd], f'{f.__name__}(mu)': [f_mu]})
    
    while k < n - 3:
        if f_lambd <= f_mu:
            a = lambd if maximization else a
            b = b if maximization else mu
            mu = a + fib(n - k - 2) * (b - a) / fib(n - k - 1) if maximization else lambd
            lambd = mu if maximization else a + fib(n - k - 3) * (b - a) / fib(n - k - 1)
            temp = f_mu
            f_mu = f(mu) if maximization else f_lambd
            f_lambd = temp if maximization else f(lambd)
        else:
            a = a if maximization else lambd
            b = mu if maximization else b
            temp = mu
            mu = lambd if maximization else a + fib(n - k - 2) * (b - a) / fib(n - k - 1)
            lambd = a + fib(n - k - 3) * (b - a) / fib(n - k - 1) if maximization else temp
            temp = f_lambd
            f_lambd = f(lambd) if maximization else f_mu
            f_mu = temp if maximization else f(mu)
        k += 1

        df.loc[len(df.index)] = [a, b, lambd, mu, f_lambd, f_mu]
    
    df.index += 1
    df.index.name = 'k'

    return df
