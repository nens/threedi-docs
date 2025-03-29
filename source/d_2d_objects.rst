.. _2d_objects:

2D Objects
==========

2D objects define properties of the computational grid of the :ref:`2D domain <computational_grid_2d_domain>`. There are several 2D objects:

* :ref:`2d_boundary_condition`
* :ref:`obstacle`
* :ref:`grid_refinement_area`
* :ref:`grid_refinement_line`
* :ref:`dem_average_area`

.. _2d_boundary_condition:

2D Boundary Condition
---------------------

Boundary condition for 2D model edge. Boundary conditions define the interactions between the modeled area and its surroundings. They define how water flows into or out of the model domain.

Layer name
^^^^^^^^^^

boundary_condition_2d

Geometry
^^^^^^^^

Line

Geometry requirements: 

- 2D boundary condition line can only touch boundary computational cells. These are defined as cells having at least one side that does not share an edge with another computational cell. This is often a cell at the outer edge of the model domain. It is also possible to schematise 2D boundaries on an inner edge of the model domain, i.e. if there is a NODATA hole in the DEM. 

- 2D boundary condition lines must intersect with one or more computational cells.

- When multiple computational cells are touched by the 2D boundary condition line, it is essential that these cells align either vertically or horizontally. Diagonal alignment is not permitted.

- All cells intersected by a 2D boundary condition line must have the same size, i.e. do not use grid refinement at the location of a 2D boundary condition.

.. tip::
  When experiencing difficulties adding 2D boundary conditions, generate the computational grid locally using :ref:`computational_grid_from_schematisation`. This helps you see where the 2D boundary condition line is located relative to the computational cells. 


Attributes
^^^^^^^^^^

.. list-table:: 2D Boundary condition attributes
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
   * - Boundary type
     - type
     - integer
     - Yes
     - \-
     - Sets the type to 1: Water level, 2: Velocity, 3: Discharge, 5: Sommerfeld, 6: Groundwater level or 7: Groundwater discharge
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
     - True: values will be interpolated between time steps. False: values will remain contant until the next time step
   * - Time series
     - timeseries
     - text
     - Yes
     - [s, min, or h] and [m MSL, m/s, m/m, m³/s]
     - CSV-style table of 'time_step,value' pairs, separated by newline character.	 
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _2d_boundary_condition_notes_for_modellers:

Time series
"""""""""""

- Format the time series as Comma Separated Values (CSV), with the time (in seconds, minutes or hours since the start of the simulation) in the first column and the value (units dependent on the boundary type) in the second column. For example::

    0,145.20
    15,145.23
    30,145.35
    45,145.38
    60,145.15

- Units used are:
    - Water level: m MSL
	- Velocity: m/s
	- Discharge: m³/s
	- Sommerfeld: m/m
	- Groundwater level: m MSL
    - Groundwater discharge: m³/s

- The time series string cannot contain any spaces or empty rows

- The boundary condition time series is stored in the simulation template and is not part of the 3Di model itself. It can be overridden when starting a new simulation, without the need to create a new revision of the schematisation.

- When posted to the 3Di server, the time steps will be converted to seconds.

- For boundary types Velocity, Discharge and Sommerfeld, the sign of the input values determines the flow direction (see the figure below). If a 2D discharge or velocity boundary condition is placed at the eastern or northern edge of the model domain, and you want water to flow in (from east to west or from north to south), the values must be negative; if it is placed at the western or southern edge, the values must be positive to make the water flow in. For the Sommerfeld boundary, a positive value (gradient) means that the water level at the western/southern side is *lower* than the water level at the eastern/northern side, i.e. if placed at the east or north, this will result in boundary *inflow* and if placed at the west or south, it will result in boundary *outflow*.

    .. figure:: image/2d_boundary_flow_directions.png
       :alt: Flow directions for velocity and discharge boundaries

- Discharge values are applied to all intersected flowlines. So if the value is 5 m³/s and the geometry of the 2D boundary condition intersects 3 flowlines, the total in- or outflow will be 15 m³/s. Generate the computational grid locally using :ref:`computational_grid_from_schematisation` to determine how many flowlines are intersected.

- The time series must cover the entire simulation period.

- In case of multiple boundaries in one model: make sure they all have the same number of time series rows with the same temporal interval. This also applies if you have e.g. one 1D boundary and one 2D boundary.

- When editing the time series field in using SQL (sqlite dialect), use ``char(10)`` as line separator. The example time series shown above would look like this::

    "0,145.20"||char(10)||"15,145.23"||char(10)||"30,145.35"||char(10)||"45,145.38"||char(10)||"60,145.15"


.. _obstacle:

Obstacle
--------

Line with fixed crest level that overrides DEM values at edges of computational cells when calculating the cross-section between cells if they are lower than the obstacle crest level. Or, in other words, the exchange level of the flowlines that intersect with this obstacle will increased to the obstacle's crest level.

Layer name
^^^^^^^^^^

obstacle

Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^

.. list-table:: Obstacle attributes
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
   * - Crest level
     - crest_level
     - decimal number
     - Yes
     - m MSL
     - Exchange level of intersected flowlines will be updated to this value
   * - Affects 2D
     - affects_2d
     - boolean
     - No
     - \-
     - Determines wether 2D flowlines are :ref:`affected <obstacle_notes_for_modellers>`
   * - Affects 1D2D open water
     - affects_1d2d_open_water
     - boolean
     - No
     - \-
     - Determines wether 1D2D open water flowlines are :ref:`affected <obstacle_notes_for_modellers>`
   * - Affects 1D2D closed
     - affects_1d2d_closed
     - boolean
     - No
     - \-
     - Determines wether 1D2D closed flowlines are :ref:`affected <obstacle_notes_for_modellers>`
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _obstacle_notes_for_modellers:

Notes for modellers
^^^^^^^^^^^^^^^^^^^

You can fine-tune which types of flowlines are affected by the obstacle, by setting any combination of 2D, 1D-2D open water, and 1D-2d closed. "2D" refers to flowlines between two 2D cells. "1D-2D open water" refers to a flowline between a "1D open water" node and a 2D cell. "1D-2D closed" refers to a flowline between a "1D closed" node and a 2D cell. By default, any node that is part of a channel or connected to a channel is regarded as "open water" and all other 1D nodes are regarded as "closed". Older schematisations may use a different setting, see the setting *Node open water detection* in :ref:`model_settings`.



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

.. _grid_refinement_area:

Grid refinement area
--------------------

Polygon that sets local 2D calculation grid refinement.

Layer name
^^^^^^^^^^

grid_refinement_area

Geometry
^^^^^^^^

Polygon

Attributes
^^^^^^^^^^

.. list-table:: Grid refinement area attributes
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
   * - Grid level
     - grid_level
     - integer
     - Yes
     - \-
     - Set this to 1 to let all intersected cells have the :ref:`minimum cell size<model_settings>`. Each increase by 1 doubles the cell size. The grid level cannot exceed the number of grid levels set in :ref:`model_settings`.
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _grid_refinement_line:

Grid refinement line
--------------------

Line that sets local 2D calculation grid refinement.

Layer name
^^^^^^^^^^

grid_refinement_line

Geometry
^^^^^^^^

Line

Attributes
^^^^^^^^^^

.. list-table:: Grid refinement line attributes
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
   * - Grid level
     - grid_level
     - integer
     - Yes
     - \-
     - Set this to 1 to let all intersected cells have the :ref:`minimum cell size<model_settings>`. Each increase by 1 doubles the cell size. The grid level cannot exceed the number of grid levels set in :ref:`model_settings`.
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`

.. _dem_average_area:

DEM average area
----------------

Polygon that determine in which cells DEM averaging should be applied.

Layer name
^^^^^^^^^^

dem_average_area

Geometry
^^^^^^^^

Polygon

Attributes
^^^^^^^^^^

.. list-table:: DEM average area attributes
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
   * - Tags
     - tags
     - text
     - No
     - \-
     - Comma-separated list of foreign key references to ID's in :ref:`tag`
