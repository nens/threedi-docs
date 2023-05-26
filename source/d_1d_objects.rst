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
     - Initial water level for the 1D domain
   * - Code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Storage area
     - decimal number
     - No
     - m²
     - Adds additional storage capacity to a 1D network

Notes for modellers
^^^^^^^^^^^^^^^^^^^

Connection nodes and calculation nodes
""""""""""""""""""""""""""""""""""""""

Connection nodes are not the same as calculation nodes. When 3Di generates the computational grid from the schematisation, a calculation node is created for each connection nodes, but additional 1D calculation nodes may also be created in between. See the :ref:`grid` section for further details.


Initial water level
"""""""""""""""""""

- For calculation nodes that are added along the length of a channel, pipe, or culvert, initial water levels are linearly interpolated between connection nodes. See the :ref:`grid` section for further details.

- The intial water level is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.

Storage area
""""""""""""
- Storage area on connection nodes is additional to the storage that is defined by the dimensions of channels, culverts and pipes. See :ref:`techref_storage_in_1d_domain` for more details.

- To calculate storage volume from the storage area, the height of the water column (water level minus bottom level) needs to be known. If a manhole is defined at the connection node, the manhole's bottom level is used. Otherwise, the lowest bottom (reference level or invert level) of the channels, culverts or pipes that connect to the connection node is used.

- For connection nodes that are not connected to channels, a storage area larger than zero is recommended.

- If a manhole is defined on the connection node, the storage area must be larger than zero. Note that the manhole dimensions (shape, width, and length) are for administrative purposes only and are not used to calculate the storage during the simulation.

- Connection nodes with large storage (i.e. the square root of the storage area is much larger than the width of the incoming channel) lead to loss of flow velocity and advective force.

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