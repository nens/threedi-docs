.. _combine_0d_2d_rain:

Combine direct rainfall and sewerage inflow
===========================================

3Di can be used to model any sanitary, storm and combined sewerage system, with water entering the model using the 0D inflow in combination with 2D rainfall. Combining :ref:`0d_rain` with and :ref:`2D rain <2d_rain>` can be useful in several cases, for example:

- Detailed urban water management models that use 0D inflow for the flow of water from roofs to the sewerage and 2D surface for rainfall and surface flow over roads

- Large open water systems in which a small area is modeled in detail while upstream catchments are lumped in 0D inflow.


Schematisation
--------------

Adding 0D inflow
^^^^^^^^^^^^^^^^

- Follow the steps explained in :ref:`howto_use_inflow`

Adding 2D rainfall
^^^^^^^^^^^^^^^^^^

Areas included in the 0D inflow should be excluded from the 2D rainfall. There are two ways to exclude rain from falling in the 2D domain:

- Adding a :ref:`interception` raster

- Removing the :ref:`surfaces<surface>` from the 2D rasters

Interception
""""""""""""

Interception specifies the amount of rain which can be intercepted. This parameter can also be used to intercept only precipitation where 0D-inflow surfaces are defined. To generate a interception raster you could follow these steps:

- Create a copy of the DEM and set all pixel values to 0

- At the locations of the surfaces, assign pixels an interception value that exceeds the total rainfall event. For example, if the total rainfall is 70 mm, an interception of > 70 mm should be specified at the location of the surfaces.

The advantage of using interception is that the other rasters are not affected. Therefore it remains possible to have flow through (or below if using groundwater) the surfaces.

.. figure:: image/d_interception.png
   :alt: interception_raster
   :scale: 60
     
   An example of a interception raster

Removing the surfaces from the 2D rasters
"""""""""""""""""""""""""""""""""""""""""

2D rain falls only where the DEM is defined. Therefore, by removing the surfaces from the DEM (setting them to nodata) the precipitation is removed from the 2D domain. It is recommended (but not required) to also remove the surfaces all other rasters present (e.g. infiltration, friction). The advantage of this method is that there is no additional raster required. A disadvantage might be that flow through (larger) surfaces will be obstructed.

.. figure:: image/d_hybride_dem.png
   :alt: hybride_dem
   :scale: 50
     
   Hybrid DEM with removed surfaces to limit 2D rainfall.


Simulation
----------

Following the outlined steps, a 3Di model can be created based on the schematisation. Rainfall occurring on :ref:`surface` will contribute to the volume of the designated calculation node, functioning as lateral discharge. Meanwhile, the remaining surfaces will undergo standard :ref:`surface_flow` processes.
