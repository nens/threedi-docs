.. _surface_flow:

2D Surface flow
================


The 2D surface flow is based on the 2D depth-averaged shallow water equations. These equations are based on the conservation of momentum. 3Di considers the various processes; inertia, advection, pressure and friction for computing the horizontal flow.

The methods that 3Di uses to deal with the flow in the 2D domain are thoroughly described and published in Stelling 2012 and in Volp et al. 2013.

 .. TODO: Extend

.. _flow_with_vegetation:

2D Surface flow with vegetation
===============================

Physics of flow through vegetated waterways and floodplains
-----------------------------------------------------------

Two key aspects of the vegetation formulation used in 3Di are important to understand well. First, how vegetation exerts a drag force on the flowing water and how this differs from shear stresses such as bottom friction. Secondly, the importance of high resolution variations of the flow due to the varying vegetation characteristics.

.. figure:: image/b_veggie_velocity_profile.png
    
    Vertical velocity profiles altered by vegetation.

The 3Di computational core solves a force balance for the momentum domains. Different types of forces act differently on a fluid. For example, gravity is a body force, whereas bottom friction is due to a shear stress acting on a surface. Bottom friction alters the vertical velocity profile to a profile that can be described by a logarithmic function. Vegetation exerts a drag force on the water throughout the vertical profile. This drag scales with a representative vertical plane. The drag applies to the whole vertical profile if the vegetation is emerging, or, to a part of the vertical profile if the vegetation is submerged.

Only few formulations describe the vegetation drag under both emerged and submerged conditions (Vargas-Luna 2015). However, for flooding conditions, high water forecast or tidal applications, it is crucial to be able to deal with these transitions. This is why 3Di uses the formulation of Baptist 2005, which uses the plant characteristics plant height, stem diameter, and stem density to determine the representative vertical plane.

The formulation assumes that the interaction between water and plants works one way only, i.e. the vegetation affects the flow, but the flow does not bend or otherwise affect the vegetation. This helps to limit the number of required input parameters; these types of effects may be accounted for in the drag coefficient.

Vegetation often has high spatial variability and it is important to capture this variability at a high level of detail, for various reasons. First of all, flow finds the route of least resistance. The patchiness of vegetation allows the water to find specific routes, allowing to fill up or drain certain areas much quicker than would be expected by uniform vegetation fields. Moreover, the variability in vegetation combined with the high variability of bottom elevation should be taken into account as well. Drag is determined by the vegetation height relative to the water level, not by the absolute vegetation height. This is illustrated in the figure below.

.. todo:: @Nici ik begrijp de laatste paar zinnen niet

Baptist 2005 describes the effect of the vegetated area on the flow as a shear stress that scales with the vertical plane (instead of with the horizontal plane as in bottom friction or wind shear). It is a function of the flow velocity and vegetation characteristics:

.. math::

   \tau_v = \frac{1}{2}C_D m D min[H_v, H]  \label{eq:veggie_drag_baptist} 
    
| In which: 
| :math:`U` , the velocity vector with :math:`(u,v)` the velocity components in :math:`x,y`-direction
| :math:`H` the water depth
| :math:`H_v` the relative vegetation height
| :math:`D` the stem diameter
| :math:`m` the number of stems per square meter 
| :math:`C_{DV}` The vegetation drag coefficient 


.. figure:: image/b_rekencel_veggie.png
    :scale: 80%

    A 3Di computational cell, including the subgrid bathymetry and the vegetation patches.

The final four parameters of the equation are all input parameters that are used for 2D flow with vegetation. These are described in detail in :ref:`vegetation_drag`. They can be defined as raster values and as global values. The parameters that describe the vegetation characteristics are defined at the subgrid resolution. The high resolution information is used in the computation of the drag in several ways. In the first place, to determine the correct vertical plane that enforces the drag, the vegetation height is combined with high resolution bathymetry information. This ensures that only the vegetation in the wet domain contributes to the force balance and that the correct vertical plane is defined. Moreover, knowing that the bathymetry and the drag significantly changes within a momentum domain, means that the velocity within such a domain varies as well. Based on this, an estimate is made of the high resolution velocity variation (similar to how this is implemented for bottom friction, see Volp et al. 2013. This formulation uses the vegetation characteristics, the bottom roughness and the bathymetry variations. This results in very accurate results, even when using coarse computational cells.

This formulation was deliberately chosen to be generally applicable to a large range of plant species, using a limited number of input parameters. It can be used for woody species (shrubs and trees) as well as herbaceous species (grasses, grains, reeds). The equation is applicable to both submerged and emergent vegetation, and transitions between these situations during the simulation. It does not apply not to free-floating plants.

Further details of the way 3Di calculates flow through vegetation will be described in a paper to be sumbitted to the Journal of Hydraulic Engineering.