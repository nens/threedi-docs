.. _rasters:

Rasters
=======

Raster files
------------

In 3Di we can use several raster input types. 3Di uses raster files stored in the GeoTIFF format. 3Di knows which raster files to use through a relative path-reference in the v2_global_settings table in the spatialite.

You may use any source for your raster information. Below see an example for the DEM, which is the main raster in case you want to do a simulation that includes 2D flow.

The following rasters can be included in a 3Di schematisation; they are referenced from different settings tables:

Global settings:

* Digital elevation model [m MSL]
* Friction coefficient [-]
* Initial groundwater level [m MSL]
* Initial water level [m MSL]
* Interception [m]

Simple Infiltration settings:

* Infiltration rate [mm/d]
* Max infiltration capacity [m]

Groundwater settings:

* Equilibrium infiltration rate [mm/d]
* Hydraulic conductivity [m/day]
* Impervious layer level [m MSL]
* Infiltration decay period [d]
* Initial infiltration rate [mm/d]
* Leakage [mm/d]
* Phreatic storage capacity [-]

Interflow settings:

* Hydraulic conductivity [m/d]
* Porosity [-]

DEM
---

For the Digital Elevation Model (DEM) satellite or LIDAR-based information is often used. When working with crude SRTM-data for instance, it is important to derive the genuine surface level and remove any artifacts. Also, adding bathymetry information to your raster could be useful, since the satellite and LIDAR techniques are unable to *see* under water.

Raster requirements
-------------------

How you derive your raster information is entirely up to you. 3Di rasters have to meet the following requirements:

#. Format is GeoTIFF (.tif)

#. Projection is in meters (EPSG:28992 in NL)

#. Projection is complete according to OGC (check `epsg.io <http://epsg.io/>`_)

#. Projection fits data location

#. Pixel size is square

#. Recommended: Origin is rounded to pixel size precision


Using GDAL to check and edit your rasters
-----------------------------------------

There are several packages available which allow you to meet the requirements stated above. Below are some examples using GDAL. 

*If you are using Windows, GDAL should be installed together with QGIS and available through the OSGeo4W Shell. Try finding it through your start menu. A full list of GDAL functionalities and help can be found under the* `gdal documentation <http://www.gdal.org>`_.

**Retrieve raster information using gdalinfo**

This example shows you how to find and retrieve the meta-information of your raster through the OSGeo4W Shell.

- Start the OSGeo4W Shell
- Change the directory to the location of your raster file (use for example ``D:`` and ``cd myfiles/mymodel/raster``)
- Then type: ``gdalinfo <raster-file>``

This will give you a list of all raster information available for your raster-file. Check whether your file meets the requirements listed above. Note that information that is not listed, is missing and must be added.

**Change raster information using gdalwarp**

To change or update your raster information you must be aware that some changes will affect your data content. For instance, updating your pixel size will require re-sampling or aggregation of your existing data. 

We will use gdalwarp to update our raster information. This is a versatile command that enables you to re-project, aggregate and change the data type of your raster all in one command. The first example shows you how to change the NODATA value and transform it into a GeoTiff for any given raster. If you already found your raster in the OSGeo4W Shell you can use the following commands::

    gdalwarp -srcnodata <your-NODATA-value> -dstnodata -9999 <raster-file> -of Gtiff warp_output.tif

*Note that the words that start with ‘-‘ are options in gdalwarp. They are followed by a parameter specific to that option. Also, if your NODATA value is specified in the raster information, you may omit the srcnodata option.*

The next example sets all raster-information in one command for rasters that use the Dutch projection. It is a useful example as long as you remember how it may change the actual data in your pixels::

    gdalwarp -s_srs EPSG:XXXX -t_srs EPSG:28992 -of Gtiff -ot Float32 -tap -tr 0.5 -0.5 -srcnodata XXXX -dstnodata -9999 -cutline study-area.shp -crop_to_cutline <raster-file>  warp_output.tif

Tip: Always use the ``-tap`` option to make sure all your rasters are properly aligned. 
    
The example uses an extra shape-file of the study area. This is convenient when you are using several raster-files. It ensures that all raster-files you make have the same extent and NODATA pixels. You should make sure however that the shape-file’s projection matches that of your raster information. If you are not sure what any of the commands do exactly, you can check the `gdal documentation <http://www.gdal.org>`_ or try options separately to generate several output files and checking them with gdalinfo to see which option generates the result you want.

**Compress rasters using gdal_translate**

Once your raster meets all requirements there is one last thing to consider. 3Di is cloud-based so we advise you to compress all raster-files before uploading. The example below shows you how::

    gdal_translate -co COMPRESS=DEFLATE warp_output.tif compressed.tif

This command copies all data and information but compresses the data.
 
*Note that we only recommend the DEFLATE compression option. Other options may give better compression or performance in certain cases, but they are not supported in 3Di.*