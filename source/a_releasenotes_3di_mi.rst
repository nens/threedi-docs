.. _release_notes_MI:

3Di Modeller Interface
----------------------

November 12th, 2024
^^^^^^^^^^^^^^^^^^^

3Di Models & Simulations 3.15.0
"""""""""""""""""""""""""""""""

This release introduces several useful new options for water quality simulations:

- You can now use constant substance concentrations for laterals and boundary conditions (#1024). It is also still possible to specify a concentration time series for each individual lateral or boundary condition

- You can now add substance concentrations to rain, e.g. to use as a label or tracer (#537)

- You can now add substance concentrations to 1D initial concentrations (#609). This option was already available for 2D concentrations.

- A diffusion parameter can be specified for each substance (#602)

- Using water quality is disabled if your organisation does not include the water quality module in its contract (#625). This will become effective from March 1st, 2024.

- The use of special characters in units field of substances has been restricted to the characters that are accepted by the calculation core (#621)


Other new options and additions:

- Simulation wizard: include option to select previously uploaded 1D initial water level file#610

- New options for :ref:`1d_advection` are now also available in the simulation wizard. New schematisations will by default use the combined energy/momentum conservative scheme instead of the momentum conservative scheme that was the previous default (#603).

- Simulation template creation: append prefix to saved template name in case of Multiple Simulations (#613)

Bugfixes:

- Simulation wizard now gives proper feedback if you choose an invalid boundary conditions file (#624)

- Fix for error when trying to refresh list of downloadable simulations (#622)

- "Stop after" was not read correctly from the simulation template in some cases (#616)

- Substance decay coefficients are now loaded from the simulation template (#612)


3Di Schematisation Editor 1.14.0
""""""""""""""""""""""""""""""""

- New options for :ref:`1d_advection` are now also available in *Global settings* attribute form (#255)

- Vector data importers remember the last directory from which config json was loaded (#254)

- Moving through attribute forms using TAB now follows a logical sequence (#149)

- Bugfix: you can now load multiple schematisations with the same name without getting errors (#270)



3Di Results Analysis 3.11.0
"""""""""""""""""""""""""""

- Several options were added to customise how nodes and flowlines are visualised on the map canvas (#1046)

- The cross-sectional discharge algorithm can now deal with LinestringZ input

- The "use selected features" behaviour in the cross-sectional discharge algorithm has been made more explicit

- Bugfix: Import GWSW-Hyd no longer gives a KeyError when an outlet references a non-existent node (hydxlib#59)


September 25th, 2024
^^^^^^^^^^^^^^^^^^^^

3Di Models & Simulations 3.14.1
"""""""""""""""""""""""""""""""

- Bugfix for *KeyError: 'simulation_user_first_name'* issue


September 24th, 2024
^^^^^^^^^^^^^^^^^^^^

3Di Schematisation Editor 1.13.0
""""""""""""""""""""""""""""""""

- You can now load multiple schematisations at the same time. This also makes it very easy to import (parts of) schematisations into other schematisations (#186, #250, #257)

- The vector data importer has several new features (#167)
    
    - When importing a weir, orifice, or culvert in a location where a channel is present, the structure can now be inserted into the channel network. The channel will be cut automatically, and cross-section locations will be moved and duplicated accordingly. 

    - If your culvert/weir/orifice source data has a point geometry, the importer will convert them to line geometries on the fly.

- Some changes where made to the default properties of the Digital Elevation Model layer, so that it can now be used seamlessly in the QGIS native Elevation profile tool (#116)

3Di Models & Simulations 3.14.0
"""""""""""""""""""""""""""""""

- The user interface for adding breach events to your simulation has been reimplemented for an improved user experience (#440). New possibilities include:

    - Searching for potential breaches by code or display name
    
    - Selecting any 1D2D flowline as a breach location
    
    - Adding multiple breach events in the same simulation

- The user experience in the *Download results* window has been improved in several ways (#368):

    - You can now filter the results by username 

    - You can start downloading a simulation result by double-clicking it

    - The "Simulation name" column has been made wide enough to view the whole simulation name

September 12th, 2024
^^^^^^^^^^^^^^^^^^^^

3Di Results Analysis 3.10.0
"""""""""""""""""""""""""""

- A new tool has been introduced for viewing and comparing flow summaries (#725)

- A new processing algorithm has been introduced to generate spatiotemporal forcing NetCDFs from a list of rasters (#1029)

- Several additions have been made to the *Result aggregation tool* (#861):

    - You can now choose *pump discharge* as variable.

    - The methods comparing the time series to a threshold have been extended. You can now choose the (percentage of) time a variable is below, on or above a threshold. The margin used for a value being "on" a threshold is 1e-06. The way to define the threshold has also been made much more versatile: you can choose any attribute that contains decimal numbers as threshold (e.g. pump capacity or drain level), or define a fixed number as threshold value.   

    - Preset *Total pumped volume* has been added

    - Preset *Pumps: % of time at max capacity* has been added

- Bugfix: Watershed tool: 2D flowlines intersecting obstacles are shown as 1D flowlines (#1034)

- Bugfix: In the Result manager's *Model selection* dialog, the sorting takes into account each column's data type (#1039)

- Bugfix: the cross-sectional discharge algorithm no longer gives a python error if cross-section lines have different CRS then the 3Di results. The cross-section lines are automatically reprojected.

- Bugfix: Time series plotter would give and attribute error when picking a flowline when the simulation includes both pumps and substances (#1044)


3Di Models & Simulations 3.13.0
"""""""""""""""""""""""""""""""

- You now have the option to cancel uploads of new schematisation revisions (#551)

- Several improvements where made to the *Download schematisation* dialog (#276):

    - The *Model slug* column was removed

    - A *Updated* column was added, showing the moment this schematisation was last updated

    - Revisions are automatically fetched when you click on a schematisation (the *Fetch revisions* button was removed)

    - In the *Schematisations* table, the *Created by* and *Commited by* columns now show the user's first and last name instead of their user name

- The gridadmin files are no longer downloaded to the *work in progress* folder, but to the *revision {nr}\grid* folder, because they are read-only (#449)

- The *work in progress\grid* and *work in progress\results* folders are no longer created, as they are not used for anything

- Bugfix: the *Last updated* column in the Simulation Wizard's *Select model* dialog now sorts numerically instead of lexicographically (#587)

- Bugfix for error when trying to start a simulation with laterals and substances (#589)

August 14th, 2024
^^^^^^^^^^^^^^^^^

3Di Results Analysis 3.9.3
""""""""""""""""""""""""""

- Bugfix: Fix "Not a string" error in the Watershed tool (#1032)

August 6th, 2024
^^^^^^^^^^^^^^^^^

3Di Results Analysis 3.9.2
""""""""""""""""""""""""""

- Bugfix: Removed field *max_capacity* from the Sufhyd import tool (#1030)

July 17th, 2024
^^^^^^^^^^^^^^^

3Di Models & Simulations 3.12.0
"""""""""""""""""""""""""""""""

The following new features have been added to the simulation wizard:

- Upload 1D initial water levels (#137)

- Add initial concentrations to your simulations (#535)

- Option to choose the time units for uploaded substance concentration time series on the *Boundary Conditions* page (#577)

- More intuitive navigation using *Tab* in Simulation Wizard (#480)

Other new features:

- Download multiple simulation results in parallel (#391)

- Schematisation descriptions are now also implemented in 3Di Models and Simulations (#493)
    
    - You can fill in a schematisation description when creating a new schematisation
    
    - The schematisation description is shown in the overview of schematisations available for download

- After creating, loading, or downloading a schematisation, you are now asked if you want to load the schematisation into you project

- On the first page of the wizard for uploading new schematisations, it has been made clearer that the schematisation revision history overview is purely informative, i.e. that you do not need make a choice here (#496)

- When uploading a new revision, you are no longer warned that this is not the same revision as you have loaded via the 3Di Schematisation Editor if you have not loaded any. (#526)


3Di Results Analysis 3.9.1
""""""""""""""""""""""""""

- Since the previous release, threedigrid-builder was re-installed every time at startup. This has been fixed. (#1023)

3Di Schematisation Editor 1.12.0
""""""""""""""""""""""""""""""""

- Other plugins or scripts can now tell the 3Di Schematisation Editor to load a specific sqlite or geopackage file as active schematisation (#238)

- Backwards compatibility of the 3Di Schematisation Editor for older spatialites has been increased (#241)

- The 3Di Schematisation Editor buttons are now contained in their own toolbar instead of in the generic *Plugins* toolbar, so that it is easier to customize the 3Di Modeller Interface in the way you prefer (#184)


.. _release_notes_mi_20240621

June 21st, 2024
^^^^^^^^^^^^^^^

3Di Models and Simulations 3.11.0
"""""""""""""""""""""""""""""""""

Several improvements were made to the Simulation Wizard, mainly to support Water Quality simulations:

    - Add substance concentrations to boundary conditions page (#536)

    - Add column "decay coefficient" to table on substances page (#572)

    - Read substance data from simulation template when initializing the simulation wizard (#568)

    - Set the new simulation property *started_from* to "3Di Modeller Interface" (#556)

    - (Bugfix): since the :ref:`release_notes_mi_20230605` release, 3Di simulations with 2D laterals but without substances could not be started from the 3Di Modeller Interface. This has been fixed now (#576)

The naming of downloaded simulation results has been changed to fix some issues:

    - Download results: Make simulation directory name the same for Lizard QGIS plugin and 3Di Models & Simulations (#530)

    - Download results: Remove slashes from simulation name (#497)

The computational grid can now be checked before uploading a new revision of your schematisation:

    - Upload wizard: Check computational grid before upload (#429)

3Di Results Analysis 3.9.0
""""""""""""""""""""""""""

Water quality results can now be visualized on the map canvas. Some improvements have been made in the *Time series plotter* support for Water Quality results:

    - Substance concentrations can now be visualized on the map canvas (#978)

    - Styling improvements in results shown on the map (#1020):

        - Using pretty breaks instead of equal count bins and 2 percent cutoff thresholds

        - Improved labels for first and last legend class

        - Fix drawing direction of breaches

        - Set rendering order for lines (lowest values are rendered first, highest are rendered last, i.e. on top)

    - Time series plotter: do not show warning when there is no Water Quality NetCDF (#1017)

    - Time series plotter: Show (-) if the substance that is to be plotted has no units (#1011)

- Load simulation results (Bugfix): sort by revision ID as integer not string (#1008)

3Di Schematisation Editor 1.11.0
""""""""""""""""""""""""""""""""

- Bugfix: When starting to draw a Culvert, a Python error was produced. This problem was introduced recently and has been fixed now. (#236)





.. _release_notes_mi_20230605:

June 5th, 2024
^^^^^^^^^^^^^^

3Di Results Analysis 3.8.1
""""""""""""""""""""""""""

- Time series plotter: you can now plot substance concentrations for individual nodes in the Time series plotter (#975)

- Result layers in the Result Aggregation, Cross-Sectional Discharge, and Watershed tools now have the exact same fields and field names as the input node, cell, and flowline layers (#914) 

- Several small issues were fixed in the Watershed tool:

    - Do not empty the result layers when closing the tool (and remove the result sets filter when closing the tool)

    - Do not empty the result layers when toggling "Smooth result watersheds"

    - Only show the relevant target node marker when browsing result sets

    - Do not smooth result watersheds of previous result sets; "smooth result watersheds" now only affects new result sets.

    - Bugfix: Catchment polygon was not created when Browse Results was checked (#655)

- Bugfix: when visualising results on the map, the styling of the flowline results was partly broken in QGIS 3.34 (#1005)

- Bugfix: Processing algorithm "Detect leaking obstacles in DEM" gave a Python error after completion (#1004)

3Di Models & Simulations 3.10.2
"""""""""""""""""""""""""""""""

- Several new features and improvements have been implemented in the Simulation wizard:

    - The laterals page has been improved (#467). See :ref:`simulate_api_qgis_laterals` for more information.
    
    - The CSV file format requirements for :ref:`simulate_api_qgis_boundary_conditions`, :ref:`simulate_api_qgis_laterals`, and :ref:`dry_weather_flow` have been made less strict (#560)

    - You can now add substances to your simulation via laterals (#534, #538). See :ref:`simulation_wizard_substances` for instructions on how to define the substances you want to use in your simulation and :ref:`laterals_substance_concentrations` for instructions on how to add those substances to the lateral discharges in your simulation.

- Bugfix: When sorting, table widgets that include a revision ID treat it as an integer instead of a string (#564)

- When uploading a new revision, simulation templates can now be inherited from the previous revision (#529)

- Compatibility with schema 219 to support 1D vegetation (#532)


3Di Schematisation Editor 1.10.1
""""""""""""""""""""""""""""""""

- **Vegetation** can now also be used in the 1D domain; this has been implemented in the cross-section location attribute form (#188, #229, #235)

- You can now specify a different friction value for each segment of a cross-section with YZ shape (#188, #229, #235).

- Several improvements for **manual editing** have been made:

    - Cross-section location can now be placed on a channel segment, not just on channel vertex (#196)

    - Channel ID is updated when moving a cross-section location (#221)

    - Channel ID is filled in when drawing a potential breach (#230)

    - When moving or changing the geometry of schematisation objects, related objects are also moved (topological editing). The implementation of topological editing has been improved to make it more consistent (#219, #220, #232).

        - General topological editing for Connection nodes; when moving a connection node, all schematisation objects that are connected to it are also affected.

        - Specific logic for Channels

            - Cross-section locations are topologically edited when a Channel geometry is edited. Cross-section location can be on a channel vertex or segment.

            - Potential breaches (start vertex) are topologically edited when Channel geometry is edited. Start vertex of a Potential breach can be on a channel vertex or segment.

        - Specific logic for Impervious surface

            - Impervious surface map is topologically edited when Impervious surface geometry changes. The start vertex of the Impervious surface map is on the *point on surface* of the Impervious surface.

        - Specific logic for Surface

            - Surface map is topologically edited when Surface geometry changes. The start vertex of the Surface map is on the *point on surface* of the Surface

- Several improvements have been made to the **vector data importers**:

    - Changes to the layers affected by the import are no longer committed automatically, so that you can review the added features before deciding to commit them to the layer (#228)

    - If geometries in the source layer are different from the geometry type of the target layer, the vector data importer will try to convert them to a compatible type. For example, multipart to singlepart, or MultiCurve to polygon (#222)

    - "Expression" has been added as a method to convert source attributes to target attributes (#211). This can be used e.g. to convert millimeters to meters, to create a code from a combination of source attributes, or to apply more complex if/then/else logic to the source attributes.

    - Source attributes are automatically selected if they have the same name as the target attribute (#190)

    - Import manholes: source manholes are skipped if they are snapped to connection nodes that already have a manhole (#224)

- In the processing algorithm "Map (impervious) surfaces to connection nodes", the option has been added to use "Selected features only" for all vector layer inputs (#227)




April 11, 2024
^^^^^^^^^^^^^^

**3Di Results Analysis 3.8**

- Bugfix: (Max) water depth/level processing algorithm: python error when DEM does not have a nodatavalue (#982). The previous fix for this issue (released March 14, 2024) did not solve the issue in all cases.

**3Di Models & Simulations 3.10.0**

- NetCDF files with spatio-temporal rain (raster time series) can now be uploaded through the simulation wizard (#527)

- Added option to add project name to a simulation (#517)

- Bugfix: 3Di Modeller Interface crashed if schematisation checker has too many warnings (#528)

- Bugfix: Pressing Enter when searching for a 3Di model or simulation template in the Simulation Wizard no longer closes the dialog

**3Di Schematisation Editor 1.10.0**

- Added processing algorithm :ref:`map_surfaces_to_connection_nodes`

- No longer commit changes in processing algorithms :ref:`manhole_bottom_level_from_pipes` and :ref:`map_surfaces_to_connection_nodes` so you can check your edits before committing them. This fixes some stability issues with these processing algorithms.

- Add documentation (in the tool itself) to processing algorithm :ref:`manhole_bottom_level_from_pipes`



March 14, 2024
^^^^^^^^^^^^^^

**3Di Modeller Interface installer**

- 3Di Modeller Interface is now based on QGIS 3.34.4 Long-term release instead of the previous LTR version 3.28. See :ref:`MI_installation`.

- When using the latest 3Di Modeller Interface installer, the axes of graphs on a second screen are now correct.  
 

**3Di Results Analysis 3.5**

- Add *Model properties* table to layer tree when loading a computational grid (#946)

- Add values to value maps in the stylings of computational grid layers, to make it easier to find the values e.g. when applying a filter (#990)

- Bugfix: Remove pop-ups when typing in the input fields for *Results 3Di file* or *Gridadmin.h5 file* in the water depth/level processing algorithm (#981)

- Bugfix: In the *Water balance tool*, when multiple results are loaded, switching between tabs no longer resets the water balance terms checkboxes (#967)

- Bugfix: In the *Result aggregation* tool, in the *Aggregations* tab, the units widget is now correctly updated when switching to a different Variable (#955)


**3Di Schematisation Editor 1.9**

- Create :ref:`importer for *Manholes*<vector_data_importer>` (Processing Algorithm and Graphical User Interface) (#194)

- Create :ref:`importer for *Pipes*<vector_data_importer>` (Processing Algorithm and Graphical User Interface) (#976)

- Create option "Create manholes" in the :ref:`importers for <vector_data_importer>` (#193)

- Create processing algorithm "Manhole bottom level from pipes" (#209)


**3Di Models & Simulations 3.9.1**

- Bugfix: Logging out would produce a Python error in some cases (#525)


**Lizard QGIS plugin 0.3.2**

- Bugfix: Dialog no longer closes when pressing Enter in search bar (#23)


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

-    Remove all user interface customisations, except red menu bar
-    Add "About 3Di modeller interface" dialog

*3Di Toolbox v1.33*

-    Processing tools have been added to check the Spatialite and Rasters. These processing algorithms add the check results as layers to your QGIS project, instead of in a separate shapefile, csv, or text file. You can access them through Processing > Toolbox > 3Di > Schematisation. In the future, these processing algorithms will replace the current checker tools available in the 'Commands' Toolbox.



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

-    More user feedback.
-    The animation layers are removed when the Animation Toolbar is deactivated.
-    The groundwater layers are only displayed when the simulation includes groundwater.

*Dry weather flow calculator*

In some cases it is required to add dry weather flow to a simulation. To enable this a processing tool has been added to convert dry weather flow as defined in the model spatialite (dry weather flow attribute of the impervious surface layer) to lateral discharge timeseries that can be used as in your simulations.
In our earlier API (v1), dry weather flow was read automatically from the spatialite and calculated according a standard distribution.
In the current API (v3), dry weather flow is added as lateral discharges to allow for more flexibility. E.g. in the distribution of dry weather flow over the day.

*Water depth maps for multiple timestep*

We have added the option to generate water depth/level maps for a range of timesteps. The output is a multiband geotiff, where each band contains the water depth map of one timestep.

The water depth processing algorithm also has various minor bugfixes and improvements:

-    Selecting DEM layer from project no longer gives an error.
-    Generating outputs for timestep 0 without moving the timestep slider no longer gives an error.
-    Improved readability of LCD display by adding days to the display.
-    Set LCD value to 00:00 when file is loaded.
-    More accurate description of what the tool does.


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

