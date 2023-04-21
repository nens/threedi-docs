.. _simulate_w_live_site:


Start or follow a session
---------------------------

.. _start_a_new_session:

Start a new session
^^^^^^^^^^^^^^^^^^^^

* Select the **New session** tab. 
* Select your company in the **Billing goes to:** drop down menu. 
* Select the model you want to start.

A new session will be started. During the start up of the model tips for use of the site will be shown. It may take several minutes to load the model. Actual loading time is dependent on model size, calculation grid and table step size.

.. figure:: image/d2.4_start_session.png 
    :alt: Start new session

    Loading screen.

*For each organization, the number of simultaneous sessions is limited according to the agreement (contract). If the limit is reached, the message "Your organization is already running X sessions" will show. The amount of server time used is subtracted from the time available within the agreement.*


.. _follow_a_session:

Following a session
^^^^^^^^^^^^^^^^^^^^

Through the tab **Follow session** an active session of your organization can be followed. Select an active simulation and press **follow**. The number of followers of a session is unlimited. To leave the session, go to the **user menu** under the user icon (top right) and press **Leave session**. 


.. _editing_with_live_site:

Making edits
------------

In the live site, you can temporarily adjust values. For example, you can change the pump capacity and weir height, and you can close 1D elements such as channels, pipes, weirs, culverts and orifices.
You can also perform a DEM edit via the raster edit tool. 


The buttons at the mid left of the screen are used to interactively adjust the forcing of the model. Two of these buttons can be used to alter the model:
- Discharge tool
- Pump tool
- The raster edit tool


Adding a discharge point
^^^^^^^^^^^^^^^^^^^^^^^^^^
With the discharge tool a constant source of water will be added to your model.
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. 
The water that is added to the 2D surface of your model and will flow in constantly from that point.


Adding a pump station
^^^^^^^^^^^^^^^^^^^^^^
With the pump tool a constant sink will be added to your model. 
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. The water that is taken out of the model will not flow back into the model and is considered a loss. 

DEM edit/ Raster edit
^^^^^^^^^^^^^^^^^^^^^^^^

A DEM edit is a tool in the live site, it allows to adjust the height of the bathymetry. This can be done at any time during the simulation. 

.. figure:: image/d_dem_edits.png
   :alt: Dem edits

To edit the bathymetry of the model, make sure the DEM-layer is activated. This can be done via the maplayers menu and clicking on the 'Digital Elevation Model' layer. The elevation edit is in absolute numbers in m MSL. If you are not sure about the elevation to use, use the side view tool to check the height in the model. In some cases it might be useful to also turn on the model grid layer.

After entering a value, click 'Draw on map' and start clicking. 

.. figure:: image/d_draw_dem_polygon.png
   :alt: Performing a dem edit
   
After finalising the polygon by clicking again on the first point, click on confirm. The Edit then shows in the applied items section

.. figure:: image/d_confirm_dem_polygon.png
   :alt: Confirming a dem edit

The result can be checked using the 'Side view' tool.

Please note that if there is water on the 2D while editing, and the edit lowers the surface the calculation core needs a few time steps to get to a new water level in the DEM edit location. 


.. _simulation_interventions:

Simulation interventions
---------------------------

The buttons at the mid left of the screen are used to interactively adjust the forcing of the model:

- add a :ref:`discharge_tool` (2D)
- add a :ref:`pump_tool` (2D)
- add :ref:`rain_tool`
- add :ref:`wind_tool`

The functioning of these buttons is described in the following sections.

NOTE: The result of forcing water is not visible until the simulation is running.

.. _discharge_tool:

Discharge point
^^^^^^^^^^^^^^^^^^^^

With the **Discharge tool** a constant source of water can be added to the model. Select the icon and change the amount of water you want to apply. In the dropdown menu you can change the unit. You can also change the duration of the discharge. Click **PLACE ON MAP** and click a location on the map that should be the source. The water will start flowing from this location over the 2D domain.
When you press the **Play** button the intervention will become active.

.. figure:: image/d3.6_discharge.png
    :alt: Discharge tool

.. _pump_tool:

Pumping point
^^^^^^^^^^^^^^^^^^^^

With the **Pump tool** a constant sink of water can be added to the model. Select the icon and change the amount of water you want to pump out of the model. In the dropdown menu you can change the unit. You can also change the duration of the pumping. Click **PLACE ON MAP** and click a location on the map that should be the pump. The water will be pumped out from the 2D domain from this location (1D pumps should be added in the schematisation). The water that is taken out of the model will not flow back into the model and is considered a loss.
When you press the **Play** button the intervention will become active.


.. _rain_tool:

Rainfall
^^^^^^^^^^^^^^^^^^^^

Through the **Rain tool** icon, rainfall can be added to the model. The following Type's are available:

* **Constant**: a homogeneous event in both space and time across the entire model range.
* **Radar**: use historical rainfall data (only available in the Netherlands).
* **Design**: use a design event. This event is homogeneous over the entire model area and heterogeneous in time.

These three options for adding rainfall all cover the entire model area.

When choosing a **Constant** type of precipitation, the rain intensity (in mm/h) and duration of the rain must be defined. The rain intensity is uniform and constant in the given time frame.

The option **Radar** is only available in the Netherlands and uses historical rainfall data that is based on radar rain images. Providing temporally and spatially varying rain information. The Dutch Nationale Regenradar is available for all Dutch organisations that have the NRR module. On request, the information from other radars can be made available to 3Di as well. In order to apply this type of rain a historical time frame needs to be set. 

When choosing the option **Design**, a number between 3 and 16 must be selected. These numbers correlate to predetermined rain events, with differing return periods, that fall homogeneous over the entire model. Numbers 3 to 10 originate from `RIONED <https://www.riool.net/bui01-bui10>`_ and are heterogeneous in time. Numbers 11 to 16 have a constant rain intensity. When selecting a design rain the total rainfall and duration information will change in the tab.

For a more detailed description on rainfall, see: :ref:`rain`.

When the rainfall is active a cloud icon appears on the top right of the screen. Information about the rainfall event can be accessed by keeping the rainfall tab open. Active and past (inactive) events are shown in this tab 

.. figure:: image/d3.2_rainfall.png
    :alt: Rainfall event


.. _wind_tool:

Wind
^^^^^^^^^^^^^^^^^^^^

A compass card appears after clicking on the **Wind tool** icon. By clicking in the compass card a homogeneous wind field with a specific direction and speed can be set up for the whole model (v2). This direction can also be filled in numerically. The strength and duration of the wind can be changed. Because the wind is constant for the whole model you only need to press **CREATE**. When the wind is active a wind icon appears on the top right of the screen.

.. figure:: image/d3.6_wind.png
    :alt: Wind speed, direction and duration

Breaches 
^^^^^^^^^^^^^^^^^^^^

If breach locations are predefined in the model, these can be activated as follows:

#. Check whether breaches are turned on in the map layer menu. 
#. Zoom in to a breach location
#. By clicking a breach location a pop-up screen with settings for this breach appears.


.. figure:: image/d3.8_breach_location.png
    :alt: Breach location

To show the flow rate over time, select a breach location using the point information tool. 

.. _analyzing_livesite_running:

Analyzing results while scenario is running
---------------------------------------------

.. todo:
    nog kijken welke van de kopjes ik wil houden. Misschien zit er overlap in. misschien niet. ook checken of het up to date is.

Real time results during a simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the **selection tool** (top left) is switched on. With it you can click anywhere on the map to visualize the time series at that location. Default water depth and water level will be shown. If the model contains groundwater that graph is also shown. 

The time series can all be downloaded in CSV format. The points over time that are shown are the points calculated by the 3Di calculation core and are independent from the output time step that the modeller has set.

.. figure:: image/d3.1_point_location.png
    :alt: Point selection

Also the height of a cross section can be displayed with the **Line-selection tool**, together with the water level in that transect. Click the start and end point in any place on the map for the cross section (within the 2D model domain).

.. figure:: image/d3.1_side_view.png
    :alt: Cross section selection

The side view shows the elevation in green and the water in blue. By hovering over the graph with the mouse, exact values can be seen. Keeping this graph open during a flood event will show you how the water level is slowly rising. Note that in the example also groundwater is available in the model indicating an extra blue line. 


1D network
^^^^^^^^^^

Channels and structures can be included as 1D elements in the model. The channels show the direction of flow with the help of moving points. The direction and speed are based on the flow velocity in the channel. The different sizes of the points are based on thhe discharge. The results (discharge, water level, waterdepth and flow velocity) are available at the structures by selecting them.

Discharge and velocity are in the lines:

.. figure:: image/d3.7_1d_network.png
    :alt: 1D network


And water level and water depth are in the nodes:

.. figure:: image/d3.8_1d_network.png
    :alt: 1D network


It is also possible to adapt some properties of structures during the calculation. This includes among others the closing of a culvert or increasing the pumping capacity.


.. _timeoutlivesite:

Quitting the simulation
-----------------------

In the **menu menu** you can select **quitting the simulation**, this ends the use of calculation time. If this option is not used the session remains active. One of the following scenario's might apply:

- time out after being inactive is set to 30 minute for a running simulation
- time out after being inactive is set to 5 minute for a paused simulation
- leaving the session via a tab will close the simulation after 30 minutes

You can:

- **Quit, don't store results**
- **Quit, store results**


.. _store_results_live_site:

Store results
--------------

Results can be stored by clicking **User menu**, then clicking **Quit Simulation** and then **Quit, Store Results**. There are two options:

- Download results directly via the browser
- Store them to the Lizard platform (see https://docs.lizard.net/a_lizard.html) 

Stored (raw) results can also be downloaded using the"3Di Models and Simulations" in the 3Di Modeller Interface, see: :ref:`mi_download_res`. Note that these raw results are only available for 7 days.

The options in Lizard storage are as follows:

- raw data and logging
- basic processed results
- arrival time map
- damage estimation (NL only)

The **Basic processed results** option includes the following derivations from simulation results for Lizard users:

.. figure:: image/d3.9_store_results.png
    :alt: Storing results

- Water level - temporal
- Water depth - temporal
- Maximum flow velocity
- Maximum rate of rise
- Maximum water depth
- Flood hazard rating

The **Damage estimation** option uses a module called *WaterSchadeSchatter* (currently only available in The Netherlands)
which provides two products derived from the maximum water depth.

- Damage estimation map
- Damage estimation table
