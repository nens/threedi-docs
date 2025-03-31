.. _inflow_objects:

Laterals & 0D inflow
====================

Laterals add or subtract water from the model domain. 0D inflow includes flow from *Surfaces* and dry weather flow. Surfaces calculate runoff from rain onto a predefined surface area, using a simple hydrological calculation. Dry weather flow is a specific type of lateral, used to simulate the inflow into sanitary sewers from households and industry.

For more information see:

* :ref:`laterals`
* :ref:`0d_rain`

Schematisation objects in this category are:

* :ref:`1d_lateral`
* :ref:`2d_lateral`
* :ref:`dry_weather_flow`
* :ref:`dry_weather_flow_map`
* :ref:`dry_weather_flow_distribution`
* :ref:`surface`
* :ref:`surface_map`
* :ref:`surface_parameters`

.. _1d_lateral:

1D Lateral
----------

Defines a lateral discharge (source or sink term) for the 1D domain


Layer name
^^^^^^^^^^

lateral_1d

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
   * - Offset
     - offset
     - integer
     - No
     - seconds
     - The lateral will be applied *offset* seconds after the start of the simulation
   * - Units
     - units
     - text
     - Yes
     - \-
     - Units of the lateral flux. Possible values: 'm3/s'
   * - Time units
     - time_units
     - text
     - Yes
     - \-
     - Units of the time step. Possible values: 'seconds', 'minutes', 'hours'
   * - Interpolate
     - interpolate
     - boolean
     - Yes
     - \-
     - True: flux will be interpolated between time steps. False: flux will remain contant until the next time step 
   * - Time series
     - timeseries
     - text
     - Yes
     - \-
     - CSV-style table of 'time_step,value' pairs, separated by newline character. 
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`connection_node`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _1d_lateral_notes_for_modellers:

Notes for modellers
^^^^^^^^^^^^^^^^^^^
1D laterals placed on a connection node with a 1D boundary condition will be ignored.

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in seconds, minutes or hours since the start of the simulation) in the first column and the value (m³/s) in the second column. For example::

    0,0.2
    15,10.0
    30,20.0
    45,7.5
    60,0.0

- The time series string cannot contain any spaces or empty rows
- The lateral time series is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.
- When posted to the 3Di server, the time steps will be converted to seconds. If you upload a CSV file with lateral time series via the simulation wizard, the time units should always be in *seconds* (see :ref:`simulate_api_qgis_laterals`)
- Positive values represent a source (water is added to the node), negative values represent a sink (water is extracted from the node to the extent that this water is available in the node)
- The time series does not need to cover the entire simulation period.
- When editing the time series field in using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    '0,0.2'||char(10)||'15,10.0'||char(10)||'30,20.0'||char(10)||'45,7.5'||char(10)||'60,0.0'


.. _2d_lateral:

2D Lateral
----------

Lateral discharge for 2D cell. The lateral flux will be added or subtracted from the cell the lateral is in.

Layer name
^^^^^^^^^^

lateral_2d

Geometry
^^^^^^^^

Point

Attributes
^^^^^^^^^^

.. list-table:: 2D Lateral attributes
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
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Lateral type
     - type
     - integer
     - Yes
     - \-
     - Possible values: 1 (Surface lateral)
   * - Offset
     - offset
     - integer
     - No
     - seconds
     - The lateral will be applied *offset* seconds after the start of the simulation
   * - Units
     - units
     - text
     - Yes
     - \-
     - Units of the lateral flux. Possible values: 'm3/s'
   * - Time units
     - time_units
     - text
     - Yes
     - \-
     - Units of the time step. Possible values: 'seconds', 'minutes', 'hours'
   * - Interpolate
     - interpolate
     - boolean
     - Yes
     - \-
     - True: flux will be interpolated between time steps. False: flux will remain contant until the next time step	 
   * - Time series
     - timeseries
     - text
     - Yes
     - \-
     - CSV-style table of 'time_step,value' pairs, separated by newline character. 
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`


.. _2d_lateral_notes_for_modellers:

Notes for modellers
^^^^^^^^^^^^^^^^^^^

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in seconds, minutes or hours since the start of the simulation) in the first column and the value (m³/s) in the second column. For example::

    0,0.2
    15,10.0
    30,20.0
    45,7.5
    60,0.0

- The time series string cannot contain any spaces or empty rows
- The lateral time series is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.
- When posted to the 3Di server, the time steps will be converted to seconds. If you upload a CSV file with lateral time series via the simulation wizard, the time units should always be in *seconds* (see :ref:`simulate_api_qgis_laterals`)
- Positive values represent a source (water is added to the node), negative values represent a sink (water is extracted from the node to the extent that this water is available in the node)
- The time series does not need to cover the entire simulation period.
- When editing the time series field in using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    '0,0.2'||char(10)||'15,10.0'||char(10)||'30,20.0'||char(10)||'45,7.5'||char(10)||'60,0.0'


.. _dry_weather_flow:

Dry weather flow
----------------

Location that produces a specified sewerage flow. The dry weather flow production varies throughout the day, as defined in the referenced :ref:`dry_weather_flow_distribution` record.

The geometry is purely administrative, helping you to understand where the dry weather flow is produced (e.g. a specific building, a housing block or industrial area).

Layer name
^^^^^^^^^^

dry_weather_flow

Geometry
^^^^^^^^

Polygon

Attributes
^^^^^^^^^^

.. list-table:: Dry weather flow attributes
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
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Daily total
     - daily_total
     - decimal number
     - Yes
     - Liters
     - Total dry weather flow production per day (before multiplier is applied). Can be used as e.g. dry weather flow production per inhabitant.
   * - Multiplier
     - multiplier
     - decimal number
     - Yes
     - \-
     - Daily total is multiplied by this number. Can be used as e.g. number of inhabitants.
   * - Distribution
     - dry_weather_flow_distribution_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`dry_weather_flow_distribution`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`


.. _dry_weather_flow_map:

Dry weather flow map
--------------------

Connection between a :ref:`dry_weather_flow` feature and its target connection node.

Layer name
^^^^^^^^^^

dry_weather_flow_map

Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^

.. list-table:: Dry weather flow map attributes
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
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Percentage
     - percentage
     - decimal number
     - Yes
     - %
     - Percentage of DWF produced by the referenced :ref:`dry_weather_flow` feature that should flow to the referenced connection_node
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`connection_node`
   * - Dry weather flow ID
     - dry_weather_flow_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`dry_weather_flow`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _dry_weather_flow_distribution:

Dry weather flow distribution
-----------------------------

Intra-day distribution of dry weather flow production over a 24 hour period. The first value is for the first hour (00:00-01:00), the second value for 01:00-02:00. 

Layer name
^^^^^^^^^^

dry_weather_flow_distribution

Geometry
^^^^^^^^
No geometry

Attributes
^^^^^^^^^^

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
   * - Description
     - description
     - text
     - Yes
     - %
     - Exactly 24 comma-separated values that must add up to 100
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _surface:

Surface
-------

Definition of 0D inflow surface using custom rainfall-runoff parameters. See :ref:`0d_rain` for further details.

Layer name
^^^^^^^^^^

surface

Geometry
^^^^^^^^

Polygon

Attributes
^^^^^^^^^^

.. list-table:: Surface attributes
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
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Area
     - area
     - decimal number
     - Yes
     - m:sup:`2`
     - Area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * - Surface parameters
     - surface_parameters_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`surface_parameters`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _surface_map:

Surface map
-----------

Connection between a surface and its target connection node.

.. list-table:: Surface map attributes
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
   * - Display name
     - display_name
     - text
     - No
     - \-
     - Name field, no constraints
   * - Percentage
     - percentage
     - decimal number
     - Yes
     - %
     - Percentage of runoff produced by the referenced :ref:`surface` feature that should flow to the referenced connection_node
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`connection_node`
   * - Surface ID
     - surface_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in :ref:`surface`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _surface_parameters:

Surface parameters
------------------

Custom rainfall-runoff parameters to be used by surfaces. By default, the surface parameters table is populated with the parameter set from the Dutch NWRW model for sewerage inflow; you can add other parameterisations as you see fit.

Layer name
^^^^^^^^^^

surface_parameters

Geometry
^^^^^^^^

No geometry

Attributes
^^^^^^^^^^

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
   * - Description
     - description
     - text
     - Yes
     - %
     - Exactly 24 comma-separated values that must add up to 100
   * - Surface layer thickness
     - surface_layer_thickness
     - decimal number
     - mm
     - Storage on the surface
   * - Outflow delay
     - outflow_delay
     - decimal number
     - min\ :sup:`-1`
     - Outflow delay constant :math:`k_q`
   * - Infiltration
     - infiltration
     - boolean
     - \-
     - Switches infiltration on or off
   * - Min. infiltration capacity
     - min_infiltration_capacity
     - decimal number
     - mm/h
     - Equilibrium (minimum) infiltration rate :math:`f_c`
   * - Max. infiltration capacity
     - max_infiltration_capacity
     - decimal number
     - mm/h
     - Initial (maximum) infiltration rate :math:`f_0`
   * - Infiltration decay constant
     - infiltration_decay_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration decay constant :math:`k_d`
   * - Infiltration recovery constant
     - infiltration_recovery_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration recovery constant :math:`k_r`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`
