Release notes
=============

Release 3Di – Autumn Release 2018  
+++++++++++++++++++++++++++++++++++++++++++++

On Monday October 1st 2018 the latest version of 3Di will be released. The 3Di team focussed on implementing the option to edit the bathymetry during a simulation. In addition to this we worked on software maintenance. You will be notified shortly about the details of the winter release. 

Live site
^^^^^^^^^^^^
- Users can edit the bathymetry during a simulation. An extra button has been added in the tool bar on the bottom left of the screen. When this tool is selected, one can indicate the area that is to be adjusted. 
- Since the previous release, it was possible to simulate groundwater flow with 3Di. However, in the live site, there was no visible feedback to the user about what happens in this layer. By clicking on a location, one sees a graph of the water level and the depth variation in time. We added an extra graph for the groundwater level.

Application Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For external programs DEM edits are also available via the API. However, we advise for detailed studies, to adjust the bathymetry prior to the simulation. Note, the change in bathymetry does not affect the post-processing and might give you counter-intuitive results.

Computational core
^^^^^^^^^^^^^^^^^^^^^^
3Di also accepts Chezy roughness values in order to compute the friction in the 2D domain.

Bug fixes
^^^^^^^^^^^^^^
As mentioned in the previous correspondence, we will be more strict when processing the model input. Please make sure, that the following warnings do not occur anymore, as from this release on, the input generation will notify you for errors when these occur:

- Friction type has to be specified for 2D (required as we now support both Manning and Chezy)
- Levee at inactive location in raster. Levee entree is skipped and lies between pixel coordinates ([i0,j0] and [i1,j1])
- Friction raster and DEM are not aligned, please check coordinates:
- Maximum infiltration raster and DEM are not aligned, erroneous coordinates are:
- Maximum infiltration raster and DEM are not aligned, number of erroneous coordinates exceed 10. File is not further evaluated and values are set to default value

Documentation
^^^^^^^^^^^^^^^^
We updated the overview of the spatialite database, as we found an error in the cross-section defenistion. You can download the new database overview :download:`here <pdf/database-overview.pdf>`.

On Monday October 1st 2018 the 3Di web interface will be unavailable between 8.00 AM and 12.00 AM (CEST). 


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
