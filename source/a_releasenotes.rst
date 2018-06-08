Release notes
=============

The next release of 3Di is planned in October 2018. We will inform you about the details of this release in due course.


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
