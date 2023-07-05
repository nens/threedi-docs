.. _boundary_condtions:

Boundary conditions
===================

Boundary conditions define the conditions beyond the boundary of the model and allow water to flow into or out of the model domain.

Domains
-------

Boundary conditions can be used for 1D flow, 2D surface flow and 2D groundwater flow.

Types
-----

A boundary condition must define one variable, so that the computational core can calculate the flow based on the values of the neighbouring node or flowline. You can define one of the following variables in a boundary condition:

* Water level

* Flow velocity

* Discharge

* Water level gradient (Sommerfeld boundary)

Time series
-----------

For each boundary condition, a time series for the chosen variable needs to be defined. The model cannot be run if one or more boundary conditions do not have a time series specified.

To use a constant value for a boundary condition, you will have to define the same value for each time step in the time series.


