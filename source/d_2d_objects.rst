.. _2d_objects:

2D Objects
==========

2D objects are calculated in the :ref:`2D domain <computational_grid_2d_domain>`. There are several 2D objects:

* :ref:`2d_boundary_condition`
* :ref:`2d_lateral`
* :ref:`linear_obstacle`
* :ref:`grid_refinement`
* :ref:`grid_refinement_area`
* :ref:`dem_average_area`
* :ref:`windshielding`

\
\

.. _2d_boundary_condition:

2D Boundary Condition
---------------------
Boundary condition for 2D model edge. Boundary conditions are crucial in hydraulic modeling because they define the interactions between the modeled area and its surroundings. They help simulate how water flows into or out of the simulation domain and how different types of forces, like inflows, outflows, water levels, or water velocities, are accounted for at the edges of the simulated region.

Geometry
^^^^^^^^
Line

Attributes
^^^^^^^^^^

.. list-table:: 2D Boundary condition attributes
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
   * - display_name
     - text
     - Yes
     - \-
     - Name field, no constraints
   * - boundary_type
     - text
     - Yes
     - \-
     - Sets the type to Waterlevel, Velocity, Discharge, Sommerfeld, Groundwater level or Groundwater discharge
   * - timeseries
     - text
     - Yes
     - [minutes since start of simulation],[m | m/s | m³/s]
     - Timeseries of water levels, flow velocities, discharges or water level gradients to be forced on the model boundary

.. _2d_boundary_condition_notes_for_modellers:

Time series
"""""""""""
Format the time series as Comma Separated Values (CSV), with the time (in minutes since the start of the simulation) in the first column and the value (units dependent on the boundary type) in the second column. For example::

    0,145.20
    15,145.23
    30,145.35
    45,145.38
    60,145.15

- The time series string cannot contain any spaces or empty rows

.. VRAAG: Nog niet zo uitgebreid als hij bij 1d objects is op het moment. Heb een heleboel punten rondom de notes for modellers weg gehaald omdat ik niet wist of het ook voor 2d boundary condition telte. moet een 2d boundary condition altijd deels buiten de dem vallen? 

\
\

.. _2d_lateral:

2D Lateral
---------------------
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



.. _linear_obstacle:

Linear obstacle
---------------
Line with fixed crest level that overrides DEM values at edges of computational cells when calculating the cross-section between cells.

Geometry
^^^^^^^^
Line

Attributes
^^^^^^^^^^

.. list-table:: Linear obstacle attributes
   :widths: 4 4 2 4 30
   :header-rows: 1

   * - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - fid
     - integer
     - Yes
     - \-
     - Unique identifier
   * - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - code
     - text
     - No
     - \-
     - Name field, no constraints
   * - crest_level
     - decimal number
     - No
     - m MSL
     - Lowest point of the obstacle

\
\

.. _grid_refinement:

Grid refinement
---------------
Lines that determine local 2D calculation grid refinement.

Geometry
^^^^^^^^
Line

Attributes
^^^^^^^^^^

.. list-table:: Grid refinement attributes
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
   * - display_name
     - text
     - Yes
     - \-
     - Name field, no constraints
   * - code
     - text
     - Yes
     - \-
     - Name field, no constraints
   * - refinement_level
     - integer
     - Yes
     - \-
     - The maximum number of grid-refinement levels. See :ref:`computational_grid` for more details.

\
\

.. _grid_refinement_area:

Grid refinement area
--------------------
Polygons that determine local 2D calculation grid refinement.

Geometry
^^^^^^^^
Polygon

Attributes
^^^^^^^^^^

.. list-table:: Grid refinement area attributes
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
   * - display_name
     - text
     - Yes
     - \-
     - Name field, no constraints
   * - code
     - text
     - Yes
     - \-
     - Name field, no constraints
   * - refinement_level
     - integer
     - Yes
     - \-
     - The maximum number of grid-refinement levels. See :ref:`computational_grid` for more details.

\
\

.. _dem_average_area:

DEM average area
----------------
Polygons that determine in which cells DEM averaging should be applied.

Geometry
^^^^^^^^
Polygon

Attributes
^^^^^^^^^^

.. list-table:: Dem average area attributes
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


\
\

.. VRAAG: Ik heb geen idee wat windshilding inhoudt!! Dus ik heb maar wat gedaan hier. graag critisch checken! 

.. _windshielding:

Windshielding
-------------
Windshield a channel from the prevailing winds, affecting the distribution of rainfall and subsequently impacting the hydrological processes in the region.

.. VRAAG: klopt dit?

Geometry
^^^^^^^^
No geometry

Attributes
^^^^^^^^^^

.. list-table:: Windshielding attributes
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
   * - channel_id
     - integer
     - No
     - \-
     - ID of the channel
   * - north
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the north.
   * - northeast
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the northeast .
   * - east
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the east.
   * - southeast
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the southeast.
   * - south
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the south.
   * - southwest
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the southwest.
   * - west
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the west.
   * - northwest
     - decimal number
     - No
     - \-
     - The amount of wind being shielded from the northwest.

