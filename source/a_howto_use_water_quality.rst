.. _howto_use_water_quality:


Water quality
=============

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

Water quality simulations in the 3Di Modeller Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The water quality module can be used in simulations started from the 3Di Modeller Interface. 

At the moment, the simulation wizard supports adding substances to initial water, boundary conditions, and laterals. 

Follow the :ref:`same workflow as for starting any other simulation <simulate_api_qgis>`, with the following additional steps.

#. On the scenario options page that is shown before the simulation wizard starts, check the box *Include substances*
#. After having filled in the *Name* and *Duration* pages, the :ref:`simulation_wizard_substances` page lets you define the substances that you want to use in the simulation.
#. If you want to add substance concentrations to initial water, specify the initial water inputs on the *Initial conditions* page, scroll down to the *Substances* header and choose your initial concentration inputs.
#. If you want to add substance concentrations to laterals, go to the :ref:`simulate_api_qgis_laterals` page, upload a CSV for 1D or 2D laterals and a :ref:`CSV with time series of concentrations <laterals_substance_concentrations>` for each of the substances that you want to add to your simulations.
#. If you want to add substance concentrations to boundary conditions, specify the boundary conditions you want to use on the *Boundary conditions* page (you can also use what is already in the simulation template), scroll down to the *Substances* header and choose your initial concentration inputs.
#. Go through the rest of the steps of the simulation wizard to start the simulation

Water quality simulations using the 3Di API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to use water quality features that are not yet supported in the 3Di Modeller Interface, you can use the :ref:`a_api` directly. Contact the :ref:`servicedesk` for example scripts that fit your specific purpose.


Viewing and analysing water quality results
-------------------------------------------

The results of a water quality simulation are the concentrations of each substance at each node, for each output time step. These values are written to a :ref:`separate NetCDF file<wq_netcdf>`.

A summary of the water quality calculations is available in the simulation logging. This :ref:`log file<wq_logging>` includes a substance summary, similar to the flow summary.

At the moment, the :ref:`time_series_plotter` is the 3Di Results Analysis tool with support for the 3Di water quality module.

#. :ref:`Download the simulation results <dl_via_models_simulations>` via the 3Di Models & Simulations panel. The :ref:`wq_netcdf` file will also be downloaded.
#. Load the results using the :ref:`3Di Results Manager<3di_results_manager>`
#. Open the :ref:`time_series_plotter`
#. Add one or more nodes to the plot
#. In the *Variable* dropdown menu in the Time series plotter, select the substance you want to see the concentration for.

For other visualisations of substance concentrations, e.g. as a map of the substance concentrations at a specific moment in time, or an animation of such maps, use :ref:`threedigrid`. Contact the :ref:`servicedesk` for example scripts that fit your specific purpose.
