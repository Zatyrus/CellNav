## dependencies
import numpy as np
import open3d as o3d

from typing import List, Union

## custom dependencies
from Min3D.core.util.make_3d_path import make_3d_path

__all__ = ["draw_3d_path"]


# %% Visualization functions
def draw_3d_path(
    path: Union[np.ndarray, List[np.ndarray]],
    color: Union[np.ndarray, List[np.ndarray]],
    cmap: str = "viridis",
    scale_factor: float = 1.0,
    magnitude: Union[str, float] = "auto",
) -> None:
    ## generate path3D object from the path and color information
    path_3d = make_3d_path(
        path=path,
        color=color,
        cmap=cmap,
        scale_factor=scale_factor,
        magnitude=magnitude,
    )
    # visualize the base wireframe and the path lineset together
    o3d.visualization.draw_geometries(  # type: ignore
        path_3d.to_list(),
        window_name="Path Visualization",
    )
