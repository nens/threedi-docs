.. _structures:

1D flow over structures
=======================

Structures are an integral part of water systems. Structures control the behaviour of a water system, therefore it is crucial to take the into account. 3Di recognises various types of structures, like pumps, weirs, orifices and culverts. To guarantee the structures are implemented in your 3Di model, structures are defined as connections between two computational nodes, similar to channels and pipes. The sections below give an overview of the structures available in 3Di. Moreover, structures can be controled. This means that they can be adjusted based on the simulation results. This can be done using the in 3Di implemented control functions (ref) or by controls designed by the user via the 3Di API (ref).

.. _pump:

Pump station
------------

Pumps drain water from a certain location to another location within or outside the model domain. In 3Di, users can add pumps to a schematisation via a 1D connection node. Characteristics for pumps can be set by configuring the attributes. The attributes specify the start and stop levels of the pump and the pump capacity.

The computational core can only drain water that is actually there. To avoid timestep reductions and/or continuously switching on and off of the pump, the user can request the computational core to adjust the capacity slightly for smooth computations. Than it depends on the downstream supply. The implicit ratio for pumps can be set in the numerical settings. 

.. figure:: image/b_structures_pump.png
   :alt: structures_pump
     
   Schematic display of a pump function

The pump characteristics:

* Capacity: Maximum discharge for which the pump is able to displace water from the suction node to the delivery node.

* Start level: Water level for which the pump is switched on.

* Lower stop level: Water level for which the pump will be switched off. This level should be below the start level.

* Upper stop level: Water level for which the pump is switched off. This is an optional value, and is always higher that the start level.

* Type: Parameter to set whether start and stop levels are defined at suction side or delivery side of the pump.

Furthermore, there are two methods to add a pump in a 3Di:

1. *Pump between two nodes*: A pump between two nodes drains water from the  node at suction side to the node at delivery side with the specified pump capacity. Depending on the type of pump the suction side or delivery side water levels determine the activity of the pump.

2. *End pump*:  For an end pump only the suction side node needs to be specified. With no node defined for the delivery side, all water being drained by this pump. All water pumped from the model is specified in the flow_summary.log as contribution to the global water balance. The pump characteristics to be specified are the same as for a pump type with start/stop levels at suction side. Since no delivery side node is present, it is not possible to specify a pump type with start stop level at delivery side.


.. _weir:

Weirs and Orifices
------------------

Weirs are used to maintain the water level in drainage level areas of act as threshold for sewerage water overflowing into storage basins or surface water. Again, there is no distinction between these types of usages in 3Di. The location of the weir determines the its function. The main weir characteristics that can be specified in 3Di are:

* Crest level: The threshold level or height of the weir.

* Crest type: Selects a short or long crested weir formulation.

* Discharge coefficient: The coefficient used in the weir discharge formulation.

* Cross_section_definition: For the shape and size of the weir you must define a cross section definition.

The short crested weir can be submerged or emerged. If the weir is emerged water flows over the crest freely, the downstream flow conditions have no influence on the amount of water that flows over the crest. If the weir is submerged the downstream water level approaches the crest level and affects the flow over the crest. The transition between these states in smoothed for a stable computation. The figures below illustrate these two states.

.. figure:: image/b_structures_weir_short.png
   :alt: structures_weir_short
     
   Illustration of short crested weir in two states. Emerged and Submerged. The formulas shown are used in 3Di to compute the discharge over the weir, in which a stands for the discharge coefficient.

The long crested weir uses the conservation of mass and energy equations to compute discharge. It uses the weir friction given by the user and the actual length between the connection nodes. The figure below illustrates the long crested weir.


.. figure:: image/b_structures_weir_long.png
   :alt: structures_weir_long
     
   Illustration of long crested weir.


.. _culvert:

Culvert
-------

Orifices are used in sewerage to limit flow or can be used to model a bridge or culvert. The separate culvert table differs from orifices in the way the flow is calculated. Culverts are closely related to pipes in this sense. The Culvert table can be used for longer sections of pipe-like structures and may be curved. Shorter, straight culverts are best modeled as an orrifice. An orrifice is treated as a weir to allow for larger time steps. 

For culverts and orifices, the energy loss caused by the change in flow velocity at the in- and outlet are accounted for by 3Di. The discharge coefficients for orifices can be used to account for any additional energy loss. 

The input parameters for orifices are similar to those for weirs, specified in the section above. Culverts use invert levels at the start and end instead of the crest level in weirs and orifices. The input parameters are all described in the spatialite database :download:`here <pdf/database-overview.pdf>`.


Control on structures is described in a separate section: :ref:`control_structures`.
