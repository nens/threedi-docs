.. _water_quality:

Water quality
-------------

3Di has a module that can be used for water quality calculations. More specifically, you can introduce substances to the simulation, and compute how these substances spread through the water system due to advective forces and  diffusion.

- Substances can enter the model domain as concentrations in initial water, boundary conditions, laterals, rain, leakage, surface sources and sinks. This applies to the entire model domain (1D, 2D, and groundwater).

- Each forcing can contain concentrations of one or multiple substances

- Units can be defined for each substance

- The water quality module can also be used to trace water throughout the system. Water can then be labelled as a fraction or a percentage. 

- The :ref:`output of water quality simulations<wq_netcdf>` is in NetCDF format; the file has the same structure as hydrodynamic results (results_3di.nc).

- Some characteristics can be set per substance, these are introduced in the sections below.

Decay rate constant
~~~~~~~~~~~~~~~~~~~~
.. _adding_decay_term:

Modelling accurately the decay of a substance  is highly complex. This is mainly due to the dependence on environmental conditions that are often unknown, interact with each other, and rely strongly on empirical relations. To keep it simple, 3Di supports only a constant decay rate. Results can be refined through external scripting to meet specific needs.

.. figure:: image/h_decay_terms.png
   :scale: 55%
   :align: center

   Decay of a substance fraction over time for different decay rate constants, and where :math:`A_i=100`. Dotted lines indicate the concept of half life periods.

To introduce the concept of a constant decay rate, an idealised case is considered. Assume a basin without any spatial flow and no source or sink terms, in such case the transport equation reduces to:

.. math::

   \frac{\partial c}{\partial t} = -\mu c

where :math:`\mu \, [s^{-1}]` is the decay rate constant, :math:`c` is the concentration and :math:`t` is the time. In case there is an initial amount of a substance, it will decay exponentially over time. The solution for such a system is:

.. math::

   c(t) = A_i e^{\mu t}

In which :math:`A_i` depends on the initial conditions. 
Figure :numref:`fig:decay_term` shows the results for various decay rate constants (:math:`\mu \, [s^{-1}]`). The dotted lines indicate the half-life period (:math:`t_{1/2}`) for :math:`\mu = 0.001 \, s^{-1}`. This is time it takes to reduce the amount of substance with a factor two. The half-life periods of the other decay rate constants are listed in :numref:`tab:mu`. The decay rate constant and half-life period can be converted:

.. math::

   t_{1/2} = \frac{\ln(2)}{\mu}


.. table:: Overview of decay rate constants and their half-life periods. 
   :name: tab:mu
   :align: center
   :widths: auto

   ====================  ===================
   :math:`\mu [s^{-1}]`  :math:`t_{1/2} [s]`   
   ====================  ===================
   0.000001              693147.18
   0.00001               69314.718
   0.0001                6931.4718
   **0.001**             **693.14718**
   0.01                  69.314718
   0.1                   6.9314718
   ====================  ===================


.. warning::

	You cannot add multiple laterals to a single node or cell if they have different substance concentrations. This will be resolved in the near future.

