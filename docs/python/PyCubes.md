# PyCubes

Marching cubes is an algorithm to extract a 2D surface mesh from a 3D volume. This can be conceptualized as a 3D generalization of isolines on topographical or weather maps. It works by iterating across the volume, looking for regions which cross the level of interest. If such regions are found, triangulations are generated and added to an output mesh. The final result is a set of vertices and a set of triangular faces.


## Reference

- https://github.com/pmneila/PyMCubes
- https://scikit-image.org/docs/stable/auto_examples/edges/plot_marching_cubes.html