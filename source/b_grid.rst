.. _grid:

The grid
-----------

To allow flow to be computed numerically, space and time need to be discretised. For time are time-steps defined, and for space is a grid defined. In the sections below we elaborate on the grid specified for computations in the 1D and in the 2D domain.

Computational grid for 2D domain
===================================

In 3Di we make use of a so-called structured, quad-tree based, staggered grid. This implies for the two dimensional domain that computational cells are perfect squares, where the pressure/ water levels and volumes are defined in the cell centres and velocities and discharges are defined at the cell edges. In the Figure below, an example is shown of a grid in a 2D domain. 

.. figure:: image/b1_1.png
   :figwidth: 400 px
   :alt: grid 2d
   :align: right

   
   Example of a staggered 2D grid including a refinement; water levels/ pressures are defined in the cell centres (blue dots) and velocities at the cell edges (blue bars). Water level domains are indicated by blue areas, and the momentum domains by green and orange areas. 
   
.. figure:: image/b1_2dv.png
   :figwidth: 300 px
   :alt: grid 2dv
   :align: left   
   
   Example of a vertical staggered grid
   
The hydrodynamic computations are based on the conservation of volume and momentum. In the next sections (:ref:`cons_volume`,  :ref:`flow1d`, :ref:`surface_flow`, and :ref:`groundwater`), the methods concerned for the computations are discussed. However, in order to solve the equations, the domains in which they are valid, need to be defined. In the Figure above, the volume and momentum domains are shown.
   
The computational cost of a simulation is strongly related to the number of computational cells. One always needs to find a balance between grid resolution and computational time. There are often regions where the flow is more complex or where one requires results with a finer resolution. To optimize the computational cost and grid resolution, users can refine the grid locally. 3Di uses a method called quad-tree refinement. This means, that in space, refinements can be added by dividing neighboring cells by a factor 4 (Figures below and above). This is a simple refinement method that allows the equations to be solved efficiently and accurately. 

.. figure:: image/b1_6_quadtree_grid.png
   :figwidth: 400 px
   :alt: quadtree_refinement
   :align: right

   
   An example of a computational grid with quad-tree refinements.
   
3Di offers the possibility to take a groundwater layer into account, thereby extending the two dimensional model to a 2-layer system. The horizontal computational grid of the groundwater layer is exactly equal to the computational grid of the 2D surface layer. The coupling between the two layers is consistent with the approach of a staggered grid. That means that between the two pressure points a velocity and discharge is defined. 
   
Subgrid method
++++++++++++++++

Flow is strongly affected by the bathymetry. Therefore, to simulate flow accurately, information of the bathymetry is crucial. To illustrate the importance of a well described bathymetry, consider the three flows in a flume shown shown in the Figure below. While the bathymetry differs only slightly, the flow behaves  completely different.

Nowadays, detailed bathymetry information becomes more and more available.  However, it is difficult to take detailed grid information into account, without a strong increase in computational cost. In search of an optimal balance between computational cost and accuracy, the so-called subgrid method (Casulli 2009, Casulli&Stelling 2011, Stelling 2012, Volp & Stelling 2013) is developed and implemented in 3Di.

.. figure:: image/b1_3.png
   :figwidth: 600 px
   :alt: bathymetry variations example
   :align: center

   
   Examples of flow in a flume, where a slight change in bathymetry, strongly affects the flow.

The basic idea behind the subgrid method, is that water levels vary much more gradually than the bathymetry. In hydrodynamic computations, water levels are assumed to be uniform within a computational cell. Traditionally, this is also assumed for the bathymetry within such a cell. The subgrid-based approach allows the bathymetry to vary within one computational cell, while the water level remains uniform. In 3Di two grids are to be defined; a high resolution subgrid and a coarse(r) computational grid. All input data, such as the bathymetry, roughness and infiltration rates can be defined on the high resolution grid, while the computations are performed on the coarse computational grid. Volumes and cross-sectional areas are based using the high resolution bathymetry information. The variation of the bathymetry within a computational cell means that a cell can be dry, wet or partly wet. This approach has two implications:

- The volume has a non-linear relation with the water level, because when the water level rises, the wet surface area increases is well. Such a system can be solved using a newton iteration. To compute the volumes at the next time step.

- As we are allowed to have a non-linear relation between water level and volume, 3Di can deal automatically with flooding and drying. No artificial thresholds are necessary. 

.. figure:: image/b1_4.png
   :figwidth: 400 px
   :alt: subgrid_bathymety_cell
   :align: left
   
   An example of a computational cell with a bathymetry defined on the subgrid.

Input
++++++

Users define for the grid generation a cell size (of the finest grid resolution) and the number of refinement layers. A computational cell consists always of an even number of subgrid cells. In addition, the user needs to define where and if refinements should be defined. One can define polygons or lines to indicate these areas and the refinement level. For a detailed example, see :ref:`flood_model`.


Some facts and figures:
++++++++++++++++++++++++++++

-	The use of high resolution information goes hand in hand with large amounts of data. To compress this data, it is stored during the computations in tables. More information about this can be found in :ref:`tables`.
-	There are more variables that are defined at the high resolution grid; such as roughness, infiltration capacity and hydraulic connectivity. These will be introduced later in the documentation.

     
Computational grid for 1D domain
====================================

For studying the flow of narrow features in the landscape or sewer systems, it is advantageous to use one dimensional models. This allows for an extensive description of the system, without actually computing cross-flow phenomena. These are in those cases limited and the use of a 1D representation will reduce the computational cost. In 3Di 1D networks can be defined, representing open channels, manholes, weirs, orifices, culverts and closed pipes. There are several options to couple the 1D and the 2D domain (see Section :ref:`flow1d`). All options for the coupling allow for a fully integrated computation, this means that the full 1D and 2D systems are solved as one.

To compute the flow in a 1D network a grid is to be defined as well. Consistent with the grid defined for the 2D domain, a staggered grid is used again. Pressure/ water level points are allocated with a velocity point. An example can be seen in the Figure below. 


.. figure:: image/b1_1d.png
   :figwidth: 400 px
   :alt: 1D structure of the grid.
   :align: right
   
   An example of the grid of a 1D Network. Water levels/ pressures are defined in the cell centres (blue dots) and velocities at the cell edges (blue bars). Water level domains are indicated by blue areas, and the momentum domains by green and orange areas.

Input
++++++

1D networks can consist of open channels, closed pipes and various structures. More about the various options can be found in the Sections :ref:`structures` and :ref:`channels`. The resolution of the 1D domain can be defined per 1D element.