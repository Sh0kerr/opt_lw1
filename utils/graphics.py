import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot(f: callable, data: pd.DataFrame, min: int | float, max: int | float, step: int | float=100) -> None:
    x = np.linspace(min, max, step)

    plt.plot(x, f(x))
    plt.plot(data.iloc[len(data) - 1][0], f(data.iloc[len(data) - 1][0]), 'g*', 
             data.iloc[len(data) - 1][1], f(data.iloc[len(data) - 1][1]), 'g*')
    
    plt.show()
