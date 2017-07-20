Structures
============
UNDER CONSTRUCTION

Pumpstation
------------

Pumps can be an integral part of different water systems. Pumps are in place to move water from one location to another, usually to conquer elevation diffences. Some examples of this displacement function of pumps are:

* Polder pump: Water needs to be transported out of the polder to drain the area of excess water and keeps the polder dry. A pump transports the water from low lying canals in a polder system to the higher lying drainage canal through which it can be transported further.

* Sewer pump: In a sewer system  sewer water needs to be transported to a treatment plant. A pump in a sewer system moves the sewer water from the sewer system to the treatment plant.

**Implementation details**

In 3Di, the modeler can add pumps to a 1D channel and/or 1D sewer networks. There is no distinction made for pumps in sewer systems and channel networks, since their function is the same. Characteristics for the pump, as needed for a specific water system, can be set by configuring attributes of the pumps. The attributes specify at which water levels the pump starts moving water from one node to the other and what the discharge is. The pump characteristics that can be specified in a 3Di schematisation are:

* Capacity: Maximum discharge for which the pump is able to displace water from the suction node to the delivery node.
* Start level: Water level for which the pump will be turned on.
* Lower stop level: Water level beneath start level for which the pump will be turned off.
* Upper stop level: Water level above start level for which the pump will be turned off.
* Type: Parameter to set whether start and stop levels are measured at suction side or delivery side of the pump.
* Furthermore, there are two methods to add a pump in a 3Di:
* Pump between two nodes: A pump between two nodes moves water from the  node at suction side to the node at delivery side with the specified pump capacity. Depending on the type of pump the suction side or delivery side water levels determine the activity of the pump.
* End pump:  For an end pump only the suction side node needs to be specified. With no delivery side all water being moved by this pumped is taken out of the model. All water pumped from the model is specified in the flow_summary.log as contribution to the global water balance. The pump characteristics to be specified are the same as for a pump type with start/stop levels at suction side. Since no delivery side node is present, it is not possible to specify a pump type with start stop level at delivery side.

**Technical description**

UNDER CONSTRUCTION


Weir
------------

Culvert
------------

Orifice
------------
