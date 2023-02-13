.. _flood_model:

Flood model
========================

In this instruction we will set up a relatively simple model that can simulate floods, using a DEM and some levee’s. For a flood model we need a DEM and possibly a friction raster. For this instruction it is assumed you have both at the ready.

Spatialite database
-------------------

Once all your raster-files meet the requirements (as outlined in :ref:`rasters`) we can set up the model through the spatialite database. The spatialite database contains all the information that goes into your model except the raster-files. To see what is inside the database, you have to connect to the spatialite database using the :ref:`qgisplugin`. This way, all relevant 3Di-layers are loaded.


Global settings
-------------------

The global settings table (v2_global_settings) contains all general settings for your model. It must contain at least one row for your model to work. You can find a complete overview of all settings through :ref:`database-overview`. Here some basic settings are discussed as well as how to set up your computational grid, but you will need the database overview as well.

Some basic settings you must fill out have to do with keeping track of your scenario and the type of model you are making. Consider the following steps:
 
#. The first basic settings you must fill out are the scenario id and a simple name for your scenario. The scenario name will be shown in the 3Di web portal once you uploaded your model. 

#. Set ``use_2d_flow`` to 1 (we want to make a 2D flood model) and set ``use_1d_flow`` and ``use_0d_flow`` to 0.

#. Set the default simulation time step (``sim_time_step``) to (for instance) 30 seconds. 3Di will automatically decrease the time step if no solution can be found in the given time step size. 

#. Set your output time step (``output_time_step``) to 300 seconds. This setting is important since 3Di will generate a larger results-file the smaller your output time step is. 

#. The flooding threshold determines when water starts to flow from one cell to the next. Set it to 0.01 meter. This ensures a more stable and quicker simulation.

#. Set the DEM and friction files relative paths to the raster-files you created. Make sure you use the full path (relative from the folder in which the spatialite is stored) and full filenames (including .tif).

#. Set the friction type so that it matches your friction raster-file.

#. Check the 3Di :ref:`database-overview` for the remaining settings and fill-out all those listed as mandatory. Except ``kmax`` and ``grid_space``, they are explained below.

.. _computational_grid:

Computational grid
-------------------

The computational grid consists of all the calculation cells combined. It consists of square calculation cells, that may vary in size. In each calculation cell a volume and water level is computed. Velocity and discharge are computed on the edges between these calculation cells. The sizes of the calculation cells depend on two global settings: ``kmax`` and ``grid_space``.
The ``grid_space`` defines the size of the smallest calculation cell in your computational grid. The ``kmax`` is your maximum refinement level that determines the biggest possible calculation cell. If you do not define any local grid refinement, all calculation cells will have the maximum size (i.e. ``grid_space`` * 2^(``kmax``-1)). Below, a picture is shown to remind you of the way the computational grid is created. Every large cell can be split into four smaller cells by adding local grid refinement. 

.. figure:: image/grid-refinement-in-3-layers.png
   :alt: Grid refinement

   Grid refinement

For now, set your ``grid_space`` and ``kmax``. Your grid space must be a multitude of your raster pixel size. If we assume you are using a pixel size of 5 meter, a ``grid_space`` of 10 meter and a ``kmax`` of 4, then your biggest calculations cells will become 80 meters high and wide. The next section shows you how to add local grid refinement.

Local grid refinement
--------------------------------------

Adding local grid refinement allows you to calculate the flow of water in a certain area in greater detail while maintaining larger calculation cells in other areas. This way you can keep the model as fast as possible. Generally speaking, you will use grid refinement in areas of your model where you expect high variability in water levels and flow. For instance, near a breach location, levee or river bent. In other areas, like a floodplain or relatively flat farm land, you can use larger cells as they tend to flood quite gradually. 
You have two options to add local grid refinement:
#. by drawing polylines and storing them in the ``v2_grid_refinement`` table in your spatialite database;
#. by drawing polygons and storing them in the ``v2_grid_refinement_area`` table in your spatialite database.
Any calculation cell that is intersected by a grid refinement line will be split until it meets the given grid refinement. You can set the refinement level for every line segment or polygon. Set it to 1 for your smallest calculation cell equal to grid_space.

You will not be able to see the resulting computational grid until after you upload your model.

Levees or obstacles
--------------------------------------

Flow from one calculation cell to the next is determined at the edge of each cell and depends on the local pixel values along the edge. In the case of a thin levee this could mean your calculation cell edges don’t align with the highest pixel values of the levee. This means 3Di will not pick up on the correct height of the levee. To solve this problem, you must add levees or obstacles to your model as a vector , i.e. a polyline, in your spatialite database in the tables ``v2_levee`` or ``v2_obstacle``. 
Both tables allow you to set the minimum crest level at the edge of a calculation cell. The location of the polyline you draw determines which edges are affected. The image below shows an example.

.. figure:: image/levee-in-non-uniform-grid.png
   :alt: Levee in quadtree

   Levee in computational grid

The table ``v2_levee`` works similar to the ``v2_obstacle`` but allows you the set some additional parameters that are used to simulate a breach. When the 2D-levee varies in height you can use different line segments. Make sure all your levee segments are drawn within the extent of your raster-files.

More information about levees or obstacles can be found in :ref:`obstacles`.

Breach locations
----------------

There are two ways to add breach locations to a model, manually for each breach or automatically for selected channels. In both cases the table ``v2_connected_pnt`` and ``v2_calculation_points`` must be filled completely and correctly. The calculation points are points on which 3Di will place water level calculation points. The connected points refer to these calculation points by a unique id. The location of the connected points marks the location where the 1D2D connection is made to the 2D computational grid. If a straight line between the calculation point and the connected point crosses a 1D-levee, a breach location is generated.

To add a breach location next to a levee you have to have a model that has a connected channel and at least one levee. 
The :ref:`qgisplugin` can be used to add breach locations to your model.
    
No actual breach points will become visible for either of these options in QGIS. These will only become visible on the 3Di web portal.

More information about breaches can be found in :ref:`breaches`.
