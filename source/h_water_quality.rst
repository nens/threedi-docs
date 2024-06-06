.. _water_quality:

Water quality
-------------

3Di has a module that can be used for water quality calculations. More specifically, you can introduce concentrations of substances to the simulation, and compute how these substances spread through the water system due to advective forces and (numerical) diffusion.

- Substances can enter the model domain as concentrations in initial water, boundary conditions, laterals, rain, leakage, surface sources and sinks. This applies to the entire model domain (1D, 2D, and groundwater).

- Each forcing can contain concentrations of one or multiple substances

- Units can be defined for each substance

- A decay coefficient (s\ :sup:`-1`) can be defined for each substance. If the decay coefficient is specified, the substance decreases at a rate that is proportional to the current concentration; the substance will decay exponentially in time. The decay coefficient is inversely proportional to a so-called mean lifetime (T). The decay coefficient is defined as 

.. math::
   :label: Decay coefficient

   C_{decay} = frac{1}{T}

| where: 
| :math:`T`: mean lifetime in seconds

- The :ref:`output of water quality simulations<wq_netcdf>` is in NetCDF format; the file has the same structure as hydrodynamic results (results_3di.nc).

.. warning::

	You cannot add multiple laterals to a single node or cell if they have different substance concentrations

