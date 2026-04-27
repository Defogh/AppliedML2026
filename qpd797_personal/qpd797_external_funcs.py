import corner
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def corner_by_class(
    data,
    features,
    class_col="isb",
    positive_class=1,
    class_names=("b-jets", "light jets"),
    colors=("blue", "red"),
    bins=30,
):
    mask = data[class_col].to_numpy() == positive_class

    x_pos = data.loc[mask, features].dropna().to_numpy()
    x_neg = data.loc[~mask, features].dropna().to_numpy()

    # First class
    fig = corner.corner(
        x_pos,
        labels=features,
        color=colors[0],
        bins=bins,
        show_titles=True,
        hist_kwargs={"density": True, "linewidth": 2},
        plot_datapoints=False,
        plot_contours=True,
        fill_contours=False,
        no_fill_contours=True,
    )

    # Second class overlaid on same figure
    corner.corner(
        x_neg,
        fig=fig,
        labels=features,
        color=colors[1],
        bins=bins,
        show_titles=False,
        hist_kwargs={"density": True, "linewidth": 2},
        plot_datapoints=False,
        plot_contours=True,
        fill_contours=False,
        no_fill_contours=True,
    )

    # Manual legend
    handles = [
        Line2D([0], [0], color=colors[0], lw=2, label=class_names[0]),
        Line2D([0], [0], color=colors[1], lw=2, label=class_names[1]),
    ]
    fig.legend(handles=handles, loc="upper right", frameon=False)

    return fig