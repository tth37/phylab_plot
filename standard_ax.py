import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt


def get_standard_ax(fig: plt.Figure, rect, xlabel="x", ylabel="y", xlim=None, ylim=None, xticks=None, yticks=None) -> AA.Axes:
    ax = fig.add_subplot(rect, axes_class=AA.Axes)
    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_fixed_axis(loc="bottom", offset=(0, 0))
    ax.axis["x"].set_axisline_style("-|>", size=1)
    ax.axis["x"].label.set_text(xlabel)
    ax.axis["x"].set_axis_direction("bottom")
    ax.axis["x"].label.set_axis_direction("bottom")
    if xlim is not None:
        ax.set_xlim(xlim)
    if xticks is not None:
        ax.set_xticks(xticks)

    ax.axis["y"] = ax.new_fixed_axis(loc="left", offset=(0, 0))
    ax.axis["y"].set_axisline_style("-|>", size=1)
    ax.axis["y"].label.set_text(ylabel)
    ax.axis["y"].set_axis_direction("left")
    ax.axis["y"].label.set_axis_direction("left")
    if ylim is not None:
        ax.set_ylim(ylim)
    if yticks is not None:
        ax.set_yticks(yticks)

    return ax
