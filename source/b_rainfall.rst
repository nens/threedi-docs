Rainfall
========

.. _rain:

In 3Di rainfall can be used as model input in different ways. The most simple one is letting it rain on the 2D surface, in other words on the 2D computational cells. The general rainfall unit is mm/hr. In 3Di calculation, the rainfall is automatically converted into rainfall volume (m3 [cell area x rainfall intensity x delta t]). 

The basic rainfall input types for 3Di include: 

1. rain cloud - a circle type of spatial rainfall with a constant value within the circle and specified time period, 

#. radar rainfall - gridded rainfall type with non-uniform spatial and temporal rainfall, 

#. design or time series rainfall - time series of rain from Lizard used global on the model domain, and 

#. constant rainfall - temporally and spatially constant rainfall event over the simulation.  

These types can be accessed through the 3Di live site and the API. 


Rainfall on 0D node (inflow)
----------------------------

Apart from rainfall on the 2D domain, 3Di uses an 0D inflow module (impervious area or surface area). The rainfall volume (area x rainfall_intensity x delta t) is calculated for each time step for each impervious area or surface area. Based on the formulation of the impervious area or surface area (:ref:`inflow`), the discharge hydro-graph (discharge over time) is calculated as a lateral discharge on its downstream 1D node.  

.. figure:: image/b_rainfall_inloop.png
   :alt: rainfall_inloop
     
   Rainfall is translated to a lateral discharge on a 1D node.

Rainfall on 0D and 2D
----------------------------

3Di allows the user to select whether rainfall falls on 0D, 2D or both. Using both 0D and 2D rainfall can be useful in several cases, for example:

- complex sewerage models that use inflow for the flow of water from roofs to the sewerage and 2D surface for rainfall and discharge over roads, or

- large (river) systems in which a small area is modeled in detail while upstream catchments are lumped in 0D inflow.

When using both 0D and 2D rainfall one must be aware that the user is responsible for defining the correct areas in 0D and make sure to remove these from the 2D model to avoid double counting of one surface.

.. figure:: image/b_rainfall_hybrid.png
   :alt: rainfall_hybrid
     
   Rainfall over 2D and through 0D surface as a lateral discharge.


Gridded rainfall
----------------

The resolution of spatially distributed rainfall data does usually not match the resolution of the 2D calculation cells. If a rainfall grid covers the center of a 2D cell, there will be rain on the whole of the calculation cell (when the rain covers a whole 2D cell) or partially (if the rain covers part of a 2D cell). This indicates when a rain cloud or grid covers only part of a 2D cell, there will be either no rain (if the rain does not cover the 2D cell center) or partial rain (if the rain partially cover a 2D cell).  Furthermore, no rain can fall on a nodata pixels in the calculation cell.

For gridded rainfall on 0D the rainfall intensity is determined on the location of downstream the connection node related to the inflow surface.
