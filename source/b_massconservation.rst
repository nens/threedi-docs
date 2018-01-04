Conservation of mass
=========================

To make simulations of flow in order to make simulate the behavior under varying condition, one is often forced to use the computational power of computers. Since the introduction of computers various methods have been introduced and improved. Some aspects are true for all types of methods. Here, we will limit ourselves to the methods used in the computational core of 3Di.

3Di is a subgrid based, two dimensional, depth averaged hydrodynamical model. Flow is described by water levels and velocities. These are computed by 2 fundamental laws of physics; i) Conservation of mass and ii) Conservation of momentum. In this section we will describe how we deal with conservation of mass in combination with the so-called subgrid method.


In 3Di we make use of a so-called staggered grid. This implies in 3Di for the two dimensional domain that computational cells are perfect squares, where the water levels and volumes are defined in the cell centres and velocities and discharges are defined at the cell edges (Figure b1.1). In such grid a volume domain and two momentum domains can be defined in which the two fundamental laws are applied. In the one dimensional domain, it means that we have points and lines connecting as seen in Figure b1.1.

.. figure:: image/b1_1.png
   :scale: 30%
   :alt: virtual_conservation_box
   :align: right

   
   An example of a staggered grid. Water levels are defined in the cell centres and velocities at the cell faces.


The conservation of Mass can be described mathematically as:

.. math::
   :label: mass_conservation    

   \frac{\Delta \rho V}{\Delta t}=\sum_i^{in} \rho_i Q_i -\sum_k^{out} \rho_k Q_k + \sum_i \rho_j S_j 

In which :math:'\rho' is the density, :math:'V' is the volume, :math:'Q' is a discharge and :math:'Q' is a sink or source term. The counters :math:'i, j, k' count over all existing discharges, sink and source terms. In 3Di we do not account for density variations, so the density :math:'\rho' is assumed uniform and constant. This simplifies the equation for conservation of mass, to the following equation for conservation of volume:

.. math::
   :label: volume_conservation    
   
   \frac{\Delta V}{\Delta t}=\sum_i^{in} Q_i -\sum_k^{out} Q_k + \sum_i S_j 


But this can be described much more intuitively. When focusing on a virtual box as shown in Figure b1.2. You see a box with flow (discharges in blue) sources and sink terms (in yellow) entering and leaving the box. When more water enters the box, the volume increases and when more water leaves the box the volume decreases. Naturally, this is true for the flow simulated in one and in two dimensions. 

.. figure:: image/b1_2.png
   :scale: 30%
   :alt: virtual_conservation_box
   :align: right

   
   A virtual box for conservation of mass.

Subgrid method
---------------------

Flow is strongly affected by the bathymetry. Therefore, to simulate flow accurate, information of the bathymetry information is crucial. In figure b1.3 three flows in a flume in which the bathymetry differs only slightly, are shown. While the obstacle in the flume is changed only a bit, the flow would react strongly on it. Nowadays, detailed bathymetry information becomes more and more available.  However, when computing with such high resolution the simulation would take too long. As the simulation time increases strongly with increase of computational cells. In order to find a balance between computational time and accuracy, we make use of the so-called subgrid method (Casulli 2009). 

.. figure:: image/b1_3.png
   :scale: 20%
   :alt: virtual_conservation_box
   :align: centre

   
   A virtual box for conservation of mass.

The basic idea is that water level vary much more gradually than the bathymetry (figure b1.4). Therefore while we assume within a water level domain the water level to be uniform, the bathymetry is allowed to vary. Therefore, the volume and the cross-sectional areas can be defined using the high resolution bathymetry information. It also means that a computational cell can be dry, wet or partly wet. This has two implications:
- The volume becomes a non-linear relation with the water level, because when the water level rises, the wet surface area increases is well. Such a system can be solved using a newton iteration. To compute the volumes at the next time step.
- As we are allowed to have a non-linear volume, we can allow automatically deal with flooding and drying. No artificial thresholds are necessary, to deal with this. 

.. figure:: image/b1_4.png
   :scale: 50%
   :alt: subgrid_bathymety_cell

   
   An example of a computational cell with a bathymetry defined on the subgrid.

In this we do not make any distinction between the 1D or the 2D model elements. 

Pressurized flow
---------------------
However, a typical characteristic of some 1D elements is that they can have closed cross-sections (Figure b1.5). In this the violate one of the requirements in order to solve the non-linear system. Therefore, a new method had to be introduced to solve such non-linear systems. This was introduced with the so-called nested Newton method (Casulli & Stelling 2013).

.. figure:: image/b1_5.png
   :scale: 50%
   :alt: open_closed_crosssections
   
   Examples of cross-sectional areas. An open and closed cross-sectional area

By this not only flooding and drying is automatically accounted for, also pressurized flow can simply be solved. One of the advantages is that the volume in an element, like a pipe can be limited, while the water level can still rise. At some point, when the pipe is full, the water level than represents a pressure (Figure b1-6). 



Local refinements
-----------------------------
In the 1D domain, one can add extra computation point to any 1D element, this is described later in the tutorials. In 2D, the adding of extra resolution is slightly more complex. In 3Di we have chosen to use method called quad-tree refinement method. This means that in space refinements can be added by dividing neighboring cells by a factor 2 (figure b1.6). This is a simple refinement method that allows our equations to be solved efficiently. Moreover, by using the subgrid method the grids take effectively the shape of the flow. 

.. figure:: image/b1_6_quadtree_grid.png
   :scale: 30%
   :alt: quadtree_refinement
   :align: right

   
   An example of a computational grid with quad-tree refinements.

Some facts and figures:
---------------------------------
-	A computational cell consists always of an even number of subgrid cells
-	To compress the large amounts of data, the high resolution information is stored in tables (see section tables)
-	There are more variables that are defined at the high resolution grid. Such as roughness, infiltration capacity and hydraulic connectivity. These will be introduced later in the documentation.

   
   A virtual box for conservation of mass.
