.. _1Dtypes:

1D Flow
-------

3Di offers the possibility to model areas as 1D networks. Generally, these models are very fast, but also strong simplifications of the real world. Therefore, 3Di has various options to integrate 1D networks in 2D domain. This offers the possibility to preserve the complexity of the modelling domain, but to make use of the extra resolution option and speed of 1D computations.

The flow in 1D networks is computed, using the equation of conservation of mass and momentum, more specifically the 1D depth-averaged shallow water equations. The momentum equation for 1D flow is:

.. math::
   :label: 1D momentum equation

   \frac{\partial u}{\partial t}+u \frac{\partial u}{\partial s}=-g\frac{\partial \zeta}{\partial x}-\frac{\tau_f}{\rho}-\frac{\tau_w}{\rho}

| In which: 
| :math:`u` is the cross-sectionally averaged velocity
| :math:`s` is the 1D coordinate in along the network
| :math:`g` is the gravitational acceleration
| :math:`\rho` is the density of the water
| :math:`\tau_f` is the shear stress due to bottom friction
| :math:`\tau_w` is the shear stress due to wind

In words; in 1D, 3Di takes inertia, advection, pressure gradients, bottom friction and wind shear stresses into account. This yields for all types of 1D network applications. However, in the computation of advection and the effect of wind stress on specific 1D network configurations, some differences are applied. This will be explained more elaborated below.  

.. figure:: image/b_1dcrosssections.png
   :alt: cross-sections_1D_networks
   
   Examples of cross-sections in 1D networks

A 1D Network
------------

In the most abstract form, a 1D network can be viewed as a combination of nodes and connections. Such a network is translated to a grid, as described in :ref:`1dgrid`. The nodes and the connections have their own characteristics. Based on those cross-sectional areas and storage is computed. 

.. figure:: image/1dnetworkabstract.png
   :alt: abstract_1D_networks
   
   Example of a 1D network


Types of 1D elements
--------------------

Often a water system of small channels, ditches and pipes are schematised using the 1D network options in 3Di. These elements can interact with the 2D computational domain. There are three different options that determine the interaction with the 2D domain. The elements can be defined as:

- Embedded

- Connected

- Double Connected

- Isolated.

In the sections below, these options are further discussed.

In a one network all these types of 1D elements can be used together. The sections :ref:`sewerage`, :ref:`structures` and :ref:`channels` describe how these elements can be defined in a model schematisation.


 
Isolated 1D network elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**When do you use this?**

In case the 1D network is defined as Isolated. The element does not interact with the 2D surface domain.

**How it works?**




Connected 1D network elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**When do you use this?**

In case the 1D network is defined as Connected. The element does  interact with the 2D surface domain. 

**How it works?**



Embedded 1D network elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**When do you use this?**


In case the 1D network is defined as Connected. The element does  interact with the 2D surface domain. 

**How it works?**



These types of elements differ in the way they exchange water with the 2D domain. An embedded element is fully integrated in the 2D computational domain. These elements share the water level of the computational cell but it contains its own velocity points to model the real flow through the element. Embedded velocity points will be put on the edges of the calculations cells. The element length depends on the 2D computational cell size.

A connected element is linked to the 2D computational domain. Hereby you can think of a belt element/ drainage system. The water level in the belt element is mostly higher than the surface level in the polder, the levee of the element makes sure that the water stays in the drainage system. With a connected element it is possible to model the belt element levee. If the level of water in the belt element rises above the levee, than the discharge that flows over the embankment will be computed based on a simplified momentum equation. The deepest point of the connected element can also exceed the height in the 2D elevation grid.

An isolated element is fully disconnected from the 2D computational domain, the water level is independent of the water level in the 2D domain and there will be no exchange. The isolated element can be used for modelling external forcings. These elements can also be outside the elevation grid and the calculation grid (spatially). Therefore parts of the water system which are beyond the study area can still be modelled.