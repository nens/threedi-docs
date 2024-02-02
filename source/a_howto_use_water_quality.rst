.. _howto_use_water_quality:

Use water quality
=================

3Di can be used in water quality assessments. More specifically, you can introduce concentrations of substances to the simulation, and compute how these substances spread through the water system due to advective forces and (numerical) diffusion. See :ref:`water_quality`.

Running water quality simulations
---------------------------------

Simulations with water quality can be run with any 3Di model. You do not need to make any changes to the model schematisation.

It involves the following steps:

- Define one or more substances that you want to use in the simulation, e.g. "Benzene hexachloride", "Biological Oxygen Demand (BOD)", or "Contaminant".

.. note:
	
	All substances must be defined at the start of the simulation (the substances themselves, not their concentrations). You cannot define new substances while the simulation is already running. 

- If the simulation includes initial water (in the 1D and/or 2D domain), you may set an initial concentration of the substance(s) you have defined in the initial water.

- If the simulation includes forcings, such as rain, boundary conditions, or laterals, you may add a concentration of the substance(s) you have defined to these forcings. Each forcing can contain concentrations of multiple substances at the same time.

.. note:: 
    The way substance concentrations are defined, mirrors the way that the initials or forcings are defined. I.e., 2D initial water levels are supplied as a raster, so 2D initial substance concentrations are also supplied as a raster; substance concentrations in time series rain is also provided as a time series; et cetera.

- Run the simulation in the same way as you are used to

- Currently, there is not yet a graphical user interface for adding substances to simulations. Use the :ref:`a_api` to use this functionality.

Viewing and analysing water quality results
-------------------------------------------

The results of a water quality simulation are the concentrations of each substance at each node, for each output time step. These values are written to a :ref:`separate NetCDF file<wq_netcdf>`.

You can visualise these concentrations by plotting a graph of the concentration of a substance at specific locations over time. Or you can generate a map of the substance concentrations at a specific moment in time, e.g. by scaling the color of the nodes or cells by their concentration.

Currently, there is not yet a graphical user interface for visualising water quality results. Use :ref:`threedigrid` to do this.

A summary of the water quality calculations is available in the simulation logging. This :ref:`log file<wq_logging>` includes a substance summary, similar to the flow summary.
