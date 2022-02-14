Basic Modelling Concepts
===========================================================


Introduction
^^^^^^^^^^^^^

In the workflow of 3Di we distinguish a schematisation and a simulation template.

.. figure:: image/d_modelling_concepts.png
   :alt: 3Di Modelling Concepts
   
   The modelling concepts of 3Di

In general, the schematisation contains all information that 3Di needs for preprocessing, e.g. to create a calculation grid, and subgrid tables. 
The converted schematisation we call a 3Di model. 
This 3Di model needs information to run, which are initial conditions or events (e.g. rain). 
To run a simulation, a user can use a simulation template or select a 3Di model and add all information required to run a simulation. 

We provide all models of a simulation template based on the sqlite. 

.. TODO:      [create infographic]


The simulation template can be selected in QGIS.

.. TODO:  [insert screenshot]
 

The simulation template can either be used as is, or can be run with changes and stored as a new simulation template. 

Schematisation
^^^^^^^^^^^^^^

A schematisation consists of:

General rasters: 

-	dem_file
-	frict_coef_file
-	interception_file

Simple infiltration rasters:

-	infiltration_rate_file
-	max_infiltration_capacity_file

Interflow rasters:

-	hydraulic_conductivity_file
-	porosity_file

Ground water rasters

-	equilibrium_infiltration_rate_file
-	groundwater_hydro_connectivity_file
-	groundwater_impervious_layer_level_file
-	infiltration_decay_period_file
-	initial_infiltration_rate_file
-	leakage_file
-	phreatic_storage_capacity_file

1D elements:

-	channels
-	pipes
-	manholes
-	connection nodes
-	structures:
	o	weirs
	o	culverts
	o	orifices
	o	pumps
-	location (node id) & type (e.g. water level / discharge / etc) of boundary conditions 
-	dem averaging
-	impervious surfaces & mapping
-	surfaces
-	dem refinement 
-	cross section locations 
-	levees & obstacles

GridSettings

-	use_2d: bool
-	use_1d_flow: bool
-	use_2d_flow: bool
-	grid_space: float
-	dist_calc_points: float
-	kmax: int
-	embedded_cutoff_threshold: float = 0.05
-	max_angle_1d_advection: float = 90.0

TableSettings

-	table_step_size: float
-	frict_coef: float
-	frict_coef_type: InitializationType
-	frict_type: int = 4
-	interception_global: Optional[float] = None
-	interception_type: Optional[InitializationType] = None
-	table_step_size_1d: float = None  # actual default is set in __post_init__
-	table_step_size_volume_2d: float = None  # actual default  is set in __post_init__

Simulation template 
^^^^^^^^^^^^^^^^^^^^

A simulation template consists of:

Simulation settings:

aggregation settings () (TODO Jonas: refine this one more)

numerical settings

- pump_implicit_ratio: 0,
- cfl_strictness_factor_1d: 0,
- cfl_strictness_factor_2d: 0,
- convergence_cg: 0,
- flow_direction_threshold: 0,
- friction_shallow_water_depth_correction: 0,
- general_numerical_threshold: 0,
- time_integration_method: 0,
- limiter_waterlevel_gradient_1d: 0,
- limiter_waterlevel_gradient_2d: 0,
- limiter_slope_crossectional_area_2d: 0,
- limiter_slope_friction_2d: 0,
- max_non_linear_newton_iterations: 0,
- max_degree_gauss_seidel: 0,
- min_friction_velocity: 0,
- min_surface_area: 0,
- use_preconditioner_cg: 0,
- preissmann_slot: 0,
- limiter_slope_thin_water_layer: 0,
- use_of_cg: 0,
- use_nested_newton: true,
- flooding_threshold: 0

physical settings

- use_advection_1d: 0,
- use_advection_2d: 0

time step settings 

- time_step: 0,
- min_time_step: 0,
- max_time_step: 0,
- use_time_step_stretch: true,
- output_time_step: 0

Initial Water in the simulation:

- initial_groundwater (file / global setting)
- initial_waterlevels (file / global setting)
- saved state

Events:

-	Dem edit
-	Breach
-	Laterals
-	DWF
-	structure controls:

	- table
	- time
	- memory

Forcings:

-	Rain
-	Wind
-	Inflow 0D (impervious surfaces & surfaces)

Migration to new work flow
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current situation is that users create a repository. This repository can contain multiple sqlites, these sqlites can contain multiple global settings entries. With each edit a new version of the sqlites is pushed to the server. This situation will change. In the new workflow 3Di accepts only one global settings entry. To aid users to get to the new situation we migrate as follows: 

Each of the global settings entries has been extracted into a schematisation with the following name:
{repo slug}-{sqlite filename}_{global settings name}-{extra info}

In the metadata of the threedimodel the current slug can be found. 
[include screenshot with examples from API]


Workflow
^^^^^^^^^^

In the 3Di workflow a user creates a schematisation. This schematisation consists of sqlite & rasters. The simulation template is extracted from the spatialite. The name of the simulation template is the same as the name in global settings.





