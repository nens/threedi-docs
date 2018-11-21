.. _breaches:

Breaches
========

In the case of a levee or dike breach, the dimensions of the breach determine how much water enters through the breach and thus how quickly the flood spreads. The growth of a breach is a very complex process, many aspects of which are unknown. It is a phenomenon where hydrodynamics, morphology, groundwater and soil mechanics interact. This interaction is complex and largely unknown. Nevertheless, rules of thumb have been developed that describe the breach growth.


Breaches from 1D channels to 2D grid
-----------------------------------------

In a 3Di model, flow may occur between 1D and 2D elements. In certain cases this exchange is limited by a dike. The exchange height is then determined by the height of the dike and the cells where the exchange takes place is determined by the location of the dike. When a few extra properties of the dike are specified for these connections, a breach can be modeled that can grow over time.

Breach growth formulation
++++++++++++++++++++++++++++++++++++++

The breach growth formula of Verheij and Knaap (2003) is used in 3Di to describe the growth of breaches. For this formulation it is expected that the material of the dike (sand or clay), an initial breach width, the maximum breach depth and the length of time to reach this depth are known.

.. figure:: image/b_breach_growth.png
   :alt: breach growth
   :align: right
   
   Longnitudal cross section of breach showing the breach growth parameters. 

The development of the breach has been split into two phases for this formulation; the first phase is the deepening of the breach. The second phase is the widening of the breach. In formula form, the first phase can be described as:   

.. math::
   :label: breach_growth1

   B(t) = B_0         t_{start} < t < T_0
   \eta(t + \Delta t) = \eta(t) - (t / T_0) * (\eta(t) - \eta_{min})         t < T_0

| In which: 
| :math:`B_t` is the width of the breach at time t, 
| :math:`\eta_{min}` is the lowest breach depth, 
| :math:`T_0` is the time at which the lowest depth is reached,
| :math:`B_0` is the initial breach width, and
| :math:`\Delta t` is the time step, and
| :math:`\eta(t)` is the depth of the breach at time t. 
|

Once the lowest breach depth is reached, the width of the breach increases according to:

.. math::
   :label: breach_growth2

   B(t + \Delta t) = B(t) + \Delta t * (\delta B / \delta t)  |_t       t > T_0
   (\delta B / \delta t)  |_t = (f_1 * f_2) / (u_c^2 ln[10]) * [g*(h_{up}(t) - h_{down}(t))]^(3/2) / (1 + (f_2g/u_c)(t - T_0) )        t > T_0

| In which: 
| :math:`f_1, f_2` emperically derived parameters for sediment type, 
| :math:`u_c` is the critical velocity,  and
| :math:`h_{up}, h_{down}` is the water level upstream and downstream of the breach. 
|

Because the slope (difference in water level) before and after the breach is included in the formulation, a natural balance may arise. This means that the breach does not continue to grow if the water levels are equal.

The above formulation also corrects for the presence of different types of materials by using a critical speed. The growth rate of the breach increases as the material erodes  more easily. This information is included in the coefficients f1 and f2.

Exchange formulation
++++++++++++++++++++++++

The flow between 1D and 2D at hte breach is calculated on the basis of a simplified impulse balance. A balance is made between the friction and the forcing. Note that the volume in the breach is neglegled.

More details on how to use obstacles, levees and breaches can be found in :ref:`flood_model`.

