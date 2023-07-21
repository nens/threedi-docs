.. _subgridmethod:

Subgrid method
==============

Flow is strongly affected by the bathymetry. Therefore, to simulate flow accurately, information of the bathymetry is crucial. To illustrate the importance of a well described bathymetry, consider the three flows in a flume shown in the Figure below. While the bathymetry differs only slightly, the flow behaves completely different.

Nowadays, detailed bathymetry information becomes more and more available.  However, it is difficult to take detailed grid information into account, without a strong increase in computational cost. In search of an optimal balance between computational cost and accuracy, the so-called subgrid method (:cite:t:`Casulli2009`, :cite:t:`Casulli2011`, :cite:t:`Stelling2015`, :cite:t:`Volp2013`) is developed and implemented in 3Di.

.. figure:: image/b1_3.png
   :figwidth: 600 px
   :alt: bathymetry variations example

   Examples of flow in a flume, where a slight change in bathymetry strongly affects the flow.

The basic idea behind the subgrid method, is that water levels vary much more gradually than the bathymetry. In hydrodynamic computations, water levels are assumed to be uniform within a computational cell. Traditionally, this is also assumed for the bathymetry within such a cell. The subgrid-based approach allows the bathymetry to vary within one computational cell, while the water level remains uniform. In 3Di two grids are to be defined; a high resolution subgrid and a coarse(r) computational grid. All input data, such as the bathymetry, roughness and infiltration rates can be defined on the high resolution grid, while the computations are performed on the coarse computational grid. Volumes and cross-sectional areas are based using the high resolution bathymetry information. The variation of the bathymetry within a computational cell means that a cell can be dry, wet or partly wet. This approach has two implications:

- The volume has a non-linear relation with the water level, because when the water level rises, the wet surface area increases is well. Such a system can be solved using a newton iteration. To compute the volumes at the next time step.

- As we are allowed to have a non-linear relation between water level and volume, 3Di can deal automatically with flooding and drying. No artificial thresholds are necessary.


.. figure:: image/b1_4.png
   :figwidth: 400 px
   :alt: subgrid_bathymety_cell

   An example of a computational cell with a bathymetry defined on the subgrid.

Input
-----

Users define for the grid generation a cell size (of the finest grid resolution) and the number of refinement layers. A computational cell consists always of an even number of subgrid cells. In addition, the user needs to define where and if refinements should be defined. One can define polygons or lines to indicate these areas and the refinement level.

Some facts and figures
----------------------

-	The use of high resolution information goes hand in hand with large amounts of data. To compress this data, it is stored during the computations in tables. More information about this can be found in :ref:`tables`.
-	There are more variables defined at the high resolution grid; such as roughness, infiltration capacity and hydraulic connectivity. These will be introduced later in the documentation.


.. _tables:

Subgrid tables
--------------

In 3Di we make use of detailed data to compute the hydrodynamics via the so-called subgrid technique. For all spatially varying parameters, high resolution raster data is used. For example, we use high resolution raster data for the bathymetry to calculate detailed volumes in our model, but also roughness coefficients to calculate friction are based on high resolution raster data. In 1D elements we use detailed vector attribute data and compress this in the same manner to subsequently calculate for instance 1D volumes or friction. 

For this large amount of data, we execute a data compression by building tables per cell containing the information needed from the raster or vector data. The data is scaled down from the subgrid resolution to the resolution of the computational grid. Thereby, reducing the demand on hardware resources. The detailed information is preserved and can now be accessed fast during the simulations due to the compression. 

Table structure
^^^^^^^^^^^^^^^

Information in the tables is stored relative to possible water depths. This is only necessary for the range of water levels where the relation between water level and volume is non-linear as displayed in figure 1-4: In other words, the information is to be tabulated for water levels for which a cell is only partly wet.

Between the deepest and highest pixel values within a computational cell and for a 1D elements. The parameters for which information is translated into tables:

* Volumes per calculation cell (1D, 2D)
* Cross-sectional area per half of cell face (2D)
* Friction parameters per waterlevel (2D)
* Infiltration rates (2D)
* Interception rates (2D)
* Interflow volumes per calculation cell (2D)
* Groundwater volumes per calculation cell (2D)


Table step size 2D
^^^^^^^^^^^^^^^^^^

Tables for a computational cell are a combination of pixel heights and corresponding table information at that height, depending on the type of table. For volume tables this means
each table entry corresponds with the total volume below the corresponding pixel height in the cell. This information is generated by evaluating the 
high resolution information within a cell. Users have control over the table sizes and compression by setting a 2D table step size (table_step_size) in the global settings.

The 2D table step size will be used as a minimum increment height between successive table entries. For example, if the 2D table step size is 0.1m, and we have previously found a
table increment at pixel height 1.5m, the pixel values that are considered for the next table increment have to be at least 1.6m. Decreasing the 2D table step size will increase
numerical precision at the cost of computational speed. For simulations with extensive flooding and drying it can be advantageous to increase the 2D table step size, thereby
increasing the linearization of the system and simplifying the mathematical equations.

The maximum distance between height increments is determined by the pixel values. This way we prevent generating height increments for which each subsequent table entry would
only be linear increase with respect to the previous table entry, thereby omitting an opportunity for data reduction and gain in computational speed. The exceptions are 
tables with a non-linear relation regarding water depths, for example for friction tables. Interpolation between table entries that are too far apart will cause a loss in numerical
precision due to the non-linear friction profile. For these tables we set the maximum 2D table step size to be 100 times the minimum 2D table step size.


.. figure:: image/table_2d_increments.png
   :scale: 50 %
   :align: center
   :alt: Figure 3 Table structure 2D

   2D table increments. Pixel height for node 8 is the first increment height in the table, pixel heights for pixels 6, 7, and 8 are below the table step size with respect to the
   pixel height of node 8 and are therefore skipped. Pixel heights for pixels 1, 2, 3, and 4 are above the previous table increment height + table_step_size, and are therefore
   in the table for this cell.  

Table step size 1D
^^^^^^^^^^^^^^^^^^

To be able to make an optimal balance between memory use, computational speed and accuracy, users can also differ the 2D table step sizes from 1D table step sizes. 
When the 1D table step size (table_step_size_1d) is set different from the general table_step_size, the tables containing the information for the 1D domain are processed
with a different increment than information for the 2D tables. This can be beneficiary for the simulation, for instance when 2D data needs to be compressed strongly due
to hardware limitations.

For 1D tables the 1D table step size is used as a fixed increment height between table entries, as opposed to the dynamic increment heights for the 2D tables.

.. figure:: image/table_1d_increments.png
   :scale: 40 %
   :align: center
   :alt: Figure2 Table increments 1D

   1D table increments. Fixed distance between increments.