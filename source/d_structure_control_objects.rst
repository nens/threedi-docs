.. _structure_control_objects:

Structure control objects
=========================

Structure control objects allow you to let structures react to changes in flow variables such as water level or flow velocity, see :ref:`control`. To define them in the schematisation, the following objects are available:

* :ref:`layer_measure_location`
* :ref:`layer_memory_control`
* :ref:`layer_table_control`
* :ref:`layer_measure_map`

To get started with schematising structure control, read :ref:`this practical introduction guide<schematising_structure_control>`.


.. _schematising_structure_control:

Schematising structure control
------------------------------

To schematise structure control, follow these steps:

* Add a :ref:`layer_measure_location` to a connection node
* Add a :ref:`layer_memory_control` or a :ref:`layer_table_control` to a weir, orifice, or pump
* Add a :ref:`layer_measure_map`, which is a line from the :ref:`layer_measure_location` to the :ref:`layer_memory_control` or :ref:`layer_table_control`
* Make sure *Use structure control* in :ref:`simulation_template_settings` is set to *True*.

.. note::
    Timed control cannot be included in the schematisation. You can only add timed control to the simulation; they can also be saved in a simulation template.

.. _layer_measure_location:

Measure location
----------------

A location at which the water level or volume is measured, to serve as input for a :ref:`layer_memory_control` or :ref:`layer_table_control`.

Layer name
^^^^^^^^^^

measure_location

Geometry
^^^^^^^^

Point

Attributes
^^^^^^^^^^

.. list-table:: Measure location attributes
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
   * - Measure variable
     - measure_variable
     - text
     - Yes
     - \-
     - Valid values: *water_level*, *volume*
   * - Connection node ID
     - connection_node_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in the *Connection node* table
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _layer_memory_control:

Memory control
--------------

This object defines a :ref:`memory_control`.

Layer name
^^^^^^^^^^

memory_control

Geometry
^^^^^^^^

Point

Attributes
^^^^^^^^^^

.. list-table:: Memory control attributes
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
   * - Upper threshold
     - upper_threshold
     - decimal number
     - Yes
     - Depends on the *Measure variable* of the :ref:`layer_measure_location`. *Water level*: m MSL; *Volume*: m³.
     - See :ref:`memory_control`
   * - Lower threshold
     - lower_threshold
     - decimal number
     - Yes
     - Depends on the *Measure variable* of the :ref:`layer_measure_location`. *Water level*: m MSL; *Volume*: m³.
     - See :ref:`memory_control`
   * - Is inverse
     - is_inverse
     - boolean
     - Yes
     - \-
     - If set to *True*, the memory control is inverted, see :ref:`memory_control`
   * - Is active
     - is_active
     - boolean
     - Yes
     - \-
     - If *True*, the control is active at the start of the simulation, see :ref:`memory_control`
   * - Target type
     - target_type
     - text
     - Yes
     - \-
     - See :ref:`note_target_types`.
   * - Target ID
     - target_id
     - integer
     - Yes
     - \-
     - ID of the feature in the table specified by *target_type*
   * - Action_type
     - action_type
     - text
     - Yes
     - \-
     - Choose from *set_discharge_coefficients*, *set_crest_level*, *set_gate_level*, or *set_pump_capacity*.
   * - Action value 1
     - action_value_1
     - decimal number
     - Yes
     - Depends on the *Action type*.
	     
		 - Set crest level: m MSL
		 - Set gate level: m MSL
		 - Set pump capacity: L/s
		 - Set discharge coefficients: unitless
     - The value to which the structure property must be set when the upper threshold is passed (or lower threshold when *Is inverse* is *True*).
   * - Action value 2
     - action_value_2
     - decimal number
     - Only if *Action type* is *Set discharge coefficients*
     - unitless
     - The value to which the negative discharge coefficient must be set when the upper threshold is passed (or lower threshold when *is_inverse* is ``True``).
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _layer_table_control:

Table control
--------------

This object defines a :ref:`table_control`.

Layer name
^^^^^^^^^^

table_control

Geometry
^^^^^^^^

Point

Attributes
^^^^^^^^^^

.. list-table:: Table control attributes
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
   * - Target type
     - target_type
     - text
     - Yes
     - \-
     - See :ref:`note_target_types`.
   * - Target ID
     - target_id
     - integer
     - Yes
     - \-
     - ID of the feature in the table specified by *target_type*
   * - Action_type
     - action_type
     - text
     - Yes
     - \-
     - Choose from *set_discharge_coefficients*, *set_crest_level*, *set_gate_level*, or *set_pump_capacity*.
   * - Measure operator
     - measure_operator
     - text
     - Yes
     - \-
     - Choose from *>* or *<*. See :ref:`table_control`.
   * - Action table
     - action_table
	 - text
	 - Yes
	 - \-
	 - :ref:`action_table_formatting<CSV-style table>` that defines the value to set when the measured value exceeds or falls below the specified value.
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _action_table_formatting:

Action table formatting
^^^^^^^^^^^^^^^^^^^^^^^

The *Action table* is a CSV-style table with three columns. The columns are comma-separated, the rows are newline-separated. Example for action type *Set crest level* (note the comma at the end of each row)::
    
	-1.7,-1.4,
	-1.6,-1.3,
	-1.5,-1.2,

Example for an action table for a timed control with action type *Set discharge coefficients* that changes the discharge coefficients after 1, 2, and 3 hours::
    
    3600,0,0
	7200,0.5,0.5
	10800,1,1

The first column contains the value to compare the measured value to. The second column contains the value to set the structure property to (e.g. weir crest level). The third column is only used when the *Action type* is *Set discharge coefficients*, to store the negative discharge coefficient. For all other action types, leave this column empty. 

When editing the action table using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    '-1.7,-1.4,'||char(10)||'-1.6,-1.3,'||char(10)||'-1.5,-1.2,'



.. _layer_measure_map:

Measure map
-----------

This object maps a :ref:`layer_measure_location` to a :ref:`layer_table_control` or :ref:`layer_memory_control`.

Layer name
^^^^^^^^^^

measure_map

Geometry
^^^^^^^^

Linestring (exactly two vertices)

Attributes
^^^^^^^^^^

.. list-table:: Table control attributes
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
   * - Measure location ID
     - measure_location_id
     - integer
     - Yes
     - \-
     - Foreign key reference to an ID in the :ref:`layer_measure_location` table
   * - Control type
     - control_type
     - text
     - Yes
     - \-
     - Valid values: 'table', 'memory'
   * - Control ID
     - control_id
     - integer
     - Yes
     - \-
     - ID of a feature in the table specified by *Control type*
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

 

.. _note_target_types:

Notes on target types
---------------------

- References to target types must include the *v2_* prefix. This is a legacy of the table names in the schematisation database as defined up until March 2025 that has been upheld for reasons of backward compatibility.
- In the schematisation, Mmemory and table control cannot be specified for culverts, channels, and pipes. Please contact the :ref:`servicedesk` if you need this feature.