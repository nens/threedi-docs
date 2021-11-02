Release notes
=============

.. _release_notes_LS:

3Di Live Site
--------------

October 18th 2021
^^^^^^^^^^^^^^^^^

We have released new versions of the live site

- Saves the organisation you have selected and your previous search term last
- Forms reflect the last action from the user. E.g. for rainfall it doesn't reset to the default value anymore
- Events can be deleted or stopped. For now pumps, discharges, rain and wind are supported

March 23rd 2021
^^^^^^^^^^^^^^^^

We have update the 3Di live site with following features:

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


.. _release_notes_MI:

3Di Modeller Interface 
----------------------

August 2021
^^^^^^^^^^^^^

We have released a new version of the Modeller Interface with the following:

- Update on the animation toolbar
- Added tooling for dry weather flow calculations
- Water depth maps for multiple timesteps 
- Bugfix Sideview Tool

Download here the latest version: `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.7-1-Setup-x86_64.exe>`_ 

Also we have included a comprehensive table on our docs showing the current status of implementation of features of API v3: :ref:`simulate_api_qgis_overview`

*Important note for QGIS Users*

Please note that installing QGIS has been undergoing some changes, at the moment the OSGeo4W Network Installer is the recommended way to install QGIS. See https://www.qgis.org/en/site/forusers/download.html for more information. This change does not apply for users that use the Modeller Interface installer.


*Animation Toolbar update*

The styling of all animation layers has been improved. The value categories are no longer fixed but based on the value distribution in the entire simulation. In the 2D domain, the animation toolbar now visualizes cells instead of nodes. Furthermore, the option 'relative to timestep 0' was introduced. This allows you to switch between e.g. absolute water levels and water level relative to the start of your simulation.
 
Below are examples of a dike breach. Animation 1 is showing relative change in water level and discharge. The plot is done for every calculation cell and flow line. Animation 2 is the same situation as an absolute plot showing the water level per calculation cell and the discharge over the flow lines.
Some other improvements to the toolbar include:

•	More user feedback.
•	The animation layers are removed when the Animation Toolbar is deactivated.
•	The groundwater layers are only displayed when the simulation includes groundwater.

*Dry weather flow calculator*

In some cases it is required to add dry weather flow to a simulation. To enable this a processing tool has been added to convert dry weather flow as defined in the model spatialite (dry weather flow attribute of the impervious surface layer) to lateral discharge timeseries that can be used as in your simulations.
In our earlier API (v1), dry weather flow was read automatically from the spatialite and calculated according a standard distribution.
In the current API (v3), dry weather flow is added as lateral discharges to allow for more flexibility. E.g. in the distribution of dry weather flow over the day.

*Water depth maps for multiple timestep*

We have added the option to generate water depth/level maps for a range of timesteps. The output is a multiband geotiff, where each band contains the water depth map of one timestep.
 
The water depth processing algorithm also has various minor bugfixes and improvements:

•	Selecting DEM layer from project no longer gives an error.
•	Generating outputs for timestep 0 without moving the timestep slider no longer gives an error.
•	Improved readability of LCD display by adding days to the display.
•	Set LCD value to 00:00 when file is loaded.
•	More accurate description of what the tool does.


*Bugfix SideView tool*
 
The SideView tool no longer worked since QGIS 3.16.6. This has now been fixed


May 21st 2021 - 3Di API QGIS Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.7-1-Setup-x86_64.exe>`_ and an update of our 3Di API QGIS Client to version 2.4.1. The following has been fixed:

- Users no longer get a throttling warning when trying to start a simulation. 
- Results download only shows results for the model that is selected in the panel.

The location of plugins has changed from https://plugins.lizard.net/plugins.xml to https://plugins.3di.live/plugins.xml

April 22nd 2021 - 3Di Toolbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`_ and the `ThreediToolbox 1.18 <https://plugins.lizard.net/ThreeDiToolbox.1.18.zip>`_ .
This is a fix for the error *"Couldn't load plugin 'ThreeDiToolbox' due to an error when calling its classFactory() method
ModuleNotFoundError: No module named 'alembic' "*

April 1st 2021 - 3Di Toolbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Due to some changes under the hood in QGIS 3.16 we have released a new version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`_ and the `ThreediToolbox 1.17 <https://plugins.lizard.net/ThreeDiToolbox.1.17.zip>`_ 

March 8th 2021
^^^^^^^^^^^^^^^^

Download the latest version of the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.16.4-1-Setup-x86_64.exe>`_ , which at the time of writing uses QGIS 3.16.4. 
For QGIS users: upgrade the plugin using the plugin panel. In case this doesn't work, it is possible to install the plugins as zip file. The latest versions are `ThreediToolbox 1.16 <https://plugins.lizard.net/ThreeDiToolbox.1.16.1.zip>`_  and `Threedi-API-QGIS client is 2.4.0 <https://plugins.lizard.net/threedi_api_qgis_client.2.4.0.zip>`_. 


*Local calculation of water depth & water level maps*

It is possible to generate water depth maps for every time step with the newest version of the Modeller Interface. To generate these water depth maps, 3Di applies a special algorithm that combines the water level results with the information of the DEM. This algorithm creates visually appealing maps. The maps show the water level and water depth results on high resolution, these can be based on the interpolated and on the non-interpolated water level results.

A quick guide to generate water depth maps:

Processing ^^> Toolbox ^^> 3Di ^^> post-processed results ^^> water depth

Or check out our documentation: :ref:`waterdepthtool`


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
^^^^^^^^^^^^^^^^^^^^^^

- We now support QGIS 3.16 for our toolbox

Download the latest version of the :ref:`qgisplugin`

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
----------


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
- API version v3.0 renamed from to v3. Version v3.0 still works for backwards compatibilty.

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

Using this settings endpoint overrules the settings that are uploaded with the spatialite. Currently this option is only available via our API. For more information on usage please check the `swagger pages <https://api.staging.3di.live/v3.0/swagger>`_ 

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

3Di computational core releases
-------------------------------

October 18th 2021
^^^^^^^^^^^^^^^^^

We have released a new version of the computational core.

- There is an improved version to compute flow through a breach. The new formula is 2D-grid-size independent and allows sensitivity studies to be conducted based on the discharge. In most cases, your discharge results will remain roughly the same. Also, the discharge becomes tunable, to offer an easy sensitivity option. It also allows you to get back your previous results.
 
Bugfixes:

- Fixed the computation of the breach width. Especially, the initial growth was underestimated in case the time to reach the maximum breach depth was large.
- Fixed a small bug in the raster edits. This fixed also the option to perform rsater edits in computational cells having only 4 subgrid cells.
- Fix for broad weir formulation for the critical conditions

March 8th 2021
^^^^^^^^^^^^^^

In short the following fixes are included in the calculation core:
- Fix for long crested weir; new routine that does not request an extra computational node. 
- Fix for short crested weir; Fix to determine super- from sub-critical regime. 
- Fix for weirs for negative subcritical flows 
- Fix for 1D coordinates in netcdf file: The z-coordinates of the boundary points, are now set correctly in the netcdf
- Fix for initial conditions in netcdf file: In case of 1D-2D models, some variables, like the wet-surface areas of a computational node, the wrong value was written in the results netcdf at the start of the simulation. 

Long crested weirs: The formulation of the long crested weir has been replaced by a new one. This new version is based on the law of Bernouilli instead of an alternative implementation of the advective terms for a regular 1D element. The flow over the weir is an accurate computation of the flow under ideal circumstances, but the new formulation does not require an extra computational node and has proven to be more stable under varying flow conditions.

Short crested weirs: Flow over a weir knows three different stages: sub-, supercritical and critical flow.  Under super-critical flow conditions, the formulation remains the same. We fixed the formulation under sub-critical flow conditions and in strong varying flow conditions.  The biggest change in discharge behaviour is expected for weirs that flow in negative direction. Moreover, the time dependency of the flow over the weir has been adjusted. This has no effect on stationary flow, but has a slightly improved stabilizing effect on the flow under changing flow conditions. 


.. _general_3di_releases:

3Di general releases
--------------------


March 23rd 2021
^^^^^^^^^^^^^^^^

3Di is expanding! We are proud to announce that due to international recognition we are expanding the capacity of 3Di:

- The first stage of setting up our second calculation center in Taiwan is finished. Organizations that prefer this center can connect to 3Di via `3di.tw <https://www.3di.tw>`_.  
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
