.. _structure_control_objects:

Structure control objects
=========================

Structure control objects allow you to let structures react to changes in flow variables such as water level or flow velocity, see :ref:`control`. To define them in the schematisation, the following objects are available:

* :ref:`2d_boundary_condition`


.. _control_the_layer:

Control
-------

This object connects a *Control timed*, *Control table* or *Control memory* to a control group and (optionally to a measure group), and defines the period in which it is active.


Attributes
^^^^^^^^^^

.. list-table:: Control attributes
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
   * - control_id
     - integer
     - Yes
     - \-
     - Sets the row in the *Control timed*, *Control table*, or *Control memory* table (depending on the *Control type*) to be used for this control
   * - control_group_id
     - integer
     - Yes
     - \-
     - ID of the control group that this control is part of.
   * - control_type
     - integer
     - Yes
     - \-
     - Choose from "timed", "table", or "memory"
   * - measure_group_id
     - integer
     - If control_type is "table" or "memory"
     - \-
     - ID of the measure group that supplies the measured value for this control
   * - measure_frequency
     - integer
     - No
     - \-
     - Not implemented
   * - start
     - text
     - No
     - seconds since start of simulation
     - Start of period in which this control is active. If not filled in, starts at t=0.
   * - end
     - text
     - No
     - seconds since start of simulation
     - End of period in which this control is active. If not filled in, ends at end of simulation.


.. _control_group:

Control group
-------------

This object groups one or more *Control* objects. It is referred to from the *Global settings*. Only one control group can be used at the same time, so usually there is only one control group.

Attributes
^^^^^^^^^^

.. list-table:: Control group attributes
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
   * - name
     - text
     - No
     - \-
     - Name of this control group
   * - description
     - text
     - No
     - \-
     - Description of this control group


.. _control_measure_group:

Control measure group
---------------------

This object defines control measure groups, which calculate a weighted average of the measured values. Each *Control measure map* is part of a *Control measure group*. A *Control* uses a single measure group to retrieve measured values.

Attributes
^^^^^^^^^^

.. list-table:: Control measure group attributes
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



.. _control_measure_map:

Control measure map
---------------------

This object defines control measure maps, which define the weight and the object. Each *Control measure map* is part of a *Control measure group*. A *Control* uses a single measure group to retrieve measured values.

Attributes
^^^^^^^^^^

.. list-table:: Control measure map attributes
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
   * - measure_group_id
     - integer
     - Yes
     - \-
     - Determines to which group the measured value belongs
   * - object_id
     - integer
     - Yes
     - \-
     - Reference to the ID of the connection node on which the measurement should be made
   * - object_type
     - text
     - Yes
     - \-
     - Currently, only "v2_connection_nodes" is supported.
   * - weight
     - decimal number
     - Yes
     - \-
     - Value between 0 and 1. The weight of this measurement in calculating the weighted average of the whole group. All weights for one group must add up to 1.

.. _control_table:

Control table
-------------

This object defines a :ref:`table_control`.

Attributes
^^^^^^^^^^

.. list-table:: Control table attributes
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
   * - action_type
     - text
     - Yes
     - \-
     - Choose from *set_discharge_coefficients*, *set_crest_level*, *set_gate_level*, or *set_pump_capacity*.
   * - action_table
     - integer
     - Yes
     - \-
     - See :ref:`action_table`
   * - measure_operator
     - text
     - Yes
     - \-
     - Choose from *>* or *<*. See :ref:`table_control`.
   * - target_type
     - text
     - Yes
     - \-
     - Choose from *v2_pumpstation*, *v2_pipe*, *v2_orifice*, *v2_culvert*, *v2_weir*, or *v2_channel*.
   * - target_id
     - decimal number
     - Yes
     - \-
     - ID of the feature in the table specified by *target_type*
   * - measure_variable
     - text
     - Yes
     - \-
     - Choose from *waterlevel*, or *volume*
    
.. _control_timed:

Control timed
-------------

This object defines a :ref:`timed_control`.

Attributes
^^^^^^^^^^

.. list-table:: Control timed attributes
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
   * - action_type
     - text
     - Yes
     - \-
     - Choose from *set_discharge_coefficients*, *set_crest_level*, *set_gate_level*, *set_pump_capacity*
   * - action_table
     - integer
     - Yes
     - \-
     - See :ref:`action_table`
   * - target_type
     - text
     - Yes
     - \-
     - Choose from *v2_pumpstation*, *v2_pipe*, *v2_orifice*, *v2_culvert*, *v2_weir*, *v2_channel*
   * - target_id
     - decimal number
     - Yes
     - \-
     - ID of the feature in the table specified by *target_type*
	 
	 
.. action_table:

Action table formatting
-----------------------

*Control timed* and *Control table* objects have an attribute *action_table*. This is a table stored in a text field. The format is as follows:

- Lines or rows are seperated by a "#" character
- Columns are separated by a ";" character
- The first column contains the time in seconds since the start of the simulation (*Control timed*), or the threshold values (in a *Control table*).
- The second column contains the action values, i.e. the value for the crest level [m MSL], gate level [m MSL], pump capacity [L/s] or discharge coefficients [-] to be set.
- If the *action_type* is *set_discharge_coefficients*, the second column contains two values instead of one. These two values are separated by a space.

Example for an action table for a table control with action type *set_crest_level*: ``-1.7;-1.4#-1.6;-1.3#-1.5;-1.2``.

Example for an action table for a timed control with action type *set_discharge_coefficients*, that changes the discharge coefficients after 1, 2, and 3 hours: ``3600;0 0#7200;0.5 0.5#10800;1 1``.
