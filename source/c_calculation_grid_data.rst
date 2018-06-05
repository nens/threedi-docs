Tabulated data storage
===================================

.. _tables

In 3Di we make use of detailed data to compute the hydrodynamics via the so-called subgrid technique. For all spatially varying parameters, high resolution raster data is used. For example, we use high resolution raster data for the bathymetry to calculate detailed volumes in our model, but also roughness coefficients to calculate friction are based on high resolution raster data. In 1D elements we use detailed vector attribute data and compress this in the same manner to subsequently calculate for instance 1D volumes or friction. 

For this large amount of data, we execute a data compression by building tables per cell containing the information needed from the raster or vector data. The data is scaled down from the subgrid resolution to the resolution of the computational grid. Thereby, reducing the demand on hardware resources. The detailed information is preserved and can now be accessed fast during the simulations due to the compression. 

Table structure
---------------

Information in the tables is stored relative to possible water depths. This is only necessary for the range of water levels where the relation between water level and volume is non-linear as displayed in figure 1-3: In other words, the information is to be tablelized for water levels for which a cell is only partly wet.

Between the deepest and highest pixel values within a computational cell and for a 1D elements. The parameters for which information is translated into tables:

* Volumes per calculation cell (1D and 2D)
* Cross-sectional area per half of cell face (2D)
* Friction parameters per waterlevel (2D)
* Infiltration rates (2D)

.. figure:: image/crossection_table_increments.png
   :scale: 60 %
   :align: center
   :alt: Figure 1 Table increments 2D

.. figure:: image/table_1d_increments.png
   :scale: 40 %
   :align: center
   :alt: Figure2 Table increments 1D

.. figure:: image/volume_table_2d_increments.png
   :scale: 50 %
   :align: center
   :alt: Figure 3 Table structure 2D


Table step size
^^^^^^^^^^^^^^^

The user has control over the table sizes and compression by setting a table step size (table_step_size) for the tables in the global settings. The table step size defines the height interval between succeeding increments. The increment size determines the amount of increments in a table and thus the amount of compression. In 3Di one general table step size can be set for all of the above mentioned tables. However, there are two extra tables step size parameters that can overrull the table step size for some of the tables. The optional table steps size parameters are:

* table_step_size_1d
* table_step_size_volume_2d

When the table_step_size_1d is set different from te general table_step_sizem, the tables containing the information of the 1D domain is processed with a different increment than information in the 2D modelling. This can be beneficiary for the simulation, when for instance the 2D date needs to be compressed strongly due to hardware limitations. Same principle applies for the table step size for 2D volume tables. To be able to make an optimal balance between memory use, computational speed and accuracy, one can also differ the table step sizes of the volume tables and the other tables necessary in the 2D domain. In order to keep the most detailed discription of the cross-sections and the friction, one can increase the table step size for the volume tables. There linearizing the system and thereby simplifing the mathematical solution. This can be advantage for the swftness of the programm, especially for simulations with extensice flooding and drying. 
