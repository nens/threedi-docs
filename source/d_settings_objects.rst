.. _settings_objects:

Settings objects
================

On this page an overview of all settings objects is provided.

.. _global_settings:

Global settings
---------------

The global settings of your schematisation. These can be grouped into categories: *General*, *Grid*, *Terrain information*, *Time*, *Settings id's*, *Extra options 1D*, and *Extra options 2D*.

Global settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Global settings attributes
   :widths: 20 20 15 10 10 25 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
     - Category
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
   * - Use 0D inflow
     - use_0d_inflow
     - Integer
     - Yes
     - \-
     - Choose between: *0: do not use 0d inflow*, *1: use v2_impervious_surface*, or *2: use v2_surface*. See :ref:`howto_use_inflow` for more details.
     - General
   * - Use 1D flow
     - use_1d_flow
     - Boolean
     - Yes
     - \-
     - Indicates whether 1D flow is taken into account in a simulation.
     - General
   * - Use 2D rain
     - use_2d_rain
     - Boolean
     - Yes
     - \-
     - Indicates whether rain on the 2D domain is taken into account in a simulation.
     - General
   * - Use 2D flow
     - use_2d_flow
     - Boolean
     - Yes
     - \-
     - Indicates whether 2D flow is taken into account in a simulation.
     - General
   * - Grid space
     - grid_space
     - Integer
     - Yes
     - m
     - The width/length of the smallest possible 2D computation cell. See :ref:`2d_grid_settings` for more details.
     - Grid
   * - Number of grid refinement levels
     - kmax
     - Integer
     - Yes
     - \-
     - The maximum number of grid refinement levels. See :ref:`2d_grid_settings` for more details.
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
     - Defines the maximum height interval between successive increments in the subgrid tabulation. Defaults to 100 × minimum table step size. See :ref:`subgrid_tables` for more details.
     - Grid
   * - DEM file
     - dem_file
     - Text
     - No
     - m MSL
     - Location of your DEM file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\dem.tif*
     - Terrain information
   * - EPSG code
     - epsg_code
     - Integer
     - Yes
     - \-
     - Defines the coordinate reference system (CRS) to define the spatial reference system for you schematisation.
     - Terrain information
   * - Friction coefficient file
     - frict_coef_file
     - Text
     - No
     - m\ :sup:`1/2`/s (Chèzy) or s/m\ :sup:`1/3` (Manning)
     - Location of your friction coeffient file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\friction.tif*. This superseeds any global friction coefficient.
     - Terrain information
   * - Friction coefficient
     - frict_coef
     - Decimal number
     - Yes
     - m\ :sup:`1/2`/s (Chèzy) or s/m\ :sup:`1/3` (Manning)
     - Defines a friction coefficient for your schematisation. This global value is superseded in case a friction coefficient file is provided.
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
     - Location of your initial groundwater level file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\initial_groundwater_level.tif*. This superseeds any global initial groundwater level. See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial groundwater level
     - Initial_groundwater_level
     - Decimal number
     - No
     - m MSL
     - Initial groundwater level. This global value is superseded in case an initial groundwater level file is provided. See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial groundwater level type
     - initial_groundwater_level_type
     - Integer
     - Only when using an initial groundwater level file
     - \-
     - Choose between: *0: Max*, *1: Min*, or *2: Average*. See :ref:`groundwater` for more details.
     - Terrain information
   * - Initial water level file
     - initial_waterlevel_file
     - Text
     - No
     - m MSL
     - Location of your initial water level file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\initial_water_level.tif*. This superseeds any global initial water level.
     - Terrain information
   * - Initial water level
     - initial_waterlevel
     - Decimal number
     - Yes
     - m MSL
     - Initial water level. This global value is superseded in case an initial water level file is provided.
     - Terrain information
   * - Initial water level type
     - water_level_ini_type
     - Integer
     - Yes
     - \-
     - Choose between: *0: Max*, *1: Min*, or *2: Average*.
     - Terrain information
   * - Interception file
     - interception_file
     - Text
     - No
     - m
     - Location of your interception file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\interception.tif*. This superseeds any global interception value. See :ref:`interception` for more details.
     - Terrain information
   * - Interception global
     - interception_global
     - Decimal number
     - No
     - m
     - Interception value. This global value is superseded in case an interception file is provided. See :ref:`interception` for more details.
     - Terrain information
   * - Wind shielding file
     - wind_shielding_file
     - Text
     - No
     - \-
     - Location of your wind shielding factor file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\wind_shielding.tif*. See :ref:`wind_effects` for more details.
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
     - Maximum time step that is allowed in the simulation. Use in conjunction with *Time step plus*.
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
     - Reference to the interflow settings ID.
     - Settings ID's
   * - Groundwater settings ID
     - groundwater_settings_id
     - Integer
     - Only when using groundwater
     - \-
     - Reference to the groundwater settings ID.
     - Settings ID's
   * - Numerical settings ID
     - numerical_settings_id
     - Integer
     - Yes
     - \-
     - Reference to the numerical settings ID.
     - Settings ID's
   * - Simple infiltration settings ID
     - simple_infiltration_settings_id
     - Integer
     - Only when using simple infiltration
     - \-
     - Reference to the simple infiltration settings ID.
     - Settings ID's
   * - Control group ID
     - control_group_id
     - Integer
     - Only when using controls
     - \-
     - Reference to the control group ID.
     - Settings ID's
   * - Vegetation drag settings ID
     - vegetation_drag_settings_id
     - Integer
     - Only when using vegetation
     - \-
     - Reference to the vegetation drag settings ID.
     - Settings ID's
   * - Advection 1D
     - advection_1d
     - Integer
     - Yes
     - \-
     - Choose between *0: Do not use advection 1D* or *1: Use advection 1D*. Options 2-6 are in an experimental phase.
     - Extra options 1D
   * - Calculation point distance
     - dist_calc_points
     - Decimal number
     - Yes
     - \-
     - Distance between calculation points for line elements. This global value is superseded in case this  is specified with the specific 1D objects.
     - Extra options 1D
   * - Manhole storage area
     - manhole_storage_area
     - Decimal number
     - Only when using only 1D-flow without a specified DEM
     - m\ :sup:`2`
     - Manhole storage area. This global value is the surface area that each manhole is given when water reaches above the drain level. To use this feature, do not specify a DEM file and set the manhole calculation types to *Connected*. Must be left empty when using only 2D flow.
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
     - User-defined table step size/increment (m) for 1d cross-sections and volumes; see :ref:`subgrid_tables`. Default value = table_step_size. Supersedes the table step size for 1D domain.
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
     - The water depth threshold for flow between 2D cells. The depth is relative to the lowest DEM pixel at the edge between two 2D cells. It should be equal or higher than 0.
     - Extra options 2D


.. _aggregation_settings:

Aggregation settings
--------------------

You can set multiple aggregation options for each *flow_variable* as long as the *aggregation_method* is not used twice for the same flow_variable. For more information about aggregation, see :ref:`aggregationnetcdf`.

Aggregation settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
     - Unique identifier. Each aggregation needs a unique ID.
   * - Flow variable
     - flow_variable
     - Text
     - Yes
     - \-
     - Variable that is to be aggregated. Text to fill in vs. how it is displayed in the 3Di Modeller Interface:
     
       - discharge (Discharge)
       - flow_velocity (Flow velocity)
       - pump_discharger (Pump discharge)
       - rain (Rain)
       - waterlevel (Water level)
       - wet_cross-section (Wet cross-sectional area)
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
       - cum (Cumulative): Calculates the cumulative value of the variable over the aggregation interval by integrating over time [dt * variable].
       - med (Median): Calculates the median value of the variable over the aggregation interval.
       - cum_negative (Cumulative negative): Calculates the cumulative negative value of the variable over the aggregation interval by integrating over time [dt * variable].
       - cum_positive (Cumulative positive): Calculates the cumulative positive value of the variable over the aggregation interval by integrating over time [dt * variable].
       - current (Current): Uses the current value of a variable. This is for the Water Balance Tool. This is only valid for volume and intercepted_volume.
   * - Aggregation interval
     - time_step
     - Integer
     - Yes
     - s
     - Determines the interval over which the aggregation will be calculated
   * - Aggregation variable name
     - var_name
     - Text
     - No
     - \-
     - This field is no longer used
   * - Global settings id
     - global_settings_id
     - Integer
     - Yes
     - \-
     - Reference to the global settings ID

.. _simple_infiltration_settings:

Simple infiltration settings
----------------------------

Settings for :ref:`simpleinfiltration`. 

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
     - Infiltration rate.  This global value is superseded in case an infiltration rate file is provided.
   * - Infiltration rate file
     - infiltration_rate_file
     - Text
     - No
     - mm/day
     - Location of your infiltration rate file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\infiltration.tif*. This superseeds any global infiltration rate.
   * - Maximum infiltration capacity
     - max_infiltration_capacity
     - Decimal number
     - No
     - m
     - Maximum infiltration capacity, which uses the sum of pixel values per 2D cell. Once this capacity has been reached there will be no more infiltration. This global value is superseded in case a maximum infiltration capacity file is provided.
   * - Maximum infiltration capacity file
     - max_infiltration_capacity_file
     - Text
     - No
     - m
     - Location of your maximum infiltration capacity file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\max_infiltration.tif*. This superseeds any global maximum infiltration capacity.
   * - Infiltration surface option
     - infiltration_surface_option
     - Integer
     - Yes
     - \-
     - Option that determines how the infiltration works in 2D cells. Choose between *0: Rain (whole surface when raining, only wet pixels when dry)*, *1: Whole surface*, *2: Only wet surface*.


Groundwater settings
--------------------

Settings for groundwater models. For more information on groundwater, see :ref:`groundwater`.

Groundwater settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Groundwater settings attributes
   :widths: 25 25 15 10 10 45 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
     - Category
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier. A schematisation should have only one groundwater settings ID.
     - General
   * - Display name
     - display_name
     - Text
     - No
     - \-
     - For user administration only.
     - General
   * - Equilibrium infiltration rate
     - equilibrium_infiltration_rate
     - Decimal number
     - No
     - mm/day
     - The equilibrium infiltration rate for Horton-based infiltration. For more information, see :ref:`grwhortoninfiltration`.
     - Equilibrium infiltration
   * - Equilibrium infiltration rate file
     - equilibrium_infiltration_rate_file
     - Text
     - No
     - mm/day
     - Location of your equilibrium infiltration rate file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_equilibrium_infiltration.tif*. For more information, see :ref:`grwhortoninfiltration`.
     - Equilibrium infiltration
   * - Equilibrium infiltration rate type
     - equilibrium_infiltration_rate_type
     - Integer
     - Yes
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Equilibrium infiltration
   * - Groundwater hydraulic connectivity
     - groundwater_hydr_connectivity
     - Decimal number
     - Yes
     - m/day
     - Darcy coefficient.
     - Hydro connectivity
   * - Groundwater hydraulic connectivity file
     - groundwater_hydr_connectivity_file
     - Text
     - No
     - m/day
     - Location of your groundwater hydraulic connectivity file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_hydro_conductivity.tif*.
     - Hydro connectivity
   * - Groundwater hydraulic connectivity type
     - groundwater_hydr_connectivity_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Hydro connectivity
   * - Groundwater impervious layer level
     - groundwater_impervious_layer_level
     - Decimal number
     - Yes
     - m MSL
     - Level of the impervious layer that acts as the bottom (and thus boundary) of the groundwater layer.
     - Impervious layer level
   * - Groundwater impervious layer level file
     - groundwater_impervious_layer_level_file
     - Text
     - No
     - m MSL
     - Location of your groundwater impervious layer level file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_imp_layer_lvl.tif*.
     - Impervious layer level
   * - Groundwater impervious layer level type
     - groundwater_impervious_layer_level_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Impervious layer level
   * - Initial infiltration rate
     - initial_infiltration_rate
     - Decimal number
     - Yes
     - mm/day
     - The initial infiltration rate for Horton-based infiltration. For more information, see :ref:`grwhortoninfiltration`.
     - Initial infiltration
   * - Initial infiltration rate file
     - initial_infiltration_rate_file
     - Text
     - No
     - mm/day
     - Location of your initial infiltration rate file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_ini_infiltration.tif*.
     - Initial infiltration
   * - Initial infiltration rate type
     - initial_infiltration_rate_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Initial infiltration
   * - Infiltration decay period
     - infiltration_decay_period
     - Decimal number
     - Yes
     - days
     - Period in which the infiltration rate decays to an equilibrium for Horton-based infiltration.
     - Infiltration decay
   * - Infiltration decay period file
     - infiltration_decay_period_file
     - Text
     - No
     - days
     - Location of your infiltration decay period file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_infil_decay.tif*.
     - Infiltration decay
   * - Infiltration decay period type
     - infiltration_decay_period_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Infiltration decay
   * - Leakage
     - leakage
     - Decimal number
     - Yes
     - mm/day
     - The bottom boundary condition (constant in time) that describes the leakage to deeper ground layers.
     - Leakage
   * - Leakage file
     - leakage_file
     - Text
     - No
     - mm/day
     - Location of your leakage file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_leakage.tif*.
     - Leakage
   * - Phreatic storage capacity
     - phreatic_storage_capacity
     - Decimal number
     - Yes
     - \-
     - The potential storage in the saturated zone (= porosity). The phreatic storage capacity is described by a value between 0 and 1.
     - Phreatic storage capacity
   * - Phreatic storage capacity file
     - phreatic_storage_capacity_file
     - Text
     - No
     - \-
     - Location of your phreatic storage capacity file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\gw_phrea_storage_cap.tif*.
     - Phreatic storage capacity
   * - Phreatic storage capacity type
     - phreatic_storage_capacity_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
     - Phreatic storage capacity

Interflow settings
------------------

Interflow can be used as an extra layer below the surface. For more information on Interflow, see :ref:`interflow`.

Interflow settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Interflow settings attributes
   :widths: 20 20 15 10 10 40 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
     - Category
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
     - General
   * - Display name
     - display_name
     - Text
     - No
     - \-
     - For user administration only.
     - General
   * - Interflow type
     - interflow_type
     - Integer
     - Yes
     - \-
     - Choose between: (0) No interflow, (1) Local deepest point scaled porosity, (2) Global deepest point scaled porosity, (3) Local deepest point constant porosity, (4) Global deepest point constant porosity.
     - General
   * - Porosity
     - porosity
     - Decimal Number
     - Yes
     - \-
     - Porosity value of the interflow layer. It should be a value between 0 and 1. This global value is superseded in case a porosity file is provided.
     - Porosity
   * - Porosity file
     - porosity_file
     - Text
     - Yes
     - \-
     - Location of your porosity file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\porosity.tif*. This superseeds any global porosity value.
     - Porosity
   * - Porosity layer thickness
     - porosity_layer_thickness
     - Decimal Number
     - Only if using interflow type *(1) Local deepest point scaled porosity* or *(2) Global deepest point scaled porosity*.
     - m
     - Thickness of the porosity layer relative to the DEM.
     - Porosity
   * - Hydraulic conductivity file
     - hydraulic_conductivity_file
     - Text
     - No
     - m/day
     - Location of your hydraulic conductivity file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\hydraulic_conductivity.tif*. This superseeds any global hydraulic conductivity value.
     - Hydraulic conductivity
   * - Hydraulic conductivity
     - hydraulic_conductivity
     - Decimal Number
     - Yes
     - m/day
     - Hydraulic conductivity value. This global value is superseded in case a hydraulic conductivity file is provided.
     - Hydraulic conductivity
   * - Impervious layer elevation
     - impervious_layer_elevation
     - Decimal Number
     - Yes
     - m
     - Depth of impervious layer below lowest pixel. Value has to be greater than 0.
     - Impervious layer


.. _numerical_settings:

Numerical settings
------------------
 
Most users do not need to worry about these settings. More advanced users can change the default settings to improve their models. These can be grouped into categories: *General*, *Limiters*, *Matrix*, *Time*, *Thresholds*, *Miscellaneous*. For more information on the numerical settings, see :ref:`numerics`.

Numerical settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Numerical settings attributes
   :widths: 20 20 15 10 10 40 15
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
     - Category
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier. A schematisation should have only one numerical settings ID.
     - General
   * - Limiter 1D gradient
     - limiter_grad_1d
     - Integer
     - No
     - \-
     - Limiter on the 1D water level gradient to allow the model to deal with unrealistically steep gradients. For more information, see :ref:`limiters`.
     - Limiters
   * - Limiter 2D gradient
     - limiter_grad_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D water level gradient to allow the model to deal with unrealistically steep gradients. For more information, see :ref:`limiters`.
     - Limiters
   * - Limiter 2D slope cross-sectional area
     - limiter_slope_crosssectional_area_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D slope cross-sectional area to allow the model to deal with unrealistically large cross-sectional areas resulting from the subgrid method in sloping terrain. Choose between *0*, *1*, *2*, and *3*. A limiter of 3 has to be used in combination with this water layer definition. For more information, see :ref:`limiters`.
     - Limiters
   * - Limiter 2D slope friction depth
     - limiter_slope_friction_2d
     - Integer
     - No
     - \-
     - Limiter on the 2D slope friction depth to allow the model to deal with unrealistically small friction values resulting from the subgrid method in sloping terrain. For more information, see :ref:`limiters`.
     - Limiters
   * - Convergence definition
     - convergence_cg
     - Decimal number
     - No
     - \-
     - Convergence definition to iteratively solve matrices. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Minimum residual for convergence
     - convergence_eps
     - Decimal number
     - Yes
     - \-
     - Minimal residual for convergence of Newton iteration. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Number of conjugate gradient method iterations
     - use_of_cg
     - Integer
     - Yes
     - \-
     - Number of iterations of the conjugate gradient method before switching to another method. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Use of nested Newton
     - use_of_nested_newton
     - Integer
     - Yes
     - \-
     - Choose between *0: When the schematisation does not include 1D-elements with closed profiles* and *1: When the schematisation includes 1D-elements with closed profiles*. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Maximum degree
     - max_degree
     - Integer
     - Yes
     - \-
     - Determines the efficiency of the matrix solver. Advised values depend on the type of model:
	 
       - Only 1D flow: 700
       - 1D and 2D flow: 7
       - Only surface 2D flow: 5
       - Surface and groundwater flow: 7
       - 1D, 2D surface and groundwater flow: 70 (or higher). Play around with this value in case of groundwater. This could potentially significantly speed up your model.
     - Matrix
   * - Maximum number of nonlinear iterations
     - max_nonlin_iterations
     - Integer
     - Yes
     - \-
     - Maximum number of nonlinear iterations in a single time step. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Gradient method preconditioner
     - precon_cg
     - Integer
     - No
     - \-
     - Preconditioner for the matrix solver. Setting this to 1 generally increases simulation speed. For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Time integration method
     - integration_method
     - Integer
     - Yes
     - \-
     - For more information, see :ref:`matrixsolvers`.
     - Matrix
   * - Flow direction threshold
     - flow_direction_threshold
     - Decimal number
     - No
     - m/s
     - Threshold to determine the flow direction, in order to avoid flows of exactly 0.0 m/s.
     - Thresholds
   * - General numerical threshold
     - general_numerical_threshold
     - Decimal number
     - No
     - \-
     - Generally used numerical threshold to avoid singularities due to limited numerical accuracy.
     - Thresholds
   * - Thin water layer definition
     - thin_water_layer_definition
     - Decimal number
     - No
     - m/s
     - Has to be used in combination with a Limiter 2D slope cross-sectional area of 3. For more information, see :ref:`limiters`.
     - Thresholds
   * - Minimum friction velocity
     - minimum_friction_velocity
     - Decimal number
     - No
     - m/s
     - Minimum velocity that is used for the transition of a cell from dry to wet. This is done for model stability.
     - Thresholds
   * - Minimum surface area
     - minimum_surface_area
     - Decimal number
     - No
     - m\ :sup:`2`
     - Numerical setting to guarantee proper matrix characterics
     - Thresholds
   * - Strictness of CFL-condition for 1D flow
     - cfl_strictness_factor_1d
     - Decimal number
     - No
     - \-
     - Strictness of the Courant-Friedrichs-Lewy ratio for 1D flow.
     - Miscellaneous
   * - Strictness of CFL-condition for 2D flow
     - cfl_strictness_factor_2d
     - Decimal number
     - No
     - \-
     - Strictness of the Courant-Friedrichs-Lewy ratio for 2D flow.
     - Miscellaneous
   * - Shallow water friction correction
     - frict_shallow_water_correction
     - Integer
     - No
     - \-
     - Determines how the friction is calculated. Choose between *0*, *1*, *2*, and *3*. For more information, see :ref:`friction_settings`.
     - Miscellaneous
   * - Pump implicit ratio
     - pump_implicit_ratio
     - Decimal number
     - No
     - \-
     - Determines whether and how 3Di will adjust the pump capacity based on the (expected) available water. Should be between 0 and 1.
     - Miscellaneous
   * - Preissmann slot
     - preissmann_slot
     - Decimal number
     - No
     - m\ :sup:`2`
     - Mimics the effect of pressurized flows by creating a narrow slot on top of a pipe. Note that this method is not required for 3Di, but it can be used to compare results with other hydrodynamic software.
     - Miscellaneous

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

.. _vegetation_drag:

Vegetation drag settings
------------------------

The *vegetation drag* table contains the input parameters that are used for 2D flow with vegetation. For an in-depth explanation of how 2D flow with vegetation is calculated by 3Di, see :ref:`2D flow with vegetation<flow_with_vegetation>`. For more information on using vegetation in your 3Di model and choosing the right parameter values, see :ref:`How to model vegetation<a_how_to_vegetation>`.

Vegetation drag can only be used with friction type 'Chezy', because the vegetation formulation (initially introduced by :cite:p:`Baptist2007`) uses Chezy.


Vegetation drag settings attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Vegetation drag settings attributes
   :widths: 20 20 15 10 10 40
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
     - Unique identifier. A schematisation should have only one vegetation drag settings ID.
   * - Display name
     - display_name
     - Text
     - No
     - \-
     - For user administration only.
   * - Vegetation height
     - vegetation_height
     - Decimal number
     - Yes
     - m
     - Height of the vegetation, i.e. the length of the plant stems. This global value is superseded in case a vegetation height file is provided.
   * - Vegetation height file
     - vegetation_height_file
     - Text
     - No
     - m
     - Location of your vegetation height file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\veg_height.tif*. This supersedes any global vegetation height.
   * - Vegetation stem count
     - vegetation_stem_count
     - Integer
     - Yes
     - #/m\ :sup:`2`
     - Density of plant stems. This global value is superseded in case a vegetation stem count file is provided.
   * - Vegetation stem count file
     - vegetation_stem_count_file
     - Text
     - No
     - #/m\ :sup:`2`
     - Location of your vegetation stem count file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\veg_stem_count.tif*. This supersedes any global vegetation stem count.
   * - Vegetation stem diameter
     - vegetation_stem_diameter
     - Decimal number
     - Yes
     - m
     - Mean diameter of plant stems. This global value is superseded in case a vegetation stem diameter file is provided.
   * - Vegetation stem diameter file
     - vegetation_stem_diameter_file
     - Text
     - No
     - m
     - Location of your vegetation stem diameter file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\veg_stem_diam.tif*. This supersedes any global vegetation stem diameter value.
   * - Vegetation drag coefficient
     - vegetation_drag_coefficient
     - Decimal number
     - Yes
     - \-
     - Coefficient to linearly scale the drag that vegetation exerts on the water. The drag resulting from vegetation is different for each situation. A large share of this variation is captured by choosing the correct values for vegetation height, stem count, and stem diameter. The drag coefficient can be used to account for the other factors that affect the drag. The drag coefficient can also be used as a calibration parameter. This global value is superseded in case a vegetation drag coefficient file is provided.
   * - Vegetation drag coefficient file
     - vegetation_drag_coefficient_file
     - Text
     - No
     - \-
     - Location of your vegetation drag coefficient file, relative to the location of your sqlite in the folder structure. It should look something like *rasters\\veg_drag_coeff.tif*. This supersedes any global drag coefficient.
