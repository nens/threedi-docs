Hybrid Models
=============

In urban areas rain falls directly on the surface before it finds its way into the sewer system or it might "directly" enter the sewer system through drainpipes. 3Di can be used to model any sanitary, storm and combined sewer system, with water entering the model through 0D (NWRW) and 2D rainfall. Especially in urban areas the most accurate results are obtained when both types of rainfall are used in their appropriate manner. However, specifying both 0D and 2D rainfall simultaneously requires modification of both the 0D (impervious) surfaces and the 2D rasters. 

0D Rainfall
-------------------------

0D rainfall precipitates on predefined (impervious) surfaces. These surfaces represent (urban) elements which are coupled to the sewer system, for example houses, or more distant roads which are included in the 1D domain only. The rainfall volume (area x rainfall_intensity x delta t) is calculated for each time step for each impervious area or surface area. The impervious surfaces table uses the Dutch NWRW model. In this model characteristics like whether the surface is sloping or flat, paved or unpaved etc. are specified and translated to hydrological parameters like storage and delay of inflow. These are translated into a discharge hydrograph which is added as a lateral inflow to the sewer system. The surface table works similar to the impervious surface table but differs because you have to specify all the hydrological parameters of the surface yourself (i.e. infiltration, outflow delay, storage). For more information on 0D rainfall: :ref:`rain`.

.. figure:: image/d_panden.png
   :alt: impervious_surfaces_for_0D_inflow
     
   Impervious surfaces which facilitate the 0D inflow.

2D Rainfall
-------------------------
Rain which falls in the 2D domain precipitates on every calculation cell where a DEM is present. After the rain has fallen on the surface model it flows freely and interacts with connected 1D elements and therefore might enter the sewer system through manholes. 

Hybrid Modelling
-------------------------
Key to properly representing the precipitation processes in urban areas is the combination of 0D and 2D inflow, so called "hybrid modelling". Rain which falls on roofs or other surfaces which are directly coupled to the sewer system (through drain pipes) should be included in 0D inflow and therefore be excluded from the 2D rainfall. 

There are two ways to exclude rain from falling in te 2D domain:

- Interception;

- Removing the (impervious) surfaces from the 2D rasters;

Interception is a parameter which can be defined as a (2D) raster. It specifies the amount of rain which is intercepted and therefore does not reach the surface. This parameter can also be used to solely remove precipitation where 0D-inflow surfaces are specified. To make sure the model receives the correct amount of rainfall an interception raster which consists solely of zeros should be created. Afterwards a value (in mm) which exceeds the total rainfall event should be burned in underneath the surfaces (i.e. if the total rainfall in the model will be 70 mm an interception of >70 mm should be specified underneath the surfaces). The advantage of using interception is that the other rasters are not affected. Therefore it remains possible to have flow through (or below if using groundwater) the surfaces. A disadvantage is that the model becomes larger and might become too large for grid generation. 

.. figure:: image/d_interception.png
   :alt: interception_raster
     
   Raster with solely zeros and interception underneath the surfaces.


Removing the (impervious) surfaces from the 2D rasters is the second option to exclude precipitation from the 2D domain. 2D rain falls only where the DEM is present. Therefore, by removing the (impervious) surfaces from the DEM (turning them into nodata) the precipitation is removed from the 2D domain. As all 2D rasters have to overlap precisely one should remove the surfaces from the DEM and all other rasters present (i.e. infiltration, friction). The advantage of this method is that there is no additional raster required. A disadvantage might be that flow through (larger) surfaces will be obstructed.

.. figure:: image/d_hybride_dem.png
   :alt: hybride_dem
     
   Hybrid dem with removed surfaces to limit 2D rainfall.