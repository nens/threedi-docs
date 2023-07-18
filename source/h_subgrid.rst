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

Groundwater storage
-------------------

.. todo::
   @Nici kan jij hier uitleggen hoe subgrid wordt gebruikt voor het berekenen van de volume/waterstandsrelatie als er ook grondwater is?


.. _tables:

Subgrid tables
--------------

In 3Di we make use of detailed data to compute the hydrodynamics via the so-called subgrid technique. For all spatially varying parameters, high resolution raster data is used. For example, we use high resolution raster data for the bathymetry to calculate detailed volumes in our model, but also roughness coefficients to calculate friction are based on high resolution raster data. In 1D elements we use detailed vector attribute data and compress this in the same manner to subsequently calculate for instance 1D volumes or friction. 

For this large amount of data, we execute a data compression by building tables per cell containing the information needed from the raster or vector data. The data is scaled down from the subgrid resolution to the resolution of the computational grid. Thereby, reducing the demand on hardware resources. The detailed information is preserved and can now be accessed fast during the simulations due to the compression. 

Table structure
^^^^^^^^^^^^^^^

Information in the tables is stored relative to possible water depths. This is only necessary for the range of water levels where the relation between water level and volume is non-linear as displayed in figure 1-3: In other words, the information is to be tabulated for water levels for which a cell is only partly wet.

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

The user has control over the table sizes and compression by setting a table step size (table_step_size) for the tables in the global settings. The table step size defines the height interval between succeeding increments. The increment size determines the amount of increments in a table and thus the amount of compression. In 3Di one general table step size can be set for all of the above mentioned tables. However, there are two extra tables step size parameters that can overrule the table step size for some of the tables. The optional table steps size parameters are:

* table_step_size_1d
* table_step_size_volume_2d

When the table_step_size_1d is set different from the general table_step_size, the tables containing the information of the 1D domain is processed with a different increment than information in the 2D modelling. This can be beneficiary for the simulation, when for instance the 2D date needs to be compressed strongly due to hardware limitations. Same principle applies for the table step size for 2D volume tables. To be able to make an optimal balance between memory use, computational speed and accuracy, one can also differ the table step sizes of the volume tables and the other tables necessary in the 2D domain. In order to keep the most detailed description of the cross-sections and the friction, one can increase the table step size for the volume tables, thus linearizing the system and thereby simplifying the mathematical solution. This can be advantageous for the speed of the program, especially for simulations with extensive flooding and drying. 
