.. _1Dtypes:

Types of 1D elements
-----------------------

The water system of channels, ditches and pipes (1D elements) can be schematised as a 1D network in 3Di. This network can interact with the 2D computational domain. There are three different types of 1D elements to be distinguished for different purposes:

- Embedded

- Connected

- Isolated

These three types of elements differ in the way they exchange water with the 2D domain. An embedded element is fully integrated in the 2D computational domain. These elements share the water level of the computational cell but it contains its own velocity points to model the real flow through the element. Embedded velocity points will be put on the edges of the calculations cells. The element length depends on the 2D computational cell size.

A connected element is linked to the 2D computational domain. Hereby you can think of a belt element/ drainage system. The water level in the belt element is mostly higher than the surface level in the polder, the levee of the element makes sure that the water stays in the drainage system. With a connected element it is possible to model the belt element levee. If the level of water in the belt element rises above the levee, than the discharge that flows over the embankment will be computed based on a simplified momentum equation. The deepest point of the connected element can also exceed the height in the 2D elevation grid.

An isolated element is fully disconnected from the 2D computational domain, the water level is independent of the water level in the 2D domain and there will be no exchange. The isolated element can be used for modelling external forcings. These elements can also be outside the elevation grid and the calculation grid (spatially). Therefore parts of the water system which are beyond the study area can still be modelled.