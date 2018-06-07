.. _cons_volume:

Conservation of mass
========================

To capture or predict flow under varying conditions, one is often forced to use the computational power of computers. Since the introduction of computers various methods have been introduced and improved. Some aspects are true for all types of methods. Here, we will limit ourselves to the methods used in the computational core of 3Di.

3Di is a two-layer, subgrid based hydrodynamical model, where a surface and a sub-surface layer can be defined. In these layers, flow is computed based on the depth-averaged equations. In addition, 3Di offers the possibility to add a 1D network to the system as well. Independent of the flow being in the 1D, 2D surface or 2D subsurface domain can be described by a consistent set of equations. These are based on two fundamental laws of physics; i) Conservation of mass and ii) Conservation of momentum. In this section we will describe how we deal with conservation of mass in combination with the so-called subgrid method.


Conservation of mass states that mass cannot disappear or appear in a certain domain without clear source. For a defined domain, when all fluxes (discharges) in and out of that domain are known, the change in mass can be computed. Conservation of mass can be described mathematically as:

.. math::
   :label: mass_conservation    

   \frac{\Delta \rho V}{\Delta t}=\sum_i^{in} \rho_i Q_i -\sum_k^{out} \rho_k Q_k + \sum_i \rho_j S_j 

| In which: 
| :math:`\rho` is the density, 
| :math:`V_\Omega` is the volume, 
| :math:`Q` is a discharge and 
| :math:`S` is a sink or source term. 


The counters i, j, k count over all existing discharges, sink and source terms. In 3Di we do not account for density variations, so the density :math:`\rho` is assumed uniform and constant. This simplifies the equation for conservation of mass, to the following equation for conservation of volume:

.. math::
   :label: volume_conservation    
   
   \frac{\Delta V}{\Delta t}=\sum_i^{in} Q_i -\sum_k^{out} Q_k + \sum_i S_j 

It is important to define the domain for which this is true. In the finite volume approach, used in 3Di, a volume domain equals a computational cell, i.e. the water level domain. For such a domain, as shown in the Figure below, all discharges (in blue) sources and sink terms (in yellow) entering and leaving the box are to be determined. The discharges are computed based on the momentum equations. The next sections :ref:`flow2d`, :ref:`flow1d`, :ref:`interflow` and in :ref:`groundwater` elaborate about the computation of flow. Sources and sink terms are general terms for water that is added or extracted in a domain. Examples of such are :ref:`simpleinfiltration` and :ref:`rain`. In 3Di, the conservation of volume is where all flow parameters are combined. This is independent whether flow originates from the 1D, 2D surface or subsurface domain. 

.. figure:: image/b1_2.png
   :scale: 30%
   :alt: virtual_conservation_box
   :align: right

   
   A virtual box for conservation of mass.








