from standard_ax import get_standard_ax
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import math


def main():
    t2 = pd.read_csv("t2.csv")
    theta = t2["theta"].to_numpy()
    T = t2["T"].to_numpy()

    ln = np.array([math.log(theta[i]) - math.log(theta[i + 5])
                   for i in range(0, 5)])

    print("ln[] =", ln)
    print("mean(ln[]) =", np.mean(ln))
    print("mean(T[]) =", np.mean(T))


if __name__ == "__main__":
    main()
