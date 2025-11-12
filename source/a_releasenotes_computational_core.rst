.. _computational_core_3di_releases:

3Di Computational core
----------------------

November 12th, 2025
^^^^^^^^^^^^^^^^^^^

**Water quality**

- Substance concentrations that are added to rain are now also applied to surface inflow
- Use global implicit solve for water quality if implicit is needed somewhere.
- In substance summary, sort on substance id

**Hydrodynamics**

- Bugfix for 2D advection in cases of dry and/or inactive neighbouring cells in grid transitions
- Improve formulation of inflow infiltration by improving the recovery rates

**General**

- Extra checks on file close for NetCDF files based on allocation

June 10th, 2025
^^^^^^^^^^^^^^^

- Improved stabilitity of water quality module

April 30th, 2025
^^^^^^^^^^^^^^^^

- Refactor of laterals and substance laterals to make it possible to use substances in DWF and fix several issues with laterals and DWF (threedi-calculationcore#852, #860, #859, #861, #857)
- Total discharge boundary condition is now compatible with interflow (threedi-tables#280, threedi-calculationcore#821)
- Interflow discharge and velocity at boundary lines for total discharge boundary type are added in netCDF file 


February 24th, 2025
^^^^^^^^^^^^^^^^^^^

- Total discharge boundary for 2D and Groundwater

- Upgrade to python 3.12

- Fix NaN value propagation from gridadmin and tables files

- Bugfix for 0D inflow from impervious surfaces



October 10, 2024
^^^^^^^^^^^^^^^^

- Customized result files for hydrodynamic and water quality results (nens/threedi-api#2339, threedi-calculationcore#803, threedi-calculationcore#799, threedi-calculationcore#823)

- Receive new result file settings from API (#798)

- Bugfix: Set threedicore-version in attribute of netcdf result files (#841)


September 11, 2024
^^^^^^^^^^^^^^^^^^

- When using a saved state for a model with interflow, the interflow velocities and discharges from that saved state are now written to the results NetCDF at timestep 0.

- When using a saved state, the initial intercepted volume and initial infiltrated volume from that saved state are now included in the flow summary (#766)

- In water quality, support for (physical) diffusion has been implemented in the computational core (not yet in the API) (#773, #774)

- For 1D advection, two new types of calculating 1D advection have been introduced. The current advection method (1) is momentum conservative. The two new methods are (2) energy conservative and (3) a 'smart' method that uses the energy conservative or momentum conservative method depending on the situation. See :ref:`1d_advection` for details. (#753, #754, #755)

.. _release_notes_calccore_20240605:

June 5, 2024
^^^^^^^^^^^^

- In the water quality module, a discretisation method has been implemented that improves the stability and reduces numerical diffusion. It uses a combination of explicit and implicit solving methods. This two-step method overcomes limitations of the accurate explicit method and ensures stability with the implicit part of the method. (#794)

- Improved stability of water quality calculations in case of shallow, fast flowing water (#795)

- Bugfix: Load entering via leakage not included in substance summary (#808)


.. _release_notes_calccore_20240530:

May 30, 2024
^^^^^^^^^^^^

- Timestep handling in the water quality module has been improved significantly (#742, #751, #752). This makes water quality calculations much faster, more stable, and more accurate.

- A decay coefficient (half-life) can now be set for each substance (#700, #775)

- It is now possible to use single vegetation parameter values (constant over the whole cross-section) when using cross-section shape *YZ* and friction type *Chezy with conveyance* (#800)

- Bugfix: Some types of raster NetCDF forcings (e.g. NetCDF rain) were not accepted by the 3Di API because of a bug in the routine that compares the spatial extent of the forcing to the spatial extent of the 3Di model. This has been fixed now (#2221).


April 29, 2024
^^^^^^^^^^^^^^

- Separate friction values can now be defined for each segment of a YZ profile when using friction with conveyance (threedigrid-builder#342, threedi-calculationcore#738, threedi-tables#271, threedi-schema#42, threedi-modelchecker#354)

- Vegetation can now also be used in the 1D domain (threedi-calculationcore#735, threedi-schema#42)


March 18, 2024
^^^^^^^^^^^^^^

- Add substance settings to water quality module.

- Add numerical setting to water quality module.

- Fix polygon creation bug for DEM and raster edits.

- Fix water quality time step reduction and initialize concentrations to zero if there is no volume in the cell.

- Set fill value for NetCDF result files.

- Use Shapely 2 instead of pygeos


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

- Channels with exchange type *connected* or *double connected* can now be placed outside the DEM, as long as they connect to a location where a 2D cell is present. If a 'potential breach' or 'exchange line' is used to set the location to which the calculation node connects, the location of those features determines whether an error is raised. If a channel with exchange type connected is outside of the DEM, but the closest point on its exchange_line is on the DEM, the computational grid can be built and the 3Di model is valid.

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

- The exchange type of culverts is not ignored anymore.

- For calculation nodes on channels with connected exchange type, the cross section will be used until the surface level of the DEM. This will give differences for channels with connected exchange type in case the cross section is below the surface level.


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