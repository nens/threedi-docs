.. _structure_control_objects:

Structure control objects
=========================

Structure control objects allow you to let structures react to changes in flow variables such as water level or flow velocity, see :ref:`control`. To define them in the schematisation, the following objects are available:

* :ref:`2d_boundary_condition`


.. _control_the_layer:

Control
-------

This object connects a *Control timed*, *Control table* or *Control memory* to a control group and (optionally to a measure group), and defines the period in which it is active.


Geometry
^^^^^^^^
No geometry

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
     - seconds ???
     - ????
   * - start
     - text
     - ????
     - ????
     - ????
   * - end
     - text
     - ????
     - ????
     - ????


