.. _qgisplugin:

QGIS Plugin
================

Introduction
--------------
The 3Di Toolbox is a QGIS plugin for working with 3Di models and netCDF results. For more information see `3Di Toolbox plug-in <https://github.com/nens/threedi-qgis-plugin/wiki>`_. The section below explains the use of the water balance tool. More subjects will be added soon, as this is only one of the features of the 3Di Toolbox.

Water Balance Tool
-------------------------

The water balance tool computes the water balance in a sub-domain of your model. It uses the incoming and outgoing flows in that domain and visualizes the various contributions of the flow in graphs. 

.. _waterbalanceactivate:

Activating the water balance tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The water balance tool is activated by clicking the balance icon in the 3Di-Toolbox bar. 

.. figure:: image/d_qgisplugin_waterbalance1.png 
	:alt: 3Di Toolbox Bar
    
To be able to use the water balance tool, aggregated results are required for a range of variables. This to ensure, that the shown water balance is consistent and complete. In case, the aggregated results are missing or incomplete the following error pops up:

.. figure:: image/d_qgisplugin_wb_error_no_aggregation.png 
	:alt: Error no aggregation settings
    
The aggregation settings can be found and configured in the model table *v2_aggregation_settings*. For more information on the aggregation settings, see :ref:`aggregationnetcdf`. The default settings for the water balance tool are listed below.

.. csv-table:: Aggregation settings for water balance tool
   :file: other/water_balance_aggregation_settings.csv
   :widths: 5, 10, 20, 15, 15, 20
   :header-rows: 1
   

The time step is of course adjustable. For new models, these settings are included in the empty spatialite database (:ref:`empty_database`). For existing models, these settings must be added to the *v2_aggregation_settings* -table. These SQL queries will help you in doing so:

  -- empty v2_aggregation_settings table
  DELETE FROM v2_aggregation_settings;
  
  -- add aggregation settings one by one
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (1, 9999, 'discharge_pump_cum', 'discharge_pump', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (2, 9999, 'lateral_discharge_cum', 'lateral_discharge', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (3, 9999, 'simple_infiltration_cum', 'simple_infiltration', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (4, 9999, 'rain_cum', 'rain', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (5, 9999, 'leakage_cum', 'leakage', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (6, 9999, 'interception_current', 'interception', 'current', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (7, 9999, 'discharge_cum', 'discharge', 'cum', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (8, 9999, 'discharge_cum_neg', 'discharge', 'cum_negative', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (9, 9999, 'discharge_cum_pos', 'discharge', 'cum_positive', 
              'FALSE', 300);
  
  INSERT INTO v2_aggregation_settings(
              id, global_settings_id, var_name, flow_variable, aggregation_method, 
              aggregation_in_space, timestep)
      VALUES (10, 9999, 'volume_current', 'discharge', 'current', 
              'FALSE', 300);

Note that in both cases, in case of a new model or an existing model, you must update the global settings id to the id of the scenario for which you wish to generate aggregated results. For multiple scenarios, you must add these settings multiple times (and update row id's). Also, you may choose to change the aggregation time step, but make sure to use the same time step for all aggregation variables.

Using the water balance tool 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After loading a model and matching results, a polygon needs to be drawn to define the domain of the model for which the water balance needs to be calculated for. This can be done by clicking multiple points on the map of the model. Click *Finalize polygon* to finish the polygon. The graph shows the water balance over time for the selected area. 

By right-clicking the graph, a menu appears in which the range of the x-axis and y-axis can be adjusted. The visible x-axis determines the period over which the water balance is calculated. 

By clicking the button *Hide on map* the polygon over which the water balance is calculated is hidden.

.. figure:: image/d_qgisplugin_wb_draw_polygon.png 
	:alt: Draw polygon to define water balance area
    
Display settings
~~~~~~~~~~~~~~~~~~

The different colours show the different flow types, explained in the legend on the right. By hovering over a flow type in the legend, the corresponding plane lights up in the graph and the corresponding flow lines will be marked with red dotted lines in the map of the model. The different flow types can be activated and deactivated in the graph by clicking the box next to the flow type name. All flow types can be activated or deactivated using the buttons *activate all* and *deactivate all*. 

.. figure:: image/d_qgisplugin_wb_marked_flow.png 
	:alt: Marked flow types
    

In the water balance menu different display options can be chosen. In the first drop-down menu (default = '1d and 2d') you can choose to display only 1D-flow ('1d') or 2D-flow ('2d') or both ('1d and 2d'). In the second drop-down menu (default = 'everything') you can choose to display all flows ('everything') or only the main flows ('main flows'). In the last drop-down menu (default = 'm3/s') you can choose to display flow ('m3/s') or cumulative volume ('m3'). 

Note: the different flow types are 'stacked' in the graph. This means the flow volumes are added to each other when activating multiple flow types. 

Volume change is shown in the graph as well. In this case, the volume change is the result of the total positive and negative flow (inflow and outflow of the area). The volume change is not stacked but shown as a separate line in the graph. 

Total balance 
~~~~~~~~~~~~~~

By clicking the button *Show total balance* a new screen will pop-up, showing the total volume balance over the period set on the x-axis of the graph (shown in title). To adjust this period, close the screen with the bar diagrams, right click on the water balance graph, open the option *x-axis*, activate the option *manual* and set the minimum and maximum time. Then, click again on *Show total balance* to create the water balance diagrams for the new time range. The diagrams can be edited by clicking the graph button at the top. A menu pops-up in which you can choose which diagram you want to edit. Click *OK* to proceed to the *Figure options*-menu. Under the tab *Axes* the ranges and labels for the axes can be set. Under the tab *Curves* the layout of the lines in the graph can be changed. The diagrams can be saved as image by clicking the save-button at the top. 

The top diagram shows the net water balance from all domains. The bottom diagrams show the water balance per domain. 

.. figure:: image/d_qgisplugin_wb_totalbalance_gw.png 
	:alt: Total balance


Explanation of flow types 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


| **2D Surface water domain**
| *2D Boundaries:* Inflow and outflow through 2D boundary conditions
| *2D Flow:* Inflow and outflow in the surface domain crossing the borders of your polygon
| *2D Laterals:* Inflow and outflow through 2D laterals
| *2D: 1D-2D exhange:* Flow exchange between the 2D surface domain and the 1D network elements (e.g. surface runoff from rain into a 1D-channel) within your polygon
| *2D: 1D-2D-flow:* Flow exchange between the 2D surface domain and the 1D network elements crossing the borders of your polygon
| *Infiltration/exfiltration (domain exchange):* Flow exchange between the 2D surface domain and the 2D groundwater domain
| *Rain:* Incoming water from rain
| *Simple infiltration:* Flow out of the 2D domain through simple infiltration

| **2D Groundwater domain**
| *Groundwater flow:* Inflow and outflow through the 2D groundwater domain crossing the borders of your polygon
| *Infiltration/exfiltration (domain exchange):* Flow exchange between the 2D surface domain and the 2D groundwater domain (generally inflowing water through infiltration). 
| *Leakage:* Inflowing water from leakage

| **1D Network domain**
| *1D Boundaries:* Inflow and outflow through 1D boundary conditions
| *1D Flow:* Inflow and outflow in 1D network elements crossing the borders of your polygon
| *1D Laterals:* Inflow and outflow through 1D laterals
| *1D: 1D-2D exhange:* Flow exchange between the 2D surface domain and the 1D network elements (e.g. surface runoff from rain into a 1D-channel) within your polygon
| *1D: 1D-2D-flow:* Flow exchange between the 2D surface domain and the 1D network elements crossing the borders of your polygon
| *Pump:* Inflow and outflow through pumpstations




    


