.. _onedee_flow:

1D Flow
==========

Introduction
------------

3Di offers the possibility to simulate 1D flow. This means that the calculated flow velocity and discharge is averaged over both depth and width. Effects of variations in depth and width are included, but flow within a segment has only one direction. A 1D element can represent, for example, a water course, a hydraulic structure or a sewer pipe. The sections below describe the several types of 1D elements that are available in 3Di.

The flow in 1D networks is computed using the equations of conservation of mass and momentum, more specifically the 1D depth-averaged shallow water equations. The momentum equation for 1D flow is:

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

1D Network
----------

In the most abstract form, a 1D network can be viewed as a combination of nodes and lines. Such a network is translated to a grid, as described in :ref:`1dgrid`. The nodes and the connections have their own characteristics. Based on those, cross-sectional areas, storage and flow is computed.

.. figure:: image/1dnetworkabstract.png
   :figwidth: 400 px
   :alt: abstract_1D_networks

   Example of a 1D network

.. _cross_section_of_1d_element:

Cross-section shapes
--------------------

Cross-sections in 1D can be open or closed. In open cross-sections, the width at the highest point in the cross-section definition is extrapolated straight up (red dashed lines in the figure below). In closed cross-sections, if the water level rises above the top of the cross-section, the volume and wet cross-sectional area remain the same, and the flow becomes pressurized. See :ref:`1Dpressurized`.

The table below gives an overview of the types of cross-section shapes available in 3Di.

.. list-table:: Cross-section shapes
   :widths: 1 1 4
   :header-rows: 1

   * - Shape
     - Value
     - Description
     - Open or closed
   * - Closed rectangle
     - 0
     - Rectangular cross-section
     - Closed
   * - Open rectangle
     - 1
     - Rectangular cross-section
     - Open
   * - Circle
     - 2
     - Circular cross-section
     - Closed
   * - Egg
     - 3
     - Egg-shaped cross-section with the narrow end at the bottom. Width:height ratio is 1:1.5.
     - Closed
   * - Tabulated rectangle
     - 5
     - Custom shape, with a width defined at each height. The width is used up to the next height/width pair without interpolation.
     - Open if width at top > 0; Closed if width at top = 0
   * - Tabulated trapezium
     - 6
     - Custom shape, with a width defined at each height. The widths are interpolated between height/width pairs.
     - Open if width at top > 0; Closed if width at top = 0
   * - YZ
     - 7
     - Custom shape, with a height (Z) defined at each distance (Y) across the channel or structure.
     - Usually open, but can be closed when first YZ pair equals last YZ pair
   * - Inverted egg
     - 8
     - Egg-shaped cross-section with the narrow end at the top. Width:height ratio is 1:1.5.
     - Closed

Some examples are shown in the figures below.

.. figure:: image/b_1dcrosssections.png
   :alt: crosssec_1D_networks

   Examples of cross-section shapes in 1D networks. Top row: Closed rectangle, Tabulated rectangle (open), Tabulated trapezium (open). Bottom row: Circle, Tabulated rectangle (closed), Tabulated trapezium (closed).

.. figure:: image/b_1d_cross_section_egg.png
   :alt: Cross-section shape 'Egg'

   Examples of cross-section shape 'Egg' in 1D networks. The 'Inverted egg' shape is the same, but upside-down.

.. _channelflow:

Channels
---------

Some model elements of the water system can be modelled better in 1D. This mainly involves specific characteristics of these elements which are very important for the model (like the discharge equation of a weir). Currently available within 3Di are the following 1D elements; channels, structures, like weirs, orifices and culverts, and levees or obstacles. This section is limited to channels.
Simulating the 1D water courses is possible in three ways. This includes three types of 1D elements; Isolated, (Double) Connected and Embedded.  The difference between these 1D elements is their interaction with 2D flow.


While modelling think of the type of 1D channel type that fits the watercourses in the study area best. For small ditches in an area without elevation, where the flow velocity is low it is sometimes useful not to use 1D channels. Digging ditches in the elevation map will probably lead to sufficient drainage and will make it possible to use bigger calculation cells. The size of the calculation cells is also important. If you expect water differences, make sure that there are small calculation cells in that area. If there is an unsuspected flooding somewhere then reduce the size of the cells in that area or choose a connected channel. Remember that a calculation cell can only have one water level. The volume will then be distributed over the calculation cell whereby as a result the lowest part are inundated first. Therefore it may look like the watercourses are leaking like the example below.

.. figure:: image/b_channel_leak.png
   :scale: 90%
   :align: center

   Example of channel leaking

Sections
^^^^^^^^

All channel sections are defined by polylines. The polyline accurately defines the geography of a channel. It does not define it’s width or depth. On several locations along the polyline characteristics can be define in a cross section definition. For channels of the (Double) Connected type, a bank level can also be specified at these locations. Every polyline needs at least one point on which these characteristics are described.

A flow area needs to be described with a table, or by means of a diameter (for a circular flow area) and a width (for a rectangular flow area). When a closed section is defined, the channel is seen as a pipe. In reality, cross-sections are rarely symmetrical. In the 3Di calculation core, the information of the cross-section is stored in tables, which means that part of the geometry information is lost. This loss of information does not affect the accuracy of the 1D calculations.

A Channel is divided into several sections. The length of each section depends on the specified grid distance, but can sometimes be smaller due to the presence of structures. The properties are assigned to each section by means of interpolation or projection. The width and shape of the cross section determine the dimensions of the section and thus determine the storage in the channel. If the water level rises above the 'end' of the given section, the water rises upwards as a column within the dimensions of that section. This means that above the highest point of the section the wet cross section increases linearly and with it the volume.

Every channel section has a water level point on which volume and water level are computed. For connected channels there is an exchange taking place between the surface water between this node and 2D calculation cell. This determines that the 1D network is more or less detached from the 2D calculation grid. Channel sections are linked by velocity points, on which discharge and velocity are computed.

For all sections, the 1D shallow water equations are solved. The basis for the calculation of flow is solving the continuity and momentum equations of Saint-Venant.  The terms included in the momentum equation are inertia, advection and friction. We assume hydrostatic pressure thus pressure loss is rewritten as a water level gradient.

.. figure:: image/b_channel_network.png
   :align: center

   Example network of connected channel sections and 2D quadtree with channel sections in blue, 1D2D connections in orange and the 2D quadtree in gray

.. _pump:
Pumps
------

Pumps in 3Di drain water from one location to another location, within or outside the model domain. The behaviour of a pump is specified by defining the start and stop levels of the pump and the pump capacity. Naturally, water cannot be drained by a pump when it is not there. In real life, pump capacities are often larger than its supply. This behaviour will be seen in your model results. However, this behaviour causes alternating water levels and discharges. This happens in real life and also in your simulations on short time scales, but will effectively not affect the behaviour of your system.
In the computational core, we can adjust the pump capacity to ensure a more balanced of the pump.
This functionality is called the pump_implicit_ratio and can be switched off or on. In default it is switched on. More about this functionality can be found in this section in the documentation: :ref:`matrixsolvers` --> pump_implicit_ratio.

.. figure:: image/b_structures_pump.png
   :alt: structures_pump

   Schematic display of a pump function

In 3Di, users can add pumps to a schematisation via a connection node. Characteristics for pumps can be set by configuring the attributes:

.. TODO:  Eenheden van attributen toevoegen

* Capacity: Maximum discharge for which the pump is able to displace water from the suction node to the delivery node.

* Start level: in case of water levels higher than the start level, the pump is switched on.

* Lower stop level: in case of water level below the stop level, the pump is switched off. This level should be below the start level.

* Upper stop level: in case of water levels above this level the pump is switched off as well. This is an optional value, but if it is used, it is always higher that the start level.

* Type: Parameter to set whether the start and stop levels are defined at suction side or delivery side of the pump. [See Figure]


There are two methods to define a pump in a 3Di schematisation:

1. *Pump between two nodes*: A pump between two nodes drains water from the  node at suction side to the node at delivery side with the specified pump capacity. Depending on the type of pump the suction side or delivery side water levels determine the activity of the pump.

2. *End pump*:  For an end pump only the suction side node needs to be specified. With no node defined for the delivery side, all water being drained by this pump. All water pumped from the model is specified in the flow_summary.log as contribution to the global water balance. The pump characteristics to be specified are the same as for a pump type with start/stop levels at suction side. Since no delivery side node is present, it is not possible to specify a pump type with start stop level at delivery side.


**Pumps in combination with structure controls**

Pumps can be used in combination with controls. You can design a control that allows the water level at different or multiple locations determine the pumps behaviour, instead of purely local water levels. However, the local availability of water will always affect the pump capacity as well. As water that is not locally at the pump cannot be drained away. This is ensured by stopping the pump when the local water level is below the stop level. Your control affects the pumps’ behaviour, within the range of conditions for which the pump is designed.

*Example*

Given a controlled pump at location X with a stop and start level of 0.0 mNAP and 2 mNAP, respectively. The trigger for the control is the water level from location A. For higher waterlevels the pump capacity is increased. However, in case the water level at X is below 0.0 mNAP, but at A in a active range, the pump will stop. The pump can only become active again for waterlevels at X above 2.0 mNAP.


.. _weirs_and_orifices:
Weirs and Orifices
------------------

Weirs are generally used to maintain and control the water level. Orifices connect two parts of channel networks. Both structures force the flow to converge strongly at the entrance and to diverge behind the structure. At the converging part of the flow, the assumption of conservation of momentum in 1D is invalid. Locally at the structure, conservation of energy is much more suited. The formulations for the flow over the weir and through the orifice are therefore based on Bernoulli's principle. The computations of the flow of both structures follow the same reasoning. In the explanation below, the focus is on an open water rectangular weir, but similar steps are taken for structures with different open/closed cross-sections.

For a weir in open water the energy head balance reads:

.. math::

   h_I+\frac{u_I^2}{2g}=h_{II}+a+\frac{u_{II}^2}{2g}

where :math:`h` is the local water depth, :math:`u` the local cross-sectionally averaged velocity, :math:`g` the gravitational acceleration  and :math:`a` the height of the crest. The sub-scripts refer to the flow domains, indicated in the figure below.

.. figure:: image/b_structure_weir_orifice.png
   :alt: structures_weir_short

   Illustration of short crested weir and orifice under sub- and (super-)critical conditions; a simplified view of the 1D network and a sketch of the available discretized information.

In case of structures with closed profiles, in the equation of the energy balance :math:`h` is not the water depth, but the energy height. For structures having closed profiles, the transition of water depth to energy height is automatically taken care of in case the area fills with water.

For robustness, 3Di schematizes structures as connections between two nodes, as can be seen in the third panel of the figure. This assumption implies that the water level on the location of the structure is unknown. To compute accurately the discharge over the structure, a difference is made between long crested and short crested structures. Both resulting formulations are based on Bernoulli's principle, but for long crested structures, frictional losses are computed separately.


Short crested
^^^^^^^^^^^^^

The discharge over the structure is computed based on the effective cross-sectional area :math:`A_{eff}` and the velocity over the structure :math:`u_{II}`. Two states of the flow can occur over the structure: sub- and (super)-critical flow. For both states, different assumptions are valid. However, for both states it is assumed that :math:`u_I` is negligible compared to :math:`u_{II}`.

In case of (super-)critical flow, the downstream waterlevel does not affect the flow over the structure, as is the case under sub-critical conditions. The fourth panel of the figure shows the information known in a discretized world. In case the flow is critical, the water depth at the crest can be determined using the upstream waterlevel and the definition for critical flow:

.. math::
   h_{cr}= \frac{2}{3}(h_I-a) = h_{II}

The critical velocity over the structure is given by:

.. math::
   u_{II}= C_1 \sqrt{\frac{2}{3} g (h_I-a)}

:math:`C_1` is a loss coefficient, which can be set depending on the type and the shape of the structure itself and the entrance. The effective cross-sectional area is in this case based on the critical water depth. For a simple rectangular cross-section:

.. math::
   A_{eff}= C_2 W \frac{2}{3}(h_I-a)

In which :math:`C_2` is a loss coefficient due to contraction of the flow. For the total discharge in 3Di, the discharge under free flowing conditions is computed as:

.. math::
   Q_{cr} = C_1 \sqrt{\frac{2}{3} g (h_I-a)} C_2 W \frac{2}{3}(h_I-a) = C W g^{\frac{1}{2}} \left(\frac{2}{3}(h_I-a)\right)^{\frac{3}{2}}

Note, that the coefficients :math:`C_1` and :math:`C_2` are combined is the general discharge coefficient :math:`C`, which can be set by the user.

In case of sub-critical flows, the waterlevel downstream of the structure is important.  Under these conditions the flow velocity over the structure is:

.. math::
   u_{II}= C_1 \sqrt{2 g (h_{I}-h_{II}-a)}

To determine the depth at the crest, it is assumed that the waterlevel at the crest is equal to the waterlevel downstream. Based on that assumption, the effective cross-section becomes:

.. math::
   A_{sub}= C_2 W h_{II}

Combining these equations, results in the discharge formulation.

.. math::
   Q_{sub} = C_1 \sqrt{2 g (h_I-h_{II})} C_2 W h_{II}= C W \sqrt{2 g (h_I-h_{II})} h_{II}

Long crested
^^^^^^^^^^^^

For longer structures, frictional effects can become important. For the so-called broad-crested weirs and orifices an extra loss-term is added to Bernoulli's equation. The frictional losses :math:`\Delta h_F` are computed as:

.. math::
   \Delta h_F= \frac{c_f L u_{II}^2}{2 g R}

where :math:`c_f` is the dimensionless friction coefficient, :math:`L` the length of the structure and :math:`R` is the hydraulic radius. The dimensionless friction coefficient can be based on either Manning or the Chézy formulation. It is also of importance that the structure length is correctly set. The computational core expects that this is the geometrical distance between the two connection nodes. The friction coefficient can be defined either by a Manning or a Chézy value.

An advantage of these formulations is that these do not limit the timestep during the simulation.

The attributes that define these structures are:

* Crest level: The crest level of the weir. In case of an orifice this could be equal to the bottom level.

* Crest type: Selects a short or broad crested weir/orifice formulation.

* Discharge coefficient positive/negative: The coefficient used in the discharge formulation. Depending on the flow direction the coefficients could be different.

* Cross-section definition: This defines the cross-section of the structure.


.. _culvert:

Culvert
-------

Culverts can connect parts of 1D networks and allow flow under roads or other obstacles. In contrast to orifices, the flow behaviour in a culvert is assumed to be determined by shape and much less dominated by entrance losses. The flow in culverts is assumed to be a pipe flow with possible changes in cross-section. Culverts can be used for longer sections of pipe-like structures and do not have to be straight. Shorter, straight culverts are best modelled as an orifice.

For culverts and orifices, the energy loss caused by the change in flow velocity at the entrance and exit are accounted for by 3Di. The discharge coefficients for culverts can be used to account for any additional energy loss.

The input parameters for culverts are similar to those for orifices, specified in the section above. Culverts use invert levels at the start and end instead of the crest level in weirs and orifices. The input parameters are all described in the spatialite database :download:`here <pdf/database-overview.pdf>`.


.. _1Dpressurized:

Pressurized flow
---------------------

A typical characteristic of some 1D elements is that they can have closed cross-sections (Figure b1.5). Thereby, it is possible that the flow becomes pressurized. By introducing the subgrid method :ref:`subgridmethod`, it was explained that cells could be dry, wet and partly wet. By allowing the bed height to vary within a computational cell, the system of equation became non-linear. This was solved with a highly efficient method. However, there are some requirements for such system to be solved. In case the surface area decreases for increasing water levels, one of these requirements is violated.  Therefore, a new method had to be introduced to solve such a non-linear system of equations. This method is based on the so-called nested Newton method (Casulli & Stelling 2013).

.. figure:: image/b1_5.png
   :scale: 50%
   :alt: open_closed_crosssections

   Examples of cross-sectional areas. An open and closed cross-sectional area

By this not only flooding and drying is automatically accounted for, but also pressurized flow can be taken into account. One of the advantages is that the volume in an element, like a pipe can be limited, while the water level can still rise. At some point, when the pipe is full, the water level than represents a pressure (Figure b1-6).

.. _sewerage:

Pipes
-----

The dynamic flow through complex sewer networks can be computed fast, stable and accurately by 3Di. 3Di can be used to model any sanitary, storm and combined sewer system, offering complete hydrology and hydraulic simulation and real-time control (RTC) modeling capabilities. 3Di uses the complete “de Saint Venant Equations”, including backwater and transient flow phenomena. The computational core has an automatic drying and pressurized procedure and handles both subcritical and supercritical flow. The computation is 100% mass conservative, machine precision.

.. figure:: image/b_sewerage_overview.png
   :alt: b_sewerage_overview

   Sewerage system overview

The sewer network has to be defined in the 3Di model schematization. A sewer network is based on manholes connected by pipes. In the model a wide variety of cross sections and manhole shapes are available, including user-defined ones. In the sewer network one can specify any type of hydraulic structure, such as single or multiple stage pumps, weirs of any shape, rectangular and circular gates, culverts and storage and overflow basins. All structures handle free, submerged and transient flow conditions. Real-time control, including PID control, are available for all structures to simulate real time controlled networks.

Combination of sewer network with other 0D, 1D and 2D networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sewer network is a special type of 1D network. Another type of the 1D network is an open water network. Both type of 1D networks can be combined in one model. There is no limitation to number of sewer pipes, the number of networks or the complexity of the networks.

The 1D sewer network can be linked to a 2D terrain model above that network. The spatial boundaries of the 1D and 2D model can be different. This implies that if desired, only a specific part of the 1D network can be covered by the 2D network, or the other way around.

The 1D sewer network can also be linked to a 0D network of nodes. The 0D nodes can be used for rainfall runoff inflow and dry weather flow. In the rainfall runoff process various types of paved and unpaved areas, such as streets, roofs and parking lots can be simulated (see :ref:`inflow`). Detailed infiltration as a time-dependent process following the HORTON equation is also available.

Schematization
^^^^^^^^^^^^^^

Basically, a sewer network is built of manholes and sewer pipes. Each manhole is represented as a node, and each node has x,y,z coordinates. The sewer pipes are defined by a begin and an end node. Any number of sewer pipes can be connected to a manhole node. Lateral inflow and outflows are located on the manhole nodes. In the computational core, a volume and water level is computed at each manhole node. Thereby the volume of each manhole and the connected sewer pipes is taken into account. In between two nodes a discharge is computed, based on the water levels and pipe characteristics.

.. figure:: image/b_sewerage_schematization.png
   :alt: b_sewerage_schematization

   Sewerage system schematization

.. _fig_sewerage_volume_flow:
.. figure:: image/b_sewerage_volume_flow.png
   :alt: b_sewerage_volume_flow

   Distribution of volume and flow in 3Di sewerage system

If the water level rises above the street level, as defined on each manhole, the water can be stored on the street, by defining storage above street level. Typically, a manhole has a storage area of 1 m2, and the street has a storage area of 100 m2. By defining street storage above the manholes, the water level rise is slowed down, by the increased storage volume. After the storm event, the water stored above the manhole is discharges by the sewer network.

.. figure:: image/b_sewerage_surface_storage.png
   :alt: b_sewerage_surface_storage

   Storage above manhole

A more refined approach is to link the manholes with a 2d terrain model. In that case, water is not only stored above the manholes, but it can also flow away to lower areas. This approach is preferred for cases with heavy rainfall where a considerable amount of water is discharges by overland flow.

Another possibility is to model the streets only by defining an open sewer pipe which represents the street profile. In that case a 1d model is used to represent street flow between manholes. Although this possibility exists, a 2d model terrain model is preferred for its accuracy.

