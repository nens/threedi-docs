.. _1d_objects:

1D Objects
==========

.. _1d_boundary_condition:
1D Boundary Condition
---------------------

Boundary condition for 1D connection nodes.

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^

.. list-table:: 1D Boundary condition attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - ID of the connection node to place the 1D boundary condition on
   * - Boundary type
     - boundary_type
     - integer
     - Yes
     - \-
     - Sets the type to water level (1), velocity (2), discharge (3) or Sommerfeld (5). See :ref:`1d_boundary_condition_notes_for_modellers` for details.
   * - Time series
     - timeseries
     - text
     - Yes
     - [minutes since start of simulation],[m | m/s | m³/s]. See :ref:`1d_boundary_condition_notes_for_modellers` for details.
     - Timeseries of water levels, flow velocities, discharges or water level gradients to be forced on the model boundary

.. _1d_boundary_condition_notes_for_modellers:
Notes for modellers
^^^^^^^^^^^^^^^^^^^

General notes
"""""""""""""
- 1D boundary conditions can only be applied to connection nodes that have a single connection to the rest of the network.
- The pipe, channel, or structure directly connected to the boundary condition must have calculation type isolated.
- 1D boundary conditions cannot be placed on the same connection node as a pump station.
- 1D laterals placed on a connection node with a 1D boundary condition will be ignored.
- Surfaces and impervious surfaces mapped to a connection node with a 1D boundary condition will be ignored.

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in minutes since the start of the simulation) in the first column and the value (units dependent on the boundary type) in the second column. For example::

    0,145.20
    15,145.23
    30,145.35
    45,145.38
    60,145.15

- The time series string cannot contain any spaces or empty rows
- The boundary condition time series is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.
- The time unit in the 1D boundary condition table *in the schematisation* is minutes, while the 3Di API expects this input in seconds. A conversion is applied when the reading the data from the schematisation. If you upload a CSV file with 1D boundary condition time series via the simulation wizard, you can choose the time unit (see :ref:`simulate_api_qgis_boundary_conditions`)
- For boundary types velocity (2), discharge (3) and Sommerfeld (5), the drawing direction of the channel, pipe, or structure determines sign of the input value. For velocity and discharge, this means that if the 1D boundary condition is placed on the end connection node, positive values result in boundary *outflow*. For the Sommerfeld boundary, a positive gradient for a 1D boundary condition that is placed at the end connection node means that the waterlevel downstream is higher than upstream, i.e. this will result in boundary *inflow*.
- The time series must cover the entire simulation period.
- All 1D boundary conditions must have the same time steps
- The time series values are interpolated between the defined times
- In case of multiple boundaries in 1 model: make sure they all have the same number of timeseries rows with the same temporal interval.
- When editing the time series field in using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    "0,145.20"||char(10)||"15,145.23"||char(10)||"30,145.35"||char(10)||"45,145.38"||char(10)||"60,145.15"

.. _1d_lateral:
1D Lateral
----------

Defines a lateral discharge (source or sink term) for the 1D domain

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^

.. list-table:: 1D Lateral attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - ID of the connection node on which the 1D lateral should be placed
   * - Time series
     - timeseries
     - text
     - Yes
     - [minutes since start of simulation],[m³/s]. See :ref:`1d_lateral_notes_for_modellers` for details.
     - Timeseries of lateral discharges to be added to the specified location

.. _1d_lateral_notes_for_modellers:
Notes for modellers
^^^^^^^^^^^^^^^^^^^
1D laterals placed on a connection node with a 1D boundary condition will be ignored.

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in minutes since the start of the simulation) in the first column and the value (m³/s) in the second column. For example::

    0,0.2
    15,10.0
    30,20.0
    45,7.5
    60,0.0

- The time series string cannot contain any spaces or empty rows
- The lateral time series is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.
- The time unit in the 1D lateral table *in the schematisation* is minutes, while the 3Di API expects this input in seconds. A conversion is applied when the reading the data from the schematisation. If you upload a CSV file with 1D lateral time series via the simulation wizard, the time units are *seconds* (see :ref:`simulate_api_qgis_laterals`)
- Positive values represent a source (water is added to the node), negative values represent a sink (water is extracted from the node to the extent that this water is available in the node)
- The time series does not need to cover the entire simulation period.
- The time series values are interpolated between the defined times
- When editing the time series field in using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    "0,0.2"||char(10)||"15,10.0"||char(10)||"30,20.0"||char(10)||"45,7.5"||char(10)||"60,0.0"


.. _channel:

Channel
-------

A natural or artificial open channel. Channels can have a variable bed level, bed friction and cross section along their length. This information is stored in another object, the :ref:`cross_section_location`. A channel can have one or more cross-section locations, depending on the variability of the channel.

See :ref:`channelflow` for more details.

Geometry
^^^^^^^^
Linestring (two or more vertices)

Attributes
^^^^^^^^^^

.. list-table:: Channel attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Calculation type
     - calculation_type
     - integer
     - Yes
     - \-
     - Sets the 1D2D exchange type: embedded (100), isolated (101), connected (102), or double connected (105). See :ref:`calculation_types`.
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Distance between calculation points
     - dist_calc_points
     - decimal number
     - No
     - m
     - Maximum distance between calculation points, see :ref:`techref_calculation_point_distance`
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of end connection node
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of start connection node
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*


Notes for modellers
^^^^^^^^^^^^^^^^^^^

.. todo::
   Refer to "how to schematise open water systems" when that section is finished

- Use 1D channels wisely. In many applications, schematising waterways in 2D is preferable. See :ref:`channelflow` and :ref:`calculation_types`.
- All channels must have at least one :ref:`cross_section_location`.

Calculation type 'embedded'
"""""""""""""""""""""""""""
- Embedded channels add extra connections between 2D grid cells, but ignore obstacles and levees.
- Make sure the embedded channel profile always lays partially below the DEM; embedded channels cannot 'float' above the DEM.
- Embedded channels only function when they connect several 2D grid cells, so make sure no embedded channel falls completely inside one 2D grid cell
- Do not place boundary conditions directly on embedded channels.


.. _connection_node:
Connection node
---------------

Location and ID of nodes to connect :ref:`channel`, :ref:`culvert`, :ref:`orifice`, :ref:`weir`, :ref:`pipe`, :ref:`pumpstation_with_end_node`, or :ref:`pumpstation_without_end_node` features. :ref:`manhole`, :ref:`1d_lateral`, and :ref:`1d_boundary_condition` features are also defined at connection nodes. See :ref:`inflow_objects` for more information on how surfaces and impervious surfaces can be mapped to a connection node.

Geometry
^^^^^^^^
Point


Attributes
^^^^^^^^^^

.. list-table:: Connection node attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Initial water level
     - initial_waterlevel
     - decimal number
     - No
     - m above datum
     - Initial water level for the 1D domain
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Storage area
     - storage_area
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

- Connection nodes with large storage (i.e. the square root of the storage area is much larger than the width of the incoming channel) reduce the flow velocity and advective force.

.. _cross_section_location:
Cross-section location
----------------------

Object to define the dimensions, levels, and friction at a specified point along a :ref:`channel`.

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^
.. list-table:: Cross-section location attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Bank level
     - bank_level
     - decimal number
     - Yes
     - m MSL
     - Exchange level for the 1D2D connections. Only used when calculation type is 'connected'.
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Cross-section height
     - cross_section_height
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Height of the cross-section (only used for Closed rectangle cross-sections)
   * - Cross-section shape
     - cross_section_shape
     - decimal number
     - Yes
     - \-
     - Sets the cross-section shape, :ref:`cross-section_shape`
   * - Cross-section table
     - cross_section_table
     - text
     - see :ref:`cross-section_shape`
     - m
     - CSV-style table of [height, width] or [Y, Z] pairs, see :ref:`cross-section_shape`
   * - Cross-section width
     - cross_section_width
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Width or diameter of the cross-section, see :ref:`cross-section_shape`
   * - Friction type
     - friction_type
     - decimal number
     - Yes
     - \-
     - Sets the friction type to Chézy (1) or Manning (2)
   * - Friction value
     - friction_value
     - decimal number
     - Yes
     - m:sup:`1/2`/s or s/m:sup:`1/3`
     - Friction or roughness value
   * - Reference level
     - reference_level
     - decimal number
     - Yes
     - m MSL
     - Lowest point of the cross-section


.. _cross_section_location_notes_for_modellers:

Notes for modellers
^^^^^^^^^^^^^^^^^^^

- If the channel calculation point distance is smaller than the distance between cross section locations, values in the cross section locations along the channel are interpolated, see :ref:`techref_calculation_point_distance`.
- If there are multiple cross-section locations between two **calculation nodes** (not connection nodes), only the first cross-section location is used.

Reference level
"""""""""""""""
This is the bed level of the channel and the reference level for the cross-section. For example, if the reference level is 12.0 m MSL and the cross-section a tabulated rectangle with a width of 5 m at height 0, this means that the channel is 5 m wide at 12.0 m MSL.

.. _cross-section_shape: 
Cross-section shape
"""""""""""""""""""
The following shapes are supported:

.. list-table:: Cross-section shapes
   :widths: 1 1 4
   :header-rows: 1

   * - Shape
     - Value
     - Instructions
   * - Closed rectangle
     - 0
     - Specify cross-section height and cross-section width
   * - Open rectangle
     - 1
     - Specify cross-section width
   * - Circle
     - 2
     - Specify cross-section width (i.e., diameter)
   * - Egg
     - 3
     - Specify cross-section width. Height will be 1.5 * width.
   * - Tabulated rectangle
     - 5
     - Fill cross-section table as CSV-style table of height, width pairs 
   * - Tabulated trapezium
     - 6
     - Fill cross-section table as CSV-style table of height, width pairs
   * - YZ
     - 7
     - Fill cross-section table as CSV-style table of Y, Z pairs
   * - Inverted egg
     - 8
     - Specify cross-section width. Height will be 1.5 * width.


.. _culvert:
Culvert
-------

Culverts are used to schematise pipes in open water systems.

In contrast to an :ref:`orifice`, the flow behaviour in a culvert is assumed to be determined by shape and much less dominated by entrance losses. Culverts can be used for longer sections of pipe-like structures and do not have to be straight. Shorter, straight culverts are best schematised as an :ref:`orifice`.


Geometry
^^^^^^^^
Linestring (two or more vertices)

Attributes
^^^^^^^^^^

.. list-table:: Culvert attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Calculation type
     - calculation_type
     - integer
     - Yes
     - \-
     - Sets the 1D2D exchange type: embedded (100), isolated (101), connected (102), or double connected (105). See :ref:`calculation_types`.
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Cross-section height
     - cross_section_height
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Height of the cross-section (only used for Closed rectangle cross-sections)
   * - Cross-section shape
     - cross_section_shape
     - decimal number
     - Yes
     - integer
     - Sets the cross-section shape, :ref:`cross-section_shape`
   * - Cross-section table
     - cross_section_table
     - text
     - see :ref:`cross-section_shape`
     - m
     - CSV-style table of [height, width] or [Y, Z] pairs, see :ref:`cross-section_shape`
   * - Cross-section width
     - cross_section_width
     - decimal number
     - see :ref:`cross-section_shape`
     - integer
     - Width or diameter of the cross-section, see :ref:`cross-section_shape`
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Distance between calculation points
     - dist_calc_points
     - decimal number
     - No
     - m
     - Maximum distance between calculation points, see :ref:`techref_calculation_point_distance`
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of end connection node
   * - End invert level
     - invert_level_end_point
     - decimal number
     - Yes
     - m MSL
     - Level of lowest point on the inside at the end of the culvert
   * - Friction type
     - friction_type
     - decimal number
     - Yes
     - \-
     - Sets the friction type to Chézy (1) or Manning (2)
   * - Friction value
     - friction_value
     - decimal number
     - Yes
     - m:sup:`1/2`/s or s/m:sup:`1/3`
     - Friction or roughness value
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of start connection node
   * - Start invert level
     - invert_level_start_point
     - decimal number
     - Yes
     - m MSL
     - Level of lowest point on the inside at the start of the pipe
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*

Notes for modellers
^^^^^^^^^^^^^^^^^^^

The cross-section describes the inside of the culvert. If you only know the outer dimensions, you have to discount the wall thickness.

Discharge coefficients
""""""""""""""""""""""
The discharge is multiplied by this value. The energy loss caused by the change in flow velocity at the entrance and exit are accounted for by 3Di. The discharge coefficients can be used to account for any additional energy loss. 'Positive' applies to flow in the drawing direction of the structure (from start node to end node); 'negative' applies to flow in the opposite direction.



.. _manhole:
Manhole
-------

Manholes are used to explicitly define the calculation type, bottom level, and/or 1D2D exchange level at the location of a connection node. In sewer models, they are commonly used to schematise inspection manholes, pumping station reservoirs and outlets. Manholes can also be used in open water systems, when you want to to explicitly set the calculation type, bottom level or 1D2D exchange level at a specific location.

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^

.. list-table:: Manhole attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Bottom level
     - bottom_level
     - decimal number
     - Yes
     - m MSL
     - Manhole bottom level
   * - Calculation type
     - calculation_type
     - integer
     - Yes
     - \-
     - Sets the type of 1D2D exchange: embedded (0), isolated (1), or connected (2). See :ref:`calculation_types`.
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Connection node ID
     - id
     - integer
     - Yes
     - \-
     - ID of connection node on which manhole is placed
   * - Drain level
     - drain_level
     - decimal number
     - No
     - m MSL
     - Exchange level for the 1D2D connection. See :ref:`manhole_notes_for_modellers`.
   * - Length
     - length
     - decimal number
     - No
     - m
     - Horizontal length of the manhole (not used in the calculation)
   * - Manhole indicator
     - manhole_indicator
     - integer
     - Yes
     - m MSL
     - Defines the type of the manhole: inspection (0), outlet (1), or pumping station (2)
   * - Shape
     - shape
     - text
     - No
     - \-
     - Shape of the manhole in the horizontal plane (not used in the calculation): square (00), round (01), or rectangle (02)
   * - Surface level
     - surface_level
     - decimal number
     - No
     - m MSL
     - Top of the manhole, e.g. street level (not used in the calculation).
   * - Width
     - width
     - decimal number
     - No
     - m
     - Horizontal width of the manhole (not used in the calculation)
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*

.. _manhole_notes_for_modellers:
Notes for modellers
^^^^^^^^^^^^^^^^^^^
- Connection nodes for which a manhole is defined, must have a storage area larger than zero.
- Only one manhole can be defined for each connection node.

Drain level
"""""""""""
- Water can flow from the 1D domain to the 2D domain if the 1D water level exceeds the drain level (and vice versa).
- In 1D-2D models, this setting only applies to manholes with calculation type 'connected'
- In 1D-only models, the drain level is used as the street level, above which the storage area widens to the "manhole storage area" value specified in the global settings.
- If the drain level is not filled in, 3Di will use the DEM value at the location of the manhole, or, in case of 1D-only models, the highest top of the pipes starting or ending at this manhole.

Shape, width and length
"""""""""""""""""""""""
These values describe the shape of the manhole in the horizontal plane (i.e. the manhole bottom). They are for administrative purposes only and do not affect the storage area of the connection node. These values are not used by 3Di.

Manhole indicator
"""""""""""""""""
This value is used for administrative and visualisation purposes only. It does not affect the calculation.

Surface level
"""""""""""""
This value is used for administrative purposes only. It does not affect the calculation

.. _pumpstation_without_end_node:
Pumpstation (without end node)
-------------------------------

Pumpstation that pumps water out of the model domain. This can be used, for example, to simulate a final pumpstation that pumps the water to a sewage treatment plant that is outside of the model domain. See :ref:`pump` for details on how pumping stations work in 3Di.

If you want the pumpstation to pump the water to another location *within* the model, use :ref:`pumpstation_with_end_node`

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^

.. list-table:: Pumpstation (without end node) attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Capacity
     - capacity
     - decimal number
     - Yes
     - L/s
     - Pump capacity
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - ID of connection node on which the pumpstation is placed
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Lower stop level
     - lower_stop_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches off when the water level becomes lower than this level
   * - Sewerage
     - sewerage
     - boolean
     - Yes
     - \-
     - Indicates if the pumpstation is part of the sewer system (True) or not (False)
   * - Start level
     - start_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches on when the water level exceeds this level
   * - Type
     - type
     - integer
     - Yes
     - \-
     - Sets whether pump reacts to water level at: suction side (1) or delivery side (2)
   * - Upper stop level
     - upper_stop_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches off when the water level exceeds this level
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*


Notes for modellers
^^^^^^^^^^^^^^^^^^^
- Multiple pumpstations may be defined for the same connection node. If their active ranges (start/stop level) overlap, they may pump at the same time.


.. _pumpstation_with_end_node:
Pumpstation (with end node)
----------------------------

Pumpstation that transports water from one connection node to another. See :ref:`pump` for details on how pumping stations work in 3Di. If you want the pumpstation to pump the water out of the model, use :ref:`pumpstation_without_end_node`. You do *not* need to use a 1D boundary condition for this.

Geometry
^^^^^^^^
Linestring (exactly two vertices)


Attributes
^^^^^^^^^^

.. list-table:: Pumpstation (with end node) attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Capacity
     - capacity
     - decimal number
     - Yes
     - L/s
     - Pump capacity
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of connection node to which the water is pumped
   * - Lower stop level
     - lower_stop_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches off when the water level becomes lower than this level
   * - Sewerage
     - sewerage
     - boolean
     - Yes
     - \-
     - Indicates if the pumpstation is part of the sewer system (True) or not (False)
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of connection node from which the water is pumped
   * - Start level
     - start_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches on when the water level exceeds this level
   * - Type
     - type
     - integer
     - Yes
     - \-
     - Sets whether pump reacts to water level at: suction side (1) or delivery side (2)
   * - Upper stop level
     - upper_stop_level
     - decimal number
     - Yes
     - m MSL
     - Pump switches off when the water level exceeds this level
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*


Notes for modellers
^^^^^^^^^^^^^^^^^^^
- Multiple pumpstations may be defined for the same connection node. If their active ranges (start/stop level) overlap, they may pump at the same time.

.. _orifice:
Orifice
-------

An orifice can be used to schematise hydraulic structures like gates, bridges, or culverts. It can be used in open water systems as well as in sewerage systems.

An orifice is commonly used to schematise structures that are closed at the top of the cross-section, whereas the :ref:`weir` is commonly used for structures that are open at the top. However, both types of cross-sections can be used for either structure, and 3Di uses them in the calculation in the same way. See :ref:`weirs_and_orifices` for further details.

Geometry
^^^^^^^^
Linestring (exactly two vertices)

Attributes
^^^^^^^^

.. list-table:: Orifice attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Crest level
     - crest_level
     - decimal number
     - Yes
     - m MSL
     - Lowest point of the cross-section.
   * - Crest type
     - crest_type
     - integer
     - Yes
     - \-
     - Sets the crest type: broad-crested (3) or short-crested (4)
   * - Cross-section height
     - cross_section_height
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Height of the cross-section (only used for Closed rectangle cross-sections)
   * - Cross-section shape
     - cross_section_shape
     - decimal number
     - Yes
     - \-
     - Sets the cross-section shape, :ref:`cross-section_shape`
   * - Cross-section table
     - cross_section_table
     - text
     - see :ref:`cross-section_shape`
     - m
     - CSV-style table of [height, width] or [Y, Z] pairs, see :ref:`cross-section_shape`
   * - Cross-section width
     - cross_section_width
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Width or diameter of the cross-section, see :ref:`cross-section_shape`
   * - Discharge coefficient negative
     - discharge_coefficient_negative
     - decimal_number
     - Yes
     - \-
     - Discharge in the negative direction is multiplied by this value
   * - Discharge coefficient positive
     - discharge_coefficient_positive
     - decimal_number
     - Yes
     - \-
     - Discharge in the positive direction is multiplied by this value
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of connection node to which the water is pumped
   * - Friction type
     - friction_type
     - decimal number
     - Yes
     - \-
     - Sets the friction type to Chézy (1) or Manning (2)
   * - Friction value
     - friction_value
     - decimal number
     - Yes
     - m:sup:`1/2`/s or s/m:sup:`1/3`
     - Friction or roughness value
   * - Sewerage
     - sewerage
     - boolean
     - Yes
     - \-
     - Indicates if the structure is part of the sewer system (True) or not (False)
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of the start connection node
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*


Notes for modellers
^^^^^^^^^^^^^^^^^^^

In the computational grid, an orifice will always be represented by a single flowline. Therefore, orifices do not have a calculation point distance and calculation type. The calculation type of the start and end nodes is determined by the channels, culverts, manholes, and pipes connected to them.

Crest level
"""""""""""
This is the reference level for the cross-section. For example, if the crest level is 12.0 m and the cross-section a circle with a diameter of 0.5 m, the opening will start at 12.0 m and end at 12.5 m

Discharge coefficients
""""""""""""""""""""""
The discharge is multiplied by this value. The energy loss caused by the change in flow velocity at the entrance and exit are accounted for by 3Di. The discharge coefficients can be used to account for any additional energy loss. 'Positive' applies to flow in the drawing direction of the structure (from start node to end node); 'negative' applies to flow in the opposite direction.

.. _pipe:
Pipe
----

Pipe in a sewer system.

Geometry
^^^^^^^^
Linestring (exactly two vertices)

Attributes
^^^^^^^^^^

.. list-table:: Pipe attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Calculation type
     - calculation_type
     - integer
     - Yes
     - \-
     - Sets the 1D2D exchange type: embedded (0), isolated (1), or connected (2). See :ref:`calculation_types`.
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Cross-section height
     - cross_section_height
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Height of the cross-section (only used for Closed rectangle cross-sections)
   * - Cross-section shape
     - cross_section_shape
     - decimal number
     - Yes
     - integer
     - Sets the cross-section shape, :ref:`cross-section_shape`
   * - Cross-section table
     - cross_section_table
     - text
     - see :ref:`cross-section_shape`
     - m
     - CSV-style table of [height, width] or [Y, Z] pairs, see :ref:`cross-section_shape`
   * - Cross-section width
     - cross_section_width
     - decimal number
     - see :ref:`cross-section_shape`
     - integer
     - Width or diameter of the cross-section, see :ref:`cross-section_shape`
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Distance between calculation points
     - dist_calc_points
     - decimal number
     - No
     - m
     - Maximum distance between calculation points, see :ref:`techref_calculation_point_distance`
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of end connection node
   * - End invert level
     - invert_level_end_point
     - decimal number
     - Yes
     - m MSL
     - Level of lowest point on the inside at the end of the pipe
   * - Friction type
     - friction_type
     - decimal number
     - Yes
     - \-
     - Sets the friction type to Chézy (1) or Manning (2)
   * - Friction value
     - friction_value
     - decimal number
     - Yes
     - m:sup:`1/2`/s or s/m:sup:`1/3`
     - Friction or roughness value
   * - Sewerage
     - sewerage
     - boolean
     - Yes
     - \-
     - Indicates if the pumpstation is part of the sewer system (True) or not (False)
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of start connection node
   * - Start invert level
     - invert_level_start_point
     - decimal number
     - Yes
     - m MSL
     - Level of lowest point on the inside at the start of the pipe
   * - Material
     - material
     - integer
     - No
     - \-
     - Pipe wall material, not used in the calculation. See :ref:`pipe_notes_for_modeller`.
   * - Sewerage type
     - sewerage_type
     - integer
     - Yes
     - \-
     - Function of the pipe in the sewer system. Used for visualisation and administrative purposes only. See :ref:`pipe_notes_for_modeller`.
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*

.. _pipe_notes_for_modeller:

Notes for modellers
^^^^^^^^^^^^^^^^^^^

The cross-section describes the inside of the pipe. If you only know the outer dimensions, you have to discount the wall thickness.

Adding a pipe trajectory
""""""""""""""""""""""""
When you digitize (draw) a pipe feature with more than two vertices, each vertex will be converted into a connection node plus manhole, connected by pipes. If you digitize a pipe that connects existing manholes, the pipe(s) will use the manholes' bottom levels as their invert levels and automatically refer to the correct the connection nodes. Therefore, the quickest way to  digitize a trajectory of multiple pipes is to first digitize the manholes, fill in the bottom levels, and then draw the pipe trajectory over these manholes by adding a vertex at each of the manholes.

Material
""""""""
The material is not used in the calculation, but can be used to estimate the friction value. The processing algorithm "Guess Indicators" recognizes the following values:  0: concrete; 1: pvc; 2: gres; 3: cast iron; 4: brickwork; 5: HPE; 6: HDPE; 7: plate iron; 8: steel.

Sewerage type
"""""""""""""
The following types are supported:
- Combined sewer (0)
- Storm drain (1)
- Sanitary sewer (2)
- Transport (3)
- Spillway (4)
- Syphon (5)
- Storage (6)
- Storage and settlement tank (7)



.. _weir:
Weir
----

Overflow structure, used to control the water level. It can be used in open water systems as well as sewerage systems.

A weir is commonly used to schematise structures with open cross sections, whereas the :ref:`orifice` is commonly used for structures that are closed at the top. However, both types of cross-sections can be used for either structure, and 3Di uses them in the calculation in the same way. See :ref:`weirs_and_orifices` for further details.

Geometry
^^^^^^^^
Linestring (exactly two vertices)

Attributes
^^^^^^^^^^

.. list-table:: Weir attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Code
     - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - Crest level
     - crest_level
     - decimal number
     - Yes
     - m MSL
     - Lowest point of the cross-section.
   * - Crest type
     - crest_type
     - integer
     - Yes
     - \-
     - Sets the crest type: broad-crested (3) or short-crested (4)
   * - Cross-section height
     - cross_section_height
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Height of the cross-section (only used for Closed rectangle cross-sections)
   * - Cross-section shape
     - cross_section_shape
     - decimal number
     - Yes
     - \-
     - Sets the cross-section shape, :ref:`cross-section_shape`
   * - Cross-section table
     - cross_section_table
     - text
     - see :ref:`cross-section_shape`
     - m
     - CSV-style table of [height, width] or [Y, Z] pairs, see :ref:`cross-section_shape`
   * - Cross-section width
     - cross_section_width
     - decimal number
     - see :ref:`cross-section_shape`
     - m
     - Width or diameter of the cross-section, see :ref:`cross-section_shape`
   * - Discharge coefficient negative
     - discharge_coefficient_negative
     - decimal_number
     - Yes
     - \-
     - Discharge in the negative direction is multiplied by this value
   * - Discharge coefficient positive
     - discharge_coefficient_positive
     - decimal_number
     - Yes
     - \-
     - Discharge in the positive direction is multiplied by this value
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - End connection node ID
     - connection_node_end_id
     - integer
     - Yes
     - \-
     - ID of connection node to which the water is pumped
   * - Friction type
     - friction_type
     - decimal number
     - Yes
     - \-
     - Sets the friction type to Chézy (1) or Manning (2)
   * - Friction value
     - friction_value
     - decimal number
     - Yes
     - m:sup:`1/2`/s or s/m:sup:`1/3`
     - Friction or roughness value
   * - Sewerage
     - sewerage
     - boolean
     - Yes
     - \-
     - Indicates if the structure is part of the sewer system (True) or not (False)
   * - Start connection node ID
     - connection_node_start_id
     - integer
     - Yes
     - \-
     - ID of the start connection node
   * - Zoom category
     - zoom_category
     - integer
     - No
     - \-
     - *Deprecated*


Notes for the modeller
^^^^^^^^^^^^^^^^^^^^^^

In the computational grid, a weir will always be represented by a single flowline. Therefore, weirs do not have a calculation point distance and calculation type. The calculation type of the start and end nodes is determined by the channels, culverts, manholes, and pipes connected to them.

Crest level
"""""""""""
This is the reference level for the cross-section. For example, if the crest level is 12.0 m and the cross-section a circle with a diameter of 0.5 m, the opening will start at 12.0 m and end at 12.5 m

Discharge coefficients
""""""""""""""""""""""
The discharge is multiplied by this value. The energy loss caused by the change in flow velocity at the entrance and exit are accounted for by 3Di. The discharge coefficients can be used to account for any additional energy loss. 'Positive' applies to flow in the drawing direction of the structure (from start node to end node); 'negative' applies to flow in the opposite direction.
