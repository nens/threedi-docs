Release notes
=============

Release 3Di - Hotfix
++++++++++++++++++++++++

On Monday April 30th, we have released a minor hotfix on our 3Di servers.

The following issue has been fixed:

- In case of a table control structure with discharge_coefficients, settings
  are applied in the right order.

The next full release of 3Di is scheduled for the 8th of July. Then, the Web
Interface will be unavailable between 8.00 AM and 12.00 AM (CEST).


Release 3Di - Carnival Release 2019
++++++++++++++++++++++++++++++++++++

The newest version of 3Di is released on March the 4th. This Carnival release contains various new features. Moreover, we are preparing for a huge product upgrade of the back-end of 3Di. We will explain this in more detail in the next releases. Furthermore, a brand new 3Di start page has been made available to all users: 3Di `startpage <https://3diwatermanagement.com/3di-start>`_.

Usage
^^^^^^

We are happy to introduce a brand new usage `page <https://usage.3di.lizard.net>`_. Users will have an overview of their use of 3Di. This contains the time spend and the time still available for simulations, how many sessions are currently available and who is simulating at that moment. Moreover an overview is given of all simulations that have been performed.

Surface source and sink terms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the Carnival release, it is possible to add a surface source and sink term to your 3Di model. The surface source and sink term will allow users to add or substract water from your 2D surface domain. This can be used for many purposes. An example, could be a simplified method to capture evapotranspiration effects during your simulation. This feature will only be available via the API. In a follow-up release of 3Di, we will support not only time-series, but also time-varying rasters. In the example mentioned above, it would allow for a time-varying evapotranspiration based on satellite imagery. A more detailed description of the :ref:`sssdischarges` is given wit the surface sources and sinks.

Download option for migrated SpatiaLite files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The models in the 3Di repository are migrated after every 3Di release. This to ensure they are still available and working. After this release, the migrated spatialite can be downloaded. New features can than be directly added to existing models. Users will find, after the release, their migrated Spatialite in their model repository at https://3di.lizard.net/models. Users have to download and manually check in the updated Spatialite file in their own repository if they wish to work the latest Spatialite file. This is optional, and only required if you wish to use the newest 3Di features.


QGIS 3.4.5 support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are happy to announce the support on QGIS 3.4.5 for all 3Di related QGIS tools and plugins! We follow the lead of the QGIS in releases and in support of our plugins. This means that we will also stop active development on QGIS 2.18. New features will only be available for QGIS 3.4.5 as this is the new Long Term Release from QGIS. A technical overview can be found `here <changelog.qgis.org/en/qgis/version/3.4-LTR/>`_.
Some nice animations of several of the new features are published `here <https://north-road.com/2017/12/24/24-days-of-qgis-3-0-features/>`_.
Specifically for 3Di, one of the most exciting new features is the new *Mesh support*. This will allow to visualise easily your water levels and velocities in the 2D  domain. This will show the raw data as available in the NetCDF. When using the Crayfish plugin, users can create movies. Note, that results of surface source and sink terms will only be visualised in the plugin supported by QGIS 3.4.5.

The 3Di plugin is tested against windows7, windows10, Linux16.04, Linux18.04. The easiest way to install QGIS with the correct dependencies is using the stand-alone installation package (https://www.qgis.org/nl/site/forusers/download.html). Under Windows, it is recommended to use a 64-bits version of QGIS (a compiled 64-bit version of the netCDF library is included. For the 32-bit version of QGIS you have to install/compile a version of the python netCDF library under QGIS yourself).


Raster Checker
^^^^^^^^^^^^^^

Rasters contain important input data for 3Di. It can be a challenge to have perfectly fitting rasters with all the proper settings. Therefore, we introduce the Raster Checker. It is a tool in the 3Di toolbox of the QGIS plugin that assist the user in checking the consistency of the provided rasters. For example, it checks the alignment of the rasters and the correct settings for nodata values and the pixel dimensions. The DEM raster is taken as leading for all checks. The following checks are performed on all referenced raster in the Spatialite file for all global settings entries:

1. Are all filenames of rasters within one setting_id unique? (3Di can handle this, but the RasterChecker not).
2. Do the referenced rasters (in all v2_tables) exist on your machine?
3. Is the raster file extension .tif / .tiff?
4. Is the raster filename valid? (no special characters, no space, max one '.' and '/')
5. Is the raster single- (not multi-) band?
6. Is the raster nodata value -9999?
7. Does the raster have a projected coordinate system (unit: meters)?
8. Is the raster data type float 32?
9. Is the raster compressed? (compression=deflate)
10. Does the pixel-size have max three decimal places?
11. Are the pixels square?
12. Are there no extreme pixel values? (dem: -10kmMSL<x<10kmMSL, other rasters: 0<x<10k)

After running the tool a pop up window will appear which shows the name and location of the log file with detailed error logging and a shapefile with point information to show you were errors have been found.

Bug fixes
^^^^^^^^^^^^^^

The following bugs have been fixed in this 3Di release:

- Water balance tool now correctly checks whether rain has been applied to simulation
- Fixed bug in netcdf_groundwater not reading in correctly the aggregate variable
- Apply conversion from hours to seconds of inundation_period in damage_estimation settings when headless calculation is started from queue (after "currently no sessions available"). When storing results, the applied unit is now consistently in hours in the whole 3Di stack.
- Error related to case sensitivity in email addresses resolved in user management screen.
- Show polygon of raster edit for v2 models in live site.
- Handling DEM edits through levees correctly. Users don’t have to edit the full width of the cell edge anymore to lower the levee.
- Use of correct primary key in relation between manholes and connection nodes when visualizing water depth, water level and groundwater level on the live site.
- Fixed deletion of generated inp-files of deprecated model revisions. Users have access to max three revisions of their models. Before, models were incorrectly being stored on the server.
- [3Di QGIS plugin] Select correct scenario results after filtering in list.
- [3Di QGIS plugin] Fixed visualization of interception time-series.
- [3Di QGIS plugin] Water balance now correctly checks availability of rain in scenario results.
- API Calls are being checked for invalid options. It is no longer possible to pass an invalid option into the API.
- Time out on the live site has been adjusted to 15 minutes in case of inactivity.


Release 3Di - Hotfix
++++++++++++++++++++++++

On Monday January 14th, we will release a hotfix on our 3Di servers. We expect a very limited downtime around 8.00 AM (CEST).

After the hotfix, the following issues will be fixed:

- Bug concerning the chosen boundary condition type for some cases that include 1D and 2D boundaries
- For a specific combination of SpatiaLite-settings, e.g. multiple entries in v2_global_settings table, egg-shaped profiles were not processed correctly
- DEM edits are now possible outside the -10 m and +10 m range

Furthermore, in the LiveSite a wider range of design rainfall events is available. This concerns some specific Dutch rainfall events (DPRA buien).

The next full release of 3Di is scheduled for the 4th of March. Therefore, the Web Interface will be unavailable between 8.00 AM and 12.00 AM (CEST).

Release 3Di – Hotfix
++++++++++++++++++++++++++++

On the 5th of December 2018 3Di, will be updated with some minor fixes. These include:

-  The cross-sections in case of a breach in combination with interflow
-  The 1D discharge written in the results NetCDF and the aggregation NetCDF in some special cases
-  Included a correct initialisation for aggregation setting 'current'



Release 3Di – Fall Release 2018
+++++++++++++++++++++++++++++++++++++++++++++

The newest version of 3Di is released on 26th of November 2018. With this update, the following features are available for all users of 3Di:

- Interception
- Culvert discharge coefficients
- Water balance tool
- Option for custom rain event
- Software updates and bug fixes

Interception
^^^^^^^^^^^^^

With this release, we introduce a new process in 3Di to extend the processes of the hydrological cycle. It is now possible to take interception into account during your simulation. Interception refers to precipitation that does not reach the bottom, but is instead intercepted by buildings or vegetation.

The interception layer can be used in the following situations:

- The obvious application is to take the effect of interception into account due to vegetation, green roofs and other buildings.
- However, it can also be used in the so-called hybride models, where urban areas are modelled and the inflow to the sewer from buildings is directly coupled to the sewer system.

It is possible to edit the interception layer in the 3Di live site.

Culvert discharge coefficients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From this release, the culvert discharge coefficient will be enabled. The coefficient allows to take inlet losses for culverts into account and can be defined for positive and negative flow directions.  The coefficient is defined via an attribute per culvert in the table 'v2_culvert'. Prior to the release, the coefficients were already available in the spatialite. However, these coefficients were not yet taken into account. After the release, these will become active, this might, of course, affect the results. In case, these coefficients were unintended, set these coefficients to 1, and you will return to your previous results.

Water balance Tool
^^^^^^^^^^^^^^^^^^

A new version of the 3Di QGIS plugin is released as well. Hereby, we also release the 3Di water balance tool. Users can select an area on the map and see the exact water balance, including an overview of the flows between the 2D surface water, 2D groundwater and the 1D flow domains for a certain area and period. To be able to use this water balance an aggregation NetCDF is required. This exciting new tool helps users to get an improved insight in their water system. With this water balance tool, we help experts in their analysis and understanding of the modeling results.

For more information have a look at our documentation on the :ref:`waterbalance`. Here, one finds an overview of the aggregation settings required for the use of the water balance tool as well.

The water balance tool is an initiative of Deltares and a co-creation of experts of Deltares and Nelen & Schuurmans. It is co-funded by the Ministry of Economic Affairs (Top Sector Water).

Option for custom rain event
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the 3Di live site, the options for rain events are extended. It is now possible to define a time-varying rain event.


Software updates and bug fixes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Behind the scenes there have been some major changes to the 3Di software. We have fundamentally improved the server-interaction. Note, this changed some minor things. When you want to load a new model, quit your previous session first. Your session on the live site will close after 1 hour of inactivity. Use the API, for longer simulations with no interaction.


Threedigrid has been extended with some more information of your model to allow for a more accessible analysis.

Moreover, several bug fixes have been performed.  These include;

- The message *No more sessions available* was sometimes visible, when it was not true. We have added a new session count system, which eliminates this bug
- No more potentially leaking levees in case of interflow
- Removed check for type 2 pumps on lower stop level.
- Added check for overlapping vertices in channels and culverts
- Fix in visualizing the groundwater results in the live site
- Fix for dealing with obstacles after a DEM-edit


Release 3Di – Autumn Release 2018
+++++++++++++++++++++++++++++++++++++++++++++

The newest version of 3Di is now available. With this update, it is possible to edit the bathymetry layer in the 3Di live site.
The following has been adjusted in 3Di:

- Bathymetry edits in live site
- Groundwater levels visible in live site
- Friction based on the Chezy formulation in 2D domain
- Adjusted logging
- Documentation update

Moreover, we took measures for the maintenance of the 3Di software. Soon you will receive an update with several developments around our QGIS plugin.

Please note! Due to technical problems, not all input files are updated to the newest 3Di version. We expect all models to be available October 8th. You can update the input files of your own model to the newest version manually, by following the tutorial at the end of these release notes. You are also welcome to contact our service desk to update the model for you.


Bathymetry edits in Live Site
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A DEM (Digital Elevation Model) edit is the newest tool in our live site, it allows to adjust the height of the bathymetry. This can be done at any time during the simulation by drawing a polygon. The DEM edit is immediately committed when finishing the polygon. The result can be checked using the 'Cross profile' tool. A DEM edit is also possible via our `API <:https://3di.lizard.net/api/v1/docs/>`_ , thereby allowing external applications to perform a DEM edit as well. However, the steps performed by ‘process results’ do not take the DEM edit into account.  Take this into consideration when interpreting the results.

Groundwater
^^^^^^^^^^^^^

In our previous release ground water has been added to 3Di. From now on groundwater levels are visible in the live site in the cross-profiles and in a pop-up panel for waterlevels.

Chezy resistance (2D)
^^^^^^^^^^^^^^^^^^^^^^
From the start of 3Di, the Manning formulation is implemented to compute friction. In some cases users prefer to use a different friction formulation, for this the Chezy formulation is now available in the 2D domain.


Spatialite database in documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The overview of the spatialite database is updated in our documentation, because we found an error in a cross-section definition. It concerns type 1 rectangle. We advise everyone to download the newest database overview: :download:`here <pdf/database-overview.pdf>`

Error and warning messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The next cases will be marked  as “Error” instead of “Warning”.
- Non-Existing foreign key relations, for example non-existing connections to impervious surfaces
- Friction type has to be specified for 2D (required as we now support both Manning and Chezy)
- Levee at inactive location in raster. Levee entree is skipped and lies between pixel coordinates ([i0,j0] and [i1,j1])
- Friction raster and DEM are not aligned, please check coordinates:
- Maximum infiltration raster and DEM are not aligned, erroneous coordinates are:
- Maximum infiltration raster and DEM are not aligned, number of erroneous coordinates exceed 10. File is not further evaluated and values are set to default value

We hope by doing this, to improve the feedback for users about errors in the model, before the model starts with the computation. When you receive one or more errors, you cannot proceed with your simulation until your errors are resolved. We ask users to check the warning and error messages after the model generation and try to solve them before contacting the service desk.


Tutorial: Update input for 3Di model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To run some simulations in first week of October, you may need to update the input files of your model manually. This tutorial explains the manual steps:

- Browse to https://3di.lizard.net/models
- Search your model. If not listed, click on ‘also show repositories that do not have inp files yet’. Only the version of your latest commit of your model will be listed, during this week. When you need an older and/or pinned version, please contact the service desk. We will make this version for you available.

.. figure:: image/rn_tut_1.png

- After you have found your model, click the icon in the column ‘initialize inp generation’

.. figure:: image/rn_tut_2.png

- Depending on the size of your model, the input generation can take a few minutes up to 15 minutes before it appears.
- As soon as the model appears, the column ‘last run’ will show a green button with the word ‘success’ or a red button with ‘failed’. In case, the generation failed, take a look at the log files.
- Click on the button ‘success’

.. figure:: image/rn_tut_3.png

- Click on the pencil icon on the left [1] and then on the button ‘visible’. [2]

.. figure:: image/rn_tut_4.png

- Store your result (save icon appears on the location of the pencil icon) [1].
- Your model is now ready for use in the live site and for use with the API.



Release 3Di - Hotfix
+++++++++++++++++++++++++

On Thursday the 5th of July, we released a new version of 3Di to solve some minor bugs. The following has been added or changed:


LiveSite and API
^^^^^^^^^^^^^^^^^^^^
- The wind forcing was not working properly after the previous release.

- Some computations, run with the rain radar input from The Netherlands, endured from a specific technical problem with map projections between the live site and rain radar. This is fixed.

Input
^^^^^^^^
The log-messages concerning errors in input data is improved. Users can find the error messages in the logging files on the model page. However, 3Di became also more strict to errors. If errors occur in the grid generation, a simulation cannot be initiated. An example of an error, that is often ignored: is when the lower stop level of a pump is defined below the bottom level of the connection node. Naturally, this is an impossible configuration. Therefor, this needs to be fixed by the modeller.

Furthermore, if a certain error occurs more than 10 times it will stop printing the error. This is to ensure that the log files remain compact and readable. This does not mean that the error is less important. An example of an error message that is encountered many times is when users supply rasters that are not aligned.


Inflow model
^^^^^^^^^^^^^^^^
In 1D modelling, a mapping table is build to map connection nodes with the (impervious) surfaces related to the inflow model. Previously, we needed the ids of the mapping table to be incremental with no missing numbers. This is not required anymore. An example: after building a mapping table, the user deletes one of these mappings. In the past this meant that the ids of the table needed to be rebuild. In the current situation, no further action from the user is required.

Computational core
^^^^^^^^^^^^^^^^^^^^

The formulation to compute the flow through a breach is improved, in response to lack of the flow through a breach in case of a very small breach and high infiltration.


Release 3Di – Spring Release 2018
+++++++++++++++++++++++++++++++++++++

On Monday the 28th of May 2018 the latest version of 3Di will be released. This is a so-called major release. The past months, the team included groundwater in 3Di. In close collaboration with Prof. Stelling and in association with Deltares, we extended 3Di to a two-layer system to be able to compute the interaction between surface water and groundwater. A more elaborate explanation about the new features can be found in the 3Di documentation (https://docs.3di.lizard.net).

Some other changes:

LiveSite
^^^^^^^^^^^^^^^^
Some of the visualizations in the LiveSite are improved. For example, the levees and breach locations are much better visible. Also, more information about the computational grid becomes available, such as the deepest point in the cell, the IDs and the levee heights.

Application Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The progress of simulations that are computing via the API is shown on a progress bar. The progress bar can be found from the start screen (https://3di.lizard.net) under follow running simulations.

Input
^^^^^^^^

There are several adaptations in the input. There are three new input tables; v2_groundwater, v2_interflow and v2_simple_infiltration, to which you can refer to in the v2_global_settings table. The content of the final two table is not new, but are removed, for clarity, from the v2_global_settings table. In addition to this, there are some small changes concerning the aggregation input. For more detailed information, we refer to the 3Di documentation.

QGIS Plugin and Output
^^^^^^^^^^^^^^^^^^^^^^^^

There will also be a new version of the 3Di Plugin required (Version 1.0). With this release, we meet different conventions for NetCDF (CF conventions). With the new 3Di Plugin, results from the old type and the new type of the NetCDF can be evaluated. Behind the scenes, there has been a lot of work to reorganize the Plugin, as a preparation to future developments.



Release 3Di – April 2018
++++++++++++++++++++++++++++++

On Monday the 23th of April 2018 the latest version of 3Di will be released. The 3Di team worked mainly on improving the performance of computational times when using the API, and on implementing groundwater flow. Groundwater flow will be available to everyone from next month. In this release we have worked on:


Application Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When you want to run batches of scenario’s or set up operational scenario’s the best route is using the API. An explaination for using the API can be found in the manual
:https://docs.3di.lizard.net/en/stable/d_api.html

- The computational times are greatly improved with this Release. Times can be up to ten times as fast.

Note:
The reduction in computational time does not occur for simulations, making use of wind and/or breaches. It is no longer possible to follow these API simulations via the Livesite. At the next release, user feedback for API simulations in the livesite will be improved.

Bug fixes
^^^^^^^^^^^^

There are improvements concerning:

-	Computations using embedded channels

-	The stability of connection to the livesite to make it more robust.


On Monday the 23th of April 2018  the 3Di web interface will be unavailable between 8.00 AM and 10.00 AM (CEST). The next full release is planned on Tuesday May the 22nd  2018.
