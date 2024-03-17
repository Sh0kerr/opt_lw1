from funcs import f1, f2
from methods import dichotomy, golden_section, fibbonachi
from utils import plot

MIN = -2
MAX = 2
FUNC = f1
L = 0.001
EPS = 0.0001
N = 10
MAXIMIZATION = False
METHODS = [dichotomy, golden_section, fibbonachi]

"""
import matplotlib.pyplot as plt
import numpy as np

from tabulate import tabulate


def countDihotomiya(left_border, right_border, epsilon, l, f, type):
    if l < 2 * epsilon:
        print("l can'b lower than 2 * epsilon")
        return

    data = []
    ak = left_border
    bk = right_border

    k = 1
    while bk - ak >= l:
        lambda_ = 0.5 * (ak + bk) - epsilon
        mu = 0.5 * (ak + bk) + epsilon
        f_lambda = f(lambda_)
        f_mu = f(mu)
        data.append([k, ak, bk, lambda_, mu, f_lambda, f_mu])

        if type * f_lambda < type * f_mu:
            bk = mu
        else:
            ak = lambda_
        k += 1

    data.append([k, ak, bk, ' ', ' ', ' ', ' '])
    print(tabulate(data, headers=['k', 'a_k', 'b_k', 'lyambda', 'mu', 'f(lyambda)', 'f(mu)']))

    x = np.linspace(left_border, right_border, 1000)
    y = f(x)

    plt.plot(x, y)
    plt.suptitle(f'l = {l}, eps = {epsilon}\nResult: left = {round(data[-1][1], 2)}, right = {round(data[-1][2], 2)}', size=12)
    plt.plot(data[-1][1], f(data[-1][1]), 'g*')
    plt.plot(data[-1][2], f(data[-1][2]), 'g*')
    plt.show()


print("min f1 в промежутке от [-2; 2], l = 0.3, eps = 0.1")
countDihotomiya(-2, 2, 0.1, 0.3, f1, 1)
print("\nmax f2 в промежутке от [-10; 0], l = 0.3, eps = 0.1")
countDihotomiya(-10, 0, 0.1, 0.3, f2, -1)

print("\nmin f1 в промежутке от [-3; 0], l = 0.3, eps = 0.1")
countDihotomiya(-3, 0, 0.1, 0.3, f1, 1)

print("\nmax f1 в промежутке от [0.8; 5], l = 0.3, eps = 0.1")
countDihotomiya(0.8, 5, 0.1, 0.3, f1, -1)

print("\nmin f1 в промежутке от [-10; 0.5], l = 0.3, eps = 0.1")
countDihotomiya(-10, 0.5, 0.1, 0.3, f1, 1)

print("\nmax f2 в промежутке от [-5; 0], l = 0.3, eps = 0.1")
countDihotomiya(-5, 0, 0.1, 0.3, f2, -1)

print("\nmax f2 в промежутке от [0; 10], l = 0.3, eps = 0.1")
countDihotomiya(0, 10, 0.1, 0.3, f2, -1)

print("\nmin f2 в промежутке от [-5; 5], l = 0.3, eps = 0.1")
countDihotomiya(-5, 5, 0.1, 0.3, f2, 1)


print("\nМеняем epsilon:\n")

print("min f1 в промежутке от [-2; 2], l = 0.3, eps = 0.1")
countDihotomiya(-2, 2, 0.1, 0.3, f1, 1)

print("\nmin f1 в промежутке от [-2; 2], l = 0.3, eps = 0.01")
countDihotomiya(-2, 2, 0.01, 0.3, f1, 1)

print("\nmin f1 в промежутке от [-2; 2], l = 0.3, eps = 0.001")
countDihotomiya(-2, 2, 0.001, 0.3, f1, 1)

print("\nmax f2 в промежутке от [-10; 0], l = 0.3, eps = 0.1")
countDihotomiya(-10, 0, 0.1, 0.3, f2, -1)

print("\nmax f2 в промежутке от [-10; 0], l = 0.3, eps = 0.01")
countDihotomiya(-10, 0, 0.01, 0.3, f2, -1)

print("\nmax f2 в промежутке от [-10; 0], l = 0.3, eps = 0.001")
countDihotomiya(-10, 0, 0.001, 0.3, f2, -1)

print("\nМеняем l:\n")

print("min f1 в промежутке от [-2; 2], l = 0.1, eps = 0.001")
countDihotomiya(-2, 2, 0.001, 0.1, f1, 1)

print("\nmin f1 в промежутке от [-2; 2], l = 0.01, eps = 0.001")
countDihotomiya(-2, 2, 0.001, 0.01, f1, 1)

print("\nmax f2 в промежутке от [-10; 0], l = 0.1, eps = 0.001")
countDihotomiya(-10, 0, 0.001, 0.1, f2, -1)

print("\nmax f2 в промежутке от [-10; 0], l = 0.01, eps = 0.001")
countDihotomiya(-10, 0, 0.001, 0.01, f2, -1)
"""

if __name__ == "__main__":
    print(f"\n Метод: {dichotomy.__name__}")
    res_dihotomy = dichotomy(f=FUNC, a=MIN, b=MAX, l=L, eps=EPS, maximization=MAXIMIZATION)
    print(res_dihotomy)
    plot(f=FUNC, data=res_dihotomy, min=MIN, max=MAX)

    print(f"\n Метод: {golden_section.__name__}")
    res_golden = golden_section(f=FUNC, a=MIN, b=MAX, l=L, maximization=MAXIMIZATION)
    print(res_golden)
    plot(f=FUNC, data=res_golden, min=MIN, max=MAX)

    print(f"\n Метод: {fibbonachi.__name__}")
    res_fibbonachi = fibbonachi(f=FUNC, a=MIN, b=MAX, l=L, eps=EPS, n=N, maximization=MAXIMIZATION)
    print(res_fibbonachi)
    plot(f=FUNC, data=res_fibbonachi, min=MIN, max=MAX)
