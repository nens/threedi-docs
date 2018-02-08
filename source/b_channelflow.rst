Channels
============

The 3Di model offers the possibility to simulate 1D flow. This means that the calculated flow velocity and discharge is averaged over both depth and width.  Effects of variations in depth and width are included but flow within a segment has only one direction. A 1D element can be a watercourse (open water) or a sewer pipe. This section is limited to channels.

Some model elements of the water system can be modelled better in 1D. This mainly involves specific characteristics of these elements which are very important for the model (like the discharge equation of a weir). Currently available within 3Di are the following 1D elements; channels, structures, like weirs, orifices and culverts, and levees or obstacles.
Simulating the 1D water courses is possible in three ways. This includes three types of 1D elements; Isolated, (Double) Connected and Embedded.  The difference between these 1D elements is their interaction with 2D flow.

Types of channels
------------------

The water system of channels and ditches can be schematised as a 1D network in 3Di that can interact with the 2D calculation cells of the quadtree. There are three different types of channels to be distinguished for different purposes:

- Embedded

- Connected

- Isolated

These three types of channels differ in the way they exchange water with the 2D environment. The embedded channel is fully integrated in the 2D quadtree. This channel shares the water level of the calculation cell but it contains its own velocity points to model the real flow through the channel. Embedded velocity points will be put on the edges of the calculations cells. The channels are thus depending on the calculation cell dimensions. The embedded channel can be used for most ditches in polders where the water level in the channels is lower than the surface level under normal conditions. 

A connected channel is linked to a 2D quadtree by means of an overflow relation. Hereby you can think of a belt channel/ drainage system. The water level in the belt channel is mostly higher than the surface level in the polder, the levee of the channel makes sure that the water stays in the drainage system. With the connected channel it is possible to model the belt channel levee. If the level of water in the belt channel rises above the levee, than the discharge that flows over the embankment will be calculated using an overflow equation. The bottom of the connected channel can also exceed the height in the 2D elevation grid.

The isolated channel is fully disconnected from the 2D quadtree, the water level is independent of the water level in the 2D and there will be no exchange. The isolated channel can be used for modelling external forcings. These channels can also be outside the elevation grid and the calculation grid (spatially). Therefore parts of the water system which are beyond the study area can still be modelled. 

While modelling think of the type of 1D channel type that fits the watercourses in the study area best. For small ditches in an area without elevation, where the flow velocity is low it is sometimes useful not to use 1D channels. Digging ditches in the elevation map will probably lead to sufficient drainage and will make it possible to use bigger calculation cells. The size of the calculation cells is also important. If you expect water differences, make sure that there are small calculation cells in that area. If there is an unsuspected flooding somewhere then reduce the size of the cells in that area or choose a connected channel. Remember that a calculation cell can only have one water level. The volume will then be distributed over the calculation cell whereby as a result the lowest part are inundated first. Therefore it may look like the watercourses are leaking like the example below.

.. figure:: image/b_channel_leak.png
   :scale: 90%
   :align: center
   
   Example of channel leaking

Sections
--------

All channel sections are defined by polylines. The polyline accurately defines the geography of a channel. It does not define it’s width or depth. On several locations along the polyline characteristics can be define in a cross section definition. For channels of the (Double) Connected type, a bank level can also be specified at these locations. Every polyline needs at least one point on which these characteristics are described. 

A flow area needs to be described with a table, or by means of a diameter (for a circular flow area) and a width (for a rectangular flow area). When a closed section is defined, the channel is seen as a pipe. In reality, cross-sections are rarely symmetrical. In the 3Di calculation core, the information of the cross-section is stored in tables, which means that part of the geometry information is lost. This loss of information does not affect the accuracy of the 1D calculations. 

A Channel is divided into several sections. The length of each section depends on the specified grid distance, but can sometimes be smaller due to the presence of structures. The properties are assigned to each section by means of interpolation or projection. The width and shape of the cross section determine the dimensions of the section and thus determine the storage in the channel. If the water level rises above the 'end' of the given section, the water rises upwards as a column within the dimensions of that section. This means that above the highest point of the section the wet cross section increases linearly and with it the volume.

Every channel section has a water level point on which volume and water level are computed. For connected channels there is an exchange taking place between the surface water between this node and 2D calculation cell. This determines that the 1D network is more or less detached from the 2D calculation grid. Channel sections are linked by velocity points, on which discharge and velocity are computed. 

For all sections, the 1D shallow water equations are solved. The basis for the calculation of flow is solving the continuity and momentum equations of Saint-Venant.  The terms included in the momentum equation are inertia, advection and friction. We assume hydrostatic pressure thus pressure loss is rewritten as a water level gradient.

.. figure:: image/b_channel_network.png
   :align: center
   
   Example network of connected channel sections and 2D quadtree with channel sections in blue, 1D2D connections in orange and the 2D quadtree in gray
