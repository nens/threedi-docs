Interflow
=========


In a 2D model, the water flows over the surface and it can infiltrate into the soil. Surface water flow is described by the shallow water equations. The infiltration is based on the available water above the surface, the maximum infiltration rate and the storage capacity of the soil. All these parameters are defined on a geographical raster, and translated to a set of values for each computational cell.

The interflow layer is an extra layer that can be defined below the surface. Surface water can be stored in the interflow layer and water can also flow through the interflow layer. The flow through the interflow layer is described by the Darcy equation. The Darcy type of flow is believed to be more realistic for surface/subsurface flow in rainfall runoff conditions. This is because, in these cases, one deals with very thin water layers for which small (unknown) structures in the soil and on the ground level affect the flow. In such case the flow resembles more a Darcy type of flow. 

Basic Principles
------------------

.. figure:: image/b_interflow_applications.png
   :alt: Applications of the interflow layer

The interflow layer is defined by setting the thickness of the interflow layer, the porosity and the permeability rate. The storage capacity of the interflow layer depends how the variables are interpretated and this depends on the interflow type the users specifies. 

.. list-table:: Settings for interflow layer
   :widths: 45 45 45
   :header-rows: 1

   * - Parameter
     - Uniform in Model Domain
     - Spatially Varying in Model Domain
   * - Porosity
     - .. math:: 
         \checkmark
     - .. math:: 
         \checkmark
   * - Porosity Layer
     - .. math:: 
         \checkmark
     - 			x
   * - Hydraulic Connectivity
     - .. math:: 
         \checkmark
     - .. math:: 
         \checkmark
   * - Impervious Layer Elevation
     - .. math:: 
         \checkmark
     - x

Computation of Volume
-----------------------

The volume of water in a computational cell consist of the volume in the porous layer and that of the open water layer. In principle, the porous volume is based on the porosity and the thickness of the interflow layer. These combined, determine the storage capacity of a computational cell: 

.. math::
   :label: interflow_volume
   
     V = \sum{ \hat{\alpha} H_I A} + H A_,

| In which, 
- | a is the local porosity, 
- | H\ :sub:`I`\  is the thickness of the interflow layer, 
- | A is the pixel surface and 
- | H is the water depth.

If an interflow layer is defined, water is first stored in the interflow layer and only when the waterlevel rises above the groundlevel water is stored on the surface. This implies, that H\ :sub:`I`\ can be maximally the thickness of the interflow layer and H>0 when the water level is above the ground level. However, when within a computational cell the ground level varies, the moment that the water level rises above the ground level is different per subgrid cell as the water level is uniform within a computational cell. 3Di allows four different methods to deal with the subgrid information, this is defined bij the interflow type. 

The porosity depth can be defined model wide only. The porosity can vary spatially in the model domain. The interflow type determines a so-called porosity factor. This factor determines whether the porosity remains as set or that the storage capacity is  and porosity depth is constant then this means that each cell has the same maximum volume that can be stored in the interflow layer. 

.. figure:: image/b_interflow_simple.png
   :alt: Sketch of interflow layer

To fully understand interflow with subgrids, it is important to realize that each cell (one cell has multiple subgrids) has one volume value and hence one water level. The flow from one cell to another has two components, namely interflow and surface flow. (Only when using the groundwater flow option in 3Di, two volumes are computed for each cell, a groundwater volume and a surface water volume).

.. figure:: image/b_interflow_build_volume.png
   :alt: Sketch of interflow layer

Normally the volume of water in a cell is computed from the surface of the lowest subgrid. If interflow is used, the volume is computed from another reference level, namely the impermeable layer. In the example of the figure above, the lowest elevation is 0.0 m and the interflow depth is defined by 1.0 m. This means that the reference (or impermeable) level is at -1.0 m for this cell. 

The interflow layer is completely dry (V=0 m\ :sup:`3`\) if the water level in a cell is at the level of the impermeable layer (-1.0 m). The interflow flow layer is completely filled (saturated), if the water level is at the same level of the highest subgrid in this cell (+1.0 m). Note that the volume is build out of two volumes, interflow volume and surface volume.

For all interflow types the water level is assumes uniform per calculation cell. The volume in the interflow layer is zero when the water level is at the bottom of the interflow layer. The interflow layer is completely filled when the water level is above the higher DEM pixel in the calculation cell. The volume in the calculation cell is the volume in the interflow layer plus any volume in the 2D domain. The volumes are not stored separately.


.. figure:: image/b_interflow_states.png
   :alt: Overview of different states using interflow

   Overview of different states using interflow
   
   
Computation of Flow
-----------------------

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

**Infiltration** In principle, nothing about infiltration has changed with or without interflow. Infiltration is not to interflow layer itself, but from the interflow to the subsoil. The infiltration volume is removed from the interflow layer. Infiltration stops when the water level is below the lowest pixel.

**Laterals** Nothing actually changes for the laterals. The extraction of water continues until the total volume is zero. This means that the water level can be lower than the DEM.

**Obstacles and levees** Flow in the interflow layer is affected (stopped) by obstacles and levees. Flow in the interflow layer does not flow under levees.

**Connection with 1D** There is no separate link between interflow and 1D-elements. So no seepage from deep channels, all flow between 1D and 2D happens via the 2D surface.

**Embedded channels or pipes** Both embedded elements and interflow affect the volume in 2D calculation cells and it is therefore not advised to use them together.

