Rainfall
========

The basic idea for the rainfall input to a 3Di model is on raining 2D cells. The general rainfall unit is mm/hr. In 3Di calculation, the rainfall is automatically  converted into rainfall volume (m3 [area x rainfall intensity x delta t]) in a time step for further hydrologic and hydrodynamic calculation. 

The basic rainfall input types for 3Di include: 

1. rain cloud - a circle type of spatial rainfall with a constant value within the circle and specified time period, 

#. radar rainfall - gridded rainfall type with non-uniform spatial and temporal rainfall, 

#. design rainfall - the typical hyetograph type of design rainfall event, and 

#. constant rainfall - temporally and spatially constant rainfall event over the simulation.  



Rainfall on 1D node (inflow)
----------------------------


The inflow for 1D node is calculated by the 0D module (impervious area or surface area). The rainfall volume (area x rainfall_intensity x delta t) is calculated for each time step for each impervious area or surface area. Based on the formulation of the impervious area or surface area (:ref:`inflow`), the discharge hydrograph (discharge over time) is calculated as the inflow of its downstream 1D node.  


Gridded rainfall
----------------

The resolution of spatially distributed rainfall data does usually not match the resolution of the 2D calculation cells. If a rainfall grid covers the center of a 2D cell, there will be rain on the whole of the calculation cell (when the rain covers a whole 2D cell) or partially (if the rain covers part of a 2D cell). This indicates when a rain cloud or grid covers only part of a 2D cell, there will be either no rain (if the rain does not cover the 2D cell center) or partial rain (if the rain partially cover a 2D cell).  Furthermore, no rain can fall on a nodata pixels in the calculation cell.

For gridded rainfall on 1D the rainfall intensity is determined on the location of the connection node related to the inflow surface.
