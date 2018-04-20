Infiltration
============

3Di supports to methods for computing infiltration. The so-called *simple infiltration* and the *Horton based infiltration*. The simple infiltration uses an infiltration rate that is constant in time, while the Horton based infiltration is based on the concept of infiltration that reaches in time an equilibrium rate. In 3Di, the infiltration computed with the first method removes the water from the model. For the second method, a ground water layer is defined from which water can also exfiltrate in case the groundwater level reaches the surface level.


Simple Infiltration
^^^^^^^^^^^^^^^^^^^^
 
Infiltration is the process of water slowly sinking into the soil. The infiltration rate depends on the type of soil and the land coverage. The infiltration rate is constant in time throughout the simulation. There are two exception for this: 1) the availability of water and when a user defines a maximum infiltration capacity. 

In 3Di, the infiltration rate is defined for subgrid cell and defined in mm/day. The infiltration is computed per computational cell. Therefore, the infiltration rate per pixel is translated to values per computational cell and can depend on the water level. 

When using the subgrid method, water start filling a cell from the lowest subgrid cell. When simulating rainfall run-off scenarios, the overall water depths are relatively small, therefore often only a small part of a computational cell is wet. If in this part of the cell the infiltration rate is low, the infiltration will be limited. However, in reality rain falls over a full spatial domain, and reaches the lowest areas only after a while, but might be infiltrated before it reaches that ares. Therefore, the total infiltration rate per computational can be made dependent of the rain. Besides defining the infiltration rates, a user defines also the *infiltration_surface_option* that can be found in the global settings table. In the Figure below, an overview is given of the various types.

.. figure:: image/b_infiltration_pixel_cell.png
   :alt: infiltration_pixel_cell
     
   Infiltration during rainfall acts on the whole surface within one computational cell (left). When rain stops, infiltration only acts on those pixels below the water level.
 

The first option, defines the infiltration rate in a cell based on the assumption that the full cell is wet. In other words, the infiltration rate in a cell is independent of the water level (left panel). The second option, defines the infiltration rate on the cumulative rates in the wet areas (middle panel). In this case the infiltration rate is dependent of the water level. The third option is the default option and is a combination of the two previous options. In this case the infiltration rate of the full cell domain is used when it is raining and only the infiltration rate of the wet area is used when it is dry (right panel).
 
In 3Di, many raster input variables are stored in tables. This yields as well for the infiltration rate, as this allows the infiltration rate to be dependent of the water level and for an efficient storage of the information. The table increment for the infiltration tables equals the 2D increment.
 
Maximum infiltration capacity
-----------------------------------------
 
De maximum infiltration capacity is the maximum volume of water that can infiltrate during one simulation. The user defines a layer with a thickness per pixel in meters. The maximum infiltration per computational cell is the sum of within all pixels. It will stop infiltrating when the maximum infiltration is reached.

Input
------
The user can define all the aspects for simple infiltration in the *simple_infiltration_table*.
 
Technical description
-----------------------------

The infiltration is implicitly added to the continuity equation. This means that the infiltration discharge depends on the infiltration capacity and the water level at the new and the old time level:
 
.. math::
   :label: infiltration
 
   Q_{inf} = I * ( H^{(k+1)} / H^n )
 
| in which,  
| k = the indices for the inner Newton iteration loop, 
| n = the timestep and 
| Q\ :sub:`inf`\ = the infiltrated volume per time interval.

This is to ensure stability and to ensure conservation of mass.

Horton based infiltration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Under construction. This will become available with the release of 22nd of May.






 
