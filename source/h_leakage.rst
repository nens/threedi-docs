.. _grwleakage:


Leakage
=========

We offer the possibility to define a bottom boundary condition for the subsurface domain. At this boundary condition, sources and sinks can be defined. There is a wide range of applications, as it can be used as the interaction with deeper groundwater layers, local pumping or evaporation. The formulation for leakage is therefore as general as possible.

Input
~~~~~~~~~~~~

The input for leakage is simple, it can be defined globally and with a raster to define a spatially varying values. The values can be positive or negative. Positive values are representing water going into the domain. The dimension of leakage is in *mm/day*. You can download the complete overview of tables that 3Di uses in the spatialite database :download:`here <pdf/database-overview.pdf>`. 

Output
~~~~~~~~~~~ 

Sources and sinks are defined in the cell centers. This yields also for leakage values. The fluxes per cell *[m\ :sup:`3`\ /s]* can be found in the result files and can be viewed using the Plugin. Note, that when the flow limits the extraction, the actual values are recorded in the result files. 
