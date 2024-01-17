.. _a_release_notes:

Release notes
==============

.. _general_3di_releases:

3Di general releases
--------------------

January 8th, 2023
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


.. _release_notes_LS:

3Di Live
--------

January 11th, 2024
^^^^^^^^^^^^^^^^^^

- Model elements and 1D flow are now visualised using WebGL, which improves performance. 1D flow is now visualised with moving waves instead of dots (#1341, #1342).

- The Line selection tool now supports drawing a side view trajectory with a custom path, i.e. with more than 2 vertices. (#1446)

- Option to rescale DEM color scale based on current extent (#853)

- Show days in clock, relevant for simulations longer than 24 hours (#1387)

- When starting a session, the organisation that owns the model is automatically selected in the "Billing goes to" dropdown (#1251)

- When switched on, model grid is shown regardless of zoom level. It is no longer necessary to zoom in. (#1509)

- The labels that are shown when hovering over model elements now show the display name instead of ID (#1505)

- The organisation to which the simulation is billed is now included in the info panel (#1284)

- Enforce "Simulation runner" and "viewer" roles (#437). A user must have "simulation_runner" role in a organisation to be able to start simulations billed to that organisation. A user must have "viewer" role in an organisation to be able to follow simulations of an organisation.

- Round editable values to 2 decimals (#1345)

- The user interface is loaded while loading the 3Di model, instead of after loading the 3Di model (#426)

- Bugfix: Graph data was rounded to 2 decimals, while only the value on the labels should be rounded to two decimals (#1318)

- Bugfix: Simulation could not be started if multiple simulation templates are available (#1330)

- Bugfix: Show names instead of numbers for properties of model elements (e.g. sewerage type) (#1185)

- Bugfix: Nodatavalue was shown as actual value (#434)





October 31st, 2023
^^^^^^^^^^^^^^^^^^

- Correctly show DEMs that contain None, NaN, inf or -inf values (threedi-api #2041)


October 18, 2023
^^^^^^^^^^^^^^^^
- Flood barriers can now always be clicked for more info, also when the Flood barrier tool is not active (#527)

- When hoovering over the Side view plot, the mouse position is indicated on the map (#449)

- DEM value is shown when clicking on the map using the Point tool (#526)

- Asset properties that are in decimal numbers are now rounded to two decimals (#453)

- Display names of assets are ellipsed and full name is shown when hoovering over (#431)

- 3Di Live and 3Di Management are now "domain agnostic", so they can also be hosted on other domains, like 3di.twinn.io (#1245)

- An *Info* panel was added, with details about the simulation and the 3Di model used (#273)

- Values in charts labels are now rounded to 2 decimals (#1168)


September 21, 2023
^^^^^^^^^^^^^^^^^^

- Bugfix: Allow negative and/or decimal number input in weir crest level edit (#949, #432)

April 25th 2023
^^^^^^^^^^^^^^^

- Breaches: a line has been added to the visualisation of breaches in 3Di Live. Discharge and flow velocity are visualized on these lines by moving dots.


March 20th 2023
^^^^^^^^^^^^^^^

- Now gives a message when max number of licenses is reached


November 21th 2022
^^^^^^^^^^^^^^^^^^

**Flood barriers tool**

A flood barrier can prevent a certain area from flooding. You can set the height of the flood barrier.
For more information about the flood barriers tool, you can watch the `Floodbarriers preview <https://www.youtube.com/watch?v=by4MS5DdEgY>`_ on Youtube.

**Added features**

- Show 2D flow lines (new model generation required for this)

**Fixed**

- Link to 3Di documentation under ‘help


August 2022
^^^^^^^^^^^^
- We have hotfixed the waterdepth interpolation to make sure that no water is shown visually before the start of a simulation and to avoid large patches  of interpolated water when zooming out

- Added Icon Forecast

- Implemented the following rasters:

    - ICON-global forecast of precipitation with hourly timestamp

    - ICON-EU forecast of precipitation with hourly timestamp

    - ICON-D2 forecast of precipitation with hourly timestamp


- Icon forecast gives you a global forecast of rainfall for the next 24 hours. More information can be found `here  <https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html>`__:

- Added a rainbarchart to show the amount of precipitation during the simulation time

- Limit the datepicker of forecasted rain to the range of dates that the forecast spans. Mostly 2-7 days.

- Show in the datepicker if there actually is a rain-event on the model extend.

- Improved search functionality. For instance you can now toggle to view all types of sewers when searching on sewers.

- Fixed a bug where a model without a simulation template would stall in the live-site.

- Fixed a bug where the water depth on nodes would display incorrect.

- Fixed a bug where the mouse cursor would change to a hand indicating you would be able to click the element but couldn't.



February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released new versions of 3Di Live.

- Simulation templates are used

October 18th 2021
^^^^^^^^^^^^^^^^^

We have released new versions of 3Di Live

- Saves the organisation you have selected and your previous search term last
- Forms reflect the last action from the user. E.g. for rainfall it doesn't reset to the default value anymore
- Events can be deleted or stopped. For now pumps, discharges, rain and wind are supported

March 23rd 2021
^^^^^^^^^^^^^^^^

We have update 3Di Live with following features:

- Water depth graph now also shows a graph with water depth - 0
- Add a clock time hover
- Add hh:mm at the start of the simulation, to make clear what are the units of the clock
- Add decimal support for discharge (when editing pumps)
- Add minute support for durations
- Ability to select different units when editing a pump discharge

February 22nd 2021
^^^^^^^^^^^^^^^^^^^^

Some bugfixes in 3Di live:

- Rescale DEM coloring based on model
- Correct water depth calculation for manholes
- Close culvert in both directions
- Rate limiter interferes with simulation in spectator mode
- Moving dots for 0D1D models fixed
- Correct handling of wind direction
- Breach editing used wrong id


.. _release_notes_MS:

3Di Management
--------------

January 11, 2024
^^^^^^^^^^^^^^^^

- Search and filter options were added to the 3Di models overview (#1382)

- The filters that are set on pages that list models, schematisations, or simulations are now also applied when using "Export to Excel" (1184)

- On the simulation overview page, all initials and events are listed (#1327)

- You can now search for simulations by simulation ID (#239)

- Include organisation in 3Di Management URLs, so that it is easier to share URLs (#1451)

- The user interface for "add tags" has been improved (#1504)

- Bugfix: Visualise negative laterals correctly on the simulation detail page (#1389)

- Bugfix: "Run on 3Di Live" uses the wrong template is multiple templates are available for the 3Di model (#1329)

- Bugfix: Revision nr. column now correctly displays revision numbers > 99 (#1417)

- Bugfix: Wind events were not visualised correctly for long simulations in some cases (#934)


October 18, 2023
^^^^^^^^^^^^^^^^
- The simulation overview page now shows which post-processing options have been used (#814)

- You can now post-process results in Lizard for finished simulations. This option can be used if no post-processing for this simulation has been done and the raw results are still available, i.e., within 7 days after the simulation was finished. (#835, #1249, #1160)

- The "Export to Excel" option for Simulations and 3Di Models now downloads all items, not just the ones that are shown on the page (#1040)

- Simulations can now be removed from the queue (#780)

- If you do not have management rights, the *Users* button is disabled; it will now show a list of users in your organisation that have management rights when hovering over it (#852)

- You can now select multiple 3Di models, schematisations, and/or revisions and delete them all at once, including in the *Choose other revision* window on the schematisation detail page (#815, #1228)

- Schematisations can be moved to a different organisation, if you have *Creator* or *Manager* rights for the organisation that currently owns the schematisation *and* the organisation to which you want to transfer it (#234)

- Multiple improvements were made to the 3Di model overview, especially for organisations with more than 250 3Di models (#231, #227)

- The simulation ID is now shown in the simulations overview (#233)

- Bugfix: Links in *queued simulations* list were wrong, this has been fixed (#781)

- Bugfix: Schematisation detail page: not all info was updated when switching to another revision (#1158)


.. _3di_ms_release_20230921:

September 21, 2023
^^^^^^^^^^^^^^^^^^

- Redesign of the *Schematisation details* page (#741)
  - Schematisation name can be edited
  - Schematisations now have a *Description*, which can be edited. Note: in the near future, you will also be able add a schematisation-level description when creating a schematisation in the 3Di Modeller Interface.
  - Commit message can be edited
  - Tags can be edited
  - 3Di model names can be edited
  - Simulation template names can be edited
- It has become easier to delete revisions and schematisations. When a revision is deleted, its 3Di Model is also automatically deleted. When a schematisation is deleted, its revisions are also automatically deleted. 
- Added "Delete schematisation" button in the schematisation section. This deletes the schematisation, which cascades to deletion of its revisions and 3Di models.
- Make simulation name editable on simulation detail page (#792)
- Schematisation revision detail page: show available saved states (#855)
- Simulation overview page - forcings: show two decimals (#813)
- Filter live statuses by organisation (#935)
- *Export to Excel file* on the *Simulations* and *3Di Models* overview pages now exports *all* items instead of only the listed items. #1040
- Bugfix: "Has 3Di Model" column not updated after model deletion (#686)


.. _3di_ms_release_20231807:

June 18th 2023
^^^^^^^^^^^^^^

- User management is now available on 3Di management if you have Manager rights
- Vegetation rasters are now included in schematisation revision overview
- Add time zone (UTC offset) when listing start or end datetime of simulation
- "Export to Excel file" button on schematisations page now downloads all schematisation names, and shows a modal with a progress bar
- Schematisation detail page: Disable "run in 3Di Live" option if 3Di Live is not part of contract
- Schematisation list no longer shows schematisations that have no revisions, unless you explicitly choose this option
- Bugfix: On the schematisation revision detail page, Some raster download links did not work
- Bugfix: On the schematisation revision detail page, "Predefined simulation data" section had wrong contents
- Bugfix: On the schematisation revision detail page, rasters where only listed after a 3Di model had been created


March 20th 2022
^^^^^^^^^^^^^^^^^^

- improved placement of data, using the correct definition of schematisation, simulation and model
- show current number of license and how many are in use
- show max allowed number of models
- show an error message when a simulation template fails to be created
- removed graphs from levee element


November 21th 2022
^^^^^^^^^^^^^^^^^^

- See the complete commit message in the revision overview when hovering
- This overview now also shows for which revisions a 3Di model is available

.. image:: /image/management_screen_schematisation_commit_message_when_hovering.png
   :alt: You can now see the commit message when hovering.

- When clicking on a simulation template, the link now is directed to the details page of the simulation where the template was based upon. Showing the events in the simulation template.
- Added a save as template button to simulations detail page

.. image:: /image/management_screens_save_as_template.png

- Shows queued simulations:

.. image:: /image/management_screens_queued_simulations.png

- Regenerating a model that is active now gives a clear error message

.. image:: /image/management_screens_regenerating_active_model_gives_clear_error_message.png

- If a project tag is added to a simulation it will be shown


February 2022 (Klondike) v2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-	Fixed a bug where the models map page stayed empty if there were no models
-	Fixed a bug where a schematisation that has no revisions yet showed an empty page
-	Add information about the current framework version, so the user knows if the current 3Di model is up to date
-	Show model id as well as name on the models list page
-	The gridadmin.h5 file can now be downloaded from the model detail page as well as from the simulation results download
-	Simulation templates can now also be deleted
-	The information on the models list page can be exported as an Excel file
-	Generating a model can fail if the schematisation already has the maximum number; show an error message if this happens.
-	Add a column for 'latest revision' to the Schematisations table.
-	Instead of subpages, now everything is reachable from the front page


February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^

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



.. _release_notes_MI:

3Di Modeller Interface
----------------------

January 17, 2024
^^^^^^^^^^^^^^^^

**3Di Results Analysis 3.4.0**

*Schematisation checker*

- Warning (impervious) surface geometry has different area then the 'area' attribute (tolerance is 1 m2) (#343)

- Warning for invalid references from *Surface map* or *Impervious surface map* (#337)

- Info message when refinement_level equals kmax (#345)

- Bugfix: Warning was incorrectly given when interception_global = 0.0 (#340)

- Bugfix: Schematisation checker no longer fails when values that need to be checked are NULL (e.g. pumpstation type).

*Other*

- Water depth/level processing algorithms now include days in the time display if selected time passes 24 h (#661)

- Processing algorithms "Computational grid from gridadmin.h5 file" and "Computational grid from schematisation" now show warnings (if applicable)

- Bugfix: after using the Water Depth processing tool, results_3di.nc could not be loaded as Mesh (#573)

- Bugfix: Water depth/level processing algorithms are now compatible with h5py 3.0 (#966)

**3Di Models & Simulations 3.9.0**

- Make sure all tools use the same version of the 3Di Schematisation Checker (remove python wheel threedi-modelchecker, #523)

- Add "Refresh" button to running and finished simulations lists (#491)

- Add "Refresh" button to overview of available simulation templates (#465)


January 11, 2024
^^^^^^^^^^^^^^^^

**3Di Schematisation Editor 1.8.0**

- Easily load schematisations from your 3Di working directory through the new "Load Schematisation dialog" (#117)


**3Di Models & Simulations 3.8.0**

- By default, simulations will be billed to the organisation to which the 3Di model belongs. It is still possible to bill simulations to other organisations you have access to, but only if you deliberately choose this option (#107).

- Change all functional and textuel references to "3Di Toolbox" to "3Di Schematisation Editor" (#503)

- Bugfix: In the simulation wizard, uploading a rainfall NetCDF timeseries caused a python error (#510)


December 1st, 2023
^^^^^^^^^^^^^^^^^^
**Lizard QGIS plugin 0.2.0**

The Lizard plugin for QGIS is now included in the 3Di Modeller Interface. You can use this plugin to access the Scenario Archive: browse for scenario's, add the as WMS and download raw and processed results.

**3Di Schematisation Editor 1.7.2**

- Bugfix: If the Spatialite table ``v2_surface_map`` contains rows with references to non-existent ``v2_surface`` id's, the conversion to GeoPackage no longer gives a Python error. The invalid references are reported and ignored, and the conversion is completed. (#192)

**3Di Results Analysis 3.3.0**

- All interaction with the 3Di working directory now uses the new package ``threedi-mi-utils`` (#805)

- Bugfix: pumps with display names longer than 32 characters were not shown at all when loading the computational grid via the Results Manager. This has been fixed now.



November 14th, 2023
^^^^^^^^^^^^^^^^^^^

**3Di Models & Simulations 3.7.0**

- All interaction with the 3Di working directory now uses the new package ``threedi-mi-utils`` (ThreeDiToolbox #805)

- Bugfix: Revision commit now waits for files to be in 'uploaded' or 'processed' state (#512)

- Bugfix: Simulation wizard stops trying to initialize the simulation when file processing status is "error" (#504)


October 31st, 2023
^^^^^^^^^^^^^^^^^^

**3Di Results Analysis 3.2**

- Introduced two new presets for the :ref:`results_aggregation`: *Water on street duration (0D1D)* and *Water on street duration (1D2D)* (#935)

- Bugfix: The "Catchment for polygons" option in the Watershed tool no longer gives an error (#948)

October 24th, 2023
^^^^^^^^^^^^^^^^^^

**3Di Models & Simulations 3.6.2**

- Base URL is used instead of Base API URL, so that the URLs for obtaining Personal API Keys and opening the 3Di Management page are domain dependent. For example, you can set the Base URL to "3di.twinn.io" so that the plugin knowns that the management page is located at management.3di.twinn.io. (#505)

October 19th, 2023
^^^^^^^^^^^^^^^^^^

**3Di Results Analysis 3.1.12**

- Bugfix: make Side view tool work for 3Di Models without 2D (#931)

- Temporarily remove the "Water on street duration" preset from the Result aggregation tool while a bug is being fixed

October 16th, 2023
^^^^^^^^^^^^^^^^^^

**3Di Schematisation Editor 1.7.1**

- Moving a channel vertex that has a cross section location on it now also moves the cross section location (#100)
- Vector data importer main button shows options when clicked (#185)
- Vector data importer dialog is disabled as long as no source layer is selected (#185)

**3Di Models & Simulations 3.6.1**

- Subtle redesign of the *Uploads* and *Running simulations* dialogs (#500)
- Add cancel button to "store / replace" question dialog, show correct path when download has completed (#439)
- Bugfix: Simulation wizard, rain *Stop after* value was not read correctly from simulation template if *Start after* was > 0 (#498)
- Bumped dependencies: *threedi-api-client 4.1.4*, *threedi-modelchecker 2.4.0*, *threedi-schema 0.217.11*.


October 2nd, 2023
^^^^^^^^^^^^^^^^^

**3Di Schematisation Editor 1.7.0**

- Added "Import Weirs" processing algorithm (#178)
- Added "Import Weirs" graphical user interface (#179)
- Added "Import Orifices" processing algorithm (#180)
- Added "Import Orifices" graphical user interface (#181)
- Make attribute forms scrollable (#170)

**3Di Results Analysis 3.1.11**

First official version of this plugin. This is the successor of the 3Di Toolbox plugin. See :ref:`transition_from_3di_toolbox` for details.



.. _release_notes_mi_20230921:

September 21st, 2023
^^^^^^^^^^^^^^^^^^^^

**3Di Models & Simulations 3.6.0**

- A new page "Generate saved state" was added to the Simulation Wizard. You can now name and add tags to the saved state, and choose when the saved state is created (end of simulation or specific moment in time) (#473)
- The "New schematisation" Wizard now checks if DEM and friction files actually exist (#483)
- A time zone explainer was added for 'radar rain' in the Simulation Wizard (#452)
- The time zone can now be specified on the Duration page of the Simulation Wizard (#263)
- When using *Tab* to move from one widget to the next on the Duration page, the sequence is more logical (#263)
- Bugfix: If there is global 2D initial water level in the template, this is now used to populate the Simulation Wizard and used in the simulation (#474)
- Bugfix: 'Post-processing in Lizard' settings are now correctly read from the template, Simulation Wizard is correctly populated with these settings so that they are used in the simulation (#481)
- Bugfix: Saved states were used even if the option was disabled, this has been fixed now #484


**3Di Schematisation Editor 1.6.0**

- Culverts can be imported into the schematisation with a new graphical user interface  (#118, #119, #120, #176)
- Support for using the :ref:`conveyance_method` in the calculation of friction in 1D open water: "Manning with conveyance" and "Chezy with conveyance" have been added as friction types in the :ref:`cross_section_location` layer (#159)
- All layers related to :ref:`control structures<control>` are now also added to the project (#169)
- When deleting connection nodes, you will now be asked if you want to delete all referenced features only once, instead of for each referenced feature (#67). This makes it much easier to :ref:`howto_clip_schematisations`.
- Bugfix: In some cases, surfaces and their surface maps were not converted properly from spatialite to geopackage (#161)
- Bugfix: When moving a connection node, some attributes of features referencing that connection node became NULL (#162)
- Bugfix: Improved user feedback messages when spatialite database schema is unknown, too high or too low (#103)
- Bugfix: In a new profile, the schematisation editor no longer keeps complaining about the Macro settings being wrong (#158)

**3Di Toolbox 2.5.5**

- Update *Generate computational grid* and *Check schematisation* with the new conveyance friction types, by bumping the threedi-\* dependencies (threedigrid to 2.0.\*, threedi-modelchecker to 2.4.\*, threedigrid-builder to 1.12.\*


July 20th 2023
^^^^^^^^^^^^^^

**3Di Toolbox 2.5.4**

- Add processing algorithm for generating maximum water depth / water level rasters

- Make the plugin work for both QGIS <= 3.28.5 and QGIS > 3.28.5 by making installed h5py version depend on QGIS version


June 23 2023
^^^^^^^^^^^^

**3Di Models & Simulations 3.5.1**

- Bugfix: Making a copy of a schematisation failed if sqlite did not contain *v2_vegetation_drag* table. The sqlite is now migrated to the latest schema version on the fly so this type of issue will no longer arise. (#470)


June 16 2023
^^^^^^^^^^^^

**3Di Toolbox 2.5.3**

- Compatibility with schema 217

- New version of 3Di Schematisation Editor (threedi-modelchecker 2.2.4)

**3Di Models & Simulations 3.5.0**

- Compatibility with schema 217 (#462)

- Added handling of the Vegetation drag settings rasters. (#460)

- Expose attributes for vegetation and groundwater exchange in attribute forms and attribute tables (#151)

- Improve the use of saved states in the simulation wizard (#461)

- Bugfix: uploading CSV files for both 1D and 2D boundary conditions would fail if there are 1D boundary conditions with the same ID as a 2D boundary condition

**3Di Schematisation Editor 1.5.0**

- Compatibility with schema 217 (#148)

- Copy friction value from nearest cross-section location (if exists) when digitizing a new cross section location (#141)

- Bugfix: Error when adding new cross section location > empty bank level field > commit (#142)

- Added Vegetation drag settings table with associated raster layers (#145)

- "Import culverts" processing algorithm (#127)


April 25th 2023
^^^^^^^^^^^^^^^
**3Di Toolbox 2.5.2**

- Compatibility with schema 216


**3Di Models & Simulations v3.4.5**

- If your organisation has a large number of models or (finished) simulations, you will notice major performance improvements when loading the list of results available for download, or when loading the overview of running simulations. Both now load instantaneously, while this previously took seconds to minutes for some organisations. This improvement also prevents API requests to be throttled (#408)

- Compatibility with schema 216 (#451).


**3Di Schematisation Editor v1.4**

*Cross sections*

- Tabular cross-sections can now be edited in a table instead of in a text field. This applies to cross-section shapes Tabulated Rectangle, Tabulated Trapezium, and YZ (#90)

- The 3Di Schematisation Editor now fully supports cross-section shapes "YZ" and "Inverted egg" (#89, #91)

- The 'cross-section' stylings for Culvert, Cross-section location, Orifice, Pipe, and Weir have been re-implemented. Some bugs were fixed and support for recently introduced cross-section shapes was added. The stylings are now based on custom expressions, that can also be used for other purposes in any QGIS expression (#96)


*1D2D exchange*

- Add processing algorithm 'Generate exchange lines' (#93, #131)


*Database schema*

- Compatibility with schema 216 (#451).


*Bugfixes*

- Setting the reference level cross-section locations on newly digitized channel to 0 is now committed as 0 instead of NULL (#129)

- Clicking on layer Potential breach in QGIS 3.28 no longer gives an error (#126)

- Adding a cross-section location to a Channel between two cross-section locations with bank_level NULL no longer gives an error (#102)

- Allow negative values for bank level and reference level in Cross section locations tab of Channel layer (#95)

- Multipolygons in a *v2_surface* or *v2_impervious_surface* layers no longer raise a KeyError when loading from spatialite. If possible, they will be converted to Polygons (singlepart) (#134)

April 11th 2023
^^^^^^^^^^^^^^^

**3Di Models & Simulations v3.4.4**

- Bugfix: after installing the 3Di Modeller Interface with installer version 3.28.5-1-3 or higher, installing the 3Di Models & Simulations plugin in a new user profile would fail. This was fixed (#454)

- Bugfix: Simulation template is now created if this option is checked in the simulation wizard; this was broken since version 3.4 (#447)

**3Di Modeller Interface installer 3.28.4-2-1**

- Add option to install for all users. Especially useful for system administrators.

- New user profiles use the 3Di default settings.

March 10th 2023
^^^^^^^^^^^^^^^

**3Di Models & Simulations v3.4.3**

- Bugfix: dialog "Remove excess 3Di models" sometimes did not pop up, even though the maximum model count for the given schematisation and/or organisation had been reached. This has been fixed now.

**3Di Modeller Interface installer 3.28.4-2-1**

- The 3Di Modeller Interface is now based on QGIS 3.28, which became the Long-Term Release (LTR) in March 2023

- Installing a 3Di User Profile is now optional; if a user profile called 'default' already exists, installing a new one (overwriting it) is opt-in.

- Installing the 3Di Modeller Interface is now optional (i.e. you can also use the installer to install a user profile only)

- The name of the app is now "3Di Modeller Interface 3.28" instead of "3DiModellerInterface3.28"


February 6th 2023
^^^^^^^^^^^^^^^^^^

**3Di Toolbox v2.5.0**

A new processing tool is introduced:

- Import GWSW HydX files to a 3Di Spatialite, including the possibility to download it directly from the server

The 'Commands' toolbox has been removed, and tools that are still relevant have been deleted or moved to the QGIS native Processing Toolbox (#715):

- 'Raster checker' has been removed, as it has been integrated into Schematisation Checker (#710). Most checks in the raster checker are no longer relevant, because 3Di can now handle most of these cases.
- 'Schematisation checker' is available from the Processing Toolbox > 3Di > Schematisation
- 'Create breach locations', 'Add connected points' and 'Predict calc points' have been removed. These are no longer compatible with the latest sqlite schema version (214), where v2_connected_pnt, v2_calculation_point and v2_levee where replaced by v2_exchange_line and v2_potential_breach. Please use the 3Di Schematisation Editor for schematising breaches and/or setting the 2D cell with which 'connected' channels connect.
- 'Import SufHyd' is available from the Processing Toolbox > 3Di > Schematisation
- 'Guess indicators' is available from the Processing Toolbox > 3Di > Schematisation
- 'Control structures' has been removed. Please fill the spatialite tables directly or upload a JSON file through the Simulation Wizard to use structure control.

Other improvements:

- Processing algorithm 'Computational grid from schematisation' no longer remembers the input parameters from previous uses, because this was confusing (#723)

**3Di Schematisation Editor v1.3**

- You can now add 'Exchange lines' to your schematisation to set the 2D cells with which a Channel should make 1D2D connections (#92)
- You can now add 'Potential breaches' to your schematisation by drawing a line starting from a connected channel (#92)
- Bugfix: editing attributes of referenced, not yet committed features (e.g. the connection node of a new manhole) now works without issues. #107

**3Di Models & Simulations v3.4**

The simulation wizard has been improved and some important additions have been made:

- Boundary conditions timeseries can be uploaded as CSV files, so it is no longer needed to make a new revision when you want to use different boundary conditions. (#134)
- Structure control can be set by uploading a JSON file (#313)
- Upon completion of the simulation wizard, all data for the starting the simulation is sent to the 3Di API. This upload now happens in the background, so that you can continue working while the simulation is starting. (#389)
- Because of this, the upload timeout can be set to a much higher value; please change this yourself if you after upgrading to the new version. The default upload timeout has been set to 15 minutes (#216). This is relevant when your simulation includes large files, such as laterals, dry weather flow, or 2D initial conditions.
- Progress through the steps of the simulation wizard has been improved to only include the steps that you included in the 'options' screen before starting the simulation wizard. (#262)
- The "Options" dialog that is shown before starting the simulation wizard has been reordered and clearly shows which options are available to the 3Di model you have chosen. (#261)
- "Post-processing in Lizard" now has its own page in the simulation wizard. #432
- Invalid parameter values for damage estimations (repair times of 0 hours) can no longer be chosen. #104
- Forcings and events that cannot (yet) be added to a simulation through the simulation wizard, will now be preserved if they are part of the simulation template (#316). This applies to the following forcings and events:

  - Raster edits 
  - Obstacle edits
  - Local or Lizard time series rain
- When selecting a breach, the breach's code and display name are shown on the map along with the id. 


The schematisation checker in the "Upload new revision" wizard has been improved in the following ways:

- The raster checker has been integrated in the schematisation checker (#412). Most checks in the raster checker are no longer relevant, because 3Di can now handle most of these cases.
- You can now export schematisation checker results to a CSV file (#230)

Other changes and bugfixes:

- The minimum friction velocity in new schematisations now defaults to 0.005 instead of 0.05 (#411)
- A newer version (4.1.1) of the python package threedi-api-client is now used (#417)
- If the maximum number of 3Di models for your organisation has been reached, a popup will allow you to delete one or more of them before uploading a new revision (#367)
- Bugfix: in some cases, schematisation revisions could not be downloaded if "Generate 3Di model" had failed for that revision (#428)
- Bugfix: prevent python error when attempting to start the simulation wizard with a template that has NULL as maximum_time_step value #418


December 8th 2022
^^^^^^^^^^^^^^^^^^

**3Di Toolbox v2.4.1**

Due to changes introduced in v2.4, threedi-modelchecker would re-install on every startup. This has been fixed now. (#729)
Fixed 'Import sufhyd': this routine expected the table v2_pipe to have a column 'pipe_quality', which was removed recently (#728)
A schema version check was added to 'Import sufhyd'. If the target spatialite has a too low schema version, you will be instructed to migrate it and try again (#726)


November 21th 2022
^^^^^^^^^^^^^^^^^^

**3Di Toolbox v2.4**

- Bugfix: "predict calc points" tool no longer fails with "TypeError: not all arguments converted during string formatting" #699

- Spatialite schema version compatibility upgraded from schema version 207 to 209 (#693, #648)

**3Di Schematisation Editor v1.2**

- Editing channel start- or end vertices now disconnects channel from connection node, consistent with behaviour for other line features (#66)

- Unused field "max_capacity" has been removed from Orifice layer (#73)

- Spatialite database schema version is now saved to Geopackage during conversion (#72)

- "Load from Spatialite" no longer fails when the spatialite contains a v2_surface_map or v2_impervious_surface_map with a connection_node_id that does not exist (#75)

- In all attribute forms, units are added to fields for which this is relevant (#8)

- Explainer text has been added to cross section 'table' input boxes in the attribute forms (#64)

- Mistakes in cross_section_table inputs are fixed if possible, and mistakes that cannot be fixed are identified and reported to the user before "Save to Spatialite" starts. are checked GPKG to Spatialite (#70)

- Remove unnecessary popup "Save edits to Manhole?" in specific cases (#80)

- Spatialite schema version compatibility upgraded from schema version 207 to 209 (#71, #83)

- Add cross section shape 0: "Closed rectangle" (#79)

- Enable/disable the width, height and table widgets based on cross section shape (#78)

**3Di Models & Simulations v3.3**

- 2D grid (geojson file) is no longer downloaded after choosing model for new simulation. Instead, please use the processing algorithms in Processing > Toolbox > 3Di > Computational Grid (#325)

- New project > New simulation no longer fails (#400)

- Fix issues with Models & Simulations Panel when other dock widget on the right are also opened. The status bar at the bottom no longer disappears when opening the Models & Simulations Panel. (#153)

- New schematisation: spatialite is migrated to most recent version (#359)

- New schematisation becomes the active schematisation after "New schematisation from existing spatialite" (#385)

- Add option to upload new initial water level rasters in the Simulation wizard (#280)

- In the dropdown for selecting an initial water level raster in the Simulation Wizard, show name of the source file instead of "initial_waterlevels.msgpack" (#179)

- In the simulation wizard, you can now set the discharge coefficients and max breach depth in the breach tab (#187)

- Spatialite schema version compatibility upgraded from schema version 207 to 209 (#398, #406)

- When downloading simulation results, the gridadmin.h5 file is now (also) downloaded to {3Di working directory}\{schematisation}\{revision n}\grid (#403)

- When downloading a revision, the gridadmin.h5 is also downloaded if available (#402)

*Checker*

- Warning for double cumulative cumulative discharges in the aggregation NetCDF - https://app.zenhub.com/workspaces/team-3di-5ef60eff1973dd0024268b90/issues/nens/threedi-api/1766 ?

- Check on flooding threshold is now more strict

*Postprocessing Lizard*

- Added the possibility to use the projects in Lizard directly. Give your simulation as a tag: ‘project:number’ and the number will be added in lizard to the project.

*Reminder*

- The server known as inpy is no more. If you started using 3Di this year you can ignore this message. For the other users: the 3Di models cannot run anymore on 3Di Live. But the schematisations are all available. The be able to run the 3Di model again, simply look for your schematisation on management.3di.live and press ‘generate model’.

- If you’re not sure whether your model is generated using inpy, go to management.3di.live search for your model. If there is no details page available (link is greyed out) then the model is generated via inpy.


August 2022
^^^^^^^^^^^^

**3Di Toolbox v2.3**


- Visualise any computational grid (gridadmin.h5 file), using the new Processing Algorithm "Computational grid from gridadmin.h5". This works for gridadmin.h5 files that were generated on the server as well as those generated locally.
- Generate the computational grid for your schematisation in the 3Di Modeller Interface. The routine that is used on the server to generate the computational grid, has now also been made available locally, so that you can continuously check how your schematisation is translated to a computational grid. Use the new Processing Algorithm "Computational grid from schematisation".
- Bugfix: pumped volume for pumps without end note is now also included in the water balance
- Bugfix: total balance in water balance tool now also works in QGIS 3.22
- Bugfix: water balance tool now handles aggregation netcdf's that have different timesteps for different variables
- Bugfix: side view tool now handles models that contain cross section locations that refer to non-existent cross section definitions
- Bugfix: statistics tool gave IndexError for some datasets
- Bugfix: processing algorithm for water depth/level: batch functionality has been repaired



July 2022
^^^^^^^^^^^^

*3Di Models & Simulations v3.2*

- Logging in with your username and password is no longer needed. Instead, you can now set a Personal API Key in the plugin settings. The Personal API Key will be stored (encrypted) in the QGIS Password Manager. (#382, #372, #366)
- Migrating spatialites to the newest schema version now follows the same logic in all plugins: if a migration is required, a popup message will ask you if you want this. If you click Yes, migration will be performed immediately. (#377)
- Some users experienced SSL Errors, caused by expired SSL certificates that are not properly removed by Windows. A popup message with specific instructions on how to fix this issue now appears when the error occurs. (#379)
- When creating a new schematisation based on an existing spatialite, all rasters will be copied into the new schematisation. In the previous version, only the rasters referenced from the global settings were copied. (#375)

June 2022
^^^^^^^^^^^^

*3Di Toolbox v2.2*

- Introducing the Watershed Tool! Analyse upstream and downstream areas of any location in your model area, based on a network analysis of your simulation results (#641)
- Migrating spatialites to the newest schema version now follows the same logic in all plugins: if a migration is required, a popup message will ask you if you want this. If you click Yes, migration will be performed immediately. (#644)
- Added 3Di logo in the Plugin Manager (#606)
- Installation and update procedure has been improved. Black command prompt windows are no longer shown on startup. (#621, #625)

Documentation on the Watershed Tool can be found `here <https://github.com/nens/threedi-network-analyst#user-manual>`_.


*3Di Schematisation Editor v1.1.1 - EXPERIMENTAL*

- Migrating spatialites to the newest schema version now follows the same logic in all plugins: if a migration is required, a popup message will ask you if you want this. If you click Yes, migration will be performed immediately. (#50)


*3Di Schematisation Editor v1.1 - EXPERIMENTAL*

This is a new plugin that will make editing schematisations much easier than before.

What does this plugin have to offer for modellers?

- Directly edit all layers of your schematisation, using all native QGIS functionality for editing vector features
- Quickly add features to your schematisation with the "magic" editing functionality for 1D layers. For example: existing connection nodes are used when drawing a pipe between them, new connection nodes and manholes are created when a new pipe is digitized, etc.
- Easily move nodes and all connected lines using the smartly pre-configured snapping and topological editing settings
- Easily move the start or end of pipes, channels, culverts, orifices, weirs, pumps, and the connection node id's will be automatically updated for you
- Get a complete overview of your schematisation: all rasters that are part of your schematisation are added to the QGIS project when the schematisation is loaded
- Spot the tiniest local variation in elevation with the hillshade layer is automatically added on top of your DEM
- Visualise the mapping of (impervious) surfaces to connection nodes and change them by updating the geometries
- Easily navigate through your schematisation: layers in the layer panel are neatly grouped together in collapsed groups

Version 1.1 is 'experimental' plugin, because it is not yet fully integrated with the other components of the Modeller Interface. In practice, this mainly means that you will have to convert between the Spatialite and the Schematisation Editor's Geopackage format every time you start or finish editing your schematisation.

New in version 1.1 (for those users who already tried out version 1.0):

- Facilitate adding channels and cross section locations (also fixes the issue that sometimes it was not possible to fill in channel start or end node ids)
- Delete referencing features
- Release through plugins.3di.live as experimental plugin
- Rename to 3Di Schematisation Editor
- Set scale dependent visibility for manholes
- Fix export to spatialite in QGIS 3.22 (was fixed by adding a schema migration in threedi-modelchecker)
- Fix drawing of pipe trajectory over existing manholes
- Consistent handling of geometry edits
- Check write permissions for Geopackage target location
- Support spatialite schema_version 206 + updated the popup message if schema is not up to date
- Remove field cross_section_code
- Remove table cross_section_definition
- Make all id fields autoincrement
- End all editing sessions when user clicks Save to Spatialite
- Rename column calculation_pnt_id of connected_point to calculation_point_id
- Pump capacity should be NULL by default
- Add geopackage database connection to QGIS list
- Refresh map canvas after removing 3Di model
- Correct list of calculation types in culvert attribute form
- Guarantee that layers are added to the correct group
- Add hillshade styled DEM
- Raster styling classes
- Hide 'fid' columns
- More intuitive validation color logic in attribute forms
- Make snapping work properly after saving/loading project
- Fix scale dependent visibility for manholes
- Rename plugin to 3Di Schematisation Editor
- Fix width and diameter labels for tabulated cross sections
- Compatibility with QGIS 3.22 / Spatialite v4.3
- Drop-downs are used in the attribute table for fields with a limited list of valid integer values (e.g. calculation type).

*3Di Toolbox v2.1*

- IMPORTANT: If you update to 3Di Toolbox v2.1, you also _must_ update the 3Di Models & Simulations plugin to version 3.1. Failing to do so may lead to unexpected behaviour of several tools.
- Fix several issues with 3Di Spatialites in QGIS 3.22. Until now, all 3Di Spatialites were built using Spatialite 3, which QGIS 3.22 no longer supports. Migrate Spatialite now tranfers all data to a Spatialite 4.3 file.
- Graph Tool and Water Balance Tool plots now render properly on second screens
- Bugfix for using the SideView tool for open water
- Water Balance Tool in/out labels near the x axis are now located correctly
- Graph Tool and Water Balance Tool plots: time units can be chosen as s / min / hrs.
- SideView Tool and Statistics Tool: Feedback is given to user when manhole surface level is not filled in.

*3Di Models & Simulations v3.1*

- Compatibility with migrating to the new Spatialite v4.3 file
- Support rainfall events from csv with more than 300 steps
- The "New schematisation" wizard now has the option to use an existing spatialite
- You will receive a warning when trying to upload a rainfall CSV with non-equidistant timesteps
- Errors from the 3Di API are reported more clearly
- You can now view all simulation results available for download, even when more than 50 are available



March 2022
^^^^^^^^^^^^

*3Di Models & Simulations v3.0.3*

- Show schematisation checker results in two separate, tidy list widgets: one for spatialite checks, one for raster checks (#229)
- Include 'info' and 'warning' level log messages in schematisation checker output (#286)
- Fix 'Revision is not valid' error when uploading new revision (#334)
- Fix 'Revision does not exist' error when uploading new revision (#344)
- On startup, check if any incompatible version of the python package threedi-api-client version is installed and attempt to upgrade to correct version (#348)
- Allow rain intensities < 1 mm/hr (#180, #347)

*3Di Customisations  v1.2*

-	Remove all user interface customisations, except red menu bar
-	Add "About 3Di modeller interface" dialog

*3Di Toolbox v1.33*

-	Processing tools have been added to check the Spatialite and Rasters. These processing algorithms add the check results as layers to your QGIS project, instead of in a separate shapefile, csv, or text file. You can access them through Processing > Toolbox > 3Di > Schematisation. In the future, these processing algorithms will replace the current checker tools available in the 'Commands' Toolbox.



February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^

We have released threeditoolbox 1.31 and 3Di Models & simulations 3.0.2.
"3Di Models & simulations" is the new name for what was previously called "API client".
Please note: If you continue to use the old route, you still need the previous version of the plugin as well.

We have also released a new version of the Modeller Interface:
Download here the latest version: `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.22.7-1-3-Setup-x86_64.exe>`__



August 2021
^^^^^^^^^^^

We have released a new version of the Modeller Interface with the following:

- Update on the animation toolbar
- Added tooling for dry weather flow calculations
- Water depth maps for multiple timesteps
- Bugfix Sideview Tool

Download here the latest version: `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.7-1-Setup-x86_64.exe>`__


*Important note for QGIS Users*

Please note that installing QGIS has been undergoing some changes, at the moment the OSGeo4W Network Installer is the recommended way to install QGIS. See https://www.qgis.org/en/site/forusers/download.html for more information. This change does not apply for users that use the Modeller Interface installer.


*Animation Toolbar update*

The styling of all animation layers has been improved. The value categories are no longer fixed but based on the value distribution in the entire simulation. In the 2D domain, the animation toolbar now visualizes cells instead of nodes. Furthermore, the option 'relative to timestep 0' was introduced. This allows you to switch between e.g. absolute water levels and water level relative to the start of your simulation.

Below are examples of a dike breach. Animation 1 is showing relative change in water level and discharge. The plot is done for every calculation cell and flow line. Animation 2 is the same situation as an absolute plot showing the water level per calculation cell and the discharge over the flow lines.
Some other improvements to the toolbar include:

-	More user feedback.
-	The animation layers are removed when the Animation Toolbar is deactivated.
-	The groundwater layers are only displayed when the simulation includes groundwater.

*Dry weather flow calculator*

In some cases it is required to add dry weather flow to a simulation. To enable this a processing tool has been added to convert dry weather flow as defined in the model spatialite (dry weather flow attribute of the impervious surface layer) to lateral discharge timeseries that can be used as in your simulations.
In our earlier API (v1), dry weather flow was read automatically from the spatialite and calculated according a standard distribution.
In the current API (v3), dry weather flow is added as lateral discharges to allow for more flexibility. E.g. in the distribution of dry weather flow over the day.

*Water depth maps for multiple timestep*

We have added the option to generate water depth/level maps for a range of timesteps. The output is a multiband geotiff, where each band contains the water depth map of one timestep.

The water depth processing algorithm also has various minor bugfixes and improvements:

-	Selecting DEM layer from project no longer gives an error.
-	Generating outputs for timestep 0 without moving the timestep slider no longer gives an error.
-	Improved readability of LCD display by adding days to the display.
-	Set LCD value to 00:00 when file is loaded.
-	More accurate description of what the tool does.


*Bugfix SideView tool*

The SideView tool no longer worked since QGIS 3.16.6. This has now been fixed


May 21st 2021 - 3Di API QGIS Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.7-1-Setup-x86_64.exe>`__ and an update of our 3Di API QGIS Client to version 2.4.1. The following has been fixed:

- Users no longer get a throttling warning when trying to start a simulation.
- Results download only shows results for the model that is selected in the panel.

The location of plugins has changed from https://plugins.lizard.net/plugins.xml to https://plugins.3di.live/plugins.xml

April 22nd 2021 - 3Di Toolbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`__ and the `ThreediToolbox 1.18 <https://plugins.lizard.net/ThreeDiToolbox.1.18.zip>`_ .
This is a fix for the error *"Couldn't load plugin 'ThreeDiToolbox' due to an error when calling its classFactory() method
ModuleNotFoundError: No module named 'alembic' "*

April 1st 2021 - 3Di Toolbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Due to some changes under the hood in QGIS 3.16 we have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`_ and the `ThreediToolbox 1.17 <https://plugins.lizard.net/ThreeDiToolbox.1.17.zip>`_

March 8th 2021
^^^^^^^^^^^^^^^^

Download the latest version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`_ , which at the time of writing uses QGIS 3.16.4.
For QGIS users: upgrade the plugin using the plugin panel. In case this doesn't work, it is possible to install the plugins as zip file. The latest versions are `ThreediToolbox 1.16 <https://plugins.lizard.net/ThreeDiToolbox.1.16.1.zip>`_  and Threedi-API-QGIS client is 2.4.0.


*Local calculation of water depth & water level maps*

It is possible to generate water depth maps for every time step with the newest version of the Modeller Interface. To generate these water depth maps, 3Di applies a special algorithm that combines the water level results with the information of the DEM. This algorithm creates visually appealing maps. The maps show the water level and water depth results on high resolution, these can be based on the interpolated and on the non-interpolated water level results.

A quick guide to generate water depth maps:

Processing ^^> Toolbox ^^> 3Di ^^> post-processed results ^^> water depth

Or check out our documentation: :ref:`3di_processing_toolbox`


*Extended support for starting simulations using the Modeller Interface*

We have added the following support for starting simulations from the Modeller Interface:

- added support for wind. See our user manual: :ref:`simulate_api_qgis` or our technical documentation : :ref:`wind_effects`  for more information.
- added option of tags. This can be used to tag a simulation with a project related tag. This way it is easier to organise simulations.
- added time-interpolation options for laterals
- added the option for Netcdf upload for rain
- option to set base URL for the API (for use of 3Di in other countries)

The following bugs have been fixed:

- start time is now correctly used
- search window for models is now case insensitive
- bug fix lateral file upload

*Bugfix in the ThreeDiToolbox*

- Fix import sufhyd coordinates swapped on newer gdal versions.


February 22nd 2021
^^^^^^^^^^^^^^^^^^

- We now support QGIS 3.16 for our toolbox.

Please not that the Modeller Interface is not yet upgraded to QGIS 3.16, we will do so when the QGIS repo's are updated.

For QGIS users: upgrade the plugin using the plugin panel.


*3Di Modeller Interface styling improvements*

Based on your feedback we have improved the styling of the schematizations in the Modeller Interface. Not only that, we now have support for multiple stylings! Check out the video to see how it works.

The improvements are:

- For weirs, orifices and culverts, the styling now indicates when flow in one or both directions is impossible (discharge coefficient - 0)
- Grid refinement styling now indicates the refinement level
- Multiple stylings are added next to the default. Switching to these stylings allows you to visualize flow direction, code, id, storage area, bank level, reference level, invert level, crest level, diameters and dimensions, min/max of timeseries, and pump capacity. How it works is explained in the docs: :ref:`multiplestyles`

*Schematization checker improvements*

We are constantly working on improving the 3Di experience. Based on user experience analysis we have added the following checks to the schematization checker:

- Add check ConnectionNodesDistance which ensure all connection_nodes have a minimum distance between each other.
- Set the geometry of the following tables as required: impervious_surface, obstacle, cross_section_location, connection_nodes, grid_refinement, surface, 2d_boundary_conditions and 2d_lateral.
- Add check for open cross-section when NumericalSettings. use_of_nested_newton is turned off.
- Add checks to ensure some of the fields in numerical settings are larger than 0.
- Add check to ensure an isolated pipe always has a storage area.
- Add check to see if a connection_node is connected to an artifact (pipe/channel/culvert/weir/pumpstation/orifice).

*Bugfixes in 3Di Modeller Interface*

- Fixed h5py error, it is now possible to use the 3Di toolbox on QGIS 3.10.12
- Fixed x-axis bug in the water balance tool


.. _release_notes_api:

3Di API
-------

September 21, 2023
^^^^^^^^^^^^^^^^^^

- Added *archived* field to Schematisation, allowing it to be soft-deleted. A delete request archives the schematisation. A superuser can (hard) delete it afterwards by performing a second delete request.
- Archiving a Schematisation also archives related Revision and ThreediModel resources.
- Extend FrictionType enum with Chézy friction with conveyance and Manning friction with conveyance.

.. _3di_api_release_20231807:

June 18th 2023
^^^^^^^^^^^^^^

- Invite email for organisation for users now shows which organisation they are invited to
- An e-mail is sent when your simulation has crashed
- Allow Lizard postprocessing after simulation has finished. (when not already requested)
- Simulation templates persist when regenerating 3Di Model
- Simulation templates are inherited from 3Di Model of the previous revision
- If simulation results become > 10 GB, simulation crashes with clear error message, instead of taking down the calculation node (and any other simulations that depend on that node)
- Added dequeue action putting a queued` simulation back in created state.
- Bugfix: Set max timestep to default timestep when max timestep is undefined
- Improved speed of /simulations/ endpoint by introducing is_template field.


June 14th 2023
^^^^^^^^^^^^^^

- Added *first_name* and *last_name* to SimulationStatus API listing resources.

- Added support for setting a *start_date* on a contract. If set, the contract *hours_used* are calculated either based
  on a period of 1 year before or after the *start_date* based if the current date (month & day) are before or after start_date (month & day).

April 25th 2023
^^^^^^^^^^^^^^^

- Added support for uploading additional initial water levels to an existing 3Di models. Both 1D and 2D are supported.

- Added support for uploading and downloading computational grid Geopackage files for 3Di models.

- Bugfix: We have made the use of Lizard raster rain in a simulation more robust by using longer retries getting data from Lizard.

- The duration of a constant wind event can now be patched while the simulation is paused.

- In the near future an extra log file (scheduler.log) will be added to log files in the downloadable ZIP file. The scheduler log file is intended for 3Di developers to identify problems when simulations have crashed.

February 6th 2023
^^^^^^^^^^^^^^^^^^

- Added support for uploading and downloading (exported gridadmin.h5) Geopackage files on threedimodels.
- Added copy-to-threedimodel endpoint.
- Added exchange_lines and potential_breaches in the schematization input (sqlite). The calculation_point / connected_pnt are migrated to potential breaches. The levees are migrated to obstacles. Corresponding version updates: sqlite schema version 214, threedi-modelchecker 0.35, threedigrid-builder 1.7, threedigrid 2.0.
- The threedimodels/<id>/potentialbreaches endpoint is only filled with breaches having a content_pk, levee material and maximum breach depth (in gridadmin).
- Removed the (admin-only) threedimodels/<id>/bulk_potentialbreaches endpoint.
- Allow creation of Breach events by line_id. In that case, levee_material and maximum_breach_depth are required. Note that the old creation method will be deprecated (along with the threedimodels/<id>/potentialbreaches resource).
- Removed the "potential_breach" field on the breach event.
- Fixed model checker (v0.33), included raster checks via rasterio.
- Invalidate boundary files without any boundaries.
- Upgrade threedi-tables to 3.0, raster reading is now done through a VRT, so that any projection / sampling is allowed.
- Upgraded threedi-modelchecker to 0.34 and threedigrid-builder to 1.6, allowing TABULATED_YZ profiles, and adding rudimentary support for exchange lines and new potential breach input.
- Disable inpy model mounts


November 21th 2022
^^^^^^^^^^^^^^^^^^

When using an .env file you need to change the content of this file to:

THREEDI_API_HOST=https://api.3di.live
THREEDI_API_PERSONAL_API_TOKEN= supersecret API key

   - Instead of username / password. It is more secure and for new users the username/password combination will not work anymore. Note: Try to avoid committing passwords and API keys to public github repositories.

- Added variable increment table step sizes.

- Block obstacle/raster edits for models generated before 3.0.0 release.

- Obstacle edits support.

- Duration on structure-controls has become mandatory.

Note: this is not backwards compatible, but without duration it does not work...

- Increased total timeout for trying Lizard rain requests for one timestep to 30 minutes.

- Gridadmin.h5 `epsg_code` is only an attribute on root level.

- Threedimodel 1d/2d/0d extent's can now be zero size (singular point).

- Allow patching `duration` on Lizard raster rain and sources & sinks Lizard raster resources.

- Set `simulation.threedicore_version` on simulation start.

- Added rain (node) graph websocket to results-api and registration endpoint.

- Added rain graph endpoint in API v3

- Add endpoint for uploading and downloading 'flowlines' geojson file on threedimodel.

- Added `has_threedimodel` field to schematisation revisions and querystring filter option.

- Stopped Inpy-generated models support.

- Fixed a bug in the LizardRasterSourcesSinks serialization.

- Fixed a bug in api/v3/auth/users (non-superusers).

- Changed link in email sent when queued simulation is started. #1657

- Bugfix: get correct list of related rasters for DEM raster edits. #1711

- Bugfix: Aggregation of uploaded initial waterlevel rasters on threedimodels was not triggered.

- Allow a user to create multiple initial waterlevel rasters on a threedimodel.

- Support bigger geotiffs by enabling temporary compression for Cloud Optimize Geotiff creation.

Hotfixes that were already set in production

- Stop initializing boundaries with 0 values at t0 by default.

- Improve waterdepth interpolation by using `vol/vol1` to prune Delaunay triangles that have volume < 0.001 voor all 3 nodes.

**Fixed**

- Threedicore version is now correctly written to the simulation details


July 2022
^^^^^^^^^^

(2022-07-20)

- Bumped pyjwt in scheduler and fixed decoding issues.
- Restore simulation labels for Marathon (Mesos).
- Increased total Lizard radar rain (multiple requests) timeout to 5 minutes.
- Upgraded pypi packages in services.
- Api-workers: Added Celery readiness/liveness file probes.
- Changed order in ThreediModelTask so Simulation Template worker is started after aggregations are done.
- Fixed bug in simulation template processing.
- Fix bug where threedimodel resources were not incorporated in simulation copy using the from-template endpoint.
- Allow to dynamically enable/disable tasks in api-worker.
- Prevent simulation deletion which is simulation-template
- Frontends have moved to ghcr.io.
- Bumped threedicore to 2.2.12

June 2022
^^^^^^^^^^

(2022-06-12)

- Threedi-modelchecker now support spatialite 4
- Bugfix for file boundary conditions expiry date in simulation templates.
- Bugfix for sending e-mails for simulations picked up from the queue
- Bugfix for async (file) event validation.


May 2022
^^^^^^^^^^

- Added personal api keys (beta).
- Copy simulation template between threedimodels.
- Added user management screens
- Added users sub-endpoint to organisations to be able to patch roles.
- Enforce maximum amount of active ThreediModels per organisation and schematisation.

Moreover:

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



February 2022
^^^^^^^^^^^^^^^^

2.17.4 (2022-02-23)
- Bugfix in embedded (connection) node in lateral files processing

2.17.3 (2022-02-22)
- Make sure threedimodel workers receive tasks only once.
- Include threedimodels which are being validated in max amount of threedimodels check for schematisation.
- Support embedded (connection) nodes in laterals files and other API resources.

2.17.2 (2022-02-16)
- Bumped threedi-tables to 1.2.6
- Bumped threedigrid to 1.1.14, geometry filtering bugfix.
- All boundaries conditions in a file need to have the same timesteps.
- Bugfix: simulations need either duration or end_datetime
- Fixed uploading revision rasters with md5sum (deduplication) in case the other raster has a different type.
- Improve speed of user_organisation_roles queries.
- Allow threedimodel filtering on revision__schematisation__id.
- Maximum number active model check no longer takes non valid models into account.


February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^

**General**

- Reordering of nodes and lines: the order and ids of the calculation nodes and flowlines will be different.

- Reprojection of 1D objects: the EPSG database that is used when reprojecting spatialite geometries to the model projection was upgraded from version 7.9 to 10.041. Due to improvements in the projection definitions, this may result in effects due to geometries that are displaced relative to the DEM (and correspondingly the 2D grid), for example 1D-2D lines or grid refinements. Note that in all cases no correction grids (e.g. RDNAPTRANS) or date-dependent datum shifts (e.g. ETRS89 to WGS84) are applied. Versions corresponding to EPSG database 7.9: PROJ4 4.8.0, August 2011 Versions corresponding to EPSG database 10.041: PROJ4 8.2.1, Dec 2021


**Channels, pipes and culverts**

- 1D initial waterlevels on channels/pipes/culvert nodes are now (linearly) interpolated between connection nodes.

- The volume of an embedded channel/pipe/culvert (that is added to the 2D nodes in which they are embedded) now stems precisely from the part of the channel/pipe/culvert that is inside the 2D cell. Previously, this was not the case.

- If the direction of a channel/pipe/culvert geometry is reversed compared to the “connection_node_start” and “connection_node_end”, then this is now fixed automatically.

- The calculation type of culverts is not ignored anymore.

- For calculation nodes on channels with connected calculation type, the cross section will be used until the surface level of the DEM. This will give differences for channels with connected calculation type in case the cross section is below the surface level.


**Cross section definitions**

- A new “closed rectangle” (type 0) cross section definition is available. This definition requires both width and height.

- For tabulated cross section definitions, the input is validated more strictly. Previously, a wrong input (e.g. using a comma as separator between numbers) resulted in the table only receiving one value.


**2D initial waterlevels**

- The no data value in 2D initial waterlevels is now excluded while taking the min, max, or mean. This means that cells with partial data now receive a water level whereas in the old route they did not.


**Obstacles / Levees**

- The algorithm with which 2D flowlines are assigned to obstacles/levees is changed. Now, every flowline that intersects the obstacle/levee is assigned to it.

- Also levee/obstacle geometries can be drawn outside the DEM area, which was previously not possible.


**2D boundary conditions**

- The constraints on 2D boundary conditions have become less strict. Every border cell can now get a boundary condition. It is required however that the border cells of a single boundary condition form one horizontal or vertical edge. The boundary condition does not need to be precisely at the cell edge anymore. Also it is not required anymore to adjust the DEM to precisely align to the border cells; if there is no DEM data at the outer cell edge, the DEM data will be extrapolated.


**Gridadmin / Results NetCDF**

- The gridadmin.h5 and results_3di.nc file now uses NaN (not-a-number) instead of -9999 for missing values in float columns. Integer type columns still have –9999 to denote “missing”.


January 31st 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following endpoints have been added to the API:

- Upload Schematisations
- Download Schematisations
- Create 3Di Models from a Schematisation
- Create Simulation Templates

Technical details:

**Filters:**

- Added threedimodel__revision__id filter on simulations.
- Added threedimodel__id filter to simulations endpoint.
- Renamed revision_id filter on threedimodels endpoint to revision__id.
- Added filter on /threedimodels/ for organisation unique_id.
- Tags in filter now support icontains lookups.

**Ordering:**

- Added simulation name, simulation type, threedimodel name, schematisation name, started, total_time, and simulation username ordering options to Usage.
- Added simulation name, simulation status, threedimodel id, threedimodel name, simulation username, simulation active_status filter options to Usage.

**OpenAPI changes:**

- Changed swagger definition for LineString to array containing 2 arrays of 2 numbers.
- Added min_started and max_started to Usage serializer.
- Changed openapi tags field definition to become equivalent of Python List[str].
- Added mandatory longitude, latitude order for coordinates at all relevant places in openapi/swagger docs.

**Threedicore:**

- Updated to 2.2.3.

**Boundary conditions:**

- Boundary conditions: new format validation and docs.
- Sort new-style boundary condition files by type and id.

**DWF:**

- Periodic ("daily" only for now) file lateral support. Intended for dry weather flow.

**Results files:**

- Keep simulation log files (disable automatic cleanup)

**Debugging:**

- Enable simulation DEBUG level logging by either providing automatic-test or debugmode as tag.

**Lizard raster rain:**

- Adjust timeout of Lizard raster rain requests to 120 sec.
- Bugfix: Lizard raster rain with interval >= 1 day(s) where not processed correctly.

**Bugfixes:**

- Bugfix: added missing permissions for local rain endpoints and deleting physical/timestep/numerical settings.
- Fixed bug in threedimodels levees geojson download.
- Fixed websocket issue for raster-edit update and delete events

**1D initial waterlevels:**

- Enabled management of initial_waterlevel and initial_groundwater_level model rasters for default users.
-  Added 'dimension' field (default: 'two_d', optional new value: 'one_d') to threedimodels/{pk}/initial_waterlevels.
- Added simulations/{simulation_pk}/initial/1d_water_level/file resource to refer to initial_waterlevels with dimension = 'one_d'.
- A POST on simulations/{simulation_pk}/initial/1d_water_level/predefined now also creates a simulations/{simulation_pk}/initial/file resource. The scheduler ignores the /predefined one if the /file resource exists.


December 13th 2021  (hotfix)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released the following hotfixes:

1. Fix for cross-sectional area in case of breaches
2. Fix in breach computations in case of time step plus

November 24th 2021 (hotfix)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released the following hotfixes:

1. Writing correct value to Mesh2DFace_zcc variable in the NetCDF
2. Convert infiltration values to m/s for dem_edit input


October 18th 2021
^^^^^^^^^^^^^^^^^

We have released the API V3

After this release, we stop to support API v1. Do you still need access to API v1? Please contact our servicedesk.

*New Features*

- Added structure controls file (bulk) upload.
- Added extra fields, filtering and sorting options on statuses endpoint

*Improvements*

- Decreased SQL query count of files and threedimodels endpoints.
- Simulation can only be created by an organisation with a valid contract.
- API version v3.0 renamed from to v3. Version v3.0 still works for backwards compatibility.

*Bugfixes*

- Removed 5 min timed-out when uploading result files.
- Set simulation state to finished after pause timeout.
- File endpoint max pagination size is now 250, like rest of the API endpoints.
- Boundary conditions interpolation
- Added convergence_eps to Simulation settings
- Properly set file status after upload_processor crash.
- Gracefully handle invalid "spatial_ref" in default NetCDF.
- TMS min/max values where incorrect if the raster contained np.nan values.
- Fix versions in browsable API hyperlinks.
- Fix versions in browsable API hyperlinks.
- Disable throttling on /health/ endpoint.
- Fix authorization for objects that derive their ownership through schematisation objects (threedimodels resource and childs, threedimodel fields, initial_waterlevel field).
- Solve N+1 query issue for threedimodels with schematisation revisions.
- Results.basic field in Lizard postprocessing API is now correct.
- Levees geojson generation problem fixed due to incorrect dtype
- Simulation filtering on status endpoint is no longer possible
- Ordering of Lizard postprocessing statuses

June 25th 2021 Hotfix
^^^^^^^^^^^^^^^^^^^^^

We have released the following hotfixes:

1. fix for errors with initial waterlevels (2D only model / Embedded problems)
2. fix for edge cases regenradar concerning the 2D extent and the 0D extent

June 14th 2021
^^^^^^^^^^^^^^

We have released the following:

- Simulation settings endpoint

This settings endpoint contains 4 different type of settings:

- numerical
- physical
- timestep
- aggregation

Using this settings endpoint overrules the settings that are uploaded with the spatialite. Currently this option is only available via our API. For more information on usage please check the `swagger pages <https://api.staging.3di.live/v3/swagger>`_

For users using dry weather flow in urban sewerage systems please note that there is a difference between API v1 and v3 how inflow from dry weather flow is being handled. Please check our :ref:`simulate_api_qgis` section for more information.

April 11th 2021
^^^^^^^^^^^^^^^^

We have the following release announcements:
- API v3 now has support for leakage

March 8th 2021
^^^^^^^^^^^^^^^^

Extended API v3 with boundary conditions & bug fixing

*General*

- Remove folders in the logging zip-file
- Changed precision of float to 6 decimals for initial water levels in 1D model domain
- Now support for boundary conditions in the API
- Enabled time-interpolation for all events (forcings) in the API

*More technical details*

- Upgraded threedicore to 2.0.16
- Added additional threedimodel file validation. That is, if the threedimodel files are missing or the table_admin_file size exceeds the SIMULATION_DOCKER_MEMORY setting, a validation error will be raised and the resource will be set to disabled.
- Add details for the user for why a scheduler event-worker failed.
- Fix for the bug where shutdown_simulation is not awaited when the event-worker has failed. This caused the failed simulation to hang until the Timeouts. WORKERS.value (2 minutes) has passed.
- Various smaller fixes to avoid validating a grid event twice (closes #853).
- The event worker now converts exceptions properly to strings.
- The events.models.Simulation object expects the sim_uid as str not int.
- Added usage statistics endpoint and usage filters (including a simulation type filter ("live"/"api").
- Using django's get_valid_filename() method in combination with Path().name to avoid users posting special characters in file names.



.. _computational_core_3di_releases:

3Di Computational core
----------------------

.. _3di_calccore_release_20231807:

June 18th, 2023
^^^^^^^^^^^^^^^

- Storage in the groundwater domain is more accurate and less cell size dependent because it uses subgrid
- Initialization time (when starting a simulation) for models with many 1D lines has been reduced
- Bugfix: Missing headers in matrix.log
- Bugfix: Embedded wet surface is now calculated *after* merging the volume table.
- Bugfix: Source geometry for raster and obstacle edit would not be set, leading to incorrect assumption of EPSG:4326

June 2023
^^^^^^^^^

- Vegetation drag
- Groundwater 1D2D exchange
- Groundwater 2D boundary conditions
- Added has_vegetation attribute to model meta data
- Bugfix: DEM edit for a model with interflow would set wrong waterlevel.
- Bugfix: 1D boundary nodes are now included in the definition of the 1D extent of the model
- Output NetCDF files now contain the attributes *simulation_id*, *schematisation_id*, *revision_id*, and *model_id*

April 2023
^^^^^^^^^^

- Channels with calculation type *connected* or *double connected* can now be placed outside the DEM, as long as they connect to a location where a 2D cell is present. If a 'potential breach' or 'exchange line' is used to set the location to which the calculation node connects, the location of those features determines whether an error is raised. If a channel with calculation type connected is outside of the DEM, but the closest point on its exchange_line is on the DEM, the computational grid can be built and the 3Di model is valid.

- 1D-2D links that cross an obstacle will take the exchange level from the obstacle


August 2022 (Hotfix)
^^^^^^^^^^^^^^^^^^^^
- Fixed the initialisation of the calculation core.

- Let a simulation crash when a NaN occurs during the calculation.


March 2022
^^^^^^^^^^

**General**

- Reordering of nodes and lines: the order and ids of the calculation nodes and flowlines will be different.

- Reprojection of 1D objects: the EPSG database that is used when reprojecting spatialite geometries to the model projection was upgraded from version 7.9 to 10.041. Due to improvements in the projection definitions, this may result in effects due to geometries that are displaced relative to the DEM (and correspondingly the 2D grid), for example 1D-2D lines or grid refinements. Note that in all cases no correction grids (e.g. RDNAPTRANS) or date-dependent datum shifts (e.g. ETRS89 to WGS84) are applied. Versions corresponding to EPSG database 7.9: PROJ4 4.8.0, August 2011 Versions corresponding to EPSG database 10.041: PROJ4 8.2.1, Dec 2021


**Channels, pipes and culverts**

- 1D initial waterlevels on channels/pipes/culvert nodes are now (linearly) interpolated between connection nodes.

- The volume of an embedded channel/pipe/culvert (that is added to the 2D nodes in which they are embedded) now stems precisely from the part of the channel/pipe/culvert that is inside the 2D cell. Previously, this was not the case.

- If the direction of a channel/pipe/culvert geometry is reversed compared to the “connection_node_start” and “connection_node_end”, then this is now fixed automatically.

- The calculation type of culverts is not ignored anymore.

- For calculation nodes on channels with connected calculation type, the cross section will be used until the surface level of the DEM. This will give differences for channels with connected calculation type in case the cross section is below the surface level.


**Cross section definitions**

- A new “closed rectangle” (type 0) cross section definition is available. This definition requires both width and height.

- For tabulated cross section definitions, the input is validated more strictly. Previously, a wrong input (e.g. using a comma as separator between numbers) resulted in the table only receiving one value.


**2D initial waterlevels**

- The no data value in 2D initial waterlevels is now excluded while taking the min, max, or mean. This means that cells with partial data now receive a water level whereas in the old route they did not.


**Obstacles / Levees**

- The algorithm with which 2D flowlines are assigned to obstacles/levees is changed. Now, every flowline that intersects the obstacle/levee is assigned to it.

- Also levee/obstacle geometries can be drawn outside the DEM area, which was previously not possible. 2D boundary conditions

- The constraints on 2D boundary conditions have become less strict. Every border cell can now get a boundary condition. It is required however that the border cells of a single boundary condition form one horizontal or vertical edge. The boundary condition does not need to be precisely at the cell edge anymore. Also it is not required anymore to adjust the DEM to precisely align to the border cells; if there is no DEM data at the outer cell edge, the DEM data will be extrapolated.


**Gridadmin / Results NetCDF**

- The gridadmin.h5 and results_3di.nc file now uses NaN (not-a-number) instead of -9999 for missing values in float columns. Integer type columns still have –9999 to denote “missing”.

February 2022
^^^^^^^^^^^^^^^^

2.17.4 (2022-02-23)
- Bugfix in embedded (connection) node in lateral files processing

2.17.3 (2022-02-22)
- Make sure threedimodel workers receive tasks only once.
- Include threedimodels which are being validated in max amount of threedimodels check for schematisation.
- Support embedded (connection) nodes in laterals files and other API resources.

2.17.2 (2022-02-16)
- Bumped threedi-tables to 1.2.6
- Bumped threedigrid to 1.1.14, geometry filtering bugfix.
- All boundaries conditions in a file need to have the same timesteps.
- Bugfix: simulations need either duration or end_datetime
- Fixed uploading revision rasters with md5sum (deduplication) in case the other raster has a different type.
- Improve speed of user_organisation_roles queries.
- Allow threedimodel filtering on revision__schematisation__id.
- Maximum number active model check no longer takes non valid models into account.



January 31st 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This release contains a big change in 3Di model creation. The Grid and Table builder have been rewritten from the ground up.

**Breaking changes**

- Previously, 3Di models were created from repositories in models.lizard.net, by inpy. The new 3Di models are created from schematisations in the 3Di API, by POSTing to the "create_threedimodel" API endpoint. Because of a new Grid generation. Node ids can differ from old versions of a threedimodel.

**General**

- CRS transformation (reprojection): transformations from the native spatialite projection (WGS84) to the model projection is now done using the PROJ4 library version 8.2.0 instead of version 4.8. Expect slight changes in coordinates if you use CRS definitions that received updates in the past years (Dutch “rijksdriehoek”, British national grid).
- Quadtree creation (2D Cells)
- The behavior around refinements is altered slightly. Grid cell sizes at edges can differ slightly.

**Channels, pipes and culverts**

- The order of the coordinates in a channel or culvert linestring does not matter anymore. Previously, in case that the geometry was reversed (the first coordinate in the linestring coincides with the “connection_node_end” and vice versa), makegrid connected the “connection_node_end” to the wrong side of the channel.
- 1D initial waterlevels on channels/pipes/culvert nodes are now (linearly) interpolated between connection nodes.
- The volume of an embedded channel/pipe/culvert (that is added to the 2D nodes in which they are embedded) now stems precisely from the part of the channel/pipe/culvert that is inside the 2D cell. Previously, this was not the case.

**Cross section definitions**

- A new “closed rectangle” (type 0) cross section definition is available. This definition requires both width and height.
- For tabulated cross section definitions, the input is validated more strictly. Previously, a wrong input (e.g. using a comma as separator between numbers) resulted in the table only receiving one value.

**Obstacles / Levees**

- The algorithm with which 2D flowlines are assigned to obstacles/levees is changed. Now, every flowline that intersects the obstacle/levee is assigned to it.
- Also levee/obstacle geometries can be drawn outside the DEM area, which was previously not possible.

**2D boundary conditions**

- The constraints on 2D boundary conditions have become less strict. It is required that the 2D boundary condition intersects a horizontal or vertical string of cells. If there is no DEM data at the outer cell edge, the DEM data will be extrapolated to compute the cross sectional area of the boundary flow line.

**Gridadmin**

- The gridadmin file now uses NaN (not-a-number) instead of -9999 for missing values in float columns. Integer type columns still have –9999 to denote “missing”.
- The following datasets were added for nodes: code, dmax, s1d, embedded_in, boundary_type, has_dem_averaged
- A group "nodes_embedded” was added.
- The following datasets were added for lines: s1d, ds1d, dpumax, flod, flou, cross1, cross2, cross_weight
- The following values were removed from meta: ijmax, imax, jap1d, jmax, levnms, lgrmin, linall, lintot, n2dall, nodall, nodobc, nodtot.
- The “prepared” attributes were removed.
- The following datasets were removed from pumps: nodp1d, p1dtyp. The datasets code and upper_stop_level were added.
- A group “cross_sections” was added.
- The following datasets were removed from breaches: llev, kcu, seq_ids.
- The group “surface” was added if the model contains 0D (surfaces/impervious surfaces)


October 18th 2021
^^^^^^^^^^^^^^^^^

We have released a new version of the computational core.

- There is an improved version to compute flow through a breach. The new formula is 2D-grid-size independent and allows sensitivity studies to be conducted based on the discharge. In most cases, your discharge results will remain roughly the same. Also, the discharge becomes tunable, to offer an easy sensitivity option. It also allows you to get back your previous results.

Bugfixes:

- Fixed the computation of the breach width. Especially, the initial growth was underestimated in case the time to reach the maximum breach depth was large.
- Fixed a small bug in the raster edits. This fixed also the option to perform raster edits in computational cells having only 4 subgrid cells.
- Fix for broad weir formulation for the critical conditions

March 8th 2021
^^^^^^^^^^^^^^

In short the following fixes are included in the calculation core:
- Fix for long crested weir; new routine that does not request an extra computational node.
- Fix for short crested weir; Fix to determine super- from sub-critical regime.
- Fix for weirs for negative subcritical flows
- Fix for 1D coordinates in netcdf file: The z-coordinates of the boundary points, are now set correctly in the netcdf
- Fix for initial conditions in netcdf file: In case of 1D-2D models, some variables, like the wet-surface areas of a computational node, the wrong value was written in the results netcdf at the start of the simulation.

Long crested weirs: The formulation of the long crested weir has been replaced by a new one. This new version is based on the law of Bernoulli instead of an alternative implementation of the advective terms for a regular 1D element. The flow over the weir is an accurate computation of the flow under ideal circumstances, but the new formulation does not require an extra computational node and has proven to be more stable under varying flow conditions.

Short crested weirs: Flow over a weir knows three different stages: sub-, supercritical and critical flow.  Under super-critical flow conditions, the formulation remains the same. We fixed the formulation under sub-critical flow conditions and in strong varying flow conditions.  The biggest change in discharge behaviour is expected for weirs that flow in negative direction. Moreover, the time dependency of the flow over the weir has been adjusted. This has no effect on stationary flow, but has a slightly improved stabilizing effect on the flow under changing flow conditions.
ecko