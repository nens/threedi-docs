.. _1d2d_objects:

1D2D Objects
============

1D2D objects regulate the :ref:`exchange <1d2d_exchange>` between :ref:`1d_objects` and the :ref:`2D domain <2d_objects>`. There are two 1D2D objects in 3Di models:

* :ref:`exchange_line`
* :ref:`potential_breach`

.. _exchange_line:

Exchange line
-------------
Line that determines which 2D cells the calculation points of a :ref:`Channel` connect to. A 1D2D connection is created from each calculation point on the Channel to the cell in which the closest point on the Exchange line is located. Applies only to channels with :ref:`calculation_types` 'connected' or 'double connected'. The page :ref:`Editing schematisations <generate_exchange_lines>` contains information on generating exchange lines.

Layer name
^^^^^^^^^^

exchange_line

Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^

.. list-table:: 1D2D Exchange line attributes
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
   * - Exchange level [m MSL]
     - exchange_level
     - decimal number
     - Yes
     - m MSL
     - Exchange level for the 1D2D connections. See :ref:`1d2d_exchange` 
   * - Channel ID
     - channel_id
     - integer
     - Yes
     - \-
     - ID of the channel
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _potential_breach:

Potential breach
----------------

Line from a Channel to a 2D cell, to create a potential breach location. At these locations, the 1D2D connection can be :ref:`breached<breaches>` during the simulation.

Layer name
^^^^^^^^^^

potential_breach

Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^

.. list-table:: 1D2D Potential breach attributes
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
   * - Initial exchange level
     - initial_exchange_level
     - decimal number
     - Yes
     - m MSL
     - Exchange level for the 1D2D connection when the breach has not been activated yet
   * - Final exchange level
     - final_exchange_level
     - decimal number
     - No
     - m MSL
     - Breach will grow down to this level, before growing in width.
   * - Levee material
     - levee_material
     - text
     - No
     - \-
     - Set the material of the levee: sand (1) or clay (2)
   * - Channel ID
     - channel_id
     - integer
     - Yes
     - \-
     - ID of the channel
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`
