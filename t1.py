from standard_ax import get_standard_ax
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np


t1 = pd.read_csv("t1.csv")
theta = t1["theta"].to_numpy()
T0 = t1["T0"].to_numpy()


def f(x, a, b):
    return a * x + b


(a, b), _ = curve_fit(f, theta, T0)


def main():
    xlim = (20., 160.)
    xticks = np.arange(20., 160., 10.)

    fig = plt.figure()
    ax = get_standard_ax(fig, 111, xlabel="θ (°)", ylabel="T0 (s)",
                         xlim=xlim, xticks=xticks)

    ax.plot(theta, T0, "o")
    ax.plot(theta, f(theta, a, b))
    ax.grid()

    plt.show()


if __name__ == "__main__":
    main()
