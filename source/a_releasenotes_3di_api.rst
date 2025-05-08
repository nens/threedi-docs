.. _release_notes_api:

3Di API
-------

April 30th, 2025
^^^^^^^^^^^^^^^^

- New administration for lateral forcings and substance events to make it possible to use substances in dry weather flow (threedi-api#2393, #2394, threedi-api#2384)
- In water quality simulations, rain zones can be defined to add substance concentrations to rain that falls in specific zones (threedi-api#2372)
- Bugfix: action tables as created by the 3Di Schematisation Editor are now correctly parsed
- Bugfix: there was a bug in the conversion of time units in the schematisation to the simulation template for laterals and boundary conditions (threedi-api#2456)
- Bugfix: simulation template generator would give an error when initial conditions table has no rows (threedi-api#2464)

Database schema
"""""""""""""""

- Spatialites are deleted after conversion to geopackage if there are no errors or warnings during the migration.
- Sewerage type can now have any integer value
- Bugfix: Several fixes in progress tracking during migrations (these fixes were already included in the 3Di Modeller Interface)
- Bugfix: some old index tables would not be deleted during migration, this has been fixed now

Grid builder
""""""""""""

- Make compatible with GDAL 3.10 (threedigrid-builder#415)

Schematisation checker
""""""""""""""""""""""

- Bugfix: Schematisation checker would stop at 95% for some schematisations (threedi-modelchecker#454)
- Bugfix: Schematisation checker no longer gives Python error when it encounters an empty cross_section_table
- Add check if grid level is NULL in *Grid refinement area* or *Grid refinement line* (#459)
- Bugfix: When *Use structure control* is set to *True*, *Table control* and *Memory control* cannot both be empty. The bug was that if one of them was empty and the other one not, a warning was still given. 
- Add check (1207) for valid values for time units in boundary conditions and laterals.
- Add exporter that includes geometries
- Remove warning level override for old enum checks.
- Bugfix: cross-section checks no longer break when shape is NULL (this fix was already included in the 3Di Modeller Interface)
- Removed checks: 28, 186, 1601, 1602, 1603 (this was already included in the 3Di Modeller Interface)
- Checks 95, 96, 97 are not only run for channels (this was already included in the 3Di Modeller Interface)
- Some textual improvements (this was already included in the 3Di Modeller Interface)

February 24th, 2025
^^^^^^^^^^^^^^^^^^^

- Threedi-schema from 0.227 to 0.300

- Option to include DWF distribution from sqlite

- Modelchecker from 2.14.1 to 2.17.3

- Calccore from 3.5.4 to 3.6.4


November 18, 2024
^^^^^^^^^^^^^^^^^

- Some internal functionalities were added allowing Rana to add users and create/revoke Personal API Keys

- Restrict substance units to ASCII characters (#2343)

- Bugfix: Starting simulation from the 3Di Modeller Interface with the option to upload a local raster as 2D initial concentration raster would give the error "Failed to process Initial Concentration raster". This has now been fixed by including an internal wait time for concentration file uploads in the API (#2256) 

- Bugfix: in the *settings* migration for database schema 300, the raster paths for vegetation_drag_2d were not stripped of 'rasters/' (threedi-schema#131)

October 23, 2024
^^^^^^^^^^^^^^^^

Database schema 300
"""""""""""""""""""

In the database schema, some additional changes were made to structure control:

- Use *Measure variable* from *Control measure location* instead of from *Memory control* or *Table control* (threedi-api#2322)

- Check if all measure locations that are mapped to the same *Table control* or *Memory control* have the same *Measure variable* (threedi-modelchecker#395)

- Remove *Measure variable* from *Memory control* and *Table control*; this should be specified at the *Measure location* (nens/threedi-schema#97)

Bugfixes and minor improvements
"""""""""""""""""""""""""""""""

Several bugfixes and improvements were made:

- Improvements in "simulation crashed" email (threedi-api#2331)

- The available historical and radar rain services were recently made configurable per organisation; it is now possible to set a list of services for each, instead of only one (threedi-api#2353)

- Bugfix: Fix 1D initial substance concentration bug (threedi-api#2347)

- Bugfix: YZ cross-sections are not processed correctly if they have an irregular shape (threedigrid-builder#383)

- Bugfix: Some settings were not migrated correctly if the original spatialite still was a Spatialite 3 file instead of Spatialite 4 (threedi-schema#121)

- Bugfix: Structure control type could not be validated succesfully (threedi-api#2354)

- Bugfix: Bulk forcing does not take file offset into account (threedi-api#2351)




October 10, 2024
^^^^^^^^^^^^^^^^

More control over output files
""""""""""""""""""""""""""""""

- A new output file type has been introduced, *Customized results*. Like the *results_3di.nc* and *water_quality_results_3di.nc*, this file contains snapshots at each output time step. The advantage is that you can customize what is written to this file: limit the results to a specific area of interest, and/or to a subset of flow variables. This allows you to output e.g. water levels at the location of a stage gauging station at a very high temporal resolution, while keeping the output files small. Customized result files are available for both hydrodynamic and water quality results (threedi-api#2198, threedi-api#2199, nens/threedigrid#237).

- A new category of simulation settings has been introduced: output settings (both for hydrodynamic and water quality outputs. This includes:

    - On/off switch for creating the results_3di.nc file (i.e. if you only want customized_results_3di.nc)

    - On/off switch for creating the water_quality_results_3di.nc file (i.e. if you only want customized_water_quality_results_3di.nc)
    - Start time and end time for the results_3di.nc and customized_results_3di.nc files, for if you are only interested in a specific temporal part of your hydrodynamic simulation results

    - Start time and end time for the water_quality_results_3di.nc and customized_water_quality_results_3di.nc files, for if you are only interested in a specific temporal part of your water quality results

    - Switching between single precision or double precision outputs for each results file.

Database schema 300
"""""""""""""""""""

We continue to work on :ref:`schema_300`. Two additional migrations are now in use on the 3Di server. When a 3Di model is generated from a schematisation, the spatialite is first migrated to the latest schema version. Additional parts of the database schema that are migrated to the new database schema are from this release onwards are:

- 2D & 1D2D. This encompasses the obstacles, grid refinement (lines and areas), dem average areas, exchange lines, and potential breaches (nens/threedi-schema#73, nens/threedigrid-builder#375, nens/threedi-modelchecker#387, nens/threedi-api#2279, nens/threedi-schema#108).

- Boundary conditions (1D and 2D) and Laterals (1D and 2D) (nens/threedi-schema#69, nens/threedi-modelchecker#381, nens/threedigrid-builder#371, nens/threedi-api#2262, nens/threedi-schema#106)

Some bugfixes on the previously released schema migrations have also been released:

- Bugfix: Control measure map geometry was reversed (nens/threedi-schema#96)

- Bugfix: Ensure dry_weather_flow_map.geom and surface_map.geom are valid, also in special cases. This fixed situations where the error "dry_weather_flow_map.geom is an invalid geometry" was given (nens/threedi-schema#102)

- Bugfix: Warning instead of error for schematisations that have structure controls that reference non-existing connection nodes (#91)

- Bugfix: Prevent migrations to fail if the spatialite contains user-created tables named "temp" or having the same name of one of the new tables created in the migration (nens/threedi-schema#93, nens/threedi-schema#95)

Other changes
"""""""""""""

- Support for setting the diffusion parameter for substances has been added to the API (#2253)

- Support for the two new 1D advection types (see :ref:`1d_advection`) has been implemented in the API (#2289) and in the database schema (threedi-schema#84)


September 11, 2024
^^^^^^^^^^^^^^^^^^

Database schema 300
"""""""""""""""""""

The first migrations to :ref:`schema_300` are now in use on the 3Di server. When a 3Di model is generated from a schematisation, the spatialite is first migrated to the latest schema version. Parts of the database schema that are, from this release onwards, migrated to the new database schema are:

- Settings (threedi-schema#75, threedi-schema#81, threedi-schema#79, threedi-modelchecker#363, threedi-api#2168, threedigrid-builder#355)

- Inflow (threedi-schema#65, threedi-api#2228, threedigrid-builder#362)

- Structure control (threedi-schema#70, threedi-modelchecker#382, threedi-modelchecker#385, threedigrid-builder#373, threedi-api#2263)

Other changes
"""""""""""""

- Access to historical and forecast rain radar services can now be configured on organisation level (by the service desk) (#2244)

- Multiple 3Di accounts can now be coupled to the same Lizard account (Scenario archive) by the service desk #2203

- Tags can now be added to schematisation revisions (#1948)

- Bugfix: Substance concentrations were connected to DWF laterals while forcing only added substance to 2D lateral (#2243)

- Bugfix: Substance concentration was only added to one boundary condition, even when user specified it should be added to multiple boundary conditions (#2242)

- Bugfix: DEM en water depth maps in 3Di Live are now visualised correctly also when the DEM nodata value is not -9999 (#2257)

- Bugfix: NetCDF forcings with long projection strings are now also accepted


.. _release_notes_3di_api_20240530:

May 30, 2024
^^^^^^^^^^^^
- Implement substance decay (threedi-api #2150)

- Add a *started_from* property to simulations to indicate which user interface started the simulation (3Di Live or 3Di Modeller Interface) (threedi-api #1328)

- Add units to substances (threedi-api #2085, threedigrid #223)

- Add linestring geometry to pumps in geojson (threed-api #1955)

- Bugfix: Assymmetric YZ profiles were not processed correctly (threedigrid #228)

- Bugfix: Simulation with multiple substances no longer crashes (threedi-api #2223)


April 29, 2024
^^^^^^^^^^^^^^

- Add multiplier to all surface sources and sinks endpoint(s) (threedi-api#212). The main intended use case for this is to use it with a negative value in combination with a (Lizard) raster time series that contains (positive) evapotranspiration values.

- Make it possible to add substance concentrations to all surface sources and sinks endpoints (threedi-api#2173)

- Migration 220 introduces the option to transfer all data from Spatialite to GeoPackage (threedi-schema#45)

- Make ``threedigrid-builder`` compatible with GeoPackage (threedigrid-builder#341) 

- Add cross section table data to GeoJSON export (threedigrid#218)

- Include exchange level in breaches GeoJSON export (threedigrid#219). The ``levl`` property now contains the exchange height

- You can now get the units of a substance through a ``GridH5WaterQualityResultAdmin`` object (threedigrid#223)

- Make ``threedi-modelchecker`` compatible with GeoPackage (threedi-modelchecker#342)

- Remove schematisation check that gives an INFO level message suggesting it would be better to use a friction method with Conveyance 0029 (threedi-modelchecker#358)

- Bugfix: Simulation tags were not always created (threedi-api#2170)



March 18, 2024
^^^^^^^^^^^^^^

- Add water quality settings and substance settings.

- Add substances to leakage and surface sources and sinks endpoints.

- Improve time series validation for substances concentrations, leakage, and surface sources & sinks.

- Stream ucx / ucy over web socket (#2120)

- Change bulk lateral creation to reduce memory usage (#2129)

- Bugfix: initial substance concentrations were not always passed to the computational core correctly

February 2, 2024
^^^^^^^^^^^^^^^^

- Include substance names in water quality result file(s)
- Bugfix: issue with "Could not find aggregation file for initial groundwaterlevel raster" resolved.
- Bugfix: DEM edits in models with for groundwater

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

- The exchange type of culverts is not ignored anymore.

- For calculation nodes on channels with connected exchange type, the cross section will be used until the surface level of the DEM. This will give differences for channels with connected exchange type in case the cross section is below the surface level.


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



