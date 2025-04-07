.. _rasters:

Rasters
=======

Raster files
------------

Several 3Di inputs can be provided in a spatially variable way. The format that 3Di uses for this is a raster file (GeoTIFF). Locally, they are stored in a folder called *rasters*, in the same directory as the schematisation database. The rasters need to be referenced in specific tables in the schematisation database (e.g. 'dem.tif' in the *DEM file* field of *Model settings*), so that 3Di knows which raster file to use for what purpose.

You may use any source for your raster information. Below see an example for the DEM, which is the main raster in case you want to do a simulation that includes 2D flow.

The following rasters can be included in a 3Di schematisation; they are referenced from different settings tables:

Model settings
^^^^^^^^^^^^^^

* Digital elevation model [m MSL]
* Friction coefficient [-]

Initial conditions
^^^^^^^^^^^^^^^^^^

* Initial water level [m MSL]
* Initial groundwater level [m MSL]

Interception
^^^^^^^^^^^^

* Interception [m]

Simple infiltration
^^^^^^^^^^^^^^^^^^^

* Infiltration rate [mm/d]
* Max infiltration volume  [m]

Groundwater
^^^^^^^^^^^

* Impervious layer level [m MSL]
* Phreatic storage capacity [-]
* Hydraulic conductivity [m/day]
* Initial infiltration rate [mm/d]
* Equilibrium infiltration rate [mm/d]
* Infiltration decay period [d]
* Leakage [mm/d]

Interflow
^^^^^^^^^

* Impervious layer elevation [m MSL]
* Porosity [fraction]
* Hydraulic conductivity [m/d]

2D Vegetation drag
^^^^^^^^^^^^^^^^^^

* Vegetation height [m]
* Vegetation stem count :math:`[m/s^{-2}]`
* Vegetation stem diameter [m]
* Vegetation drag coefficient [-]

Digital Elevation Model (DEM)
-----------------------------

For the Digital Elevation Model (DEM) satellite or LIDAR-based information is often used. When working with crude SRTM-data for instance, it is important to derive the genuine surface level and remove any artifacts. Also, adding bathymetry information to your raster could be useful, since the satellite and LIDAR techniques are unable to *see* under water.

Raster requirements
-------------------

How you derive your raster information is entirely up to you. 3Di rasters have to meet the following requirements:

#. Format is GeoTIFF (.tif)

#. Coordinate reference system is Projected, not Geographic

#. Projection is in meters (EPSG:28992 in NL)

#. Projection is complete according to OGC (check `epsg.io <http://epsg.io/>`_)

#. Projection fits data location

#. Pixel size is square

#. Recommended: Origin is rounded to pixel size precision

#. The maximum size of the Digital Elevation Model is 5 billion pixels. This includes NoData pixels. The other rasters will be resampled to the resolution of the DEM, so their pixel count is not relevant.

.. note::

    The 3Di Modeller Interface includes a large number of tools for manipulating raster data. It is also possible to manipulate raster data from the :ref:`command line<gdal_cmd>` or :ref:`using Python<rasters_python>`.

