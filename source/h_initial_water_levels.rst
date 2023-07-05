.. _initial_water_levels:

Initial water levels
====================

Initial water levels in 2D
--------------------------

Initial water levels for the 2D domain can be set before the start of the simulation. This can be a global value that applies to all cells, or a different value for each cell (spatially varying initial water levels). The input for spatially varying initial water levels is a raster. Such rasters typically have pixels that are smaller than the computational cells. Because there can only be one water level per cell, the raster data is aggregated to calculate the initial water level for each cell. Three aggegation methods are available:

* Minimum: the lowest value of all pixels in the cell will be used

* Maximum: the highest value of all pixels in the cell will be used

* Average: the average of the values of the pixels in the cell will be used


Initial water levels in 1D
--------------------------

Initial water levels can be set for each 1D node before starting a simulation. The initial water levels can also be set at an earlier stage in the modellinge process, i.e. in the schematisation. In this case, the initial water levels are set for each connection node, and linearly interpolated for added calculation nodes; see :ref:`techref_calculation_point_distance`.


