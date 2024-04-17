.. _schematisation_scripting:

Editing schematisations with SQL or Python
==========================================

A :ref:`schematisation` consists of rasters, vector data (points, lines and polygons) and tables. This page outlines how you can edit these data types using Python, SQL and GDAL command line tools.


- :ref:`scripting_raster_data`

    - :ref:`gdal_cmd`

    - :ref:`rasters_python`

- :ref:`vector_and_table_data`

    - :ref:`scripting_sql`

    - :ref:`scripting_python`

.. _scripting_raster_data:

Raster data
-----------

.. _gdal_cmd:

Editing rasters with GDAL command line tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GDAL is a free open source library for handling raster data. It also includes a set of command line tools that you can use to manipulate your 3Di rasters. The :ref:`3Di Modeller Interface<mi_introduction>` includes a command line interface called the OSGeo4W Shell. It can be found through the Windows start menu. A `full list of GDAL command line programs  <https://gdal.org/programs/index.html#raster-programs>`_ can be found in the GDAL documentation.

Some examples are given below

List raster properties using ``gdalinfo``
"""""""""""""""""""""""""""""""""""""""""

This example shows you how to find the properties of the DEM through the OSGeo4W Shell.

.. code-block:: shell

    cd "C:\Users\user.name\3Di\My schematisation\work in progress\schematisation\rasters"
    gdalinfo dem.tif``

This will give you a list of all raster information available for your raster file. Note that information that is not listed, is missing and must be added.

Change nodata value using ``gdalwarp``
""""""""""""""""""""""""""""""""""""""

This example uses ``gdalwarp`` to change the nodata value of the DEM to -9999 (assuming that the raster's nodata value is defined). It will actually change the values of all the nodata pixesl to -9999 and update the nodatavalue in the raster's properties. Assuming you have already changed the directory to where the raster is located::

    gdalwarp -dstnodata -9999 dem.tif dem_new_nodata_value.tif

.. note:: 
	
	The words that start with ``-`` are parameters that are passed to the ``gdalwarp`` command. They are followed by a parameter value specific to that option.

Clip rasters to a cutline polygon
"""""""""""""""""""""""""""""""""

This example shows how to use ``gdalwarp`` to clip a raster to an area defined by a polygon ("cutline")::

	gdalwarp -crop_to_cutline -cutline study-area.shp dem.tif dem_clipped.tif

Change multiple raster properties at once
"""""""""""""""""""""""""""""""""""""""""

In the previous examples, ``gdalwarp`` was used to change only a single aspect of the input raster, but ``gdal_warp`` is a versatile command that enables you to re-project, aggregate and change the data type of your raster all in one command.

This example reprojects the DEM to EPSG:28992 (``-t_srs EPSG:28992``), sets the output type to Float32 (``-ot Float32``), resamples the raster to a 0.5 m resolution and aligns the raster's origin to the origin of the CRS (``-tap``), sets the output nodata value to -9999 (``-dstnodata -9999``) and clips the raster to a cutline polygon (``-cutline study-area.shp -crop_to_cutline``) all raster information in one command for rasters that use the Dutch projection. It is a useful example as long as you remember how it may change the actual data in your pixels::

    gdalwarp -t_srs EPSG:28992 -ot Float32 -tap -tr 0.5 -0.5 -dstnodata -9999 -cutline study-area.shp -crop_to_cutline dem.tif dem_warped.tif

Tip: Always use the ``-tap`` option to make sure all your rasters are properly aligned. 
    
The example uses an extra shape-file of the study area. This is convenient when you are using several raster-files. It ensures that all raster-files you make have the same extent and NODATA pixels. You should make sure however that the shape-file’s projection matches that of your raster information. If you are not sure what any of the commands do exactly, you can check the `gdal documentation <http://www.gdal.org>`_ or try options separately to generate several output files and checking them with gdalinfo to see which option generates the result you want.

Compress rasters using ``gdal_translate``
"""""""""""""""""""""""""""""""""""""""""

It is highly recommended to always compress all 3Di rasters to minimize the file size. The example below shows you how to do that using ``gdal_translate``::

    gdal_translate -co COMPRESS=DEFLATE -co PREDICTOR=2 -co ZLEVEL=9 dem.tif dem_compressed.tif

The creation options (``-co``) PREDICTOR and ZLEVEL are not strictly necessary, but these parameter values (2 and 9) tend to give the best compression results in most cases.

.. note::

	It is recommended to always use DEFLATE compression. Other options may give better compression or performance in certain cases, but may not work in in 3Di.

.. _rasters_python:

Editing rasters with Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The raster file format that 3Di uses is GeoTIFF. These files can be handled and edited with many Python libraries, most notably `GDAL <https://gdal.org/api/index.html#python-api>`_, `RasterIO <https://rasterio.readthedocs.io/en/stable/>`_, and `dask-geomodeling <https://dask-geomodeling.readthedocs.io/en/latest/>`_. Once the raster data is read as an array, it can be manipulated with libraries such as `NumPy <https://numpy.org/doc/stable/>`_, `SciPy <https://docs.scipy.org/doc/scipy/>`_, and/or `Xarray <https://docs.xarray.dev/en/stable/>`_


.. _vector_and_table_data:

Vector and table data
---------------------

The vector and table data is stored in a Spatialite or Geopackage file. Both of these file formats are SQLite databases, extended with capabilities for handling spatial data.

.. note::
   
   We are currently phasing out the Spatialite format and revising the database schema (see :ref:`schema_300`). It is recommended to script against the Geopackage that is created by the 3Di Schematisation Editor, because its database schema is more similar to the database schema 300. In the text below, it is assumed that this Geopackage is used.
   
`Geopackage <https://en.wikipedia.org/wiki/GeoPackage>`_ is a generic GIS file format that is widely supported by Python libraries and other tooling. 

.. _scripting_sql:

Using SQL
^^^^^^^^^

It is a relational database stored in a file, and SQL can be used to interact with its contents. The SQL dialect to use is the same as for SQLite, see `this page  <https://www.sqlite.org/lang.html>`_. The spatial function you can use are the same as for Spatialite; these functions are `listed here  <https://www.gaia-gis.it/gaia-sins/spatialite-sql-5.1.0.html>`_. 

You can use any client that has Spatialite support, for example the `Database manager <https://docs.qgis.org/latest/en/docs/training_manual/databases/db_manager.html>`_ in the 3Di Modeller Interface.

The code snippet below illustrates how you can use SQL to add a Pipe to your schematisation

.. code-block:: sql

    INSERT INTO pipe (id, code, connection_node_start_id, connection_node_end_id, cross_section_shape, cross_section_width, geom)
    VALUES (
        22160,
        'Created using SQL',
        27928,
        27918,
        2,
        0.3,
        MakeLine((SELECT geom from connection_node where id = 27928), (SELECT geom from connection_node where id = 27918))
    )
    ;
	
	
.. _scripting_python:

Using Python
^^^^^^^^^^^^

Several libraries allow you to interact with Geopackages, most notably OGR, Fiona, GeoPandas, and Shapely. An example of how you can use GeoPandas and Shapely to fix invalid *Exchange line* geometries is given below.


.. code-block:: python

    import geopandas as gpd
    from pathlib import Path
    from shapely import make_valid

    schematisation_gpkg_path = Path("C:/Users/user.name/3Di/My schematisation/work in progress/schematisation/My schematisation.gpkg")

    exchange_line = gpd.read_file(schematisation_gpkg_path, layer='exchange_line')

    def fix_invalid_geometries(gdf):

        # Function to validate and fix LineString geometries
        def fix_line(line):
            valid_line = make_valid(line)
            if valid_line.is_empty:
                return line
            else:
                return valid_line
        
        # Counters for feedback
        invalid_features_removed = 0
        invalid_geometries_fixed = 0
        too_small_features_removed = 0
        
        indices_to_remove = set()
        
        # Iterate through rows
        for index, row in gdf.iterrows():
            # Check if geometry is valid
            if not row['geometry'].is_valid:
                # Try to fix the geometry
                fixed_geometry = fix_line(row['geometry'])
                
                # If fixing is successful, update the geometry
                if fixed_geometry.is_valid:
                    gdf.at[index, 'geometry'] = fixed_geometry
                    invalid_geometries_fixed += 1
                else:
                    # If fixing is not possible, we will remove the row
                    indices_to_remove.add(index)
                    invalid_features_removed += 1
                    
            # Check if line is not too small
            if row['geometry'].length < 0.001:
                indices_to_remove.add(index)
                too_small_features_removed += 1   
        
        gdf = gdf.drop(indices_to_remove)
        
        # Print feedback
        print(f"{invalid_features_removed} invalid features removed.")
        print(f"{invalid_geometries_fixed} invalid geometries made valid.")
        print(f"{too_small_features_removed} too small geometries removed.")
        
        return gdf


    fixed_exchange_line = fix_invalid_geometries(exchange_line)

    fixed_exchange_line.to_file(schematisation_gpkg_path, layer='exchange_line', driver="GPKG")



