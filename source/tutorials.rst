Tutorials
============

We have two types of tutorials: General tutorials and Modelling tutorials. General turorials are aimed at how to make 3Di simulations through the web portal and manage revisions in the model database. Modelling tutorials help you with creating or modifying your 3Di model. You will find both below.

General tutorials
-----------------


Modelling tutorials
-------------------

The tutorials below are aimed add giving you some examples on how to create your model in 3Di. They show you how to create different types of models for different purposes or add elements to existing models. The first tutorial aims to give you an introduction to 3Di and therefore explain the steps and reasons behind them quite extensively. The later tutorials assume you have sufficient knowledge about 3Di and modelling in general. They are less extensive and can be used as cheat sheets for performing different tasks.

All tutorials assume you have some knowledge of 3Di and are able to use QGIS. Make sure you have a working 64bit QGIS version available and install the specially designed 3Di QGIS-plugin using `this <https://github.com/nens/threedi-qgis-plugin/wiki>`_ link.


2D Flood model
^^^^^^^^^^^^^^^^
In this tutorial we will set up a relatively simple model with a DEM and some levee’s that can simulate floods.


Raster-files
""""""""""""""""

In 3Di we can use several raster input types. For a Flood model we need a DEM and possibly a friction raster. 3Di uses raster-files stored in the GeoTiff format. It knows which raster-files to use through a relative reference in the v2_global_settings table in the spatialite. We will come to that later. First we must collect our raster-files.

You may use any source for your raster information. Below we discuss some examples for the DEM and friction information.

**DEM**
For the Digital Elevation Model (DEM) satellite or LIDAR based information is often used. When working with crude SRTM-data for instance, it is important to derive the genuine surface level and remove any artefacts. Also, adding bathymetry information to your raster could be useful, since the satellite and LIDAR techniques are unable to *see* under water.

**Friction**
Information about bed friction is usually derived from landcover, giving high friction to dense forest and lower values to agricultural land. In 3Di these values can be given in Manning or Chezy.

**Requirements**
How you derive your raster information is entirely up to you. For 3Di you must make sure your raster-files eventually meet the following requirements:

#. Format GEOTIFF (.tif)
#. Projection in meters (EPSG:28992 in NL)
#. Projection complete according to OGC (check epsg.io)
#. Projection fits data location
#. Pixel size is square
#. NODATA = -9999
#. Type = Float32
#. All raster-files must have the same pixel size, origin, size and NODATA pixels
#. Data values must meet input types
#. Advised: Origin is rounded to pixel size precision


Examples using GDAL
"""""""""""""""""""

There are several packages available that correctly allow you to meet these requirements. Below are some examples using GDAL. 

*If you are using Windows, GDAL should be installed together with QGIS and available through the OSGeo4W Shell. Try finding it through your start menu. A full list of GDAL functionality and help can be found under the* `gdal documentation <www.gdal.org/gdal_utilities.html>`_.

**Retrieve raster information**
This example shows you how to find and retrieve the meta-information of your raster through the OSGeo4W Shell. Make sure you have some raster-type data available.

- Start the OSGEO4W Shell
- Change the directory to the location of your raster file (use for example ``D:`` and ``cd myfiles/mymodel/raster``)
- Then type: ``gdalinfo <raster-file>``

This will give you a list of all raster information available for your raster-file. Check whether your file meets the requirements listed above. Note that information that is not listed, is missing and must be added.

**Change raster information**
To change or update your raster information you must be aware that some changes will affect your data content. For instance, updating your pixel size will require resampling or aggregating your existing data. 

We will use gdalwarp to update our raster information. This is a versatile command that enables you to re-project, aggregate and change the data type of your raster all in one command. The first example shows you how to change the NODATA value and transform it into a GeoTiff for any given raster. If you already found your raster in the OSGeo4W Shell you can use the following commands:


``gdalwarp -srcnodata <your-NODATA-value> -dstnodata -9999 <raster-file>  -of Gtiff  warp_output.tif``

*Note that the words that start with ‘-‘ are options in gdalwarp. They are followed by a parameter specific to that option. Also, if your NODATA value is specified in the raster information, you may omit the srcnodata option.*

The next example sets all raster-information in one command. It is a useful example as long as you remember how it may change the actual data in your pixels. 

``gdalwarp -s_srs EPSG:XXXX -t_srs EPSG:28992 -of Gtiff –ot Float32 -tap -tr 0.5 -0.5 -srcNODATA XXXX 
-dstnodata -9999 -cutline study-area.shp -crop_to_cutline <raster-file>  warp_output.tif``

The example uses an extra shape-file of the study area. This is convenient when you are using several raster-files. It ensures that all raster-files you make have the same extent and NODATA pixels. You should make sure however that the shape-file’s projection matches that of your raster information. If you are not sure what any of the commands do, you can check the `gdal documentation <www.gdal.org/gdal_utilities.html>`_ or try options separate generating several output files and checking the with gdalinfo.

**Compression**
Once your raster meets all requirements there is one last thing to consider. 3Di is cloud based so we advise you to compress all raster-files before uploading. The example below shows you how.

``gdal_translate -co COMPRESS=DEFLATE warp_output.tif compressed.tif``

This command copies all data and information but compresses the data.
 
* Note that we only recommend the DEFLATE compression option. Other options may give better compression or performance in certain cases, but we do not support them in 3Di.*


Spatialite database
""""""""""""""""""""

Once all your raster-files meet the requirements we can set up the model through the spatialite database. To do this, we must connect to the spatialite database using the `3Di-plugin <https://github.com/nens/threedi-qgis-plugin/wiki>`_. This way, all relevant layers are loaded.


Global settings
""""""""""""""""

The global settings table (v2_global_settings) contains all general settings for your model. It must contain at least one row for your model to work. You can find a complete overview of all settings through through :ref:`database-overview`. Here we discuss some basic settings and how to set up your calculation grid or quadtree, but you will need the database overview as well.

**Basic settings**
Some basic settings you must fill out have to do with keeping track of your scenario and the type of model you are making. Consider the following steps: 
#. The first basic settings you must fill out are the scenario id and a simple name for your scenario.  The scenario name will be shown in the 3Di web portal once you uploaded your model. 
#. Set use_2d_flow to 1 (we are making a 2D flood model) and set use_1d_flow and use_0d_flow to 0.
#. Set the default simulation timestep (sim_time_step) to (for instance) 30. 3Di will automatically decrease the timestep if no solution can be found in the given timestep size. 
#. Set your output timestep (output_time_step) to 300. This setting is important since 3Di may generate a large results-file when you choose your output timestep too small. 
#. The flooding threshold determines when water starts to flow from one cell to the next. Set it to 0.01 meter. This ensures a more stable and quicker simulation.
#. Set the dem file and friction file relative paths to the raster-files you created. Make sure you use the full filename’s (including .tif).
#. Set the friction type so that it matches your friction raster-file.
#. Check the 3Di database overview for the remaining settings and fill-out all those listed as mandatory. Except kmax and grid_space, they are explained below.

**Quadtree**
The quadtree or calculation grid consists of all the calculation cells combined. It can consist of different size calculation cells but are all square. In each cell a volume and water level is computed. Velocity and discharge are computed on the edges between these cells. The size of the cells depends on two global settings: kmax and grid_space.
The grid_space defines the size of the smallest calculation cell in your quadtree. The kmax is your maximum refinement level that determines the biggest possible calculation cell. If you do not define any local grid refinement, all calculation cells will become the maximum size. 
Below, a picture is shown to remind you to the way the quadtree is created. Every large cell can be split onto four smaller cells by adding local grid refinement. 

.. figure:: image/grid-refinement-in-3-layers.png
   :alt: Grid refinement

   Grid refinement

For now, set your grid_space and kmax. Your grid space must be a multitude of your raster pixel size. If we assume you are using a pixel size of 5 meter, set your grid space to 10 meter. Then set kmax to 4, your biggest calculations cells will this become 80 meters tall and wide. The next section shows you how to add local grid refinement.

.. figure:: image/levee-in-non-uniform-grid.png
   :alt: Levee in quadtree

   Levee in quadtree

The levee can be used in the same way as the obstacle but allows you the set some additional parameters that are used when a breach is simulated. For your model, draw a line over your dike and fill out it’s crest level. You can use different segments when the dike varies in height. Make sure all your levee segments are drawn within the extent of your raster-files.

1D2D model
^^^^^^^^^^
