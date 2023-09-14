.. _water_depth_level_rasters:

Water depth and level rasters
-----------------------------

For each timestep, 3Di calculates the water level in each computational cell. However, the water *depth* is different for each pixel within the cell. To calculate water depths from water levels, the DEM needs to be subtracted from the water level. This results in a raster with a water depth value for each pixel.

For some applications, it is useful to have water levels as a raster file. For example, to use them as :ref:`initial_water_levels` in the next simulation.

Two :ref:`3di_processing_toolbox` allow you to make such water depth and water level rasters from 3Di results: *Maximum water depth/level raster* and *Water depth/level raster*. Access these processing algorithms via *Main menu* > *Processing* > *Toolbox* > *3Di* > *Post-process results*.

Both tools have the option to spatially interpolate the water levels. This is recommended to use if the water level gradients are large, such as is often the case in sloping areas.

The resolution of the output rasters is equal to the resolution of the DEM. 

.. note:: 
   
   If these tools give unexpected results, please make sure you have used the correct computational grid file (gridadmin.h5) and the correct DEM. 

Maximum water depth/level raster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool first calculates the maximum water level that occurs in each cell during the simulation, before interpolating and/or subtracting the DEM values.  

Water depth/level raster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool can be used to generate a water depth or water level raster for a specific time step, for example, at the end of the rainfall event. It also allows you to export a set of rasters for a range of time steps.





