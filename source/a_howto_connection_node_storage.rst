Choose connection node storage area
-----------------------------------

A connection node is a schematisation object that connects channels, pipes, culverts, weirs, orifices and pumping stations. Storage can be added to these nodes by setting the *storage area* to a non-NULL value. This section provides guidelines for choosing the right storage area.

Manholes in sewerage systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In sewerage systems, the storage area corresponds to the surface area of the bottom of the manhole. If no data is available on the manhole dimensions, a storage area of 0.5 to 1 m can be used as a sensible default in most sewerage systems.


Effect on advection
^^^^^^^^^^^^^^^^^^^

If the (square root of the) storage area is much larger than the width of the channels or pipes connected to it, it will reduce the advective force: fast-flowing water that flows into a large storage will loose its momentum and not pass it on to the next channel section or pipe.

Storage area at channel junctions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The loss of advective momentum also occurs at channel junctions, because of the turbulence and still waters present at these locations. Adding a storage area corresponding to the size of the junction will lead to more accurate computation of the advective losses of the flow.

Pumping stations
^^^^^^^^^^^^^^^^

A pumping station's start connection node should be sufficiently large in comparison to the pump capacity. If you do not have data on the dimensions of the pump cellar, choose a realistic value based on how fast the water level is expected to lower as soon as the pump turns on. E.g., if the pump capacity is 3000 L/s, a storage area of 2 m:sup:`2` would lead to a drawdown of 1.5 m/s, which is not very realistic. A storage area of 20 m would be more realistic in this case.
