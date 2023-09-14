.. _boundary_conditions:

Boundary conditions
===================

Boundary conditions define the conditions beyond the boundary of the model and allow water to flow into or out of the model domain.

Domains
-------

Boundary conditions can be used for 1D flow, 2D surface flow and 2D groundwater flow.

Types
-----

A boundary condition must define one variable, so that the computational core can calculate the flow based on the values of the neighbouring node or flow-line. You can define one of the following variables in a boundary condition:

* Water level, a user defines a water level (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface and groundwater domains).

* Flow velocity, a user defines the flow velocity (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface).

* Discharge, a user defines the discharge (time series). This value is fixed at the boundary cell (1D domain) or for all cells along the boundary (2D surface and groundwater domains). Please note, the total amount of water is the sum of the discharge over all boundary flow lines.

* Water level gradient (Sommerfeld boundary)



Time series
-----------

For each boundary condition, a time series for the chosen variable needs to be defined. The model cannot be run if one or more boundary conditions do not have a time series specified.

To use a constant value for a boundary condition, you will have to define the same value for each time step in the time series.


