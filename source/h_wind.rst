.. _wind_effects:

Wind effects  
------------------------------------

The water levels and the flow velocities can be influenced by the wind. The extent to which this happens depends on the wind force that exerts on the water surface. Historical, actual and forecasts wind data are available from the meteorological institutes. Wind speed and wind force can vary in space and in time. It is possible to take both the spatial and temporal variations into account in 3Di. In addition, it is possible to take local shield factor into account, caused by buildings or trees.  

Wind input data
===============

The standard wind data gives the speed and direction of the wind at a height of 10 m. In order to determine what force the wind actually exerts on the water surface, this information must be adapted to local conditions on the water surface. In the first approach, the vertical wind profile can be described with a logarithmic profile:

.. math::
   :label: vertical wind profile

   u_{wind}(z,t) = \frac{u^*}{\kappa} log( \frac{z}{z_0} )

| In which: 
| u\ :sub:`wind`\ = wind speed at level z, 
| u\ :sup:`*`\ = resistance speed, 
| κ = von Karmen constant and 
| z\ :sub:`0`\ = roughness height.


Drag coefficient
================

The drag-coefficient translates the wind speed on a 10 m elevation to the speed on the ground. The value is 0.005 by default, but can be defined by the user. At present this factor is global factor for the entire model, but in the future this factor could be defined as a spatial field on basis of land use maps and digital elevation models (DEM).

.. figure:: image/b_wind_vertical_profile.png
   :alt: Vertical wind profile

   Vertical wind profile

Wind shield factor
==================

The water surface can be located behind a row of trees, or below the bank level of the channel. This local variation of the wind depends on the wind direction with respect to the orientation of the obstacles and the orientation of the channel. 

.. figure:: image/b_wind_local_circumstances.png
   :alt: Local circumstances can have a high impact on the wind force

   Local circumstances can have a high impact on the wind force 

To take these local circumstance into account a wind shield factor is introduced for 1D open-channels. In the 2D domain it is not possible to use the wind shield factor. The wind shield factor varies between 0 and 1 to scale down the wind speed. A value of 0 means that there is no wind and a value of 1 means no reduction. The wind shield factor is defined in 8 spatial directions. In between a linear interpolation of the value is made. The wind shield factor is defined for each 1D schematization element. If no factor is defined, a factor of 1 is assumed by default.

.. figure:: image/b_wind_shield_directions.png
   :alt: The wind shield factor is defined in 8 directions

   The wind shield factor is defined in 8 directions

Wind set-up 
===========
The impact of wind on water levels and flow velocities can be made clear by looking at the balance of forces on a liquid particle. It is important to note that gravity is a force that works on the entire volume, whereas the friction and the wind forces work on a surface. This implies that the wind has more impact on a thin layer of water than a deep layer of water. 

.. figure:: image/b_wind_force_balance.png
   :alt: Force balance with gravity (blue), friction (green) and wind (red)

   Force balance with gravity (blue), friction (green) and wind (red)

If we take into account gravity, friction and wind forces, the equation looks like this:

.. math::
   :label: wind set-up equation

   \frac{d(Hu)}{dt} = -gH \frac{\delta \zeta}{\delta x} - \frac{\tau _{friction}}{\rho} + \frac{\tau_w}{\rho}

| In which: 
| u = flow velocity, 
| H = water depth, 
| ζ = water level, 
| ρ = density of water, 
| τ\ :sub:`friction`\ = friction shear stress and 
| τ\ :sub:`w`\ = wind shear stress.


The shear stresses are dependent on the local velocity of water and wind. The wind shear stress is described by:

.. math::
   :label: wind shear stress

   \tau_w = - \rho_a C_w L \left | u_{wind} \right | u_{wind}^{//}

| In which: 
| ρ\ :sub:`a`\ = density of the air, 
| C\ :sub:`w`\ = drag-coefficient of the wind, 
| L = Local wind shield factor, 
| \|u\ :sub:`wind`\| = wind speed and 
| u\ :sub:`wind`\ \ :sup:`//`\ = wind speed in the channel direction. 


- The drag-coefficient translates the wind speed on a 10 m elevation to the speed on the ground.

- The local wind shield factor is defined by the user. 

- The wind speed in the direction of the 1D channel is computed by 3Di on basis of the geo orientation of the 1d channel network.

In summary, the wind forcing is formulated by:

.. math::
   :label: wind forcing

   \tau_w = \rho_{lucht}\iint \chi^2 C_w L \left \| \frac{u_{wind}}{\chi} - u \right \| \left ( \frac{u_{wind}^{//}}{\chi} - u \right ) d \Omega

The wind forcing is determined over the total area of the calculation domain (Ω). In addition, we look at the relative speed of the wind in relation to the speed of the water. On thin water layers, such as in case of a flood, the wind has a lot of influence on the velocity of the water. However, the speed of the water is limited by its critical velocity. Other processes such as waves and foaming will then dominate and remove energy from the system (as it is no longer converted into speed). These waves are not included in the 3Di model. The factor χ overcomes this limitation. This factor is important for the stability of the model, especially when the wind works on very shallow water layers.

In the 2D domain the impact of wind is formulated by:


.. math::
   :label: wind impact 2D

   \frac{d u}{dt}+g\frac{\partial \zeta}{\partial x} = -\frac{|u|u}{H_f}+\frac{\rho_{lucht}}{\rho_{water}V} \iint \chi^2 C_d \left \| \frac{U_{wind}^x}{\chi} - u \right \| \left ( \frac{U_{wind}^{x}}{\chi} - u \right ) d \Omega^x 

   \frac{dv}{dt}+g\frac{\partial \zeta}{\partial y} = -\frac{|u|v}{H_f}+\frac{\rho_{lucht}}{\rho_{water}V} \iint \chi^2 C_d \left \| \frac{U_{wind}^y}{\chi} - v \right \| \left ( \frac{U_{wind}^{y}}{\chi} - v \right ) d \Omega^y 

| The additional variables (in comparison tot 1D are): 
| u,v = velocity of the water in x- en y –direction, 
| \|u\| = absolute velocity of the water, 
| H\ :sub:`f`\ = Friction depth on basis of subgrids, 
| U\ :sub:`wind`\ \ :sup:`x`\, U\ :sub:`wind`\ \ :sup:`y`\ = wind component in x- and y- direction and 
| Ω\ :sup:`x`\, Ω\ :sup:`y`\ = Domain of the impulse balance in x- en y- direction.


Important to know
================= 

- At present wind input fields are uniform in space.
- The drag coefficient can only be set via the API.
- In 1D, wind has no impact on closed open channel profiles and sewer pipes. 
- If a 1D element has both an open and a closed profile, we assume no wind impact. If the user wants to compute the impact of wind in this case, separate 1D elements should be used. 

