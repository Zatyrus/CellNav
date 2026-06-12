## dependencies
import matplotlib
import numpy as np
from PltStyler import PltStyler
import matplotlib.pyplot as plt
from rustworkx.visualization import mpl_draw

## custom dependencies
from Min3D.core.framework.surface_graph import SurfaceGraph

__all__ = ["shortest_path_mpl"]


# %% Visualization functions
def shortest_path_mpl(
    graph: SurfaceGraph, start_node: int, end_node: int, return_figure: bool = True
) -> plt.Figure:

    if not __check_plot_feasibility__(graph):
        return None

    # stylesheet for plotting
    PltStyler().set_stylesheet("bright").set_font(size=12).apply_stylesheet()

    # create color array for visualization
    colors_nodes = np.full(graph.graph.num_nodes(), fill_value=0)
    colors_edges = np.full(graph.graph.num_edges(), fill_value="k", dtype=object)

    path = graph.get_shortest_path(start_node, end_node)
    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

    for i, node in enumerate(path):
        colors_nodes[node] = i + 3
    for i, edge in enumerate(graph.graph.edge_list()):
        if (edge[0], edge[1]) in edges_in_path or (
            edge[1],
            edge[0],
        ) in edges_in_path:
            colors_edges[i] = "r"

    # Generate a visualization with a colorbar
    colormap = matplotlib.colormaps["plasma"]
    ax = plt.gca()
    sm = plt.cm.ScalarMappable(
        norm=plt.Normalize(
            vmin=min(colors_nodes),
            vmax=max(colors_nodes),
        ),
        cmap=colormap,
    )
    # colorbar
    colorbar = plt.colorbar(sm, ax=ax, label="Node Color (Path Progression)")
    colorbar.set_ticks([])
    ax.set_title(f"Shortest Path from Node {start_node} to Node {end_node}")

    fig = mpl_draw(
        graph.graph,
        node_size=100,
        node_color=colors_nodes,
        edge_color=colors_edges,
        cmap=colormap,
    )

    if return_figure:
        return fig
    else:
        plt.show()


# %% Helper functions
def __estimate_magnitude_scaler__(graph: SurfaceGraph, scale_adjust: int = -2) -> float:
    return np.power(
        10,
        np.floor(np.log10(np.diff(graph.vertices.get_points(), axis=0).max()))
        + scale_adjust,
    )


def __check_plot_feasibility__(graph: SurfaceGraph) -> bool:
    if graph.graph.num_nodes() > 1000:
        print(
            f"Graph has {graph.graph.num_nodes()} nodes, which may be too large for effective visualization. Consider using a smaller graph or visualizing a subgraph."
        )
        return False
    return True
