.. _breach_flow:

Breach flow
------------

In a 3Di model, flow may occur between 1D and 2D elements. In certain cases this exchange is limited by a levee. The exchange height is determined by the height of the levee. When a few extra properties of the levee are specified for these connections, a breach can be modelled that can grow over time. More information on levees, can be found in :ref:`obstacles`


Exchange formulation
++++++++++++++++++++++++

The flow between 1D and 2D at the breach is computed based on a simplified momentum balance. A balance is made between the friction and the forcing. Note, that the volume in the breach is neglected.

More details on how to use obstacles, levees and breaches can be found in :ref:`flood_model`.
