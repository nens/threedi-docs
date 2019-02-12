.. _1Dpressurized:

Pressurized flow
---------------------

A typical characteristic of some 1D elements is that they can have closed cross-sections (Figure b1.5). Thereby, it is possible that the flow becomes pressurized. By introducing the subgrid method :ref:`subgridmethod`, it was explained that cells could be dry, wet and partly wet. By allowing the bed height to vary within a computational cell, the system of equation became non-linear. This was solved with a highly efficient method. However, there are some requirements for such system to be solved. In case the surface area decreases for increasing water levels, one of these requirements is violated.  Therefore, a new method had to be introduced to solve such a non-linear system of equations. This method is based on the so-called nested Newton method (Casulli & Stelling 2013).

.. figure:: image/b1_5.png
   :scale: 50%
   :alt: open_closed_crosssections
   
   Examples of cross-sectional areas. An open and closed cross-sectional area

By this not only flooding and drying is automatically accounted for, but also pressurized flow can be taken into account. One of the advantages is that the volume in an element, like a pipe can be limited, while the water level can still rise. At some point, when the pipe is full, the water level than represents a pressure (Figure b1-6). 