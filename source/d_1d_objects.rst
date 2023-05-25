.. _1d_objects:

1D Objects
==========

.. _1d_boundary_condition:
1D Boundary Condition
---------------------

Boundary condition for 1D connection nodes. Boundaries can only be placed on nodes connected to a single channel, culvert, orifice, weir, pipe, or pumpstation.

.. _1d_lateral:
1D Lateral
----------

Lateral for 1D connection nodes

.. _channel:
Channel
-------

Channel lines between connection nodes. All channels must have at least one cross_section_location.

..
    Not sure if this is still all true:
    Embedded channels
    ^^^^^^^^^^^^^^^^^

    Embedded channels are useful when you wish to add more detailed profiles to a course raster-file. Also, they are the most efficient way to add channels since they don't add to the number of computational points. In fact, the volume in the channel is integrated with that of the 2D computational cell. When modelling embedded channels, consider the following:

    * The water level in the embedded channel is always equal to the water level in the underlaying 2D grid cell.

    * Embedded channels add extra connections between 2D grid cells, but ignore obstacles and levees.

    * Make sure the embedded channel profile always partially lays below the surface level in you DEM (you can't have floating embedded channels).

    * Make sure no more than one channel vertice falls inside a single raster-file pixel.

    * Embedded channels only function when they connect several 2D grid cells, so make sure no embedded channel falls completely inside one 2D grid cell

    * All connection nodes connected to an embedded channel become embedded, so make sure structures or channels of other types that are connected to these connection node cross at least one 2D grid cell boundary, and

    * Do not place boundary conditions directly on embedded channels.

.. _connection_node:
Connection node
---------------

Location and ID of nodes to connect :ref:`channel`, :ref:`culvert`, :ref:`orifice`, :ref:`weir`, :ref:`pipe`, :ref:`pumpstation_with_end_node`, or :ref:`pumpstation_without_end_node` features. :ref:`manhole`, :ref:`1d_lateral`, and :ref:`1d_boundary_condition` features are also defined at connection nodes. See :ref:`inflow_objects` for more information on how surfaces and impervious surfaces can be mapped to a connection node.

Attributes
^^^^^^^^^^

.. list-table:: Connection node attributes
   :widths: 6 4 2 4 30
   :header-rows: 1

   * - Attribute
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Initial water level
     - decimal number
     - No
     - m above datum
     - Initial water level for the 1D domain. For calculation nodes that are added along the length of a channel, pipe, or culvert, initial water levels are linearly interpolated between connection nodes.
   * - Code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Storage area
     - decimal number
     - No
     - m²
     - Adds additional storage capacity to a 1D network. In sewerage models, this is usually combined with a manhole. If a manhole is present on the connection node, the storage area must be larger than zero. Note that the storage area defined in the manhole is used in the calculation, whereas the manhole's shape, width, and length are for administration only and do not influence the storage area used during simulation. Storage area can also be added to a connection node without the use of a manhole. Connection nodes that are not connected to channels (for instance when between two culverts) require a storage area larger than zero. Connection nodes with large storage areas (i.e. the square root of the storage area is much larger than the width of the incoming channel) lead to loss of momentum and advective force.


.. _cross_section_location:
Cross-section location
----------------------

Location of cross-section for channels.

.. _culvert:
Culvert
-------

Culvert, a connection between connection nodes

.. _manhole:
Manhole
-------

Sewerage manhole

.. _pumpstation_without_end_node:
Pumpstation (without end node)
------------------------------

Pumpstation that pumps water out of the model domain

.. _pumpstation_with_end_node:
Pumpstation (with end node)
---------------------------

Pumpstation that transports water from one connection node to another

.. _orifice:
Orifice
-------

Structure that can be used to schematize e.g. spillways or bridges

.. _pipe:
Pipe
----

Sewer pipe

.. _weir:
Weir
----

Open water weir or sewerage overflow structure