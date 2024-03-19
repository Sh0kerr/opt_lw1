import funcs
import methods
from utils import plot, load_yaml

PATH = "./config.yml"

if __name__ == "__main__":
    constants = load_yaml(PATH)

    MIN = constants["MIN"]
    MAX = constants["MAX"]
    FUNC = constants["FUNC"]
    L = constants["L"]
    EPS = constants["EPS"]
    N = constants["N"]
    MAXIMIZATION = constants["MAXIMIZATION"]
    METHODS = [getattr(methods, method) for method in constants["METHODS"]]

    for method in METHODS:
        print(f"\n Метод: {method.__name__}")
        report, data = method(f=getattr(funcs, FUNC), a=MIN, b=MAX, l=L, eps=EPS, maximization=MAXIMIZATION)
        print(report)
        plot(f=getattr(funcs, FUNC), data=data, method_name=method.__name__, min=MIN, max=MAX)
