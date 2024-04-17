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

#. The maximum size of the Digital Elevation Model is 5 billion pixels. This includes NoData pixels. The other rasters will be resampled to the resolution of the DEM, so their pixel count is not relevant.

.. note::

    The 3Di Modeller Interface includes a large number of tools for manipulating raster data. It is also possible to manipulate raster data from the :ref:``command line<gdal_cmd>`` or :ref:``using Python<rasters_python>``.
	
