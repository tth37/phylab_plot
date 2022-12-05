from standard_ax import get_standard_ax
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
from t1 import f as t1_f
from t1 import a, b


t3 = pd.read_csv("t3.csv")
theta = t3["theta"].to_numpy()
T = t3["T"].to_numpy()
phi = t3["phi"].to_numpy()

T0 = t1_f(theta, a, b)
l = T0 / T

l, phi, T0, theta, T = zip(*sorted(zip(l, phi, T0, theta, T)))
l, phi, T0, theta, T = np.array(l), np.array(
    phi), np.array(T0), np.array(theta), np.array(T)
phi = - phi

w = np.pi * 2 / T
w0 = np.pi * 2 / T0


def draw_ax1(fig: plt.Figure):
    xlim = (0.96, 1.04)
    xticks = np.arange(0.96, 1.04, 0.01)

    ylim = (45., 130.)
    yticks = np.arange(45., 130., 5.)

    def f(x, m, w0, delta):
        return m / np.sqrt((w0 ** 2 - (x * w0) ** 2) ** 2 + 4 * (delta * (x * w0)) ** 2)

    args, _ = curve_fit(f, l, theta)

    l_ = np.linspace(l.min(), l.max(), 500)
    theta_ = f(l_, *args)

    theta_max = theta_.max()
    theta_max_l = l_[theta_ == theta_max]

    theta_sqrt_max = theta_max / np.sqrt(2)
    theta_sqrt_max_l1 = l_[np.abs(theta_[:250] - theta_sqrt_max).argmin()]
    theta_sqrt_max_l2 = l_[
        np.abs(theta_[250:] - theta_sqrt_max).argmin() + 250]

    ax = get_standard_ax(fig, 121, xlabel="ω/ω0", ylabel="θ (°)",
                         xlim=xlim, xticks=xticks, ylim=ylim, yticks=yticks)
    ax.plot(l, theta, "o")
    ax.plot(l_, theta_)

    ax.hlines(theta_max, xlim[0], theta_max_l,
              linestyles="dashed", colors="red", label="θr")
    ax.vlines(theta_max_l, ylim[0], theta_max,
              linestyles="dashed", colors="red")

    ax.hlines(theta_sqrt_max, xlim[0], theta_sqrt_max_l2,
              linestyles="dashed", colors="green", label="θr/√2")
    ax.vlines(theta_sqrt_max_l1, ylim[0], theta_sqrt_max,
              linestyles="dashed", colors="green")
    ax.vlines(theta_sqrt_max_l2, ylim[0], theta_sqrt_max,
              linestyles="dashed", colors="green")

    w0 = t1_f(theta_sqrt_max, a, b)
    w_l1 = w0 * theta_sqrt_max_l1
    w_l2 = w0 * theta_sqrt_max_l2

    print(f"θr = {theta_max:.2f}°")
    print(f"θr/√2 = {theta_sqrt_max:.2f}°")
    print(f"w0 = {w0:.2f}rad/s")
    print(f"w- = {w_l1:.2f}rad/s")
    print(f"w+ = {w_l2:.2f}rad/s")

    ax.grid()
    ax.legend()


def draw_ax2(fig: plt.Figure):
    xlim = (0.96, 1.04)
    xticks = np.arange(0.96, 1.04, 0.01)

    ylim = (-160., -10.)
    yticks = np.arange(-160., -10., 10.)

    def f(x, w0, delta):
        return np.arctan2((-2 * delta * (x * w0)), (w0 ** 2 - (x * w0) ** 2)) * 180 / np.pi

    args, _ = curve_fit(f, l, phi)

    l_ = np.linspace(l.min(), l.max(), 500)
    phi_ = f(l_, *args)

    ax = get_standard_ax(fig, 122, xlabel="ω/ω0", ylabel="φ (°)",
                         xlim=xlim, xticks=xticks, ylim=ylim, yticks=yticks)
    ax.plot(l, phi, "o")
    ax.plot(l_, phi_)
    ax.grid()


def main():
    fig = plt.figure()
    draw_ax1(fig)
    draw_ax2(fig)

    plt.show()


if __name__ == "__main__":
    main()
