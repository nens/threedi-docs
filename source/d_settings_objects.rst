.. _settings_objects:

Settings objects
================

On this page an overview is given of all settings objects.

.. _global_settings:

Global settings
---------------

The global settings of your schematisation. These are grouped in *General*, *Grid*, *Terrain information*, *Time*, *Settings id's*, *Extra options 1D*, and *Extra options 2D*.

Global settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::
	- Check if everything is correct in this table?
	- Is this still relevant: use_2d_rain
	- Same for nr_timesteps? This doesn't do anything anymore, correct? It is still mandatory to give a value for this?
	- I also don't think startdate and starttime still work.. The default is 01/01/2000, 12:00 I think and is used when starting a simulation.
	- Same for dem_obstacle_detection and dem_obstacle_height.
	
	- No idea what guess_dams does and whether it (still) works.
	- Technical documentation on maximum table step size is missing in h_subgrid.rst.
	- For the initial groundwater and initial waterlevel types the type is integer, but that is not shown in the QGIS-table. I think it should be as the frict_type. Because then it makes sense that it is an integer type.
	- Add documentation for the folder structure that 3Di uses.


.. list-table:: Global settings attributes
   :widths: 20 20 15 10 10 25 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
     - Group
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier. A schematisation should have only one global settings ID.
     - General
   * - Name
     - name
     - Text
     - No
     - \-
     - Name of simulation template. This is the default simulation name when starting a simulation. Can be changed for any simulation.
     - General
   * - Use 0D-inflow
     - use_0d_inflow
     - Integer
     - Yes
     - \-
     - Choose between: *0: do not use 0d inflow*, *1: use v2_impervious_surface*, or *2: use v2_surface*. See :ref:`howto_use_inflow` for more details.
     - General
   * - Use 1D-flow
     - use_1d_flow
     - Boolean
     - Yes
     - \-
     - Indicates whether 1D-flow is taken into account in a simulation.
     - General
   * - Use 2D-rain
     - use_2d_rain
     - Boolean
     - Yes
     - \-
     - Indicates whether rain on the 2D domain is taken into account in a simulation.
     - General
   * - Use 2D-flow
     - use_2d_flow
     - Boolean
     - Yes
     - \-
     - Indicates whether 2D-flow is taken into account in a simulation.
     - General
   * - Grid space
     - grid_space
     - Integer
     - Yes
     - m
     - The width/length of the smallest possible 2D computation cell. See :ref:`computational_grid` for more details.
     - Grid
   * - Number of grid-refinement levels
     - kmax
     - Integer
     - Yes
     - \-
     - The maximum number of grid-refinement levels. See :ref:`computational_grid` for more details.
     - Grid
   * - Table step size
     - table_step_size
     - Decimal number
     - Yes
     - m
     - Defines the height interval between successive increments in the subgrid tabulation. See :ref:`subgrid_tables` for more details.
     - Grid
   * - Maximum table step size
     - maximum_table_step_size
     - Decimal number
     - No
     - m
     - Defines the maximum height interval between successive increments in the subgrid tabulation. See :ref:`subgrid_tables` for more details.
     - Grid
   * - DEM file
     - dem_file
     - Text
     - No
     - m MSL
     - Location of your DEM file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\dem.tif*
     - Terrain information
   * - EPSG code
     - epsg_code
     - Integer
     - Yes
     - \-
     - Defines the EPSG Geodetic Parameter Dataset to define the spatial reference system for you schematisation. See `Wikipedia <https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset>`_ for more information.
     - Terrain information
   * - Friction coefficient file
     - frict_coef_file
     - Text
     - No
     - m\ :sup:`1/2`/s (Chèzy) or s/m\ :sup:`1/3` (Manning)
     - Location of your friction coeffient file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\friction.tif*
     - Terrain information
   * - Friction coefficient
     - frict_coef
     - Decimal number
     - Yes
     - m\ :sup:`1/2`/s (Chèzy) or s/m\ :sup:`1/3` (Manning)
     - Defines a global friction coefficient for your schematisation. This is superseded in case a friction coefficient file is provided.
     - Terrain information
   * - Friction type
     - frict_type
     - Integer
     - Yes
     - \-
     - Defines the friction type from two options: *1: Chèzy* or *2: Manning*. Make sure the friction type matches the friction coefficient (file).
     - Terrain information
   * - Friction average
     - frict_avg
     - Boolean
     - Yes
     - \-
     - Indicates whether the friction values in a subgrid-cell are averaged or not
     - Terrain information
   * - Initial groundwater level file
     - initial_groundwater_level_file
     - Text
     - No
     - m MSL
     - Location of your initial groundwater level file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\initial_groundwater_level.tif*.  See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial groundwater level
     - Initial_groundwater_level
     - Decimal number
     - No
     - m MSL
     - Initial groundwater level. This is superseded in case an initial groundwater level file is provided. See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial groundwater level type
     - initial_groundwater_level_type
     - Integer
     - Only when using an initial groundwater level file
     - \-
     - Choose between: *Max*, *Min*, or *Average*. See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial water level file
     - initial_waterlevel_file
     - Text
     - No
     - m MSL
     - Location of your initial water level file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\initial_water_level.tif*.
     - Terrain information
   * - Initial water level
     - initial_waterlevel
     - Decimal number
     - Yes
     - m MSL
     - Global initial water level. This is superseded in case an initial water level file is provided.
     - Terrain information
   * - Initial water level type
     - water_level_ini_type
     - Integer
     - Yes
     - \-
     - Choose between: *Max*, *Min*, or *Average*.
     - Terrain information
   * - Interception file
     - interception_file
     - Text
     - No
     - m
     - Location of your interception file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\interception.tif*. See :ref:`interception` for more details.
     - Terrain information
   * - Interception global
     - interception_global
     - Decimal number
     - No
     - m
     - Global interception value. See :ref:`interception` for more details.
     - Terrain information
   * - Wind shielding file
     - wind_shielding_file
     - Text
     - No
     - \-
     - Location of your wind shielding factor file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\wind_shielding.tif*. See :ref:`wind_effects` for more details.
     - Terrain information
   * - Start date
     - start_date
     - Date
     - Yes
     - \-
     - Start date of simulation template. The format is yyyy-mm-dd (e.g. 2023-07-21).
     - Time
   * - Start time
     - start_time
     - Date
     - Yes
     - \-
     - Start time of simulation template. The format is hh:mm:ss.
     - Time
   * - Simulation time step
     - sim_time_step
     - Decimal number
     - Yes
     - s
     - The default time step used in the simulation.
     - Time
   * - Time step plus
     - timestep_plus
     - Boolean
     - Yes
     - \-
     - Indicates whether or not time step plus is used. If possible it will use a larger time step than the simulation time step. Note that it is only useful in steady state simulation.
     - Time
   * - Minimum simulation time step
     - minimum_sim_time_step
     - Decimal number
     - Yes
     - s
     - Minimum time step that is allowed in the simulation.
     - Time
   * - Maximum simulation time step
     - maximum_sime_time_step
     - Decimal number
     - Only when using time step plus
     - s
     - Maximum time step that is allowed in the simulation. Use in conjunction with Time Step Plus.
     - Time
   * - Number of time steps
     - nr_timesteps
     - Integer
     - Yes
     - \-
     - Maximum number of time step (this is no longer used).
     - Time
   * - Output time step
     - output_time_step
     - Decimal number
     - Yes
     - s
     - The output time step that is written in the output file (NetCDF). This must be a multiplication of the simulation time step.
     - Time
   * - Interflow settings ID
     - interflow_settings_id
     - Integer
     - Only when using interflow
     - \-
     - Referral to the interflow settings ID.
     - Settings ID's
   * - Groundwater settings ID
     - groundwater_settings_id
     - Integer
     - Only when using groundwater
     - \-
     - Referral to the groundwater settings ID.
     - Settings ID's
   * - Numerical settings ID
     - numerical_settings_id
     - Integer
     - Yes
     - \-
     - Referral to the numerical settings ID.
     - Settings ID's
   * - Simple infiltration settings ID
     - simple_infiltration_settings_id
     - Integer
     - Only when using simple infiltration
     - \-
     - Referral to the simple infiltration settings ID.
     - Settings ID's
   * - Control group ID
     - control_group_id
     - Integer
     - Only when using controls
     - \-
     - Referral to the control group ID.
     - Settings ID's
   * - Vegetation drag settings ID
     - vegetation_drag_settings_id
     - Integer
     - Only when using vegetation
     - \-
     - Referral to the vegetation drag settings ID.
     - Settings ID's
   * - Advection 1D
     - advection_1d
     - Integer
     - Yes
     - \-
     - Choose between *0: Do not use advection 1D* or *1: Use advection 1D*. Options 2-6 are in an experimental phase.
     - Extra options 1D
   * - Calculation points distance
     - dist_calc_points
     - Decimal number
     - Yes
     - \-
     - Global distance between calculation points for line elements. Is superseded in case this  is specified with the specific 1D objects.
     - Extra options 1D
   * - Manhole storage area
     - manhole_storage_area
     - Decimal number
     - Only when using only 1D-flow without a specified DEM
     - m\ :sup:`2`
     - Global manhole storage area. This is the surface area that each manhole is given when water reaches above the drain level. Must be left empty when using only 2D-flow.
     - Extra options 1D
   * - Maximum angle for 1D advection
     - max_angle_1d_advection
     - Decimal number
     - No
     - Degrees
     - Maximum angle at which advection is taken into account (should be between 0 and 90 degrees).
     - Extra options 1D
   * - Table step size for the 1D domain
     - table_step_size_1d
     - Decimal number
     - No
     - m
     - User-defined table step size/increment (m) for 1d cross-sections and volumes. default value = table_step_size. Supersedes the table step size for 1D domain.
     - Extra options 1D
   * - Advection 2D
     - advection_2d
     - Integer
     - Yes
     - \-
     - Choose between *0: Do not use advection 2D* or *1: Use advection 2D*.
     - Extra options 2D
   * - DEM obstacle detection
     - dem_obstacle_detection
     - Boolean
     - No
     - \-
     - This feature is no longer supported.
     - Extra options 2D
   * - Guess dams
     - guess_dams
     - Boolean
     - No
     - \-
     - This feature is no longer supported.
     - Extra options 2D
   * - DEM obstacle height
     - dem_obstacle_height
     - Decimal number
     - No
     - m
     - This feature is no longer supported.
     - Extra options 2D
   * - Embedded cutoff threshold
     - embedded_cutoff_threshold
     - Decimal number
     - No
     - \-
     - Relative length of cell size. When an embedded channel intersects a 2D cell with a length shorter than the cell size * cutoff threshold, the embedded channel skips this 2D cell. This is useful for preventing very short embedded channel segments (which slow down your simulation).
     - Extra options 2D
   * - Flooding threshold
     - flooding_threshold
     - Decimal number
     - Yes
     - m
     - The water depth threshold for flow between 2D cells. The depth is relative to the lowest bathymetry pixel at the edge between two 2D cells. It should be equal or higher than 0.
     - Extra options 2D



.. _aggregation_settings:

Aggregation settings
--------------------

You can set multiple aggregation options for each *flow_variable* as long as the *aggregation_method* is not used twice for the same flow_variable.

Aggregation settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::
	- There are a few errors in the flow variables in the QGIS-table (: 
		- "Waterlevel" should be "Water level"
		- "Wet cross section" should be "Wet cross-sectional area"
		- "Volume" should be "Volume"
		- Not sure, but I think "Surface source sink discharge" should be "Surface source & sink discharge"

.. list-table:: Attribute Field Descriptions
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
     - Unique identifier. Each aggregation needs a unique ID.
   * - Flow variable
     - flow_variable
     - Text
     - Yes
     - \-
     - The flow variables that can be used to aggregate. Choose between:
     
       - Discharge
       - Flow velocity
       - Pump discharge
       - Rain
       - Water level
       - Wet cross-sectional area
       - Wet surface
       - Lateral discharge
       - Volume
       - Simple infiltration
       - Leakage
       - Interception
       - Surface source & sink discharge
   * - Aggregation method
     - aggregation_method
     - Text
     - Yes
     - \-
     - The aggregation methods that can be used on a flow variable. Choose between:
     
       - Average: Calculates the average value of the variable over the aggregation interval.
       - Minimum: Calculates the minimum value of the variable over the aggregation interval.
       - Maximum: Calculates the maximum value of the variable over the aggregation interval.
       - Cumulative: Calculates the cumulative value of the variable over the aggregation interval by integrating over time [dt * variable].
       - Median: Calculates the median value of the variable over the aggregation interval.
       - Cumulative negative: Calculates the cumulative negative value of the variable over the aggregation interval by integrating over time [dt * variable].
       - Cumulative positive: Calculates the cumulative positive value of the variable over the aggregation interval by integrating over time [dt * variable].
       - Current: Uses the current value of a variable. This is for the Water Balance Tool. This is only valid for volume and intercepted_volume.
   * - Aggregation interval
     - time_step
     - Integer
     - Yes
     - s
     - Determines the interval over which the aggregation will be calculated
   * - Aggregation variable name
     - var_name
     - Text
     - Yes
     - \-
     - A user-defined aggregation variable name to distinguish between aggregated configuration of variables. It should be something like *discharge_cum_pos* or *water_level_max*
   * - Global settings id
     - global_settings_id
     - Integer
     - Yes
     - \-
     - Referral to the global settings ID

.. _simple_infiltration_settings:

Simple infiltration settings
----------------------------

Settings for 'simple' infiltration in models without groundwater.

Simple infiltration attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Simple infiltration settings attributes
   :widths: 15 20 10 10 10 35
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
     - Unique identifier. A schematisation should have only one simple infiltration settings ID.
   * - Display name
     - display_name
     - Text
     - Yes
     - \-
     - For user administration only.
   * - Infiltration rate
     - infiltration_rate
     - Decimal number
     - Yes
     - mm/day
     - Global infiltration rate.
   * - Infiltration rate file
     - infiltration_rate_file
     - Text
     - No
     - mm/day
     - Location of your infiltration rate file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\infiltration.tif*.
   * - Maximum infiltration capacity
     - max_infiltration_capacity
     - Decimal number
     - No
     - m
     - Global maximum infiltration capacity, which uses the sum of pixel values per 2D cell. Once this capacity has been reached there will be no more infiltration.
   * - Maximum infiltration capacity file
     - max_infiltration_capacity_file
     - Text
     - No
     - m
     - Location of your maximum infiltration capacity file, relative to the location of your sqlite in the folder-structure. It should look something like *rasters\\max_infiltration.tif*.
   * - Infiltration surface option
     - infiltration_surface_option
     - Integer
     - Yes
     - \-
     - Option that determines how the infiltration works in 2D cells. Choose between *0: Rain (whole surface when raining, only wet pixels when dry)*, *1: Whole surface*, *2: Only wet surface*.


Groundwater settings
--------------------

Groundwater settings

Interflow settings
------------------

Interflow settings

.. _numerical_settings:

Numerical settings
------------------

Numerical settings (advanced users)


.. _vegetation_drag:

Vegetation drag settings
------------------------

The *vegetation drag* table contains the input parameters that are used for 2D flow with vegetation. For an in-depth explanation of how 2D flow with vegetation is calculated by 3Di, see :ref:`flow_with_vegetation`. For more information on using vegetation in your 3Di model and choosing the right parameter values, :ref:`a_how_to_vegetation`.

Vegetation drag can only be used with friction type 'Chezy', because the vegetation formulation (initially introduced by Baptist 2005) uses Chezy.

Columns
^^^^^^^

id
""

Unique identifier

height
""""""
Height of the vegetation (m), i.e. the length of the plant stems.  Global value that is used in the entire model domain, used by 3Di if no raster (*height_file*) is supplied.

height_file
"""""""""""
Reference to a raster file containing the *height of the vegetation (m), i.e. the length of the plant stems*. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *height* will be ignored.

stem_count
""""""""""
Density of plant stems (number of stems per m:sup:`2`). Global value that is used in the entire model domain, used by 3Di if no raster (*stem_count_file*) is supplied.

stem_count_file
"""""""""""""""
Reference to a raster file containing the *density of plant stems (number of stems per m:sup:`2`)* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *stem_count* will be ignored.

stem_diameter
"""""""""""""
Mean diameter of plant stems (m). Global value that is used in the entire model domain, used by 3Di if no raster (*stem_diameter_file*) is supplied.

stem_diameter_file
""""""""""""""""""
Reference to a raster file containing a *mean diameter of plant stems (m)* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *stem_diameter* will be ignored.

drag_coefficient
""""""""""""""""

Dimensionless coefficient to linearly scale the drag that vegetation exerts on the water. The drag resulting from vegetation is different for each situation. A large share of this variation is captured by choosing the correct values for stem count, stem diameter and vegetation height. The drag coefficient can be used to account for the other factors that affect the drag. The drag coefficient can also be used as a calibration parameter.

Global value that is used in the entire model domain, used by 3Di if no raster (*drag_coefficient_file*) is supplied.

drag_coefficient_file
"""""""""""""""""""""

Reference to a raster file containing a *drag_coefficient* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *drag_coefficient* will be ignored.
