.. _rasters:

Rasters
================

Raster-files
------------------------

In 3Di we can use several raster input types.  3Di uses raster-files stored in the Geo-Tiff format. It knows which raster-files to use through a relative reference in the v2_global_settings table in the spatialite. 

You may use any source for your raster information. Below we discuss some examples for the DEM and friction information.

DEM
------------------------

For the Digital Elevation Model (DEM) satellite or LIDAR based information is often used. When working with crude SRTM-data for instance, it is important to derive the genuine surface level and remove any artifacts. Also, adding bathymetry information to your raster could be useful, since the satellite and LIDAR techniques are unable to *see* under water.

Friction
------------------------

Information about bed friction is usually derived from land cover, giving high friction to dense forest and lower values to agricultural land. In 3Di these values can be given in Manning or Chezy.

Raster requirements
------------------------

How you derive your raster information is entirely up to you. For 3Di you must make sure your raster-files eventually meet the following requirements:

#. Format GEO TIFF (.tif)

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
------------------------

There are several packages available that correctly allow you to meet these requirements. Below are some examples using GDAL. 

*If you are using Windows, GDAL should be installed together with QGIS and available through the OSGeo4W Shell. Try finding it through your start menu. A full list of GDAL functionality and help can be found under the* `gdal documentation <http://www.gdal.org/gdal_utilities.html>`_.

**Retrieve raster information**

This example shows you how to find and retrieve the meta-information of your raster through the OSGeo4W Shell. Make sure you have some raster-type data available.

- Start the OSGEO4W Shell
- Change the directory to the location of your raster file (use for example ``D:`` and ``cd myfiles/mymodel/raster``)
- Then type: ``gdalinfo <raster-file>``

This will give you a list of all raster information available for your raster-file. Check whether your file meets the requirements listed above. Note that information that is not listed, is missing and must be added.

**Change raster information**

To change or update your raster information you must be aware that some changes will affect your data content. For instance, updating your pixel size will require re-sampling or aggregating your existing data. 

We will use gdalwarp to update our raster information. This is a versatile command that enables you to re-project, aggregate and change the data type of your raster all in one command. The first example shows you how to change the NODATA value and transform it into a GeoTiff for any given raster. If you already found your raster in the OSGeo4W Shell you can use the following commands::

    gdalwarp -srcnodata <your-NODATA-value> -dstnodata -9999 <raster-file>  -of Gtiff  warp_output.tif

*Note that the words that start with ‘-‘ are options in gdalwarp. They are followed by a parameter specific to that option. Also, if your NODATA value is specified in the raster information, you may omit the srcnodata option.*

The next example sets all raster-information in one command. It is a useful example as long as you remember how it may change the actual data in your pixels::

    gdalwarp -s_srs EPSG:XXXX -t_srs EPSG:28992 -of Gtiff –ot Float32 -tap -tr 0.5 -0.5 -srcnodata XXXX -dstnodata -9999 -cutline study-area.shp -crop_to_cutline <raster-file>  warp_output.tif

The example uses an extra shape-file of the study area. This is convenient when you are using several raster-files. It ensures that all raster-files you make have the same extent and NODATA pixels. You should make sure however that the shape-file’s projection matches that of your raster information. If you are not sure what any of the commands do, you can check the `gdal documentation <http://www.gdal.org/gdal_utilities.html>`_ or try options separate generating several output files and checking the with gdalinfo.

**Compression**

Once your raster meets all requirements there is one last thing to consider. 3Di is cloud based so we advise you to compress all raster-files before uploading. The example below shows you how::

    gdal_translate -co COMPRESS=DEFLATE warp_output.tif compressed.tif

This command copies all data and information but compresses the data.
 
*Note that we only recommend the DEFLATE compression option. Other options may give better compression or performance in certain cases, but we do not support them in 3Di.*





