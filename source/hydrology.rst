Hydrology
============

Infiltration
------------

Infiltration is water that disappears in the ground.

**Implementation details**

The modeler can choose between different options for infiltration. For option one the full surface area of the cell is used as infiltration surface when it rains. When it is dry, water can only infiltrate in  wet subgrid areas. Option 2 forces the model to use the full cell surface infiltratable area. The third option uses only the wet surface area as infiltratable surface area. 

**Technical description**

The infiltration is implicity added to the continuity equation. This meas that the infiltration discharge depends on the infiltration capacity and the water level at the new and the old time level:

.. math::
   :label: infiltration

   Q_inf = I * ( H^(k+1) / H^n )

in which, k is the indicie for the inner Newton iteration loop, n, is the timestep, Q_inf is the....

maximum infiltration

neerslag, verdamping, etc. vertical processes

NWRW inflow
-----------