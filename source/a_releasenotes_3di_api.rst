.. _release_notes_api:

3Di API
-------

March 3, 2024
^^^^^^^^^^^^^

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



