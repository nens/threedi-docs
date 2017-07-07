Numerics
==================

UNDER CONSTRUCTION

There are various numerical settings that can either improve the solution under certain conditions, and some can speed up the computations and others will improve the stability. The various options are here explained.

Nummerical Settings
-------------------

Preissman slot
^^^^^^^^^^^^^^

[preissmann_slot ] (default= 0.0 m^2)

A preissmann slot is often used to model flows in  pipes. When the pipes are not completely filled, such flows can be modelled as free surface flows. However, when the discharges increase, the pipes are filled and the flow can become pressurized.  Not all hyrdodynamic models are suited for these kind of flows. Therefore, to mimic the effects of pressurized flows, the water level can be allowed to rise higher than the upper limit of the cross section.  In order to allow this, a narrow tube is added on top of the pipe (Figure 2). These tubes are generally quite narrow to allow the water level to rise, at a minimum cost of extra added volume. In 3Di this is not necessary, however it can be added to circular tubes. This can increase the stability at larger time steps. The way flow is computed in pipes is described here.

(To add, test results flow with and without preissman slot.)

.. figure:: image/preissmanslots_schematisch.png
   :alt: Preissman slot

   Upper Panel) Flow through a half emtpty pipe. 
   Middle Panel) Pressurized flow through a pipe with a preissman slot. 
   Lower Panel) Pressurized flowtrhough a pipe with a virtual water level (red).


Integration method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[integration_method] (default=0)

There are various ways to discretize equation. At the moment only first order semi implicit is supported and tested. 


Settings for Matrix solvers 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are several methods available to solve the matrix consisting of the unknown water levels. Depending on the application, these settings can speed up the simulation or make the solutions more accurate. As 3Di uses the so-called subgrid method, the system of equations becomes a weakly non-linear system. Therefore, we need the use of a Newton iteration method in combination with matrix solvers in  order to actually solve this system of equations. The so-called nested-Newton method is needed when the application consists of closed profiles.

**The settings that belong to the Newton iteration are:**

[max_nonlin_iterations] (default = 20), [convergence_eps] (default = 1.0^-5), [use_of_nested_newton] (no default) 

Maximum number of non lineair iterations (max_nonlin_iterations) is the number the computational core will try to reach the convergence value of the Newton iteration. In cases where is extensive flooding and drying of areas, this number can be raised as it might need more iterations to find the correct solution.  The Newton iteration needs a value that defines convergence. Initially, 3Di requires a much lower value, but in case the system has difficulties with finding a solution, it will loosen this requirement with a maximum of the by the user set convergence_eps. 

Nested newton iterations are needed in case profiles in 1D are narrowing with height. Mathematically, in case d^2V/d\zeta^2<0. This occurs, for example, a lot in sewer systems. For these cases, the Newton iteration method does not guarantee a solution, so the system is split in two systems that do guarantee a solution. In case 3Di cannot find a solution it will always try, whether it can find a solution using the nested Newton method. However, in case one has an application that consists of many of these profiles it is faster to tel the system that it should always used the nested Newton method (use_of_nested_newton).

**Maximum Degree**

[max_degree](no default)

One of the methods to solve a matrix is by Gauss-Jordan elimination, substitution. Depending on the type of network, either 1D, 2D or 1D with many bifurcations or combination of those, this method is very efficient or not. It is also possible to solve parts of the system using this method and others with the other method.  The efficiency of the solver depends on the network. For 1D simulations this is a very efficient solver, for 2D simulations it is less so.

**Conjugate gradient Method**

[use_of_cg] (default =20) [convergence_cg] (default = 1.0^-9) [precon_cg] (default =1) [convergence_cg] (default=1.0^-9)

This is an iterative method to solve matrices. Therefore, also a convergence definition (convergence_cg) is required. It is possible to prepare this method to make it more efficient during the simulation. The system will than be preconditioned (precon_cg), this will take time in the initializing phase, but will safe time during the simulation itself. To limit the possible amount of iterations in order to guarantee swiftness of the solver, there can be put a maximum of iterations before the convergence threshold is loosened.

**CFL condition**

[cfl_strictness_factor_1d] (default=1.0) [cfl_strictness_factor_2d] (default=1.0)

There is a limit to the time step, called the CFL condition. This condition is due to the chosen discretization of the equations. It defined as cdt/dx<1. C is the velocity, defined as 

.. math::
   :label: CFL-condition

   C = |U| + \sqrt(gH) 

Often it is not necessary to be so strict, so sometimes the user can set this parameter which loosens the strictness of it. However, be careful stability cannot be guaranteed anymore.

**Implicit pump settings**

[pump_implicit_ratio] (default=1, between 0 and 1)

A pump will be turned on or of depending on the water level.  When the pump capacity is higher than the available volume the time step will be decreased. Another consequence is that the pump will switch often from maximum capacity to nothing. This can cause for instabilities, even though in real life this can happen as well. By allowing the pump capacity to be determined implicitly, the capacity is adjusted based on the available water. This will enhance the stability, but the pumps capacity will be affected in cases of limited supply.

**Thresholds**

For numerical computation several tresholds are needed in the code, to avoid deficiencies due to a limited numerical accuracy. Generally this is to keep the behaviour consistent: 

In order to determine the upwind method the direction of the flow is considered. To avoid the exact 0.0 m/s point we use a threshold given by flow_direction_threshold (default=1.0^-5). 

We also use for various things a general threshold, this one is defined as general_numerical_threshold, the default is 1.0d-8. 


Limiters
--------

A limiter is a general term used for certain aspects in numerical schemes that limit the effect of high gradients in flow or forcing. This is to avoid strong oscillations, instabilities in the solution and to increase the stability. 3Di has various limiters implemented, which can be turned on or off.

Limiter for water level gradient
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[limiter_grad_2d] [limiter_grad_1d]

The limiter on the water level gradient allows the model to deal with unrealistically steep gradients. These can occur when there are, for example, jumps in the bottom.  In such case the water is not forced by the difference in water level as this gradient is limited to the actual depth.   Therefore a limiter function is part of the discretization scheme. This setting exist for both the flow in the 1D domain as for the 2D domain.

.. figure:: image/lim_watlev_grad.png
   :alt: Limiter for water level gradient

   Visualization of a case where the gradient is adjusted. The red dashed line indicates the outcome of the limiter function.

Function where the ratio between water depth and  water level gradient prescribes the behaviour.   
   
.. math::
   :label: Limiter-function

   \phi_(m+1) = min[ 1 , H / ( \sigma_(m+1) - \sigma_m ) ]

   
Limiter for cross-sectional area
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[limiter_slope_crossectional_area_2d ] default = 0

In sloping areas we are dealing with a situation where the primairy assumption of a subgrid-based method does not yield. The method assumes that the water level variation in space is much smaller than the variation of the bed. This is untrue for larger cells in sloping areas. The consequence is that in that case all the water is concentrated at the lower end of the cell. The depth that defines the cross-sectional area, that determines the discharge within a time step, is overestimated (black boxes Figure 2). 

*limiter_slope_crossectional_area_2d = 1*

This limiter starts working in case the depth based on the downstream water level is zero. Than two options are possible, in case of a large difference in waterlevel the volume is spread over the cell domains (Figure 2, alternative situation 1). When the difference is smaller the average water level of upstream and downstream is used  (Figure 2, alternative situation 2). Theoretically this would make the scheme partly second order. This is described mathematically in Figure 3.

*limiter_slope_crossectional_area_2d = 2*

This is a very stable upwind method to redefine the water level depth . It is assumed that the flow behaves as a thin sheet flow. Therefore, the depth is defined as the upwind volume defined by the maximum surface area. 

*limiter_slope_crossectional_area_2d = 3, in combination with thin_layer_definition = xx [m]*

In this case the limiter is more or less effective depending of the local depth. In case the depth at the edge base on the down wind  water level is larger than the definition that is given of a thin layer, the cross-sectional area is based on the high resolution grid. When this 'down wind' depth is smaller than the thin layer definition, than the limiter described for option 2 is determining the cross-sectional area. In the in between  phase the two types of cross-sections are weighed to define a new value.

This is decribed in the figure below. Mathematical derivation will follow.

.. figure:: image/slopelimiter.png
   :alt: Limiter for cross-sectional area
.. figure:: image/lim_slope_3.png
   :alt: Limiter for cross-sectional area
   
   Grid schematisation in a sloping areas. Two alternatives to determine an effective depth for the cross-sectional area. Lower:   The alternatives for the cross-sectional area  in case of limiter option 2.

Limiter for friction depth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[limiter_slope_friction_2d] default = 0

In order to take high resolution depth and roughness variations into account to determine the friction, an estimate is made of the effective frictional depth. For this the actual depth is needed. Similar to the Limiter for the cross-sectional area, the actual depth in sloping areas is overestimated. In such case not only the depth to determine the cross-sectional area can be adjusted, but also the depth to determine the effective frictional depth. The friction can therefore  be underestimated in sloping areas. Therefor the same limiter can be used to determine the effective frictional depth by switching this limiter on. This limiter is obligated in combination with the limiter_slope_crossectional_area_2d.


Settings for Friction
----------------------

There are several settings that affect the friction.

Friction shallow water correction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[friction_shallow_water_correction]  (default =0) (possible values 0,1,2,3)

In case the friction assumptions based on the dominant friction balance gives a structurally underestimation of the friction, one can switch this setting on. This situation can occur in case the flow is  mainly distributed based on continuity in stead. In Figure 1, the difference  between the two type of flows is shown. Such a situation occurs for example in a sloping area where filled canals are cutting through in cross slope direction.  When the corrections is switched on, the friction is determined both the classical way and based on averaged values of depth, velocity and roughness coefficients. The maximum friction computed by the two is used.

It is important to define a depth for which the friction is computed. Choosing the correction for the settings 2 or 3 it will define the depth similar to the cross-sectional area limiter. For the value 1 it will use the maximum depth at the edge of the cell.

.. figure:: image/friction_cont_dominated_flow.png
   :alt: Friction shallow water correction
   
   Upper Panel) Flow distributed based on friction dominated flow. 
   Lower Panel) Flow distributed based on continuity.

Friction Average
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[frict_avg] (default = 0)

The roughness coefficient will be averaged within one cell.

Minimum Friction  velocity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

minimum_friction_velocity [float], (default = 0.05 m/s)

In case a cell is flooded, there is a moment that initially there is no water, therefore no friction as the velocity is zero. Followed by a moment that there is a velocity. To assure a smooth transition and to avoid extreem accelerations of the flow, we define a sort of minimum amount of friction based on this velocity. Generally this is important only when a cell is flooded. 
