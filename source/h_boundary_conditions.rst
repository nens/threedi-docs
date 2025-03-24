.. _boundary_conditions:

Open boundary conditions
========================

At open boundaries, one needs to define the conditions beyond the boundary of the model. This will allow water to flow into or out of the model domain. These conditions can of course change during the course of a simulation. Therefore, one defines a boundary condition type and, a time varying value. Boundary conditions are generally defined far away of the region of interest, as one wants to study the natural flow, and not the behaviour of the boundary conditions. It is important to choose the location of a boundary condition carefully. Locations, where the flow and the bathymetry is simple and predictable, generally give better results. In addtion, be careful grid resolution transistions at the boundary location. Especially, for the water level and discharge boundaries, because for those types, the boundary cells are treated independent of its resolution.

Domains
-------

Boundary conditions need to be defined at the open boundaries in the 1D, 2D surface and 2D groundwater domain. In case no boundaries are defined, 3Di it is a closed boundarie, which means that there cannot flow water in or out.

Types
-----

There are various types of boundaries, which define the in- and outgoing discharges. 3Di supports the following boundary types:

* Water level, this type defines the water level and enforces water to flow in or out of the domain to based on this condition. 

* Velocity, this type prescribes the flow velocity at the boundary location. Depending on the local depth at the boundary, the in- or out-going flux is defined. Take care of the sign of the value, as the sign of the velocity determines its flow direction. 

* Discharge, this type prescribes the discharge, it defines the flux in/out of the model domain. Generally, this is the boundary condition type one uses for upstream boundaries. Keep in mind the sign of the value, as it is linked to the flow direction. Note, that this value is defined for each boundary flow line in all model domains. However, concerning the 2D (surface and groundwater domains), the total incoming discharge is the sum of the discharge over all boundary flow lines. For 2D boundary cells, it is advised to use the Total discharge boundary type, which is explained below.

* Water level gradient (Sommerfeld boundary), this type prescribes the water level gradient at the boundary. This will try to get the system to an equilibrium condition. Use this boundary condition, when one expects a system that is in (near) equilibrium state.

* Total discharge, a user can define the total discharge for a boundary in one of the 2D domains (surface and groundwater). 3Di will distribute the total discharge over the boundary cells. For 2D surface water, the distribution of the discharge over the full edge is based on a so-called conveyance approach. It uses information of the wet area, roughness, and vegetation of the cell. When an interflow layer is present in the model, the distribution is also depending on the wet area and hydraulic conductivity there. In case of a groundwater boundary condition, the distribution of the discharge is based on the wet area and hydraulic conductivity.  


Time series
-----------

For each boundary condition, a time series for the chosen variable needs to be defined. The model cannot be run if one or more boundary conditions do not have a time series specified.

To use a constant value for a boundary condition, you will have to define the same value for each time step in the time series.


