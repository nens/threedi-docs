Infiltration
=========
 
Infiltration is the process of water slowly sinking into the soil. The infiltration capacity depends on the type of soil and landuse. In 3Di the infiltration capacity is given for every pixel of the input raster and given in mm/day. In the subgrid method, the infiltration is handled per calculation cell: the information per pixel is tabulated to form a relation between water level and infiltration capacity. The table is build using the same resolution (or step size) as the other tables.

In the subgrid method excel water ends up in the lowest pixels. The water depths caused by rainfall are relatively low in many cases and only a small part of a calculation cell will be ‘wet’. If this part of the cell has no infiltration capacity there will be no infiltration. But rain falls over the entire calculation cell. That’s why 3Di differentiates between infiltration during rainfall or not. The figure below shows the illustrates this behaviour.
 
.. figure:: image/b_infiltration_pixel_cell.png
                :alt: Infiltration during rainfall acts on the whole surface within one calculation cell (left). When rain stops, infiltration only acts on those pixels below the water level.
 
During rainfall 3Di assumes the rainfall is uniform over the calculation cell so that the same amount of rain falls on every pixel. The calculation cell infiltration rate is the sum of infiltration capacity of all pixels. This may lead to an overestimate of the infiltration capacity during rain. In some cases the user may want to use a different method for infiltration. To do so, check out the he option *infiltration_surface_option* in the global settings.

 
Maximum infiltration capacity
-----------------------------------------

 
De maximum infiltration capacity is the maximum volume of water that can infiltrate during one simulation. The users defines a layer with a maximum thickness per pixel in meters. The maximum infiltration per calculation cell is the sum of all pixels. If the maximum volume is reaches, infiltration will stop.

 
Technical description
-----------------------------

 
The infiltration is implicitly added to the continuity equation. This means that the infiltration discharge depends on the infiltration capacity and the water level at the new and the old time level:
 
.. math::
   :label: infiltration
 
   Q_inf = I * ( H^(k+1) / H^n )
 
in which, k is the indices for the inner Newton iteration loop, n, is the timestep, Q\ :sub:`inf`\ is the infiltrated volume per time interval.
 
 
