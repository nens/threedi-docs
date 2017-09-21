Calculation grid data
=====================

In 3Di we make use of large amounts of detailed data to model our area of interest. For example we use raster data from a DEM to describe the bathymetry and calculate detailed volumes in our model, but also roughness coefficients from raster data to calculate friction. In 1D elements we use detailed vector attribute data and compress this in the same manner to subsequently calculate for instance 1D volumes or friction. 

For these large amounts of data we execute a data compression by building tables for the volume and momentum domains containing the information needed from the raster or vector data. The data is scaled up from the pixel scale to the calculation grid scale, which is coarser and thus reduces the demand on hardware resources. The detailed information can subsequently be accessed very fast during the simulations due to the compression. 

Table structure
---------------

Information in the tables is stored relative to possible future water levels. This is only necessary for the range of water levels where the relation with the information is non-linear as displayed in figure 1-3: 

Between the deepest and highest pixel values within a calculation cell or for a compounded 1D profile. The information for which tables need to be calculated are:

* Volumes per calculation cell (1D and 2D)
* Cross-sectional area per half of cell face (2D)
* Friction parameters per waterlevel (2D)
* Infiltration rates (2D)


.. figure:: image/crossection_table_increments.png
	:scale: 50 %
	:alt: Figure 1 Table increments 2D
   
   
.. figure:: image/table_1d_increments.png
	:scale: 50 %
	:alt: Figure2 Table increments 1D


.. figure:: image/volume_table_2d_increments.png
	:scale: 50 %
	:alt: Figure 3 Table structure 2D


Table step size
^^^^^^^^^^^^^^^

The user has control over the table sizes and compression by setting a table step size (table_step_size) for the tables in the global settings. The table step size define the interval between succeeding increments in the tables. The increment size determines the amount of increments in a table and thus the amount of compression, since the table is only needed for information between the deepest and highest pixel values for the non-linear part within a calculation cell. 

In 3Di one general table step size can be set for all of the above mentioned tables. However there are two extra tables step size parameters that can overall the table step size for some of the tables. The optional table steps size are:

* table_step_size_1d
* table_step_size_volume_2d

The table step size 1d allows the user to compute the 1D tables at a different resolution than 2D when for instance the 1D data is coarser or finer and the user can decide a higher/lower compression of data is beneficiary for the simulation. 
Same principle applies for the table step size for 2D volume tables as 1D tables with different step size. However there is also an additional amenity. With increasing the table step size for 2D volume, the linearity of the relation between volume and water level increase, which potentially has a beneficiary effect on stability and calculation speed of the simulation. 
