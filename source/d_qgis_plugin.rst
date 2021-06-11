.. _qgisplugin:

Modeller Interface 
======================

Introduction
--------------
The Modeller Interface (MI) will help you with building 3Di models and analysing results locally. The MI will also assist you in interacting with the 3Di-API and downloading the results from the 3Di calculation servers. The MI is part of QGIS with various pre-installed plugins: the 3Di Toolbox to analyse results, the 3Di API Client to start calculations, download results and some third party plugins. The interface has been cleaned compared to a standard QGIS installation, it shows only relevant buttons for model building and analysing. 

For instructions how to download the Modeller Interface or the plugins see :ref:`plugin_installation`

Overview of the 3Di API client
-----------------------------------------

After installation of the plugin, a panel is available. If you don't see this panel, check the installation instructions.

.. figure:: image/d_qgisplugin_apiclient_overview.png
    :alt: API client overview

The API client panel consists of the following parts:

- Build (not implemented yet)
- Check (not implemented yet, please see the schematisation and raster checker in the 3Di toolbox below)
- Upload 
- Simulate 
- Results

.. _simulate_api_qgis:

Start
^^^^^^^^^^^^^^^

To start simulating you first need to login and choose several options. 
Start by clicking **start**. In the pop-up window choose **Load from Web**


.. figure:: image/d_qgisplugin_apiclient_start.png
    :alt: Load from web
	
Afer providing the Base API URL and your username and password a connection is being made with the API.

The Base API URL is in most cases https://api.3di.live/v3.0/
If you want to connect to our second calculation center in Taiwan, the base API URL is https://api.3di.tw/v3.0/ 

.. figure:: image/d_qgisplugin_apiclient_login.png
    :alt: Load from web
	
Users that have access to run simulations for more than one organisation will get a menu in which they choose the organisation: 

.. figure:: image/d_qgisplugin_apiclient_login_choose_organisation.png
    :alt: Choose organisation

Now choose 'only simulate' (only option available at the moment):

.. figure:: image/d_qgisplugin_apiclient_choose_simulate.png
    :alt: Choose simulate 

	
Choose the model that you like to run simulations on:

.. figure:: image/d_qgisplugin_apiclient_login_choose_model.png
    :alt: Choose simulate 
	
On load of the model the following files are retrieved from the server:

- cells
- breaches

.. figure:: image/d_qgisplugin_load_model_cells_breaches.png
    :alt: Loaded model with Cells and Breach 

Cells represent the computational grid comprised of computational cells. This file can help analyze modelling results when used in an overlay with the model schematization. 

Breaches can be used for breach calculations. The number of the breach as shown in the map canvas is the number required in the wizard. Alternatively, you can also select a breach before starting the wizard. This breach will then be used in the calculation. 

Note: if the files have been downloaded before the Modeller Interface will use the cached version. 
	
	
	
Simulate
^^^^^^^^^^^^^^^

The most used API options are included in the newest version of the plugin. Important consideration is a difference between API v1 and v3 how initial waterlevels, laterals and boundaries are handled. The current status is as follows:

============================= ================= ================= ===============
Forcings                        Spatialite          API             Live site
============================= ================= ================= ===============
Boundary conditions             v1, v3              v3              v1, v3
Initial water level             v1, v3              v1, v3          v3
Laterals  1D and 2D             v1                  v3              -
DWF (inflow)                    v1                  v3              -
============================= ================= ================= ===============

This means that for *boundary conditions* nothing changes between API v1 and v3. Values are taken from the spatialite. The following requirements still hold for the boundary conditions: 

- number of entries have to be exactly the same
- time has to be the same value (e.g. al time series have 0, 10, 20, 40 as time. It is not possible to have a boundary condition with the time as 0,15,20,40)

*Initial water levels* are taken from the spatialite if the users selects this in the wizard, see the section on initial conditions below for a 'how to'. 

*Laterals* are not taken into account when added to the spatialite. The user has to add them to the API call for them to be taken into account. See the section on laterals below for a 'how to'. 

*DWF (inflow)* In API v1 inflow on connection nodes is being calculated based on nr of inhabitants per impervious surface and the mapping to the connection nodes. In API v3 users can calculate the inflow seperately using the dwa calculator tool. The output of this tool is a csv with lateral inflow. This csv can be used in the 3Di API client. In this approach is more transparant and generic usable for different countries.

To start a simulation, click on the **SIMULATE** button. Next, the following window will be shown:

.. figure:: image/d_qgisplugin_apiclient_runningsimulations.png
    :alt: Choose simulate 
	
This window shows an overview of current simulations for the specific organisation. In this panel simulations can be started and also stopped. 
Using load templates enables you to re-use a previously stored template. All specific defined settings are automatically used in the wizard. 

After clicking 'new simulation' the start screen of the wizard is shown:

.. figure:: image/d_qgisplugin_apiclient_start_screen_new_simulation.png
    :alt: Choose new simulation 
	
In this window various options, to be used in the calculation, can be defined. 

**Boundary conditions**
Not configurable yet. Boundary conditions are taken from the spatialite directly.

**Initial conditions**
To define the use of a (previously) saved state or initial waterlevels in 1D, 2D or Ground water.

**Laterals**
To select laterals to use in the model.

**Breaches**
To select a breach to open in the model.

**Precipitation**
To define precipitation in the model.

**Wind**
To define wind in the model.

**Multiple simulations** (becomes available when using either breaches or precipitation)
To define multiple simulations with rainfall or breaches. Useful when simulating multiple events on the same model. 

**Generate saved state after simulation**
To save the end result of the simulation as a saved state.

**Post-processing in Lizard**

This is a feature that is only available for users of organisations that have a Lizard account. It enables you to store the results in the cloud and it triggers automated post-processing. It will generate maps of water depth for each output timestep, a maximum water depth for the whole simulation water levels for each output time step, a maximum water level for the whole simulation, time of arrival, flood hazard rating and damage estimations. The damage estimations are only available in the Netherlands. Contact us at servicedesk@nelen-schuurmans.nl if you like to use this option and don't have access yet.

Works only for users with this module. Enables storing results in the cloud, automated postprocessing of waterdepth and water levels maps, time of arrival, flood hazard rating and damage estimations (only available in the Netherlands at the moment). Contact us at servicedesk@nelen-schuurmans.nl if you like to use this option and don't have access yet.
	
The next step is to name the simulation. You and other users within your organisation will be able to find this simulation and its results based on the name. It can also be used to look up simulations later. 

Adding tags can clarify for other users what your simulation calculated or can be used to assign a simulation a certain projectname or number.

.. figure:: image/d_qgisplugin_apiclient_new_simulation.png
    :alt: Choose new simulation 


The first step in any simulation is choosing the simulation duration:


.. figure:: image/d_qgisplugin_apiclient_choose_duration.png
    :alt: Choose duration
	
The next steps depend on the selection from the initial screen of the wizard. If not checked, these steps will be omitted by the wizard.

**Initial conditions**

Initial conditions either refer to the use of saved state file, or the use of initial water level in 1D, 2D or groundwater (2D). 

.. figure:: image/d_qgisplugin_apiclient_initialconditions_start.png
    :alt: Choose initial conditions
	
1D options:

- Predefined: this refers to the initial water level as defined in the column initial_waterlevel in the connection nodes in the spatialite. 
- Global value: this would be a generic initial waterlevel value in m MSL which is applied in all 1D nodes of the model.

2D Surface Water options:

- Raster: this refers to the initial water level raster as uploaded with the model to the model databank.
- Aggregation settings: This can min, max or average 
- Global value: this would be a generic initial waterlevel value in m MSL which is applied in all 2D nodes of the model.


2D Groundwater options:

- Raster: This refers to the initial water level raster as uploaded with the model to the model databank.
- Global value: This would be a generic initial waterlevel value in m MSL which is applied in all 2D ground water nodes of the model.

**Laterals**

Laterals can be uploaded using .csv format for either 1D or 2D. 

.. figure:: image/d_qgisplugin_apiclient_laterals_start.png
    :alt: Choose laterals 

The CSV file format is generated by a right-mouse click on table: v2_1d_lateral. Then choose export --> save features as --> 

Select csv as outputformat. Choose a filename and location to store and click OK. the file should like like this:

.. figure:: image/d_qgisplugin_apiclient_laterals_export_csv_example.png
    :alt: Export laterals as csv


*Important note: Units in the CSV are seconds (for timesteps) and m3/s (for the flows).*

	
**Breaches**

A breach can be selected using the menu below:

.. figure:: image/d_qgisplugin_apiclient_breaches.png
    :alt: Breaches 

When choosing the model to calculate in a breaches file was downloaded from the server. The number of the breach as shown in the map canvas is the number required in the wizard. Alternatively, you can also select a breach before starting the wizard. This breach will then be used in the calculation. 


**Precipitation**

To define precipitation in the model. 

There are several options to define a precipitation event for your simulation. In the drop-down menu, one can choose Constant, Custom, Design and Radar events. For all events an offset can be defined. The offset is the duration between start simulation and the start of the rainfall event. 

.. figure:: image/d_qgisplugin_choose_type_of_precipitation.png
    :alt: Choose type of precipitation

When choosing a Constant type of precipitation, the stop after and rain intensity (in mm/h) must also be defined. The stop after is the duration between the start of the simulation and the end of the rain event. The rain intensity is uniform and constant in the given timeframe. The rain intensity preview provides the rain intensity throughout the simulation in the form of a histogram. 

.. figure:: image/d_qgisplugin_apiclient_rain_constant.png
    :alt: Choose constant rain

When choosing the option Custom, the event is defined in a CSV-file. The format is in minutes, and the rainfall in mm for that time step. Please keep in mind that the duration of the rain in the custom format cannot exceed the duration of the simulation. The interpolate option will gradually change the rain intensity throughout a time series. Without the interpolate function the rain intensity will stay constant within a time step and will make an abrupt transition to the next time step.

.. figure:: image/d_qgisplugin_apiclient_rain_custom.png
    :alt: Choose custom rain

.. figure:: image/d_qgisplugin_apiclient_csv_format.png
    :alt: Example CSV

When choosing the option Design, a design number between 1 and 16 must be filled in. These numbers correlate to predetermined rain events, with differing return periods, that fall homogeneous over the entire model. Numbers 1 to 10 originate from `RIONED <https://www.riool.net/bui01-bui10>`_ and are heterogeneous in time. Numbers 11 to 16 have a constant rain intensity: 

Rain 11 statistically occurs once every 100 years. The duration of this event is 1 hour with a constant rain intensity of 70 mm/h. (T= 100.0 year, V=70 mm, Standard rain event (local) from Delta Programme 2019).

Rain 12 statistically occurs once every 250 years. The duration of this event is 1 hour with a constant rain intensity of 90 mm/h. (T=250.0 year, V=90 mm, Standard rain event (local) from Delta Programme 2019).

Rain 13 statistically occurs once every 1000 years. The duration of this event is 2 hours, with a constant rain intensity of 80 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (local) from Delta Programme 2019).

Rain 14 statistically occurs once every 100 years. The duration of this event is 48 hours, with a constant rain intensity of 2.5 mm/h. (T=100.0 year, V=120 mm, Standard rain event (regional) from Delta Programme 2019).

Rain 15 statistically occurs once every 250 years. The duration of this event is 48 hours, with a constant rain intensity of 2.7 mm/h. (T=250.0 year, V=130 mm, Standard rain event (regional) from Delta Programme 2019).

Rain 16 statistically occurs once every 1000 years. The duration of this event is 48 hours, with a constant rain intensity of 3.4 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (regional) from Delta Programme 2019).


These so-called design rain events are time series, which are traditionally used to test the functioning of a sewer system in the Netherlands.

.. figure:: image/d_qgisplugin_apiclient_rain_design.png
    :alt: Choose design rain

Radar is only available in the Netherlands and uses historical rainfall data that is based on radar rain images. Providing temporally and spatially varying rain information. The Dutch `Nationale Regenradar <https://nationaleregenradar.nl/>`_ is available for all Dutch applications. On request, the information from other radars can be made available to 3Di as well.

.. figure:: image/d_qgisplugin_apiclient_rain_radar.png
    :alt: Choose radar rain


**Multiple simulations** (becomes available when using either breaches or precipitation)
To define multiple simulations with rainfall or breaches. Useful when simulating multiple events on the same model.


.. _wind_apiclient:


**Wind**

To define wind in the model. Wind in 3Di applies to 2D surface water. Read more about :ref:`wind_effects` here.

You can choose between a Constant or a Custom type of wind. For both events an offset and a drag coefficient can be defined. The offset (start after) is the duration between the start of the simulation and the start of the wind event. The drag coefficient has a default value of 0,005. By increasing the drag coefficient, you increase the influence of the wind. 

When choosing a Constant wind event, the stop after, wind speed and direction must also be defined. The stop after is the duration between the start of the simulation and the end of the wind event. 
The (meteorological) wind direction is defined as the direction from which the wind originates, measured in degrees clockwise from due north. Therefore, wind blowing toward the south has a direction of 0 degrees. You can either use the wind rose to depict which way the wind is blowing, or enter the direction manually. 

.. figure:: image/d_qgisplugin_apiclient_wind_constant.png
    :alt: Choose Constant wind

When choosing a Custom wind, the CSV format is minutes, wind speed in m/s and wind direction, both for that time step. The interpolate options will gradually change the wind speed or wind direction throughout a time series. Without the interpolate functions the wind speed and wind direction will stay constant within the time steps and will make an abrupt transition to the next time step.

.. figure:: image/d_qgisplugin_apiclient_wind_custom.png
    :alt: Choose Custom wind

.. figure:: image/d_qgisplugin_apiclient_wind_csv.png
    :alt: Example CSV wind

After choosing all the settings check the overview, press Next and Add to Queue. The simulation will start up when there is a session available on the servers within your organisation.

.. figure:: image/d_qgisplugin_apiclient_preview_simulation.png
    :alt: Overview new simulation
	
**Post processing in Lizard**

Post processing in Lizard is only available for users that have this module.

.. figure:: image/d_qgisplugin_apiclient_postprocessing_lizard.png
    :alt: Example CSV
	
*Basic processed results*

Stores the 3Di output files in the Lizard platform:

- Result NetCDF (containing actual values)
- Aggregate NetCDF (availability and content dependent on user settings. required for water balance tool in Modeller Interface)
- Grid administration (gridadmin.h5 file. required to load NetCDF results in Modeller Interface)
- Calculation core logging (A zip containing logfiles)

As a service, the following maps are available in Lizard:

- water depth maps per output time step
- maximum water depth map
- flood hazard rating
- rise velocity
- water level
- max water level
- max velocity
- rainfall 

All maps can be downloaded as GTiff, either via the interface demo.lizard.net or via the lizard API.

*Arrival time map*

When this is checked a map with arrival time is being calculated showing the time of arrival of water per pixel in hours. 

*Damage estimation*

Only available in the Netherlands: automated estimate of damage as a result of flooding. Takes into account water depth and duration of flood. Result is the following damage maps:

- Water depth (WSS)
- Damage (direct)
- Damage (indirect)
- Total damage

And a damage summary in csv format. For more information check the documentation here: https://docs.3di.lizard.net/d_results_from_lizard.html

	
Results
^^^^^^^^^^^^^^^
	
After a simulation is finished the results will be stored on our servers for 7 days. The files can be download via the Results button.

.. figure:: image/d_qgisplugin_apiclient_download_panel.png
    :alt: Example CSV

After download the NetCDF can be loaded together with the spatialite using the 3Di Toolbox as described below.


    
Overview of the 3Di Toolbox
---------------------------

After installation of the plugin a toolbar is added to the QGIS interface. The different tools are explained below. 
In the Modeller Interface the 3Di toolbar is directly available.

.. figure:: image/d_qgispluging_toolbox_overview.png
    :alt: Plugin overview

1) Clear cache 
2) :ref:`load_model_results`
3) :ref:`3ditoolbox`
4) :ref:`graph_tool` 
5) :ref:`sideviewtool`
6) :ref:`statisticaltool`
7) :ref:`waterbalance`
8) :ref:`animationtool`

    
.. _load_model_results:
    
Load 3Di model and results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A model schematisation can be loaded by clicking the database icon with the blue plus-sign (number 2 in the Figure above). A new window will be opened. 

1) Under 'Model' you need to load the Sqlite containing your model 
In case you are loading you model schemetisation for checking and editing your Sqlite, step 2 is not necessary.  
2) Under 'Results' you can load the NetCDF containing your simulation results (usually named *results_3di.nc*). It is important to select a result file that belongs to the model you used for your simulation (i.e. your NetCDF must be generated by the sqlite you loaded. Do not use an old or changed Sqlite). 
3) After the loading finished, click 'Close' to return to the QGIS interface


.. figure:: image/d_qgisplugin_select_model_results.png
    :alt: Load 3Di model and results



.. _view_model_results:
    
View and edit 3Di model a schematisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After loading your 3Di model schematization, there are several ways to inspect your model. We have added the following features to assist you in viewing and editing the model schematization:

- Multiple styles per layer
- Drop down menus
- Immediate validation
- Automated field fill
- Multi-line fields for time series 

.. _multiplestyles:


**Multiple styles per layer**


The multiple styles per layer can help you when analyzing your model. The different styles depict aspects of the layer you might be interested in, without cluttering your schematization with too much information at once. 

To switch between stylings: 1) Right click the layer you are interested in. 2) Hold your mouse over styles and the multiple styles will be shown. 3) Click on the style you want to use. The style with the dot next to it is the active style. The figure below shows an example for selecting a style. 

.. figure:: image/d_qgisplugin_multiple_stylings_drop_down_menu.png
    :alt: Selecting the drop down menu for multiple styles
	
Some styles add a label to the object. Keep in mind when using these stylings that the labels only become visible when a certain zoom level is applied. 

The default style depicts the locations of the objects in the layer. The other stylings are explained briefly below:


**1D and 2D Boundary conditions:**

=================  =====================================================================================
Style              Description  
=================  =====================================================================================
Timeseries label   The ‘timeseries label’ style adds a label to the default style, depicting the boundary

                   type, and the smallest (min:) and largest (max:) value in the time series.
=================  =====================================================================================



**1D and 2D Lateral:**

=================  =====================================================================================
Style              Description  
=================  =====================================================================================
Timeseries label   The ‘timeseries label’ style adds a label to the default style, depicting the smallest

                   (min:) and largest (max:) value in the time series.
=================  =====================================================================================

When looking at these timeseries keep in mind that the values get rounded off to 2 decimal places, which can make it seem like the values are zero (0.00) when in fact they were not.

**Connection Nodes:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Id                   The ‘id’ style adds a label to the default style, depicting the id of the connection

                     node. This can be useful when connecting other elements to existing connection 

                     nodes.
Initial water level  The ‘initial water level’ style is a categorized styling that represents the connection

                     nodes without an initial water level in the default style and the connection nodes

                     with an initial water level as blue outlined dots with labels that depict the initial 

                     water levels (in m MSL).
Storage area         The ‘storage area’ style depict the storage area of the connection nodes as a ratio 

                     style with a label. The extent of the schematization corresponds to the size of the 

                     storage area of the connection node. The label depicts the storage area. 
===================  ===================================================================================

 
**Manholes:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style is a categorized styling depicting the locations and indicators of

                     the manholes. The different manhole indicators have different zoom levels in order

                     to avoid clutter. When zooming into a certain area the local manholes will appear.
Levels               The ‘levels’ style adds a label to the default style, depicting the surface level (s:),

                     the drain level (d:) and the bottom level (b:).
Calculation type     The `’calculation type’ <https://docs.3di.lizard.net/b_1dtypes.html#types-of-1d-elements-calculation-types>`_ style is a categorized styling that depicts the way 3Di  

                     calculated the interaction between a manhole and the 2D computation domain.
Code                 The ‘code’ style adds a label to the default style, depicting the code of the manhole.
===================  =================================================================================== 


**Cross section location (view):**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Levels               The ‘levels’ style adds a label to the default style, depicting the bank level (bank:),

                     the reference level (ref:) and the difference between the two (diff:).
Cross section        The ‘cross-section’ style adds a label depicting the shape, the maximum width (w:) and  

                     the maximum height (h:) of the cross-section definition. The width (in m) is the 

                     diameter in the case of a circle and the max width in the case of a tabulated profile.
===================  =================================================================================== 


**Pumpstation view:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style depicts the locations of the pumpstation view and the drawing direction

                     of this view with arrows pointing toward the end node. 
Capacity             The icon size corresponds with the pump capacity. The label depicts the capacity of the

                     pumpstation (in L/s).
Levels               The ‘levels’ style adds a label to the default style, depicting the upper stop level (up:),  

                     the start level (st:) and the lower stop level (lo:).
===================  =================================================================================== 


**Pumpstation point view:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Capacity             The extent of the schematization corresponds to the capacity of the pump. The label

                     depicts the capacity of the pumpstation (in L/s).
Levels               The ‘levels’ style adds a label to the default style, depicting the upper stop level (up:),  

                     the start level (st:) and the lower stop level (lo:).
===================  =================================================================================== 

**Channel:**

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Calculation type             The `’calculation type’ <https://docs.3di.lizard.net/b_1dtypes.html#types-of-1d-elements-calculation-types>`_ style is a categorized styling that depicts the way    

                             3Di calculated  the interaction between a channel and the 2D  

                             computation domain.
Drawing direction            The ‘drawing direction’ styling depicts the drawing direction of the 

                             channel, with the arrows pointing toward the end connection node. Flow    

                             in the drawing direction has  positive values, flow in the opposite  

                             direction has negative values.
Code                         The ‘code’ style adds a label to the default style, depicting the code of  

                             the channel.   
Calculation point distance   The ‘calculation point distance’ styling depicts the approximate location   

                             of the calculation points. These calculation points are where the 

                             interaction with the 2D domain can take place. 
===========================  ============================================================================

**Weir:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The 'default' style depicts the locations of the weirs. When a weir is closed in 

                     one direction a perpendicular dash and arrow are added to the line.
Levels               The ‘levels’ style adds a label to the default style, depicting the crest level   

                     of a weir (in m MSL).
Drawing direction    The ‘drawing direction’ styling depicts the drawing direction of the weir,  

                     with the arrows  pointing toward the end connection node. Flow in the drawing   

                     direction has positive values, flow in the opposite direction has negative values.
Width                The line width corresponds to the (minimum) width of the weir. The label shows  

                     the shape and (minimum) width of the cross section in meters. 
===================  =================================================================================== 

**Culvert view:**

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Levels and flow direction    The ‘levels and flow direction’ style adds arrows and a label to the default

                             style. The  arrows point in the expected flow direction (high to low 

                             invert level) and the label shows the invert level for the start point (s:)  
 
                             and end point (e:) of the culvert.
Calculation type             The `’calculation type’ <https://docs.3di.lizard.net/b_1dtypes.html#types-of-1d-elements-calculation-types>`_ style is a categorized styling that depicts the way  

                             3Di calculated the interaction between a culvert and the 2D computation 

                             domain.
Drawing direction            The ‘drawing direction’ styling depicts the drawing direction of the culvert, 

                             with the arrows pointing toward the end connection node. Flow in the  

                             drawing direction has positive values, flow in the opposite direction 

                             has negative values.
Diameter                     The line width is based on the average of the (max.) width and (max.) height  

                             of the cross section. The label shows the cross section shape and the 

                             (max.) width and (max.) height (in mm). 
===========================  ============================================================================

**Orifice:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The 'default' style depicts the locations of the orifices. When a orifice is closed  

                     in one direction a perpendicular dash and arrow are added to the line.
Levels               The ‘levels’ style adds a label to the default style, depicting the crest level of an  

                     orifice (in m MSL).
Drawing direction    The ‘drawing direction’ styling depicts the drawing direction of the orifice, with  

                     the arrows pointing toward the end connection node. Flow in the drawing  

                     direction has positive values, flow in the opposite direction has negative values.
Diameter             The line width is based on the average of the (max.) width and (max.) height of  

                     the cross section. The label shows the cross section shape and the (max.) width 

                     and (max.) height (in mm). 
===================  =================================================================================== 


**Pipe:**

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Default                      The ‘default’ style is a categorized styling depicting the locations and  

                             sewerage types of the pipes.
Levels and flow direction    The ‘levels and flow direction’ style adds arrows and a label to the default 

                             style. The arrows point in the expected flow direction (high to low   

                             invert level) and the label shows the invert level for the start point (s:) 

                             and end point (e:)  of the pipe.
Calculation type             The `’calculation type’ <https://docs.3di.lizard.net/b_1dtypes.html#types-of-1d-elements-calculation-types>`_ style is a categorized styling that depicts the way 3Di   

                             calculated the interaction between a pipe and the 2D computation domain.
Drawing direction            The ‘drawing direction’ styling depicts the drawing direction of the pipe,

                             with the arrows pointing toward the end connection node. Flow in the  

                             drawing direction has positive values, flow in the opposite direction 

                             has negative values.
Diameter                     The line width is based on the average of the (max.) width and (max.) height   

                             of the cross section. The label shows the cross section shape and  

                             the (max.) width and (max.) height (in mm). 
Code                         The ‘code’ style adds a label to the default style, depicting the code of

                             the pipe. This code is bases on the two manhole codes which enclose 

                             the pipe.
===========================  ============================================================================

**Obstacle:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Levels               The ‘levels’ style adds a label to the default style, depicting the crest level of an obstacle. 

                     (in m MSL).
===================  =================================================================================== 

**Levee:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Levels               The ‘levels’ style adds a label to the default style, depicting the crest level of an Levee. 

                     (in m MSL).
===================  =================================================================================== 

**Grid refinement:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style depicts the locations of the grid refinements. The dashed   

                     pattern is based on the refinement level. The number of dots represents the 

                     refinement level.
Refinement levels    The ‘refinement level’ style adds a label to the default style, depicting 

                     the refinement level.
===================  =================================================================================== 


**Grid refinement area:**

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style depicts the locations of the grid refinement areas. The hash  

                     spacing and the dashed pattern of outline are based on the refinement level. The  

                     hash spacing represents the size of the calculation cells based on the refinement 

                     level and the number of dots in the polygon outline represents the refinement 

                     level. 
Refinement levels    The ‘refinement level’ style adds a label to the default style, depicting 

                     the refinement level.
===================  =================================================================================== 

**Impervious surface:**

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Surface inclination          The ‘surface inclination’ style is a categorized styling depicting the  

                             locations and the surface inclinations of the impervious surfaces.  
Area and dry weather flow    The ‘area dry weather flow’ style depicts the amount of dry weather flow 

                             in L/d for each impervious surface, calculated 

                             as dry_weather_flow * nr_inhabitants. 
===========================  ============================================================================

**Surface:**

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Area and dry weather flow    The ‘area dry weather flow’ style depicts the amount of dry weather flow  

                             in L/d for each surface, calculated as dry_weather_flow * nr_inhabitants.
===========================  ============================================================================


Drop down menus
^^^^^^^^^^^^^^^

We have added drop down menus for multiple value attributes in tables. This to assist you in selecting the proper values. The figure below shows an example for selecting a shape for a cross section definition. 

.. figure:: image/d_qgisplugin_vm_dropdown.png
    :width: 25pc
    :height: 25pc
    :alt: Drop down menu example

Immediate validation
^^^^^^^^^^^^^^^^^^^^^

For obligatory fields, we have added non-binding constraints. In fields that are correctly, green checks will appear next to the fields after there are filled. An orange cross will appear in case, the field is mandatory, but not filled. 

.. figure:: image/d_qgisplugin_vm_validation.png
    :width: 25pc
    :height: 25pc
    :alt: Validation example


Multi-line fields for time series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multi-line fields are designed for editing time series. In the example of the Figure, the time serie of a discharge boundary condition is edited.

.. figure:: image/d_qgisplugin_vm_timeseries.png
    :width: 50pc
    :height: 25pc
    :alt: Timeseries example

Automated field fill 
^^^^^^^^^^^^^^^^^^^^

Some fields are automatically filled to assist in making your model schematisation. Here is an overview of the fields that are filled automatically:

- The cross-section location fetches the corresponding channel-id automatically
- Channels and culverts automatically fill connection node ids when drawing between nodes with `snapping <https://docs.qgis.org/3.4/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#setting-the-snapping-tolerance-and-search-radius>`_.
- Invert level from culverts. If invert level is empty culverts assumes the invert level based on manhole bottom_level 

On top of that, some default values for some of the mandatory fields are set. This helps you build models faster. The following default values will be set, in case they are left blank. The listed values are defaults, so please change them if required for your specific application.

You need to set your QGIS locale to 'English UnitedStates' in order for this functionality to work properly. See the :ref:`Before you begin > Software <software>` section for instructions.

**v2_global_settings:**

============================= ===============
Column name						Default value 
============================= ===============
dem_obstacle_detection				0
dist_calc_points					10000
flooding_threshold					0.001
frict_avg							0
frict_type						2: Manning
guess_dams							0
numerical_settings_id 				1
start_date						today
start_time						today 00:00
table_step_size  					0.01
============================= ===============

**v2_aggregation_settings:**

============================= =========================
Column name						Default value 
============================= =========================
aggregation_in_space			False
============================= =========================


**v2_2d_lateral:**

============================= ===============
Column name						Default value 
============================= ===============
type  							1: surface
============================= ===============

**v2_connection_nodes:**

============================= ===============
Column name						Default value 
============================= ===============
code  							new
============================= ===============


**v2_channel:**

============================= ============================================================
Column name						Default value 
============================= ============================================================
display_name					new
code							new
zoom_category					5
connection_node_start_id		id of connection node on start point (when snapped)
connection_node_end_id			id of connection node on end point (when snapped)
============================= ============================================================


**v2_culvert:**

=============================== ============================================================
Column name						Default value 
=============================== ============================================================
display_name					new
code							new
calculation_type				101: isolated
dist_calc_points				10000
invert_level_start_point		bottom_level of manhole when snapped to one
invert_level_end_point			bottom_level of manhole when snapped to one
frict_type: 					2: Manning
discharge_coefficient_positive	0.8
discharge_coefficient_negative	0.8
zoom_category					4
connection_node_start_id		id of connection node on start point (when snapped)
connection_node_end_id			id of connection node on end point (when snapped)
=============================== ============================================================


**v2_pipe:**

============================= ===============
Column name						Default value 
============================= ===============
display_name					new
code							new
calculation_type				1: isolated
dist_calc_points				10000
friction_type					2: Manning
zoom_category					3
============================= ===============

**v2_simple_infiltration:**

============================= ===============
Column name						Default value 
============================= ===============
display_name  					new
infiltration_surface_option		0
============================= ===============

**v2_weir:**

=============================== ==============================
Column name						Default value 
=============================== ==============================
display_name					new
code							new
crest_type						4: short crested
discharge_coefficient_positive	0.8
discharge_coefficient_negative	0.8
friction_value					0.02
friction_type					2: manning
zoom_category					3
external						True
=============================== ==============================


**v2_orifice:**

=============================== ==============================
Column name						Default value 
=============================== ==============================
display_name					new
code							new
crest_type						4: short crested
discharge_coefficient_positive	0.8
discharge_coefficient_negative	0.8
friction_value					0.02
friction_type					2: Manning
zoom_category					3
=============================== ==============================


**v2_manhole:**

============================= ===============
Column name						Default value 
============================= ===============
display_name					new
code							new
zoom_category					1
manhole_indicator				0: inspection
============================= ===============


**v2_pumpstation:**

============================= ===========================================================================
Column name						Default value 
============================= ===========================================================================
display_name					new
code							new
type 							1: pump behaviour is based on water levels on the suction side
zoom_category					3
============================= ===========================================================================


**v2_cross_section_definition:**

============================= ===============
Column name						Default value 
============================= ===============
code  							new
============================= ===============

**v2_cross_section_location:**

============================= ===============
Column name						Default value 
============================= ===============
code  							new
friction_type					2
============================= ===============


**v2_obstacle:**

============================= ===============
Column name						Default value 
============================= ===============
code  							new
============================= ===============


**v2_levee:**

============================= ===============
Column name						Default value 
============================= ===============
code  							new
============================= ===============


**v2_grid_refinement:**

============================= ===============
Column name						Default value 
============================= ===============
display_name					new
code							new
refinement_level				1
============================= ===============


**v2_grid_refinement_area:**

============================= ===============
Column name						Default value 
============================= ===============
display_name					new
code							new
refinement_level				1
============================= ===============


**v2_numerical_settings:**

==================================== =================
Column name								Default value 
==================================== =================
limiter_grad_1d							1
limiter_grad_2d							0
limiter_slope_crossectional_area_2d		0
limiter_slope_friction_2d				0
convergence_cg							0.000000001
convergence_eps							0.00001
use_of_cg								20
max_nonlin_iterations					20
precon_cg								1
integration_method						0
flow_direction_threshold				0.000001
general_numerical_threshold				0.00000001
thin_water_layer_definition				0.05
minimum_friction_velocity				0.05
minimum_surface_area					0.00000001
cfl_strictness_factor_1d				1
cfl_strictness_factor_2d				1
frict_shallow_water_correction  		0
pump_implicit_ratio						1
preissmann_slot							0
==================================== =================


**v2_impervious_surface:**

============================= =========================
Column name						Default value 
============================= =========================
display_name					new
code							new
area							area based on geometry
zoom_category					0
============================= =========================


**v2_surface:**

============================= =========================
Column name						Default value 
============================= =========================
display_name					new
code							new
area							area based on geometry
zoom_category					0
============================= =========================


**Notables:**
The 3Di database has some fields that are not in use. To clean the view, we have hidden them in the form view. They are still available in the database. Moreover, we have made some field names easier to read: for example, prefixes are excluded (e.g. \pipe_).

.. _3ditoolbox:

Toolbox for working with 3Di models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The 3Di toolbox is actived by clicking the toolbox icon in the 3Di-Toolbox bar. 

.. figure:: image/d_qgisplugin_activate_toolbox.png 
    :alt: 3Di Toolbox Bar


After clicking the toolbox icon, a new window is opened. Click the arrow next to the *Tools* icon to open the toolbox and view the different tools that are available. 

.. figure:: image/d_qgisplugin_toolbox_window.png 
    :alt: Toolbox Window


.. _rasterchecker:

Raster checker
^^^^^^^^^^^^^^
The *Raster checker* is launched with the QGIS 3.4.5 version of the Plugin. This tool checks the rasters for your 3Di model schematisation. The tool verifies for example:

- The correct nodata value

- Consistent projection between rasters

- Alignment of all rasters

There are up to 18 checks performed. It is strongly recommended to run this tool before updating the model repository. The model generation will be unsuccessfull, when it encounters any inconsistencies in your rasters. 

To use the *Raster checker*, set up a connection with the SQlite of your model. 

1) Open the *Data Source Manager* under the drop down menu *Layer* on top of the screen. 
2) Go to *SpatiaLite* and click *New*. Browse to the location of your model Sqlite and open it. 
3) Now you can close the *Data Source Manager* window.

.. figure:: image/d_qgisplugin_load_sqlite.png
    :alt: Data Source Manager


4) The *Raster checker* can be accessed by opening the Toolbox. 
5) The *Raster checker* can be found under *Step 1 - Check data*. By double clicking *raster_checker.py* the *Raster checker* is opened in a seperate window. 

.. figure:: image/d_qgisplugin_activate_rasterchecker.png
    :alt: Data Source Manager

6) Under *Model schematisation database* you can choose the spatialite of your model. 
7) Click *OK* to start the *raster checker*. When the tool is finished the following message pops-up:

.. figure:: image/d_qgisplugin_rasterchecker_done.png 
    :alt: Raster checker Done

8) The log-file of the raster checker can be found at the same location as the location of the SQlite. The log-file can be opened with a text editor such as Notepad. The log-file looks similar to:

.. figure:: image/d_qgisplugin_rasterchecker_log_header.png
    :alt: Rasterchecker Done

Here, one can also find the overview of the 18 checks that are performed. 

9) The performed checks are numbered 1 to 18. This number is called a *check_id*. 
10) Under sub-heading *Found following raster references*, there is a list with the rasters used in your model schematisation.

Further down in the log-file, the outcome of the *raster checker* for each raster is shown.

.. figure:: image/d_qgisplugin_rasterchecker_log_checks.png
    :alt: Rasterchecker Feedback

11) The first column, named *level*, shows the importance of the notification (info, warning or error). Errors need to be solved.
12) The second column, named *setting_id*, refers to the id of the row in the v2_global_settings table of the sqlite, where the raster reference can be found. 
13) The third column contains the *check_id*. 
14) The fourth column is the *feedback*, it contains the outcome of the specific verification check. 
15) If one of your rasters is not aligned with the DEM (bathymetry file), check_id 18 will give an error. Make sure all your rasters have the same extent and and have nodata pixels at the same location. 

.. _schematisationchecker:

Schematisation checker
^^^^^^^^^^^^^^^^^^^^^^^^^

The *schematization checker* analyses your 3Di model database (.sqlite file) for completeness and consistency between tables. With the checker you can make sure most database errors are found before sending the model to the 3Di INP-server for model generation. 

In order to use the *schematization checker* follow these steps:

1. Start *QGIS*
2. Add a connection to the model database (*Layer* -> *Data Source Manager*, Select *SpatiaLite* on the left and create a *'New’* connection or connect to an existing connection)
3. Open the *schematization checker* by opening the *Toolbox* in the 3Di Plugin, select *Step 1: check data*, select *schematisation_checker.py*
4. Select the SpatiaLite connection of the model database and the location where to store the output of the schematisation checker. Click *run* to run the schematisation checker. Click *open* to open the output.

The output is a comma seperated value file, which can be opened in, for example, Excel. It contains 6 columns: *id, table, column, value, description and check*:

- **id**: identification number of the row where a check encounters an error.
- **table**: the table in which the error occurs.
- **column**: the column which contains the error.
- **value**: the current value in the cell
- **description**: description of the error
- **check**: the type of check that found the error, described below

**What is checked?**

There are currently different general checks applied on all tables and columns of the model database. These checks are:

- TypeCheck
- NotNullCheck
- ForeignKeyCheck
- EnumCheck
- UniqueCheck
- GeometryCheck
- GeometryTypeCheck

Apart from the general checks on the database data and structure there are more 3Di specific checks:

- BankLevelCheck
- CrossSectionShapeCheck
- TimeSeriesCheck
- Use0DFlowCheck

**TypeCheck** Every cell in every table will be checked if the type of the entered value is correct. A values in cell is expected to be a(n): 
- integer (-4, 0,1,2, etc…)
- real (3.6, -5.2)
- text
- varchar (text of limited length)
- geometry (point, linestring or polygon)
- bool (bolean, true or false)
- datetime (2019-07-02 14:27+02:00)

**EnumCheck** Some cells expect specific values. For example, the type of a boundary condition is either 1, 2, 3 or 5 (respectively water level, velocity, discharge or Sommerfeld). Any value other than the enumerated values will result in an EnumCheck error.

**NotNullCheck** If a cell is *NULL* it id empty. For some cells this is allowed, but others cells are obliged to contain a value. If this obligation is not met, a NotNullCheck error is given.

n.b. An empty text or varchar does not equal NULL.

**ForeignKeyCheck** Many tables contain foreign key columns which refer to other tables. An example is the column *connection_node_start_id* in the table *v2_channel*. This column refers to the column *id* in the table *v2_connection_node*. If a channel is entered with *connection_node_start_id = 1*, there should be an entry in the table *v2_connection_nodes* with *id = 1*. If this is not the case a ForeignKeyCheck error will be given.

**UniqueCheck** Some values have to be unique. An example is the name column in *v2_global_settings*. If multiple rows are entered with the same name, a UniqueCheck error will be given.

**GeometryCheck** If an entered geometry is invalid the GeometryCheck error will be returned. The most occurring reason for invalid geometries is self-intersection of polygons.

**GeometryTypeCheck** This check makes sure the geometry type (point, linestring or polygon) is consistent with the expected geometry type.

**BankLevelCheck** Check if the row *bank_level* of *v2_cross_section_locations* table is not NULL, when the corresponding channel is of the type *connected* or *double_connected*.

**CrossSectionShapeCheck** Each type of cross-section shape requires certain input. This check verifies if all cross-section shapes are well posed: 

- *Rectangle*: A width is required, a height is optional. The dimensions should be positive decimal numbers.
- *Circle*: Only a "width" is required. This is diameter of the circle and should be a positive decimal number.
- *Egg*: Only a "width" is required. The height is 1.5 times the width. This value should be a positive decimal number.
- *Tabulated rectangle or trapezium*: A list of widths and heights are required. The lists should contain only positive decimal numbers seperated by spaces and contain the same amount of values. The first value of *height* should always be 0. The height list should be increasing. In case the width is set to 0 m at the heighest increment, the cross-section is closed. 

**TimeseriesCheck** This check verifies if time series are correctly defined. It checks whether the time steps in that table are all the same. 

**Use0DFlowCheck** If 0D flow is configured in the global settings table, there should be at least 1 (impervious) surface defined in the model.

.. _importsufhyd:

Import from SUF-HYD
^^^^^^^^^^^^^^^^^^^

SUF-HYD is a Dutch standardized format for transferring data of sewerage systems for hydraulic analyses. This tool allows an automated import of the sewerage data in the 3Di model database. 

Before you can use the tool, make sure you have :ref:`downloaded an empty spatialite <empty_database>`. The SUF-HYD data will be imported to this spatialite. Save the Sqlite to a location fo choice on your computer.

The tool can be accessed by :ref:`activating the toolbox <3ditoolbox>` and double clicking 'import_sufhyd.py' under 'Step 2 - Convert and import data' 

1) First, make sure you have a connection with the sqlite you want to import your data to (see the first 3 steps under :ref:`rasterchecker`). 
2) After opening the tool, select a SUF-HYD file and the database (sqlite) to import the data into and click 'OK'

The data from the SUF-HYD will be loaded into the sqlite. A log file of this process can be found at the same location as the SUF-HYD file. This file has the name of your SUF-HYD with a *.hyd.log* extension. You can open this log file with a text editor such as Notepad. This log-file gives a summary of data errors and warnings. 

The following objects are imported:

* Manhole (``*KNP``)
    * The number of inhabitants will be added as an *Impervious surface*.

Note: the shape of the manhole is refered as 'rnd' = round, 'sqr' = square and 'rect' = rectangle

*    Pipe (``*LEI``)

    *    The number of inhabitants will be added as *Impervious surface*
	
*    Pump station (``*GEM``)

    *    If multiple stages are defined, this will be transformed into seperate pumpstations. Up to 10 stages are supported
	
*    Weir (``*OVS``)

    *    Flow direction (str_rch) is translated into discharge coefficients with a value of 0
    *    An end node with boundary condition is not automatically added.
	
*    Orifice (``*DRL``)

    *    Flow direction (str_rch) is translated into discharge coefficients with a value of 0
	
*    Boundary (``*UIT``)

    *    The water level will be the average definition (bws_gem). If not present the summer water level is used and otherwise the winter water level.
	
*    Extra manhole storage (``*BOP``)

    *    The defined storage area is added to a manhole on the bottomlevel of the manhole. The defined bottom_level of the storage (niv_001) is ignored.
    *    Only one storage area is supported
	
*    *Drainage area/ Impervious surface (``*AFV``)*

*    Linkage nodes (``*KPG``)

    *    The 'fictive' linkages (with typ_gkn == 01) are ignored, only real nodes are combined.
    *    The second node (ide_kn2) is removed. Impervious surfaces and pipes linked to the removed node are redirected to the first node. Extra manhole storage will be lost.

.. _addleveebreaches:

Add levee breaches
^^^^^^^^^^^^^^^^^^

Levee breaches can be created in 3Di-models that contain a connected *v2_channel* 
(*calculation_type* = 102) and a *v2_levee*-structure. For more information on the 
theory behind levee breaches in 3Di, see :ref:`breaches`.

Before adding levee breaches, please make sure that the data in *v2_levee*-table is 
correctly filled out. For simulating breaches, 3Di requires the *crest_level* of the 
levee in m MSL **(a)**, the *material* of the levee **(b)** and the *max_breach_depth* 
relative to the crest level in meters **(c)**.

.. image:: image/d_qgisplugin_breach_info_v2_levee_table.png

**IMPORTANT WARNING:** adding levee breaches should generally be the last step in 
the modelling process. When connected points belonging to a channel are moved 
across a levee in order to simulate a breach, they are assigned a *calculation_pnt_id*
that refers to the id number of the old calculation point. Any changes that affect 
the amount of calculation/connected points or the location of calculation points 
(like adding a new *v2_channel*) will lead to changes in the id numbers of the 
calculation points, and hence, to moved connected points referring to the wrong 
calculation points.

To add levee breaches to your model using the 3Di toolbox, please follow the steps below:

1. Set up a connection with the SQLite or PostgreSQL database of your model (see: :ref:`rasterchecker`).
2. Click on the 3Di toolbox and select *Step 3 - Modify schematization*.
3. Choose *Predict calc points* and select your SQLite or PostgreSQL model from the list. Two virtual layers will then be added called *v2_connected_pnt* and *v2_calculation_point*.

.. image:: image/d_qgisplugin_leveebreaches_predict_calc_points.png

4. Select the *v2_connected_pnt*-layer in the QGIS *Layers Panel* **(a)** and click on *Select Feature(s)* in the QGIS *Attributes Toolbar* **(b)**. 

.. image:: image/d_qgisplugin_select_cnn_pnt_layer.png

5. Now select the connected points of the channel on which you want to force a levee breach. Selected points will turn yellow.

.. image:: image/d_qgisplugin_select_levee_points.png

6. Next, double-click on *Create breach locations* and a new window will pop-up.

.. image:: image/d_qgisplugin_create_breach_locs.png

7. In the first box **(a)** the *v2_connected_pnt*-layer that was created in Step 3 is auto-selected from a drop-down menu. If it isn't in the list something went wrong in the previous steps.

.. image:: image/d_qgisplugin_create_breach_locs_window.png

8. In the second box **(b)** you enter a search distance in meters. This is the distance perpendicular to the channel that is searched for a *v2_levee*.
9. In the third box **(c)** you enter a number that controls at what distance away from the *v2_levee* the new calculation point is created. **IMPORTANT:** The levee breach will only work if the new calculation point is located in a different calculation cell from that of the original calculation point. Hence, is advised to select a *distance_to_levee* that is larger than the size of the calculation cells in which the levee breach occurs.
10. The *use only selected features* tick box **(d)** should be checked if you want the tool to create breach locations only for the points you selected in the *v2_connected_pnt*-table.
11. The *dry-run* tick box **(e)** can be checked if you first want to create a temporary layer of the moved connected points. This can be useful to compare the original locations with the new locations.
12. When the *auto commit changes* tick box **(f)** is checked, all changes made in the *v2_connected_pnt*-layer are immediately saved. Since these changes can't be reverted and they can be easily saved with the click of one button, we recommended leaving this box unchecked.
13. Click on the *OK*-button **(g)** to create the breach locations. Note that you will still need to save the *v2_connected_pnt*-layer before changes are committed to the model. An example of (not yet committed) connected points that have been moved across a levee to simulate a levee breach, can be seen in the figure below.

.. image:: image/d_qgisplugin_moved_cnn_points.png

Viewing and Analysing 3Di results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have various tools developped to assist users in analysing a viewing their results. In this section, some of these are described.

.. _waterbalance:

The water balance tool
^^^^^^^^^^^^^^^^^^^^^^

The water balance tool computes the water balance in a sub-domain of your model. It uses the incoming and outgoing flows in that domain and visualizes the various contributions of the flow in graphs. The development was an initiative of Deltares and jointly developed with Nelen & Schuurmans. The water balance tool is co-funded by the Top Sector Water (Ministry of Economic Affairs)

This is the only results tool that requeres the generation of specific results. Therefore, we also discuss the input requirements of this tool.

.. _waterbalanceactivate:

**Settings to use the water balance tool**


To be able to use the water balance tool, aggregated results are required for a range of variables. This to ensure, that the shown water balance is consistent and complete. 
    
The aggregation settings can be found and configured in the spatialite-table *v2_aggregation_settings*. For more information on the aggregation settings, see :ref:`aggregationnetcdf`. The default settings for the water balance tool are listed below.

.. csv-table:: Aggregation settings for water balance tool
   :file: other/water_balance_aggregation_settings.csv
   :widths: 5, 10, 20, 15, 15, 20
   :header-rows: 1
   

Of course, the time step, cq, the period over which is aggregated, is adjustable. For new models, these settings are included in the empty spatialite database (:ref:`empty_database`). For existing models, these settings must be added to the *v2_aggregation_settings* -table. These SQL queries will help you in doing so:

Empty v2_aggregation_settings table::

    DELETE FROM v2_aggregation_settings;
  
Add aggregation settings for all rows in the global settings table::

    INSERT INTO v2_aggregation_settings(global_settings_id, var_name, flow_variable, aggregation_method, aggregation_in_space, timestep)
    SELECT id, 'pump_discharge_cum', 'pump_discharge', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'lateral_discharge_cum', 'lateral_discharge', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'simple_infiltration_cum', 'simple_infiltration', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'rain_cum', 'rain', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'leakage_cum', 'leakage', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'interception_current', 'interception', 'current', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'discharge_cum', 'discharge', 'cum', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'discharge_cum_neg', 'discharge', 'cum_negative', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'discharge_cum_pos', 'discharge', 'cum_positive', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'volume_current', 'volume', 'current', 0, output_time_step  FROM v2_global_settings
    UNION
    SELECT id, 'qsss_cum_pos', 'surface_source_sink_discharge', 'cum_positive', 0, output_time_step FROM v2_global_settings
    UNION
    SELECT id, 'qsss_cum_neg', 'surface_source_sink_discharge', 'cum_negative', 0, output_time_step FROM v2_global_settings
    ;
	
Note that the above query sets the aggregation time step equal to the output time step. If you want to use different aggregation time step, make sure to use the same time step for all aggregation variables in order to enable the use of the water balance tool.


	UPDATE v2_aggregation_settings SET time_step = [fill in a number];
	
**Using the water balance tool**

In a few steps, one can get insight in the water balance of their own system.

1) Define a spatialite and the results that are to be analysed by loading your model and results using the 'Select 3Di results'-button in the toolbox.  

2) The water balance tool is activated by clicking the balance icon in the 3Di-Toolbox bar. 

.. figure:: image/d_qgisplugin_waterbalance1.png 
    :alt: 3Di Toolbox Bar
    
In case, the aggregated results are missing or incomplete the following error pops up:

.. figure:: image/d_qgisplugin_wb_error_no_aggregation.png 
    :alt: Error no aggregation settings
    
    
3) Draw a polygon to define the domain of the model for the area of interest. This can be done by clicking at multiple locations within the model domain. Click *Finalize polygon* to finish the polygon. The graph shows the water balance over time for the selected area. 

4) By right-clicking the graph, a menu appears in which the range of the x-axis and y-axis can be adjusted. The visible x-axis determines the period over which the water balance is calculated. 

5) The button *Hide on map* the polygon over which the water balance is calculated is hidden.

.. figure:: image/d_qgisplugin_wb_draw_polygon.png 
    :alt: Draw polygon to define water balance area
    

    
**Display settings**


6) The different colours show the different flow types, explained in the legend on the right. 
7) By hovering over a flow type in the legend, the corresponding plane lights up in the graph and the corresponding flow lines will be marked with red dotted lines in the map of the model. 
8) The different flow types can be activated and deactivated in the graph by clicking the box next to the flow type name. 
9) All flow types can be activated or deactivated using the buttons *activate all* and *deactivate all*. 
10) In the water balance menu different display options can be chosen. In the first drop-down menu (default = '1d and 2d') you can choose to display only 1D-flow ('1d') or 2D-flow ('2d') or both ('1d and 2d'). 
11) In the second drop-down menu (default = 'everything') you can choose to display all flows ('everything') or only the main flows ('main flows').
12) In the last drop-down menu (default = 'm3/s') you can choose to display flow ('m3/s') or cumulative volume ('m3'). 

Note: the different flow types are 'stacked' in the graph. This means the flow volumes are added to each other when activating multiple flow types. 

Volume change is shown in the graph as well. In this case, the volume change is the result of the total positive and negative flow (inflow and outflow of the area). The volume change is not stacked but shown as a separate line in the graph. 

.. figure:: image/d_qgisplugin_wb_marked_flow.png 
    :alt: Marked flow types
    
**Total balance**


13) By clicking the button *Show total balance* a new screen will pop-up, showing the total volume balance over the period set on the x-axis of the graph (shown in title). 
14) To adjust this period, close the screen with the bar diagrams, right click on the water balance graph, open the option *x-axis*, activate the option *manual* and set the minimum and maximum time. Then, click again on *Show total balance* to create the water balance diagrams for the new time range. 

.. figure:: image/d_qgisplugin_showbalance_axis.png
    :alt: Adjust axis range

The top diagram shows the net water balance from all domains. The bottom diagrams show the water balance per domain. 

.. figure:: image/d_qgisplugin_wb_totalbalance_new_qgis3.png
    :alt: Total balance

It is possible to save the graphs as an image or export the water balance data to a CSV-file.

15) To save an image of the graphs, right-click on one of the graphs. Choose 'Export' in the menu that opens. A new window opens.
16) In the first box you can choose the items you want to export. Click 'Entire Scene' to export all graphs or choose one of the 'Plot'-items to export a graph seperately. 
17) In the second box you can choose the export format. Choose 'Image file' for an image and choose 'CSV from plot data' to export the actual data. 
18) Click 'Export' to generate your figure. 

.. figure:: image/d_qgisplugin_export_wb_graph.png
    :alt: Export waterbalance graph


**Explanation of flow types**


In the overviews the flow is split in several domains. These distinguish themselves based on how the flow is computed. Therefore, you will find the 2D flow, groundwater and the 1D flow domain. Below a more detailed doscription of the various components.

*2D Surface water domain*


- *2D Boundary flow:* Inflow and outflow through 2D boundaries
- *2D Flow:* Inflow and outflow in the surface domain crossing the borders of the polygon
- *Lateral flow to 2D:* Sources or sinks based on 2D laterals
- *2D: 2D flow to 1D:* Flow exchange between the 2D surface domain and the 1D network elements within your polygon (for example, surface run-off from rain into a 1D-channel or water that overflows the banks in your channel). 
- *2D: 2D flow to 1D (domain exchange):* Flow exchange between the 2D surface domain and the 1D network elements crossing the borders of your polygon
- *In/exfiltration (domain exchange):* Flow exchange between the 2D surface domain and the 2D groundwater domain
- *Rain:* Incoming water from rain
- *Constant infiltration:* Flow out of the 2D domain based on simple infiltration
- *Interception:* Intercepted volume


*2D Groundwater domain*

- *Groundwater flow:* Inflow and outflow through the 2D groundwater domain crossing the borders of your polygon
- *In/exfiltration (domain exchange):* Flow exchange between the 2D surface domain and the 2D groundwater domain (generally inflowing water through infiltration). 
- *Leakage:* sources or sinks based on leakage


*1D Network domain*


- *0D Rainfall runoff on 1D:* Inflow volume from 0D module
- *1D Boundary flow:* Inflow and outflow over a 1D boundary
- *1D Flow:* Inflow and outflow in 1D network elements crossing the borders of your polygon
- *1D Laterals:* Sources and sinks based on 1D laterals
- *1D: 2D flow to 1D:* Flow exchange between the 2D surface domain and the 1D network elements (e.g. surface runoff from rain into a 1D-channel) within your polygon
- *1D: 2D flow to 1D (domain exchange)* Flow exchange between the 2D surface domain and the 1D network elements crossing the borders of your polygon
- *Pump:* pumped volume

.. _graph_tool:

Graphs of time series
^^^^^^^^^^^^^^^^^^^^^


The graph tool can be used for visualizing model results over time. for example, it allows users to quickly plot the water level variation of a specific node or the discharge variation of a flow link (e.g. a channel or pipe) over time. The information is quickly at hand in just a few steps. All the variable that are saved in the NetCDF are available. They are structured on flow lines and nodes, depending on how they are defined in the computational core. An overview of the variables in the NetCDF can be found in the section :ref:`3dinetcdf`. 

The following steps are required to view your results:
1) First, make sure you have loaded a model schematisation and the corresponding results (NetCDF) into your QGIS project using :ref:`load_model_results`.
2) Activate the graph tool by clicking the *graph* button in the 3Di toolbar. A new panel with the title *3Di result plots* is launched in your QGIS-project. 
3) In the layer overview window go to the layer group *results: results_3di* and activate the 'flow-lines' layer or the 'nodes' layer: 

.. figure:: image/d_qgisplugin_graphtool_activateresults.png
    :alt: Results layers

4) Activate the *Select features* tool in QGIS, by clicking this logo in the *Attributes toolbar* from QGIS: 

.. figure:: image/d_qgisplugin_graphtool_selectiontool.png
    :alt: Selection tool

5) Select the specific nodes or flow lines. You can select multiple nodes or flow lines simultaneously, but for speed purposes it is advised to limit it to a maximum of 20 features.

6) Click the *Add* button in the *3Di results plot* panel. The results for the selected features are loaded from the NetCDF and visualized over time in the graph.

.. figure:: image/d_qgisplugin_graphtool_graphwindow.png
    :alt: Results graph example

7) You can switch between node and flow line results by activating the tab *Q-graph* for flow lines and *H-graph* for nodes. 
8) In the drop-down menu on the right side of the panel you can choose the type of results you want to see. The y-axis shows the corresponding range and unit of the results type. The x-axis shows the time. *Note: the time is often displayed in kilo-seconds (ks). 1 ks = 1000 seconds ≈ 16.7 minutes.*
9) Below the drop-down menu there is an overview of the nodes/flow lines you selected, with the id of the node/flow line and the type. In this overview you can activate or deactivate the results in the graph by clicking the checkbox next to it. A feature can be deleted by first selecting it in this overview and then clicking the *Delete* button below the overview. 
10) The data from the graph can also be exported to an image or csv-file. Right-click the the graph figure and choose 'Export' from the drop-down menu. A new window pops-up in which you can choose the output format and settings. 

.. _animationtool:

Animation tool
^^^^^^^^^^^^^^

To understand the behaviour of your water system, it is important to get insight in the flow that changes in space and in time. The *Animation* tool allows a spacial view of the results, which can be played back and forth in time. Water level, velocities and discharges can be visualized by this tool.

1) Activate the *Animation* tool by clicking 'Animation on'. A blue progress bar appears at the top of the map-window. Wait till this progess bar has disappeared before you continue. 
2) The first drop-down menu defines the kind of results you will see on the flow lines (e.g. discharge, velocity). 
3) The second drop-down menudefines the kind of results you will see on the nodes (e.g. water level). 
4) The slider scrolls through time and allows you to go back and forth through the results of your simulation. 
5) The timestep of the slider is shown in the box on the right side. Time notation is in DAYS:HOURS:MINUTES from the start of the  simulation. 

.. figure:: image/d_qgisplugin_animation_on.png
    :alt: Animation on bar

When the *Animation* tool is activated, temporary layers are created to show the chosen results:

.. figure:: image/d_qgisplugin_animationlayers.png
    :alt: Animation layers

The thickness of the lines scale with the the size of the flow over the lines. The arrows indicate the flow direction. The colours of the nodes, represent different values of the node results.

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


.. _sideviewtool:

Side view tool
^^^^^^^^^^^^^^

.. figure:: image/d_qgisplugin_sideviewtool.png
    :alt: Sideview tool

1) Activate the *Show side view* tool by clicking the map icon in the 3Di toolbar. 
2) A new panel opens. Click ‘Choose sideview trajectory’. 
3) A new layer is created and is directly shown with yellow lines. These yellow lines are all possibile trajectories for a sideview. Choose a starting point by clicking on a yellow line (point A). By clicking on a second yellow line (point B), the end of your trajectory is defined. The tool automatically detects the shortest route from point A to B. The trajectory is shown as a red line on the map. The sideview of this trajectory is shown in the graph. 
4) A trajectory can contain multiple points. Just click on the next point on the yellow line (point C) and the sideview of the shortest route from point B to C is automatically added to the graph. 
5) The graph contains the following elements: 

    a. The pipe/channel dimensions, represented by the grey area.
    b. Dimensions and locations of manholes.
    c. Green line: surface levels of manholes
    d. Green dotted line: drain levels of manholes
    e. Blue line: the water level.

6) The slider in the *Animation* tool can be used to scroll through time. 


.. _statisticaltool:

Statistical tool
^^^^^^^^^^^^^^^^^^

The statistical tool can ben used to calculate sewerage statistics from 3Di results. To use it, first make sure you load a 3Di model together with the results you want to calculate the statistics from. 

.. figure:: image/d_qgisplugin_statisticaltool.png
	:alt: Statistical Tool

1) Activate the Statistical Tool by clicking the statistics icon in the 3Di toolbar. The tool will immediately start calculating the statistics and a progressbar at the top of the map window shows the progress. 
2) When the calculations are finished, new layers are added to the QGIS project. These layers contain statistics from the 3Di results on pipes, manholes, pumps and weirs. The layers are explained below. 

*Note: DWF = Dry Weather Flow, CSF = Combined Sewer Flow, SWF = Storm Water Flow*

**Metadata_statistics**

- *table:* Refers to the table, see below 
- *field:* Refers to the fieldname, see below
- *from_agg:* If set to 0 the statistics are derived using actual values on the output time step. This is the case if no aggregation value is available. Not using an aggregation netcdf makes the statistics derived using this tool less accurate
- *input_param:* For advanced users: Refers to the input parameter from the NetCDF
- *timestep:* When not derived from aggregation netcdf it is important what timestep has been used. It gives an indication of the accuracy of the value.

**Pipes**

- *Discharge (max):* Maximum discharge which occurs during the simulation
- *Velocity (max):* Maximum velocity which occurs during the simulation 
- *Gradient (max):* Maximum gradient of the waterlevel in the pipe 
- *Velocity (end):* Velocity in the pipe occuring at the last timestep
- *Velocity DWF and CSF (end)*: Velocity at the last timestep for DWF and CSF pipes
- *Velocity SWF (end):* Velocity at the last timestep for SWF pipes

**Manholes**

- *Fill level (max):* Percentage of manhole that is filled based on maximum water level occuring during the simulation
- *Fill level DWF and CSF (end):* Percentage of manhole that is filled based on water level at the last time step of the simulation for DWF and CSF manholes. 
- *Fill level SWF (max):* Percentage of manhole that is filled based on water level at the last time step of the simulation for SWF manholes. 
- *Duration of water on street:* The total amount of time the water level in the manhole is higher than the surface level of the manhole during the simulation. Note that the unit is in hours, so 0.25 hr means 15 minutes. 
- *Waterdepth (max):* The max water depth above the manhole surface level that is occuring during the simulation. Values greater than 0 mean there is water on the street. 
- *Waterdepth DWF and CSF (max):* The max water depth above the manhole surface level that is occuring during the simulation for DWF and CSF manholes. Values greater than 0 mean there is water on the street. 
- *Waterdepth SWF (max):* The max water depth above the manhole surface level that is occuring during the simulation for SWF manholes. Values greater than 0 mean there is water on the street. 


**Pumps**

- *Percentage of pump capacity in use (max):* The percentage of the total pump capacity that is used at the moment the pump is pumping at max. 
- *Percentage of pump capacity in use (end):* The percentage of the total pump capacity that is used at the last time step of the simulation. 
- *Total pumped volume:* The total volume that is pumped over the entire simulation. 
- *Pump duration on  max capacity:* The total amount of time the pump is pumping at its max capacity. 

**Weirs**

- *Head difference (max):* The maximum difference in head between the two sides of the weir. 
- *Overflow volume (cum):* The total cumulative volume that has flown over the weir. 

.. _waterdepthtool:

Calculate waterdepth and waterlevel maps 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The tool is location in the Processing Toolbox. It can be found via the menu, click 'Processing', then 'Toolbox'. The following window will appear. If there are a lot of tools you can use the text '3Di' in the search bar.

.. figure:: image/d_qgisplugin_location_waterdepthtool.png
	:alt: Location water depth tool
	
The tool requires gridadmin.h5 file, the result_3Di.nc file and the DEM file that was used in the model. 

There is a choice between:

- interpolated water depth
- interpolate water level
- non-interpolated water depth
- non-interpolate water level

Because 3Di calculates using the volumes in a quadtree grid, calculating water depth is done by interpolation water levels and substracting the DEM from this result. In some cases the non-interpolated water level or depth is required, the tool supports those options too. 

.. figure:: image/d_qgisplugin_waterdepthtool.png
	:alt: Screen water depth tool
	
The resulting file can be stored in the temp folder of the Modeller Interface, or stored in a project folder by the user. The resolution of the resulting map is equatl to the resolution of the DEM.

Please make sure to use the correct gridadmin file (downloaded with each simulation) and the correct DEM. 

A sample result looks like this:

.. figure:: image/d_qgisplugin_waterdepth_resultsample.png
	:alt: Sample result water depth tool
	
The processing toolbox enables users to generate water depth maps in batch in case this is required. For more information on how this works we refer to the QGIS documentation here: docs.qgis.org/3.16/en/docs/user_manual/processing/modeler.html




