.. _inflow_objects:

Laterals & 0D inflow
====================

Laterals add or subtract water from the model domain. 0D inflow includes flow from *Surfaces* and dry weather flow. Surfaces calculate runoff from rain onto a predefined surface area, using a simple hydrological calculation. Dry weather flow is a specific type of lateral, used to simulate the inflow into sanitary sewers from households and industry.

For more information see:

* :ref:`laterals`
* :ref:`0d_rain`

Schematisation objects in this category include:

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


.. _2d_lateral:

2D Lateral
----------
Lateral discharge for 2D cell.

Geometry
^^^^^^^^
Point

Attributes
^^^^^^^^^^

.. list-table:: 2D Lateral attributes
   :widths: 4 4 2 4 30
   :header-rows: 1

   * - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - type
     - text
     - Yes
     - \-
     - Type of 2D lateral: Surface
   * - timeseries
     - text
     - Yes
     - [minutes since start of simulation],[m³/s]
     - Timeseries of lateral discharges to be added to the specified location

.. _2d_lateral_notes_for_modellers:

Notes for modellers
^^^^^^^^^^^^^^^^^^^

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in minutes since the start of the simulation) in the first column and the value (m³/s) in the second column. For example::

    0,0.2
    15,10.0
    30,20.0
    45,7.5
    60,0.0

- The time series string cannot contain any spaces or empty rows

.. TODO: 
    Nog niet zo uitgebreid als hij bij 1d objects is op het moment. misschien wel relevanten dingen weggelaten nu

.. _dry_weather_flow:

Dry weather flow
----------------

Location that produces a specified sewerage flow. The dry weather flow production varies throughout the day, as defined in the referenced :ref:`dry_weather_flow_distribution` record.

The geometry is purely administrative, helping you to understand where the dry weather flow is produced (e.g. a specific building, a housing block or industrial area).

Geometry
^^^^^^^^

Polygon

Attributes
^^^^^^^^^^

.. list-table:: Dry weather flow attributes
   :widths: 4 4 2 4 30
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


Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^


.. list-table:: Dry weather flow map attributes
   :widths: 4 4 2 4 30
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

Definition of 0D inflow surface using custom rainfall-runoff parameters.

See :ref:`0d_rain` for further details.

.. list-table:: Surface attributes
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - area
     - decimal number
     - m\ :sup:`2`
     - The area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * - surface_parameters_id
     - integer
     - N/A
     - Reference to the row in the `Surface parameters` table that is to be used for this surface

.. _surface_map:

Surface map
-----------

Connection between a surface and its target connection node.

.. list-table:: Surface map attributes
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - connection_node_id
     - integer
     - N/A
     - Reference to the connection node to which the inflow from the referenced `Surface` should be mapped
   * - percentage
     - decimal number
     - N/A
     - Percentage of the runoff produced by the referenced `Surface` that should flow to the referenced connection_node
   * - surface_id
     - integer
     - N/A
     - Reference to the `Surface` feature to be mapped

.. _surface_parameters:

Surface parameters
------------------

Custom rainfall-runoff parameters to be used by surfaces. By default, the surface parameters table is populated with the parameter set from the Dutch NWRW model for sewerage inflow; you can add other parameterisations as you see fit.

.. list-table:: Surface parameters
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - infiltration
     - boolean
     - N/A
     - Switch infiltration on (1) or off (0)
   * - infiltration_decay_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration decay constant :math:`k_d`
   * - infiltration_recovery_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration recovery constant :math:`k_r`
   * - max_infiltration_capacity
     - decimal number
     - mm/h
     - Initial (maximum) infiltration rate :math:`f_0`
   * - min_infiltration_capacity
     - decimal number
     - mm/h
     - Equilibrium (minimum) infiltration rate :math:`f_c`
   * - outflow_delay
     - decimal number
     - min\ :sup:`-1`
     - Outflow delay constant :math:`k_q`
   * - surface_layer_thickness
     - decimal number
     - mm
     - Storage on the surface
