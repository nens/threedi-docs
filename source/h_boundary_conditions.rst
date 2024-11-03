.. _boundary_conditions:

Boundary conditions
===================

Boundary conditions define the conditions beyond the boundary of the model and allow water to flow into or out of the model domain.

Domains
-------

Boundary conditions can be used for 1D flow, 2D surface flow and 2D groundwater flow.

Types
-----

A boundary condition must define one variable, so that the computational core can calculate the flow based on the values of the neighbouring node or flowline. You can define one of the following variables in a boundary condition:

* Water level, a user defines a water level (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface and groundwater domains).

* Flow velocity, a user defines the flow velocity (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface).

* Discharge, a user defines the discharge (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface and groundwater domains). Please note, the total amount of water is the sum of the discharge over all boundary flow lines.

* Water level gradient (Sommerfeld boundary)

* Total discharge, a user defines the total discharge for a flowpath in 2D domain (surface and groundwater layers). 3Di will then distribute the total discharge to the boundary cells that fall within the cross-section of the flowpath depending on the resistance of each cell to the flow. This resistance depends on the wet area, friction, and vegetation of the cell for surface water, and wet area and hydraulic conductivity of the cell if interflow is included. For the ground water layer, the distribution of the discharge is determined based on the wet area and hydraulic conductivity of the soil for each cell. 

Note: In case of using different refinement levels at the boundary of the domain, the user should be aware of the difference in water level gradient for boundary type Water level. This stems from the cell size difference that might lead to different gradient, more notably in steep areas.

Time series
-----------

For each boundary condition, a time series for the chosen variable needs to be defined. The model cannot be run if one or more boundary conditions do not have a time series specified.

To use a constant value for a boundary condition, you will have to define the same value for each time step in the time series.


