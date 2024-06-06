.. _general_3di_releases:

3Di general releases
--------------------

June 5th, 2024
^^^^^^^^^^^^^^

We have released several important new features, most importantly:

- Major improvements in the **water quality** module. It is now ready for use in real-world applications.

- **Vegetation** can now also be used in the 1D domain (in open channels)

- Improvements in the tools to :ref:`vector_data_importer` to your schematisation make these tools even more powerful and versatile.

- Several improvements have been made to make **manual editing** of 1D open water systems easier.

For more details and further information, see the release notes of the different 3Di components:

- :ref:`3Di Modeller Interface <release_notes_mi_20230605>`
- :ref:`3Di Live <release_notes_3di_live_20240605>`
- :ref:`3Di API <release_notes_3di_api_20240530>`
- 3Di Computational core :ref:`May 30th <release_notes_calccore_20240530>` and :ref:`June 5th <release_notes_calccore_20240605>`

January 8th, 2024
^^^^^^^^^^^^^^^^^

**Water quality**

We are proud to announce that we have added water quality capabilities to 3Di. More specifically, you can introduce concentrations of substances to the simulation, and compute the spread of substance concentrations due to advective forces and (numerical) diffusion.

- Substances can enter the model domain as concentrations in initial water, boundary conditions, laterals, rain, leakage, surface sources and sinks. This applies to the entire model domain (1D, 2D, and groundwater).

- Each forcing can contain concentrations of multiple substances at the same time

- The substance concentration input mirrors the input of the forcing. I.e. 2D initial water levels are supplied as a raster, so 2D initial substance concentrations are also supplied as a raster; substance concentrations in time series rain is also to be provided as a time series; et cetera.

- Substances can have names set by user 

- Output is in NetCDF format. The file has the same structure as hydrodynamic results (results_3di.nc) and can be read with ``threedigrid``.

- The logging includes a substance summary (similar to the flow summary) in JSON format

.. note:
	
	- Input is purely API based (no GUI) 
    
	- Multiple laterals cannot be added to a single computational cell
	
	- All substances are known at the start of the simulation, although amounts can be set to 0.0 [g/m3,?].

**Other improvements and bugfixes**

- Memory efficiency in the generation of 3Di models has been improved. The limit for the DEM size is now 5 billion pixels (including NODATA pixels) (threedigrid-builder #345)

- The flow summary is now JSON format instead text (.log). Units and values are split

- Simulation ID is included in the flow summary (threedi-api #1303)

- Timestep reduction and matrix instability logging are no longer included in simulation.log, because this information is already available in matrix.log and timestep_reduction.log (threedi-calculationcore #674)

- The damage estimation (Netherlands only) now uses the newest land cover raster available in Lizard

- Bugfix: cross-sectional area of groundwater flow made correct on the transitions of the grid size and in case water rises above the bed level. (threedi-calculationcore #708) 

- Bugfix: several small bugfixes for structure control 

- Bugfix: DEM edits in models with interflow would crash the simulation

- Bugfix in ``threedigrid`` for 3Di models with boundary conditions. Time series of some variables did not have the correct ordering (i.e. wrong time series for node or flowline). This applies to ``infiltration_rate_simple``, ``ucx``, ``ucy``, ``leak``, ``intercepted_volume``, ``q_sss`` for Nodes and ``qp``, ``up1``, ``breach_depth``, ``breach_width`` for Lines.


October 31st, 2023
^^^^^^^^^^^^^^^^^^

- Structure controls can now set the gate level, see :ref:`controlling_gate_level`. (threedi-api #2016)

- If generating a 3Di model takes more than 24 h, the process is automatically cancelled (threedi-api #1992)

- Timestep reduction and matrix instability logging are no longer included in simulation.log, to avoid duplication with timestep_reduction.log and matrix.log (threedi-calculationcore #674)

October 2nd, 2023
^^^^^^^^^^^^^^^^^

- Bugfix: More memory is made available for generating 3Di models, to fix a performance degradation that was experienced when generating very large models (threedi-api #2005)

- Bugfix: DEM edits would crash the simulation if the edit polygon covers more than one DEM tile (threedi-tables #262)


September 21th, 2023
^^^^^^^^^^^^^^^^^^^^

- It has been made easier to :ref:`howto_clip_schematisations`.

- Culverts can be imported into the schematisation with the new :ref:`Vector data importer<vector_data_importer>`.

- The :ref:`conveyance_method` can now be used, for more accurate calculation of friction in 1D open water. For this new feature, the following checks where added to the schematisation checker.
     
	- Check 26: make sure friction types with conveyance are only used on v2_cross_section_location
	
	- Check 27: make sure friction types with conveyance are only used on tabulated rectangle, tabulated trapezium, or tabulated yz shapes.
	
	- Check 28: make sure cross-sections with conveyance friction monotonically increase in width
	
	- Check 29: advice to use friction with conveyance on cross-sections where it is possible, has not been used.
	
- The schematisation page in 3Di Management has been revised.

- Schematisation-level description can be added in 3Di Management

- In 3Di Management, many properties of online resources have been made editable: schematisation names, schematisation descriptions, schematisation tags, commit messages, 3Di model names, simulation template names.

- It has become easier to delete revisions and schematisations. When a revision is deleted, its 3Di Model is also automatically deleted. When a schematisation is deleted, its revisions are also automatically deleted.

- In the 3Di Modeller Interface, a new page for generating :ref:`saved_states` was added to the 3Di Models & Simulations simulation wizard.

For further details see the release notes for :ref:`3Di Modeller Interface<release_notes_mi_20230921>` and :ref:`3Di Management<3di_ms_release_20230921>`

.. note::
   3Di Toolbox will be replaced by 3Di Results Analysis on October 1st, 2023. See :ref:`transition_from_3di_toolbox`.

August 7, 2023
^^^^^^^^^^^^^^

- Interflow can now be combined with limiters

- The 3Di computational core now writes the actions resulting from structure controls to a file (structure_control_actions_3di.nc), which can be downloaded via the API. Functionality in threedigrid and the 3Di Modeller Interface will be released in Q4 2023 or Q1 2024.

July 18th 2023
^^^^^^^^^^^^^^

We have released several new features, improvements and bugfixes. Most notably:

- Storage in the groundwater domain is more accurate and less cell size dependent because it uses subgrid

- Simulation templates are inherited from the 3Di Model of the previous revision and persist when the 3Di Model is regenerated.

- User management is now available on management.3di.live (if you have Manager rights)

- If you have run a simulation but forgot to include Lizard postprocessing, you can now start it after the simulation has finished.


For more details, see the :ref:`release notes for the 3Di API<3di_api_release_20231807>`, :ref:`release notes for the 3Di computational core<3di_calccore_release_20231807>`, and :ref:`release notes for 3Di Management core<3di_ms_release_20231807>`


June 14th 2023
^^^^^^^^^^^^^^

**Computational core**

- Vegetation drag can now be included in the calculation of 2D flow

- Exchange between 1D and Groundwater is now possible

- 2D Groundwater boundaries can now be used


**Schematisation checker**

- Tables and columns related to vegetation and groundwater are no longer marked as beta features.

- The following checks were added or updated:

.. list-table:: New or changed checks June 14th 2023
   :widths: 10 20 40
   :header-rows: 1

   * - Check number
     - Check level
     - Check message
   * - 0008
     - Error
     - id must be a positive signed 32-bit integer.
   * - 0045
     - Warning
     - v2_channel.dist_calc_points should preferably be at least 5.0 metres to prevent simulation timestep reduction.
   * - 0045
     - Warning
     - v2_pipe.dist_calc_points should preferably be at least 5.0 metres to prevent simulation timestep reduction.
   * - 0045
     - Warning
     - v2_culvert.dist_calc_points should preferably be at least 5.0 metres to prevent simulation timestep reduction.
   * - 0056
     - Error
     - v2_channel.id has both open and closed cross-sections along its length. All cross-sections on a v2_channel.id object must be either open or closed.
   * - 0063
     - Warning
     - v2_connection_nodes.storage_area * 1000 for each pumpstation's end connection node must be greater than v2_pumpstation.capacity; water level should not rise >= 1 m in one second
   * - 0098
     - Warning
     - v2_cross_section_definition.width and/or height should probably be at least 0.1m
   * - 0202
     - Warning
     - The length of v2_channel is very short (< 5 m). A length of at least 5.0 m is recommended to avoid timestep reduction.
   * - 0202
     - Warning
     - The length of v2_culvert is very short (< 5 m). A length of at least 5.0 m is recommended to avoid timestep reduction.
   * - 0202
     - Warning
     - The length of v2_pipe is very short (< 5 m). A length of at least 5.0 m is recommended to avoid timestep reduction.
   * - 0360
     - Warning
     - v2_global_settings.dist_calc_points should preferably be at least 5.0 metres to prevent simulation timestep reduction.
   * - 0501
     - Error
     - v2_vegetation_drag.vegetation_height is <=0
   * - 0503
     - Warning
     - v2_vegetation_drag.height is recommended as fallback value when using a vegetation_height_file.
   * - 0504
     - Error
     - v2_vegetation_drag.vegetation_stem_count is <=0
   * - 0505
     - Error
     - v2_vegetation_drag.vegetation_stem_count must be defined.
   * - 0506
     - Warning
     - v2_vegetation_drag.vegetation_stem_count is recommended as fallback value when using a vegetation_stem_count_file.
   * - 0507
     - Error
     - v2_vegetation_drag.vegetation_stem_diameter is <=0
   * - 0508
     - Error
     - v2_vegetation_drag.vegetation_stem_diameter must be defined.
   * - 0509
     - Warning
     - v2_vegetation_drag.vegetation_stem_diameter is recommended as fallback value when using a vegetation_stem_diameter_file.
   * - 0510
     - Error
     - v2_vegetation_drag.vegetation_drag_coefficient is <=0
   * - 0511
     - Error
     - v2_vegetation_drag.vegetation_drag_coefficient must be defined.
   * - 0512
     - Warning
     - v2_vegetation_drag.vegetation_drag_coefficient is recommended as fallback value when using a vegetation_drag_coefficient_file.
   * - 0613
     - Warning
     - v2_connection_nodes.id has a an associated inflow area larger than 10000 m2; this might be an error.
   * - 0614
     - Warning
     - v2_connection_nodes.id has more than 50 surface areas mapped to it; this might be an error.
   * - 0717
     - Error
     - The file in v2_vegetation_drag.vegetation_height_file is not present
   * - 0718
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_count_file is not present
   * - 0719
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_diameter_file is not present
   * - 0720
     - Error
     - The file in v2_vegetation_drag.vegetation_drag_coefficient_file is not present
   * - 0737
     - Error
     - The file in v2_vegetation_drag.vegetation_height_file is not a valid GeoTIFF file
   * - 0738
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_count_file is not a valid GeoTIFF file
   * - 0739
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_diameter_file is not a valid GeoTIFF file
   * - 0740
     - Error
     - The file in v2_vegetation_drag.vegetation_drag_coefficient_file is not a valid GeoTIFF file
   * - 0757
     - Warning
     - The file in v2_vegetation_drag.vegetation_height_file has multiple or no bands.
   * - 0758
     - Warning
     - The file in v2_vegetation_drag.vegetation_stem_count_file has multiple or no bands.
   * - 0759
     - Warning
     - The file in v2_vegetation_drag.vegetation_stem_diameter_file has multiple or no bands.
   * - 0760
     - Warning
     - The file in v2_vegetation_drag.vegetation_drag_coefficient_file has multiple or no bands.
   * - 0777
     - Error
     - The file in v2_vegetation_drag.vegetation_height_file has no CRS.
   * - 0778
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_count_file has no CRS.
   * - 0779
     - Error
     - The file in v2_vegetation_drag.vegetation_stem_diameter_file has no CRS.
   * - 0780
     - Error
     - The file in v2_vegetation_drag.vegetation_drag_coefficient_file has no CRS.
   * - 1401
     - Error
     - v2_vegetation_drag.vegetation_height_file has values <0 or is empty
   * - 1402
     - Error
     - v2_vegetation_drag.vegetation_stem_count_file has values <0 or is empty
   * - 1403
     - Error
     - v2_vegetation_drag.vegetation_stem_diameter_file has values <0 or is empty
   * - 1404
     - Error
     - v2_vegetation_drag.vegetation_drag_coefficient_file has values <0 or is empty
   * - 1151
     - Warning
     - columns ['flow_variable', 'aggregation_method'] in table v2_aggregation_settings should be unique together
   * - 1152
     - Warning
     - v2_aggregation_settings.timestep is different and is ignored if it is not in the first record
   * - 1153
     - Warning
     - v2_aggregation_settings.timestep is smaller than v2_global_settings.output_time_step
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is pump_discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is lateral_discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is simple_infiltration.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is rain.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is leakage.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is current and flow_variable is interception.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum and flow_variable is discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum_negative and flow_variable is discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum_positive and flow_variable is discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is current and flow_variable is volume.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum_negative and flow_variable is surface_source_sink_discharge.
   * - 1154
     - Warning
     - To use the water balance tool, v2_aggregation_settings should have a row where aggregation_method is cum_positive and flow_variable is surface_source_sink_discharge.
   * - 1227
     - Error
     - v2_control.control_id references an id in v2_control_memory or v2_control_table, but the table it references does not contain an entry with that id. 


April 25th 2023
^^^^^^^^^^^^^^^

**3Di Live**

- Breaches: a line has been added to the visualisation of breaches in 3Di Live. Discharge and flow velocity are visualized on these lines by moving dots.

**Schematisation checker**

*New checks*

Several checks have been added.

- Add INFO 109 and 110: the bottom level of a manhole cannot be higher than the reference level of the closest cross-section of any channel it is connected to. threedigrid-builder automatically fixes this, hence info instead of warning.

- Add WARNING 108: the crest_level of a weir or orifice cannot be lower than the bottom_level of any manhole it is connected to.

- Add ERROR 326: this gives an info message if a record exists in the simple_infiltration table, but is not referenced from the global settings.

- Add ERROR 66: this raises a warning if a pumpstation empties its storage area in less than one timestep.

- Add ERROR 1205 to make sure that a timeseries is not an empty string.

- Add ERROR 1206 to confirm that the timesteps in all boundary condition timesteps are the same.

*Beta features*

The 3Di spatialite now supports *beta* tables, fields, and values. These are used for test purposes, and will become available to all users once testing has been completed.

- Added ERROR 1300: If a user puts a non-null value in a column marked as beta in threedi-schema, this will be reported by the schematisation checker.

- Added ERROR 73: groundwater boundaries are allowed only when there is groundwater hydraulic conductivity.

- Added ERROR 74: groundwater boundary types are not allowed on 1D boundary conditions.

- Added groundwater 1D2D range checks for manholes, channels, and pipes for exchange_thickness, hydraulic_conductivity_in, and hydraulic_conductivity_out.

- Add ERRORs and WARNINGs for vegetation_drag input. Both rasters and global values.

**Models & Simulations API**

- Added support for uploading additional initial water levels to an existing 3Di models. Both 1D and 2D are supported.

- Added support for uploading and downloading computational grid Geopackage files for 3Di models.

- Bugfix: We have made the use of Lizard raster rain in a simulation more robust by using longer retries getting data from Lizard.

- The duration of a constant wind event can now be patched while the simulation is paused.

- In the near future an extra log file (scheduler.log) will be added to log files in the downloadable ZIP file. The scheduler log file is intended for 3Di developers to identify problems when simulations have crashed.


**Computational grid**

- Channels with calculation type *connected* or *double connected* can now be placed outside the DEM, as long as they connect to a location where a 2D cell is present. If a 'potential breach' or 'exchange line' is used to set the location to which the calculation node connects, the location of those features determines whether an error is raised. If a channel with calculation type connected is outside of the DEM, but the closest point on its exchange_line is on the DEM, the computional grid can be built and the 3Di model is valid.

- 1D-2D links that cross an obstacle will take the exchange level from the obstacle

**Authorisation**

- The former SSO configuration has been removed. Username/passwords are now only accepted if they have a Personal API Key that was migrated earlier.

.. - Version included in release



February 24th 2023
^^^^^^^^^^^^^^^^^^

Hotfix:

- In rare cases the DEM edit was crashing. This is fixed


February 10th 2023
^^^^^^^^^^^^^^^^^^

Hotfix:

- Fixed CRS comparison in table generation (threedi-tables 3.0.5).
- Sources & sinks Lizard raster source did dot work due to problem with internal *LizardRasterSourcesSinks* serialization/deserialization.
- Max time step set to NULL is allowed 


February 6th 2023
^^^^^^^^^^^^^^^^^^

We have released the following features:

- Support to :ref:`import_gwsw_hydx`
- Eased restrictions on rasters 
- User friendly breaches editing. Also added the ability to name them and keep breaches persistent throughout revisions, model changes and calculation grid changes. 
- :ref:`Boundary conditions timeseries can be uploaded as CSV files <simulate_api_qgis_boundary_conditions>`, so it is no longer needed to make a new revision when you want to use different boundary conditions. 
- Structure control can be set by uploading a JSON file


January 3rd 2023
^^^^^^^^^^^^^^^^

Hotfix:

- Correct use of offset for timed control structures

December 16th 2022
^^^^^^^^^^^^^^^^^^

Hotfix:

- Fixed saved states using interception

December 6th 2022
^^^^^^^^^^^^^^^^^^

Hotfix:

- Fixed obstacle edits for models with maximum infiltration capacity raster

November 21th 2022
^^^^^^^^^^^^^^^^^^

**Tables**

When generating the subgrid tables the approach has changed. Instead of user defined equidistant steps 3Di now takes non equidistant steps. This saves a ton of space when generating 3Di models and is especially of impact when modelling in hilly areas or in areas where there is a large difference between pixels.

.. image:: /image/subgrid_tables_non_equidistant_steps.png
   :alt: Showing the difference between equidistant and non equidistant steps.

*DEM edits*

- Refactor of dem edits to make this feature more robust.

**Gridbuilder**

- More efficient: ignores unused refinement levels



November 2nd 2022
^^^^^^^^^^^^^^^^^^^^

Hotfix:

- Removed incorrect boundary conditions (legacy) initialization at t=0 with only 0 values

October 26th 2022
^^^^^^^^^^^^^^^^^^^^

Hotfix:

- Fixed issue with embedded channel cross-sections


May 2022
^^^^^^^^^^

The most important change in this release is the new login page.

.. image:: /image/login.png

For information about accounts and logging in, please visit this section in the documentation: :ref:`f_authentication_user_management`.

We also added or changed the following:

- Added personal api keys (beta).
- Copy simulation template between threedimodels.
- Added user management screens
- Added users sub-endpoint to organisations to be able to patch roles.
- Enforce maximum amount of active ThreediModels per organisation and schematisation.
- Anybody who has the 'simulation_runner' role will get the 'creator' role in
  a one-time data migration.
- Solved error in the Swagger page having to do with external validation.
- Set the 'security' (security requirements) in the OpenAPI spec.
- Fixed v3/statuses.
- Set up client-side OAuth2 in swagger.
- Fixed error message formatting bug in has role in organisation check.
- Fixed broken websocket `post_simulation_action`.
- Prevent browser login screens by setting the WWW-Authenticate header on a
  401 response to "Bearer".
- Fixed login/logout buttons in DRF views.
- JWT authentication needs to add `role_info` to User object.
- Ansible fixes after deployment of 2.18.1.
- Added creation of Cloud Optimize Geotiff's for `infiltration_rate_file` and `porosity_file` raster files.
- Use Celery for API workers instead of Django channels.
- Use access policies on all ViewSets, by default only admin has access.
- Reroute all login/logout to Cognito, remove SSO connection (except for the
  token endpoint which will migrate username/passwords to API Keys gradually).
- Run API websockets (ASGI) in own service.
- Threedimodel tables file can only be downloaded by admin user.
- Dropped Django `Group` and model permissions, changed to using DRF permissions.
- Automatically migrate SSO users to API keys with is_password=True when they
  authenticate with username/password through the API (token endpoint).
- Allow API keys for retrieving tokens.
- Fixed the schema for schematisations/{}/revisions/{}/create-threedimodel and
  /check.
- Changed status code of "Not Authenticated" responses from 403 to 401.
- Removed global-redis as a dependency for nginx.
- Revised roles: new roles are viewer, simulation_runner, creator, and manager.
- Catch file delete exception in post delete when file was deleted first.
- Bumped threedi-tables to 1.2.7


April 9th 2022 (hotfix)
^^^^^^^^^^^^^^^^^^^^^^^^

In this hotfix release, we fixed the following issues:

- DEM edit
- Error with type 'Half verhard' bugfix
- Refinement errors
- Sporadically filled DEM
- Initial ground water rasters 2D
- Cloning with initial saved state


.. _klondike_release:

January 31st 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On January 31st we have released the backend for the Klondike release. In this release we introduce a brand new route to process schematisations into 3Di models. This will replace the process known as 'inpy'.
For users that have not been migrated yet, this will not have effect on their work process. 3Di Models will simulate as before.

The migration will be rolled out gradually, users will be contacted for this. 3Di Management is available for all users right away, but keep in mind that the new features mostly work on migrated schematisations and 3Di Models.
Contact our servicedesk if you have any questions regarding migration.

We use the following definitions:

- Simulation templates
- Schematisations
- 3Di Models

**Simulation templates**

Simulations can be started up using a simulation template. A simulation template can be seen as a pre-defined setup of a simulation. It can contain:

- initial water level rasters
- control structures
- dry weather flow patterns
- lateral inflow
- time series of boundary conditions
- simulation settings (Aggregation settings, Numerical settings*, Physical Settings*, Time step settings*)

\*\ These settings are required


**Numerical Settings**

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

**Physical Settings**

- use_advection_1d: 0,
- use_advection_2d: 0

**Time step settings**

- time_step: 0,
- min_time_step: 0,
- max_time_step: 0,
- use_time_step_stretch: true,
- output_time_step: 0

**Initial Water**

- initial_groundwater (file / global setting)
- initial_waterlevels (file / global setting)
- saved state


**Schematisation**

A schematisation contains:

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
	-	weirs
	-	culverts
	-	orifices
	-	pumps
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
-	table_step_size_1d: float = None
-	table_step_size_volume_2d: float = None



**3Di Model**

A 3Di Model is generated from a schematisation. The generation takes the grid & table settings from the spatialite and processes the schematisation into a 3Di Model.


**3Di Management Screens**

3Di Management has been extended with a Models section. In this Models section users can:

For 3Di Models

- See an overview of Models in a list
- See an overview of Models in the map
- Per Model a detailed page is available including the location on the map, size of the Model.
- Per Model is an option to run the simulation on 3Di Live
- On the detailed Model page there is an option to run the simulation on 3Di Live
- On the detailed Model page there is an option to delete the model
- On the detailed Model page there is an option to re-generate the model from the schematisation
- A history of simulations performed with the 3Di Model
- An overview of available simulation templates. By default 1 simulation template is available for every Model. This is generated based on the spatialite. The name of the simulation template is the name in the v2_global_settings table.

For schematisations users can:

- See all available schematisations in a list.
- See past revisions of a schematisation
- Generate a 3Di Model from a schematisation or re-generate an existing model from the schematisation. Keep in mind that doing so will remove additionally generated templates




March 23rd 2021
^^^^^^^^^^^^^^^^

3Di is expanding! We are proud to announce that due to international recognition we are expanding the capacity of 3Di:

- The first stage of setting up our second calculation center in Taiwan is finished. Organisations that prefer this center can connect to 3Di via `3di.tw <https://www.3di.tw>`_.
- To cope with increasing demand for calculations the capacity of our main calculation center has been upgraded


*3Di available for scientific researchers*

Interested to use 3Di in your research? We are proud to announce that we now supply free licenses for scientific researchers.
Contact us via info@3diwatermanagement.com when you're interested.

March 8th 2021
^^^^^^^^^^^^^^

*Update land use map for the calculation of damage estimations*

For usage in The Netherlands only:

We have updated the land use map that is being used for the calculation of damage estimations. This to ensure tunnels are placed under a road.

Source date & time

- BAG: 2019-05-09
- BGT: 2019-05-09
- BRP: 2019-05-15
- NWB: 2019-05-01
- Top10NL: 2018-07-16

The map can be viewed here: stowa.lizard.net

