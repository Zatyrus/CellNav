## dependencies
import numpy as np
import open3d as o3d
from typing import NoReturn

## dustom dependency imports
from Min3D.core.framework.surface_wireframe import SurfaceWireframe


# implementation - this is a direct copy of the wireframe, but with unique edges only (i.e. no duplicate edges)
class UniqueSurfaceWireframe(SurfaceWireframe):
    def __init__(self, geometry: o3d.geometry.LineSet, **kwargs) -> NoReturn:
        super().__init__(geometry=geometry, **kwargs)

    @classmethod
    def from_wireframe(
        cls, wireframe: SurfaceWireframe, **kwargs
    ) -> "UniqueSurfaceWireframe":
        unique_edges = set()
        for edge in wireframe.get_lines():
            sorted_edge = tuple(sorted(edge))
            unique_edges.add(sorted_edge)

        unique_edges_list = list(unique_edges)
        unique_line_set = o3d.geometry.LineSet()
        unique_line_set.points = wireframe.points
        unique_line_set.lines = o3d.utility.Vector2iVector(np.array(unique_edges_list))

        return cls.from_o3d(unique_line_set, **kwargs)
