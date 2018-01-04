Interflow
=========

The interflow layer can be added to any 2D model for the following reasons:

#. For subsurface storage

#. For fast surface flow for very small water depths (thin water layer)

#. In case we assume the soil is saturated, for flow through the unsaturated zone.

The basic principles for interflow and how it may be used in these applications are explained below.

.. figure:: image/b_interflow_applications.png
   :alt: Applications of the interflow layer

   Applications of the interflow layer

Basic principles
---------------------

The interflow layer is a layer below the 2D domain. In this layer water can be stored and water may flow from one calculation cell to the next. The storage in the interflow layer is added to the total volume in the calculation cell. The water level is determined relative to the bottom of the interflow layer. All the water that enters a calculation cell will be stored in the interflow layer. Once the water level rises above the surface level, water is stored in the 2D domain as well. The flow in the interflow layer is computed separately from the flow in the 2D domain.

The volume in the interflow layer is determined by:

- The surface level elevation (DEM)

- Porosity

- Porosity layer thickness or depth of the impervious layer

The latter depends on the interflow type setting used.

Volume
-----------------------

The volume in the interflow layer is determined as follows:

.. math::
   :label: interflow_volume
   
     V = \sum{ \hat{\alpha} H_I A} + H A_,

| In which, 
| a is the local porosity, 
| H\ :sub:`I`\  is the thickness of the interflow layer, 
| A the pixel surface and 
| H the water depth.


For all interflow types the water level is assumes uniform per calculation cell. The volume in the interflow layer is zero when the water level is at the bottom of the interflow layer. The interflow layer is completely filled when the water level is above the higher DEM pixel in the calculation cell. The volume in the calculation cell is the volume in the interflow layer plus any volume in the 2D domain. The volumes are not stored separately.


.. figure:: image/b_interflow_states.png
   :alt: Overview of different states using interflow

   Overview of different states using interflow

Types
--------

There are 4 types or settings of interflow that determine the way the volume it determined.  For types 1 and 2 the user explicitly defines the thickness of the porosity layer and the depth of the impervious layer. In theory both should have the same value. But early practice showed that using a very deep depth in the interflow layers results in a more stable simulation. By choosing the thickness of the porosity layer the volume in the interflow layer can still be controlled. The water levels do become artificial low, which can be confusing. In the figure above the water level may sink to 10000 meter.

**Type 1** Fixed thickness of the porosity layer in the model domain and uniform impervious layer elevation per calculation cell

Provide a porosity, porosity layer thickness and the depth of the interflow layer. Porosity can be given global or per pixel. The porosity and the thickness of the porosity layer determine the volume stored in the calculation cell. De depth of the interflow layer determines the water level. The volume in the interflow layer is scaled to the interflow layer depth to determine the water level. 

.. math::
   :label: porosity_scaled
   
   \hat{\alpha} = \frac{\alpha * L}{max(H_I, L)}

| In which: 
| a = input porosity, 
| L = interflow layer depth and 
| H\ :sub:`I`\ = D\ :sub:`sur`\ – D\ :sub:`inp`\, in which: 
| D\ :sub:`sur`\  = surface level elevation and 
| D\ :sub:`inp`\  = elevation of the impervious layer.

 
For type 1 Interflow, the depth of the interflow layer is measured from the deepest DEM pixel in the calculation cell. The scaled porosity is then used to determine the volume in the interflow layer according to equation (1).

**Type 2** Fixed thickness of the porosity layer in the model domain and uniform impervious layer elevation over the model domain

The porosity is determined in the same as as under type 1, but the elevation of the impervious layer is determines relative to the lowest DEM pixel in the entire model.

**Type 3** Relative thickness of the porosity layer and uniform interflow depth per calculation cell

The volume in the interflow layer depends on the porosity per pixel and the depth to the impervious layer. The porosity can be given globally or as a raster with different values per pixel. In type 3 the porosity is scaled based on the distance between the lowest DEM pixel in the calculation cell and the elevation of the impervious layer while the volume is determined per pixel. This means that although you are able to spatially vary porosity in more detail, the volume in pixels that lie above the lowest pixel of the calculation cell is overestimated. 

**Type 4** Relative thickness of the porosity layer and uniform interflow depth over the model domain

Type 4 works in the same way as type 3 but determines the depth of the interflow layer as the difference between the lowest DEM pixel in the whole model and the impervious surface elevation.

*The table below shows an example of de volumes in a calculation cell with interflow relative to the water level. In the last column the interflow settings are given. The rows in the table correspond to the situations displayed in figure 2. The calculation cell's area is one square meter and for simplicity the cells contains only 4 pixels*

.. figure:: image/b_interflow_example.png
   :alt: Interflow example table

Flow
----

The flow in the interflow layer is determined according to Darcy's equation for groundwater flow:


.. math::
   :label: interflow_flow
   
   u_I = \kappa \frac{\delta \zeta}{\delta x}
   v_I = \kappa \frac{\delta \zeta}{\delta y}

| In which: 
| u\ :sub:`I`\ , 
| v\ :sub:`I`\  = the horizontal flow velocity in the interflow layer. 


The conductivity is given by constant κ and ζ is the water level in the calculation cell. The continuity equation is not expanded and thus only one volume is used for 2D flow. The head difference between calculation cells forces 2D flow both in the interflow layer and on the surface.

The hydraulic conductivity κ is related to the soil type and land use and is given in m/day. It can be given globally or as a raster with different values per pixel. For the latter all pixel values within one calculation cell are averaged.

Good to know
------------

**Infiltration** Interflow does not affect or interact with infiltration. Depending on the infiltration settings infiltration will either stop when the lowest DEM pixel (per calculation cell) is dry or when the volume in the calculation cell equals zero. 

**Rainfall or Laterals** Interflow does not affect or interact with Rainfall or laterals. Negative lateral discharge continues as long as there is volume in the calculation cell and positive discharge or rainfall is added to interflow volume before it reaches the surface.

**Obstacles and levees** Flow in the interflow layer is affected (stopped) by obstacles and levees. Flow in the interflow layer does not flow under levees.

**Connection with 1D** There is no separate link between interflow and 1D-elements. So no seepage from deep channels, all flow between 1D and 2D happens via the 2D surface.

**Embedded channels or pipes** Both embedded elements and interflow affect the volume in 2D calculation cells and it is therefore not advised to use them together.

















