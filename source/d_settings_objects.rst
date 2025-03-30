.. _settings_objects:

Settings objects
================

Objects in this category contain the settings that govern several aspects of the model and the simulation template. Tags are also included in this category.

* :ref:`model_settings`
* :ref:`aggregation_settings`
* :ref:`numerical_settings`
* :ref:`hp_groundwater`
* :ref:`physical_settings`
* :ref:`simulation_template_settings`
* :ref:`tag`

.. _model_settings:

Model settings
------------------

Defines the settings that are needed in the creation of a 3Di model (computational grid and subgrid tables).

Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

model_settings

Attributes
^^^^^^^^^^

.. list-table:: Model settings attributes
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
   * - DEM file
     - dem_file
     - Text
     - No
     - m MSL
     - Name of the DEM file (*.tif)
   * - Minimum cell size
     - minimum_cell_size
     - Integer
     - Yes
     - m
     - The width/length of the smallest possible 2D computation cell. See :ref:`computational_grid` for more details.
   * - Number of grid levels
     - nr_grid_levels
     - Integer
     - Yes
     - \-
     - The maximum number of 2D cell sizes, doubling in size each time. See :ref:`computational_grid` for more details.
   * - Calculation point distance 1D
     - calculation_point_distance_1d
     - Decimal number
     - Yes
     - \-
     - Maximum distance between calculation points for line elements. This global value is superseded in case it is specified for the specific 1D object.
   * - Minimum table step size
     - minimum_table_step_size
     - Decimal number
     - Yes
     - m
     - Defines the height interval between successive increments in the subgrid tabulation. See :ref:`subgrid_tables` for more details.
   * - Maximum table step size
     - maximum_table_step_size
     - Decimal number
     - No
     - m
     - Defines the maximum height interval between successive increments in the subgrid tabulation. Defaults to 100 × *Minimum table step size*. See :ref:`subgrid_tables` for more details.
   * - Table step size 1D
     - table_step_size_1d
     - Decimal number
     - No
     - m
     - User-defined table step size/increment (m) for 1D cross-sections and volumes; see :ref:`subgrid_tables`. Defaults to *Minimum table step size*.
   * - Friction type
     - friction_type
     - Integer
     - Yes
     - \-
     - Defines the friction type for the 2D domain: *1: Chézy* or *2: Manning*. Make sure the friction type matches the friction coefficient (file).
   * - Friction coefficient
     - friction_coefficient
     - Decimal number
     - Yes
     - m\ :sup:`1/2`/s (Chézy) or s/m\ :sup:`1/3` (Manning)
     - Defines a friction coefficient for your schematisation. This global value is superseded in case a friction coefficient file is provided.
   * - Friction averaging
     - friction_averaging
     - Boolean
     - Yes
     - \-
     - Sets whether the friction values in a subgrid cell are averaged or not
   * - Friction coefficient file
     - friction_coefficient_file
     - Text
     - No
     - m\ :sup:`1/2`/s (Chézy) or s/m\ :sup:`1/3` (Manning)
     - Name of the friction coeffient file. This supersedes the global 2D friction coefficient.
   * - Use 1D flow
     - use_1d_flow
     - Boolean
     - No
     - \-
     - If false, no 1D network and 1D2D flowlines will be created when making the computational grid.
   * - Use 2D flow
     - use_2d_flow
     - Boolean
     - No
     - \-
     - If false, no 2D flowlines will be created when making the computational grid. Note that 2D cells (for storage) and 1D2D connections will still be made and used.
   * - Use 2D rain
     - use_2d_rain
     - Boolean
     - No
     - \-
     - Sets whether rain on the 2D domain is taken into account in a simulation.
   * - Use interception
     - use_interception
     - Boolean
     - No
     - \-
     - Sets the inclusion of interception in the 3Di model.
   * - Use interflow
     - use_interflow
     - Boolean
     - No
     - \-
     - Sets the inclusion of interflow in the 3Di model.
   * - Use simple infiltration
     - use_simple_infiltration
     - Boolean
     - No
     - \-
     - Sets the inclusion of simple infiltration in the 3Di model.
   * - Use vegetation drag 2D
     - use_vegetation_drag_2d
     - Boolean
     - No
     - \-
     - Sets the inclusion of 2D vegetation drag in the 3Di model.
   * - Use groundwater storage
     - use_groundwater_storage
     - Boolean
     - No
     - \-
     - If true, groundwater cells will be created. Switch on *Use groundwater flow* to also create groundwater flowlines.
   * - Use groundwater flow
     - use_groundwater_flow
     - Boolean
     - No
     - \-
     - If true, groundwater flowlines will be created. Switching on *Use groundwater storage* is required to use this option.
   * - Max. angle 1D advection
     - max_angle_1d_advection
     - Decimal number
     - No
     - Radians
     - Maximum angle at which advection is taken into account (should be between 0 and 0.5 π).
   * - Manhole aboveground storage area
     - manhole_aboveground_storage_area
     - Decimal number
     - For models with only 1D flow
     - m\ :sup:`2`
     - Storage area for connection nodes at street level. This global value is the surface area that each connection node is given when water reaches above the exchange level. To use this feature, set the connection node exchange types to *Connected*. Must be left empty when using only 2D flow.
   * - Embedded cutoff threshold
     - embedded_cutoff_threshold
     - Decimal number
     - No
     - \-
     - When an embedded channel intersects a 2D cell with a length shorter than the cell size × cutoff threshold, the embedded channel skips this 2D cell. This is useful for preventing very short embedded channel segments (which slow down your simulation).
   * - Node open water detection
     - node_open_water_detection
     - Decimal number
     - No
     - \-
     - Sets which calculation nodes are labelled as *open water* vs. *closed*. Choose between *0: Node is regarded as open water if at least one channel connects to it* (recommended) or *1: Node is regarded as open water if it has no storage area* (not recommended; for backward compatibility only)


.. _aggregation_settings:

Aggregation settings
--------------------

You can set multiple aggregation options for each *flow_variable* as long as the *aggregation_method* is not used twice for the same flow_variable. For more information about result aggregation, see :ref:`aggregationnetcdf`.

These settings are stored in the simulation template. You can change them before starting the simulation, without the need to regenerate the 3Di model.

Layer name
^^^^^^^^^^

aggregation_settings

Attributes
^^^^^^^^^^

.. list-table:: Aggregation settings attributes
   :widths: 20 20 15 10 15 40
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
   * - Flow variable
     - flow_variable
     - Text
     - Yes
     - \-
     - Variable that is to be aggregated. Text to fill in vs. how it is displayed in the 3Di Modeller Interface:
     
       - discharge (Discharge)
       - flow_velocity (Flow velocity)
       - pump_discharge (Pump discharge)
       - rain (Rain)
       - water_level (Water level)
       - wet_cross_section (Wet cross-sectional area)
       - wet_surface (Wet surface)
       - lateral_discharge (Lateral discharge)
       - volume (Volume)
       - simple_infiltration (Simple infiltration)
       - leakage (Leakage)
       - interception (Interception)
       - surface_source_sink_discharge (Surface source & sink discharge)
   * - Aggregation method
     - aggregation_method
     - Text
     - Yes
     - \-
     - The aggregation methods that can be used on a flow variable. Text to fill in vs. how it is displayed in the 3Di Modeller Interface:
     
       - avg (Average): Calculates the average value of the variable over the aggregation interval.
       - min (Minimum): Calculates the minimum value of the variable over the aggregation interval.
       - max (Maximum): Calculates the maximum value of the variable over the aggregation interval.
       - cum (Cumulative): Calculates the cumulative value of the variable over the aggregation interval by integrating over time [dt × variable].
       - med (Median): Calculates the median value of the variable over the aggregation interval.
       - cum_negative (Cumulative negative): Calculates the cumulative negative value of the variable over the aggregation interval by integrating over time [dt × variable].
       - cum_positive (Cumulative positive): Calculates the cumulative positive value of the variable over the aggregation interval by integrating over time [dt × variable].
       - current (Current): Uses the current value of a variable. This is only valid for volume and intercepted_volume.
   * - Interval
     - interval
     - Integer
     - Yes
     - s
     - Interval over which the aggregation will be calculated

.. _numerical_settings:

Numerical settings
------------------
 
Most users do not need to worry about these settings. More advanced users can change the default settings to improve their models. For more information on the numerical settings, see :ref:`numerics`.

These settings are stored in the simulation template. You can change them before starting the simulation, without the need to regenerate the 3Di model.

Layer name
^^^^^^^^^^

numerical_settings

Attributes
^^^^^^^^^^


.. list-table:: Numerical settings attributes
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
   * - General numerical threshold
     - general_numerical_threshold
     - Decimal number
     - No
     - \-
     - Generally used numerical threshold to avoid singularities due to limited numerical accuracy.
   * - Max. non-linear Newton iterations
     - max_non_linear_newton_iterations
     - Integer
     - Yes
     - \-
     - Maximum number of non-linear Newton iterations in a single time step. For more information, see :ref:`matrixsolvers`.
   * - Minimum convergence criterion for Newton's method
     - convergence_eps
     - Decimal number
     - Yes
     - \-
     - Minimal residual for convergence of Newton iteration. For more information, see :ref:`matrixsolvers`.
   * - Use nested Newton
     - use_nested_newton
     - Integer
     - Yes
     - \-
     - Choose between *0: For schematisations without closed cross-sections* and *1: For schematisations with closed cross-sections*. For more information, see :ref:`matrixsolvers`.
   * - Number of conjugate gradient method iterations
     - use_of_cg
     - Integer
     - Yes
     - \-
     - Number of iterations of the conjugate gradient method before switching to another method. For more information, see :ref:`matrixsolvers`.
   * - Convergence criterion for conjugate gradient method
     - convergence_cg
     - Decimal number
     - No
     - \-
     - Convergence criterion to iteratively solve matrices. For more information, see :ref:`matrixsolvers`.
   * - Use preconditioner conjugate gradient
     - use_preconditioner_cg
     - Boolean
     - No
     - \-
     - Preconditioner for the matrix solver. Setting this to True generally increases simulation speed. For more information, see :ref:`matrixsolvers`.
   * - Max. degree Gauss-Seidel
     - max_degree_gauss_seidel
     - Integer
     - Yes
     - \-
     - Determines the efficiency of the matrix solver. Advised values depend on the type of model:
     
       - Only 1D flow: 700
       - 1D and 2D flow: 7
       - Only surface 2D flow: 5
       - Surface and groundwater flow: 7
       - 1D, 2D surface and groundwater flow: 70 (or higher). 
       
       Play around with this value in case of groundwater. This could potentially speed up your simulation significantly.
   * - CFL strictness factor 1D
     - cfl_strictness_factor_1d
     - Decimal number
     - No
     - \-
     - Strictness of the Courant-Friedrichs-Lewy ratio for 1D flow.
   * - CFL strictness factor 2D
     - cfl_strictness_factor_2d
     - Decimal number
     - No
     - \-
     - Strictness of the Courant-Friedrichs-Lewy ratio for 2D flow.
   * - Time integration method
     - time_integration_method
     - Integer
     - Yes
     - \-
     - The only option at the moment is 0 (Euler implicit). For more information, see :ref:`matrixsolvers`.
   * - Flooding threshold
     - flooding_threshold
     - decimal number
     - Yes
     - \-
     - The water depth threshold for flow between 2D cells. The depth is relative to the lowest DEM pixel at the edge between two 2D cells. It should be equal or higher than 0. It is recommended to keep this value very low (1e-06).
   * - Flow direction threshold
     - flow_direction_threshold
     - Decimal number
     - No
     - m/s
     - Threshold to determine the flow direction, in order to avoid flows of exactly 0.0 m/s.
   * - Minimum surface area
     - min_surface_area
     - Decimal number
     - No
     - m\ :sup:`2`
     - Numerical setting to guarantee proper matrix characterics
   * - Minimum friction velocity
     - min_friction_velocity
     - Decimal number
     - No
     - m/s
     - Minimum velocity that is used for the transition of a cell from dry to wet. This is done for model stability.
   * - Friction shallow water depth correction
     - friction_shallow_water_depth_correction
     - Integer
     - No
     - \-
     - Determines how the friction is calculated. Choose between *0*, *1*, *2*, and *3*. For more information, see :ref:`friction_settings`.
   * - Limiter slope cross-sectional area 2D 
     - limiter_slope_crosssectional_area_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D slope cross-sectional area to allow the model to deal with unrealistically large cross-sectional areas resulting from the subgrid method in sloping terrain. Choose between *0*, *1*, *2*, and *3*. A limiter of 3 has to be used in combination with this water layer definition. For more information, see :ref:`limiters`.
   * - Limiter slope friction 2D
     - limiter_slope_friction_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D slope friction depth to allow the model to deal with unrealistically small friction values resulting from the subgrid method in sloping terrain. For more information, see :ref:`limiters`.
   * - Limiter slope thin water layer
     - limiter_slope_thin_water_layer
     - Decimal number
     - No
     - m/s
     - Has to be used in combination with setting *Limiter slope cross-sectional area 2D* to 3. For more information, see :ref:`limiters`.
   * - Limiter water level gradient 1D
     - limiter_waterlevel_gradient_1d
     - Integer
     - No
     - \-
     - Limiter on the 1D water level gradient to allow the model to deal with unrealistically steep gradients. For more information, see :ref:`limiters`.
   * - Limiter water level gradient 2D
     - limiter_waterlevel_gradient_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D water level gradient to allow the model to deal with unrealistically steep gradients. For more information, see :ref:`limiters`.
   * - Preissmann slot
     - preissmann_slot
     - Decimal number
     - No
     - m\ :sup:`2`
     - Mimics the effect of pressurized flows by creating a narrow slot on top of a pipe. Note that this method is not required for 3Di, but it can be used to compare results with other hydrodynamic simulation software.
   * - Pump implicit ratio
     - pump_implicit_ratio
     - Decimal number
     - No
     - \-
     - Determines whether and how 3Di will adjust the pump capacity based on the (expected) available water. Should be between 0 and 1.


.. _physical_settings:

Physical settings
------------------
 
Settings related to the physics involved in the simulation.
 
These settings are stored in the simulation template. You can change them before starting the simulation, without the need to regenerate the 3Di model.

Layer name
^^^^^^^^^^

physical_settings

Attributes
^^^^^^^^^^

.. list-table:: Physical settings attributes
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
   * - Use advection 1D
     - use_advection_1d
     - integer
     - Yes
     - \-
     - See :ref:`1d_advection`. Choose from:
	     
	     - 0: No 1D advection
         - 1: Momentum conservative scheme
         - 2: Energy conservative scheme
         - 3: Combined momentum and energe conservative scheme (recommended)
   * - Use advection 2D
     - use_advection_2d
     - integer
     - Yes
     - \-
     - 0: Off; 1: On


.. _schema_version:

Schema version
--------------

The schema version shows the database schema version. The database schema is the definition of all tables, columns, and data types. If changes to the database schema are made, tools in the 3Di Modeller Interface will ask you to migrate the spatialite to the newer database schema version. This migration will add or delete the tables and columns that have been changed.

.. note::

    Do not change the schema version manually! Use the processing algorithm :ref:`migrate_spatialite`.

Schema version attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Schema version settings attributes
   :widths: 20 20 15 10 10 40
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - Version number
     - version_num
     - Text
     - No
     - \-
     - Number determining which schematistion version is used, left-padded with zeroes to four characters.

