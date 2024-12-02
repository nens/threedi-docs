.. _water_quality:

Water quality and the transport of substances
---------------------------------------------

3Di has a water quality and tracing module. It allows users to simulate the transport of substances throughout the model domain. 3Di focuses on the spreading of so-called *passive* substances, that do not affect the density of the water nor each other. 3Di can also calculate the decay and :ref:`diffusion` of substances.

- Substances can enter the model domain as concentrations in initial water, boundary conditions, laterals, rain, leakage, surface sources and sinks. This applies to the entire model domain (1D, 2D, and groundwater).

- Each forcing can contain concentrations of one or multiple substances

- The water quality module can also be used to trace water throughout the system. Water can then be labelled as a fraction or a percentage. 

- The :ref:`output of water quality simulations<wq_netcdf>` is in NetCDF format; the file has the same structure as hydrodynamic results (results_3di.nc).

- Some characteristics can be set per substance, these are introduced in the sections below.

.. warning::

    You cannot add multiple laterals to a single node or cell if they have different substance concentrations. This will be resolved in the near future.

.. todo:
    
	@Nici ik dacht dat hier eerst een algemener verhaal zou komen over Transport van substanties?

.. _diffusion:

Dispersion and diffusion
========================

.. todo::
    
    @Nici: in deze paragraaf worden heel veel coefficienten genoemd, maar het is denk ik moeilijk voor gebruikers hier uit te halen welke coefficient ze nou zelf kunnen invullen en hoe die voor hen heet, versus coefficienten die in deze redenering/opbouw een rol spelen of intern in het rekenhart worden gebruikt.

The transport of substances cannot be adequately described by considering the average flow only. Imagine adding a bit of lemonade to a glass of water. Even though there is no flow, it will spread throughout the glass. This spread is caused by the processes of dispersion and diffusion. There are subtle differences between (molecular) diffusivity and dispersion. The most important difference is the spatial scale on which they act. In some applications, these differences are important. However, when dealing with the simulation of transport of substances for environmental applications, the scales collapse to the scale of a computational cell. On this scale, what matters is the *cumulative* effect of these processes and generally a closure relation is used to account for this. 

.. todo::
    
	@Nici closure relation? wat is dat? de laatste zin van bovenstaande alinea vind ik sowieso wat cryptisch

A common approach to including these processes in the shallow water equations, is by using the concept of *horizontal eddy viscosity* (:math:`\nu`). It allows for the spreading of a substance due to flow on a smaller scale than the average flow. The eddy viscosity scales the fluid interior friction effect that allows for energy exchange to smaller and smaller scales. This spreading is related to Reynolds stresses and thereby relates, in this case, to concentration gradients. Such flow is gradient-driven, meaning there is a spatial gradient in concentration. The diffusivity is scaled with a coefficient associated with the transport term :math:`T_{diff}`, which for uniform diffusivity constants is given by:

.. math::

   T_{diff} = \frac{\partial}{\partial x} \left( \nu_x \frac{\partial c}{\partial x}\right) + 
              \frac{\partial}{\partial y} \left( \nu_y \frac{\partial c}{\partial y}\right) =
              \nu \frac{\partial^2 c}{\partial x^2} + \nu \frac{\partial^2 c }{\partial y^2} 

where :math:'c' is the concentration varying in an :math:`x,y`-space. The eddy viscosity is generally determined by calibration, because, in a numerical model, the grid resolution is a crucial factor determining the scales and processes captured. In principle, the eddy viscosity is proportional to the computational grid resolution (see [Saichenthur_2022]_). In order to give you an idea in the following table are some ranges listed.

.. todo:

    @Nici: is de diffusion coefficient hetzelfde als de horizontal eddy viscosity? En als het van de locatie afhangt, waarom geef je het dan op als eigenschap van de substance? 


Typical eddy viscosity values for various environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| **Environment**                              | **Typical Eddy Viscosity**        | **Description**                                                                                      |
+==============================================+===================================+======================================================================================================+
| Shallow Coastal Waters                       | 1 - 10 m\ :sup:`2` /s             | Moderate turbulence, shallow water near coasts.                                                      |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Rivers                                       | 0.1 - 1 m\ :sup:`2` /s            | Lower turbulence, confined river channels.                                                           |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Larger Rivers and Estuaries                  | 1 - 10 m\ :sup:`2` /s             | Moderate mixing, influenced by tidal action.                                                         |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Lakes and Reservoirs                         | 0.01 - 0.1 m\ :sup:`2` /s         | Still water bodies with low turbulence.                                                              |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Lakes (moderate winds)                       | 0.1 - 1 m\ :sup:`2` /s            | Presence of wind-induced turbulence.                                                                 |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Coastal Zones                                | 10 - 100 m\ :sup:`2` /s           | High turbulence in tidal flows and coastal currents.                                                 |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
| Numerical Model Calibration                  | Proportional to mesh size         | Often calibrated to mesh/grid size to control numerical stability.                                   |
|                                              | :math:`\Delta x^2`                |                                                                                                      |
+----------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+

Some more details why calibrating might be essential
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The numerical results of the transport equation are very sensitive to numerical diffusion, as there are limited sources of natural diffusion, at least not as dominant as they appear in applications suitable for the 2D (or 1D) shallow water equations. In 3Di, we aim to minimize these grid dependencies, but achieving this requires some understanding of numerical diffusion.

One can prove that the numerical error (:math:`E`) in solving such an advection equation is:

.. math::

   E=-\frac{u}{2}\frac{\partial^2 c}{\partial x^2}\left(u\Delta t-\Delta x\right)

This implies that the actual equation that is solved is:

.. math::

   \frac{\partial c}{\partial t}=-u\frac{\partial c}{\partial x}-\frac{u}{2}\left(u\Delta t-\Delta x\right)\frac{\partial^2 c}{\partial x^2}

Thus, the :math:`E` makes an advection-diffusion equation out of an advection equation, with a viscosity of:

.. math::

   \nu_{num} = -\frac{u}{2}\left(u\Delta t-\Delta x\right)

This diffusivity is solely related to the numerical schematisation, therefore it is referred to as the numerical diffusivity coefficient. This coefficient cannot be set by users, but 3Di guarantees it to be positive to ensure stability. Additionally, note that this numerical diffusivity coefficient scales with the grid resolution (:math:`\Delta x`) and the time step (:math:`\Delta t`). You can influence this numerical diffusion coefficient by setting the time step and the grid size.

.. todo::

    @Nici: zorgt een hogere diffusie coeeficient voor een snellere verspreiding van de stof? En zorgt een grotere time step en een grotere grid size voor een hogere numerical diffusion coefficient?

Considering physical diffusion, as initially introduced, an extra term is added in the transport equation. Users can set the eddy diffusion coefficient (:math:`\nu`) as shown in the table above. 3Di aims to avoid overestimating diffusive processes. The equation above shows the estimate of the numerical diffusion. Based on the amplitude of the numerical diffusion term, the local eddy diffusion coefficient :math:`\nu_l` is reduced. This results in the *effective local diffusivity coefficient*:

.. math::

   \nu_{l} = \text{MAX}[0,\nu-|u|]

The eddy diffusivity coefficient is set by users per substance. In cases where diffusion is the dominant process in flow behavior, this reduction has limited to no effect, but in dynamic flow situations with strong numerical diffusion, the diffusivity is kept within realistic limits, ensuring stability.



.. _decay_coefficient:

Decay coefficient
=================

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
   :name: fig_decay_term
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

