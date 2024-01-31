.. _water_quality:

Water quality
-------------

3Di has a module that can be used for water quality calculations. More specifically, you can introduce concentrations of substances to the simulation, and compute how these substances spread through the water system due to advective forces and (numerical) diffusion.

- Substances can enter the model domain as concentrations in initial water, boundary conditions, laterals, rain, leakage, surface sources and sinks. This applies to the entire model domain (1D, 2D, and groundwater).

- Each forcing can contain concentrations of multiple substances at the same time

- The :ref:`output of water quality simulations<wq_netcdf>` is in NetCDF format; the file has the same structure as hydrodynamic results (results_3di.nc).

.. warning::

	You cannot add multiple laterals to a single node or cell if they have different substance concentrations

