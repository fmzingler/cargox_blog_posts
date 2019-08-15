from matplotlib.pyplot import subplots
from seaborn import heatmap


def plot_cohort_matrix(cohort_matrix, plot_title):
    fig, ax = subplots(figsize=(20, 10))
    
    heatmap(cohort_matrix, mask=cohort_matrix.isnull(), annot=True, fmt='.0%', annot_kws={"size": 20}, 
        cmap="coolwarm", ax=ax)

    ax.set_title(plot_title, fontsize=30)
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.tick_params("x", labelsize=20)
    ax.tick_params("y", labelsize=20, rotation=0)

    return ax
