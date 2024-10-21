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

.. warning::

    You cannot add multiple laterals to a single node or cell if they have different substance concentrations. This will be resolved in the near future.

.. _decay_coefficient:

Decay coefficient
^^^^^^^^^^^^^^^^^

In 3Di, substances can decay by a constant decay rate. This constant decay rate is defined by the substance property *Decay coefficient* .

To introduce the concept of a constant decay rate, an idealised case is considered. Assume a basin without any spatial flow and no source or sink terms. In such case the transport equation reduces to:

.. math::

   \frac{\partial c}{\partial t} = -\mu c

where :math:`\mu \, [s^{-1}]` is the decay rate constant, :math:`c` is the concentration and :math:`t` is the time. In case there is an initial amount of a substance, it will decay exponentially over time. The solution for such a system is:

.. math::

   c(t) = A_i e^{\mu t}

In which :math:`A_i` depends on the initial conditions.

The figure below illustrates the effect of the decay coefficient on the concentration over time.

.. figure:: image/h_decay_terms.png
   :name:fig_decay_term
   :scale: 75%

   Decay of a substance concentration over time for different decay coefficients, and where :math:`A_i=100`. Dotted lines indicate the half-life.

.. note::
    Decay of substances is a complex biochemical process, governed by interactions between substances, and environmental conditions. If your aim is to model the full complexity of these processes, a constant decay rate may not be sufficient. 3Di results can be used as input for aquatic ecology or chemistry models that do include such complexity. In this way, you can combine the hydrodynamic accuracy of 3Di with a detailed handling of the processes specific to your application domain.

Half-life and decay rate
""""""""""""""""""""""""

Substance property databases often define the half-life of substances in water. The concept of half-life is related to constant decay rate and can be converted to it by a simple formula.

Figure :numref:`fig_decay_term` shows the results for various decay rate constants (:math:`\mu \, [s^{-1}]`). The dotted lines indicate the half-life period (:math:`t_{1/2}`) for :math:`\mu = 0.001 \, s^{-1}`. This is the time it takes to reduce the amount of substance to half. To determine a decay rate constant based on the half-life period, one can use:

.. math::

   \mu = \frac{\ln(2)}{t_{1/2}}

