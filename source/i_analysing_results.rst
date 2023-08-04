.. TODO: - show the new 3Di Results manager panel
.. TODO: - Temporal Controler instead of animation toolbar 
.. TODO: - Graph tool is now Time Series plotter 
.. TODO: - Statistics tool is deprecated. It is replaced by 3Di Results Aggregation (formerly known as the beta tool '3Di Custom Statistics'. Three new processing algorithms are introduced: Cross-sectional discharge, Detect obstacles in DEM (2x). See the built-in documentation for more info.
.. TODO: - Do not mention that it is 'new' in the docs, because that will require changes once it is no longer new. Explain how things work as if you are explaining it to new users that are not familiar with the 'old' situation. 

.. _analysing_results:

Analysing results 
==============================

See :ref:`mi_download_res` for information on how to download simulation results.
Once downloaded, the simulation results can be analysed in the 3Di Modeller Interface with the *Results Analysis* plugin. 

.. _3di_results_manager:

Results Manager
-------------------

Open the *Results Manager* from the toolbar (|addresultstoolbar|) to load and analyse your results. By clicking the upperright icon (|addresults|) you can search for the simulation results you want to analyse. You can choose from all simulation results that have been downloaded to your local 3Di working directory. Select the one you want to analyse and click either *Load computational grid* or *Load simulation results*. Both options will load the computational grid into the Layers panel, but the latter option is required to see the results.

Once the results have been loaded into the 3Di Modeller Interface, you have a toolbox at your disposal to help you analyse them.
You can remove a set of results first selecting the one you want to remove and then clicking the upperright icon (|removeresults|).

\*Note: By hovering the cursor over certain parts of the Results Manager, helpful tooltips will appear.

.. Ik snap het hele toctree gebeuren niet helemaal..

.. toctree::
   :maxdepth: 1
   :caption: Tools to analyse simulation results
   :name: Tools to analyse simulation results
   
   i_temporal_controller
   i_time_series_plotter
   i_sideview_tool
   i_results_aggregation
   i_water_balance_tool
   i_watershed_tool
 
- :doc:`i_temporal_controller` to show the results through time.
- :doc:`i_time_series_plotter` to plot the results in a graph.
- :doc:`i_sideview_tool` to analyze the water levels through the simulation in your 1D domain.
- **3Di Result Aggregation** to quickly aggregate the results over the entire simulation, using preset outputs and styling.
- :doc:`i_water_balance_tool` to determine the water balance for a given area that takes all flows in and out of the area into account.
- :doc:`i_watershed_tool` to determine the inflow and outflow catchments for any given location.

.. |addresultstoolbar| image:: /image/i_3di_results_analysis_toolbar_results_manager.png
	:scale: 25%

.. |addresults| image:: /image/i_add_results.png
	:scale: 90%	
	
.. |removeresults| image:: /image/i_remove_results.png
	:scale: 90%	

.. |temporalcontroller| image:: /image/i_temporal_controller.png
	:scale: 90%	
		

.. _logfile:

Log-file
-------------------
Clicking the (|loggingtoolbar|) saves the logging of your results analysis to your computer. By clicking the underlined path to the text-file in the pop-up windows you can open the logging-file. This can provide  helpful information about what went wrong in case of an error.

Also, it can be send as an attachment to our :ref:`servicedesk` at servicedesk@nelen-schuurmans.nl in case of errors.

.. |loggingtoolbar| image:: image/i_3di_results_analysis_toolbar_logging.png
	:scale: 25%


.. _animationtool:

Animation tool
^^^^^^^^^^^^^^

To understand the behavior of your water system, it is important to get insight in the flow that changes in space and in time. The Animation tool (from :ref:`3di_toolbox_plugin`) allows a spacial view of the results, which can be played back and forth in time. Water level, velocities and discharges can be visualized by this tool.

1) Activate the *Animation* tool by clicking 'Animation on'. A blue progress bar appears at the top of the map-window. Wait till this progress bar has disappeared before you continue. 
2) The first drop-down menu defines the kind of results you will see on the flow lines (e.g. discharge, velocity). 
3) The second drop-down menu defines the kind of results you will see on the nodes (e.g. water level). 
4) The slider scrolls through time and allows you to go back and forth through the results of your simulation. 
5) The timestep of the slider is shown in the box on the right side. Time notation is in DAYS:HOURS:MINUTES from the start of the  simulation. 

.. figure:: image/d_qgisplugin_animation_on.png
    :alt: Animation on bar

When the *Animation* tool is activated, temporary layers are created to show the chosen results:

.. figure:: image/d_qgisplugin_animationlayers.png
    :alt: Animation layers

The thickness of the lines scale with the size of the flow over the lines. The arrows indicate the flow direction. The colors of the nodes, represent different values of the node results.

When groundwater is not used in the model, the layers 'line_results_groundwater' and 'node_results_groundwater' can be turned off. 

An example of the animated flow lines is shown in the figure below. 

.. figure:: image/d_qgisplugin_stroming.png
    :alt: Animation flow

Here, the purple arrows show flow over the 2D domain. The pink arrows show the flow from the 1D domain to the 2D domain or vice versa. In this case this is flow from the terrain into a sewerage manhole. The blue arrows show the flow in the 1D network.

The line results can also be filtered to distinguish between type of flow. To do this, right click on the 'line_results' layer and choose 'Filter' from the drop-down menu. A new window will pop up: 

.. figure:: image/d_qgisplugin_filter.png
    :alt: Filter

Double click on 'type' and click 'Sample' to see which types are available. In the 'filter expression' field you can specify the types of flow lines you want to show, e.g. "type" = '2d'. In the Figure below, an example of filtered 2D flow is shown. 

.. figure:: image/d_qgisplugin_2d_flow.png
    :alt: Filter

.. _waterdepthtool:

Calculate waterdepth and waterlevel maps 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool is location in the Processing Toolbox (from :ref:`3di_toolbox_plugin`). It can be found by clicking 'Processing' in the menubar > 'Toolbox' > '3Di' in the panel > 'Dry weather flow' > 'DWF Calculator'

The tool requires gridadmin.h5 file, the result_3Di.nc file and the DEM file that was used in the model. 

There is a choice between:

- interpolated water depth
- interpolate water level
- non-interpolated water depth
- non-interpolate water level

Because 3Di calculates using the volumes in a quadtree grid, calculating water depth is done by interpolation water levels and subtracting the DEM from this result. In some cases the non-interpolated water level or depth is required, the tool supports those options too. 

.. figure:: image/d_qgisplugin_waterdepthtool.png
	:alt: Screen water depth tool
	
The resulting file can be stored in the temp folder of the Modeller Interface, or stored in a project folder by the user. The resolution of the resulting map is equal to the resolution of the DEM.

Please make sure to use the correct gridadmin file (downloaded with each simulation) and the correct DEM. 

A sample result looks like this:

.. figure:: image/d_qgisplugin_waterdepth_resultsample.png
	:alt: Sample result water depth tool
	
The processing toolbox enables users to generate water depth maps in batch in case this is required. For more information on how this works we refer to the QGIS documentation here: docs.qgis.org/3.16/en/docs/user_manual/processing/modeler.html
