Flood model
========================

In this tutorial we will set up a relatively simple model with a DEM and some levee’s that can simulate floods. For a Flood model we need a DEM and possibly a friction raster. We assume you have both ready.

Spatialite database
-------------------

Once all your raster-files meet the requirements we can set up the model through the spatialite database. The spatialite database contains all the information that goes into your model except the raster-files. To see what is inside the database, we must connect to the spatialite database using the `3Di-plugin <https://github.com/nens/threedi-qgis-plugin/wiki>`_. Do so, by adding the database to your project through the plugin. This way, all relevant layers are loaded.


Global settings
-------------------

The global settings table (v2_global_settings) contains all general settings for your model. It must contain at least one row for your model to work. You can find a complete overview of all settings through through :ref:`database-overview`. Here we discuss some basic settings and how to set up your calculation grid or quad tree, but you will need the database overview as well.

Some basic settings you must fill out have to do with keeping track of your scenario and the type of model you are making. Consider the following steps:
 
#. The first basic settings you must fill out are the scenario id and a simple name for your scenario.  The scenario name will be shown in the 3Di web portal once you uploaded your model. 

#. Set use_2d_flow to 1 (we are making a 2D flood model) and set use_1d_flow and use_0d_flow to 0.

#. Set the default simulation time step (sim_time_step) to (for instance) 30. 3Di will automatically decrease the time step if no solution can be found in the given time step size. 

#. Set your output time step (output_time_step) to 300. This setting is important since 3Di may generate a large results-file when you choose your output time step too small. 

#. The flooding threshold determines when water starts to flow from one cell to the next. Set it to 0.01 meter. This ensures a more stable and quicker simulation.

#. Set the dem file and friction file relative paths to the raster-files you created. Make sure you use the full filename’s (including .tif).

#. Set the friction type so that it matches your friction raster-file.

#. Check the 3Di :ref:`database-overview` for the remaining settings and fill-out all those listed as mandatory. Except kmax and grid_space, they are explained below.

Quadtree
-------------------

The quadtree or calculation grid consists of all the calculation cells combined. It can consist of different size calculation cells but are all square. In each cell a volume and water level is computed. Velocity and discharge are computed on the edges between these cells. The size of the cells depends on two global settings: kmax and grid_space.
The grid_space defines the size of the smallest calculation cell in your quadtree. The kmax is your maximum refinement level that determines the biggest possible calculation cell. If you do not define any local grid refinement, all calculation cells will become the maximum size. 
Below, a picture is shown to remind you to the way the quadtree is created. Every large cell can be split onto four smaller cells by adding local grid refinement. 

.. figure:: image/grid-refinement-in-3-layers.png
   :alt: Grid refinement

   Grid refinement

For now, set your grid_space and kmax. Your grid space must be a multitude of your raster pixel size. If we assume you are using a pixel size of 5 meter, set your grid space to 10 meter. Then set kmax to 4, your biggest calculations cells will this become 80 meters tall and wide. The next section shows you how to add local grid refinement.

Local grid refinement
--------------------------------------

Adding local grid refinement allows you to calculate the flow of water in one area in more detail while maintaining larger calculation cells in other areas. Generally speaking, you will use grid refinement in areas of your model where you expect high variability in water levels and flow. For instance, near a breach location, levee or river bent. In other areas, like a floodplain or relatively flat farm land, you can use larger cells as they tend to flood quite gradually. 
You can add local grid refinement by drawing lines and storing them in the v2_grid_refinement table in your spatialite database. Any calculation cell that is intersected by a grid refinement line will be split until it meets the given grid refinement. You can set the refinement level for every line segment. Set it to 1 for your smallest calculation cell equal to grid_space.

Try adding some grid refinement lines to your model. You can for instance draw lines over some dikes. You will not be able to see the resulting quadtree until after you uploaded your model.

Levees or obstacles
--------------------------------------

If you have read some more about 3Di and the subgrid technique, you will know that flow from one calculation cell to the next is determined on the edge of each cell and depends on the local pixel values along the edge. In the case of a thin dike this could mean your calculation cell edges don’t fall over the highest pixel values of the dike. This means 3Di will not pick up on to correct height of your dike. To solve this, you must add levees or obstacles to your model. 
The obstacle allows you to set the minimum crest level on the edge of a calculation cell. You can find the layer v2_obstacle in the spatialite database. The obstacle line you draw determines which edges are affected. The image below shows an example.

.. figure:: image/levee-in-non-uniform-grid.png
   :alt: Levee in quadtree

   Levee in quadtree

The levee can be used in the same way as the obstacle but allows you the set some additional parameters that are used when a breach is simulated. For your model, draw a line over your dike and fill out it’s crest level. You can use different segments when the dike varies in height. Make sure all your levee segments are drawn within the extent of your raster-files.
