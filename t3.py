from standard_ax import get_standard_ax
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from t1 import f, a, b


t3 = pd.read_csv("t3.csv")
theta = t3["theta"].to_numpy()
T = t3["T"].to_numpy()
phi = t3["phi"].to_numpy()

T0 = f(theta, a, b)
omega = T0 / T

omega, phi, T0, theta, T = zip(*sorted(zip(omega, phi, T0, theta, T)))
omega, phi, T0, theta, T = np.array(omega), np.array(
    phi), np.array(T0), np.array(theta), np.array(T)


def draw_ax1(fig: plt.Figure):
    def f(x, sigma, mu, k):
        return k / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))

    args, _ = curve_fit(f, omega, theta)

    omega_ = np.linspace(omega.min(), omega.max(), 500)
    theta_ = f(omega_, *args)

    ax = get_standard_ax(fig, 121)
    ax.plot(omega, theta, "o")
    ax.plot(omega_, theta_)


def draw_ax2(fig: plt.Figure):
    # omega_phi_spline = make_interp_spline(omega, phi)
    # omega_ = np.linspace(omega.min(), omega.max(), 500)
    # phi_ = omega_phi_spline(omega_)

    ax = get_standard_ax(fig, 122)
    ax.plot(omega, phi, "o")
    # ax.plot(omega_, phi_)


def main():
    fig = plt.figure()
    draw_ax1(fig)
    draw_ax2(fig)

    plt.show()


if __name__ == "__main__":
    main()
