.. _3di_live_interactive_tools:

Interactive tools
=================

In the live site, you can temporarily adjust values. For example, you can change the pump capacity and weir height, and you can close 1D elements such as channels, pipes, weirs, culverts and orifices.
You can also perform a DEM edit via the raster edit tool. 


The buttons at the mid left of the screen are used to interactively adjust the forcing of the model. Two of these buttons can be used to alter the model:
- Discharge tool
- Pump tool
- The raster edit tool

.. note::
	
	Editing of structures or DEM can only be done after *pausing* a simulation.

.. _discharge_tool_guide:

Discharge tool
^^^^^^^^^^^^^^^

With the **Discharge tool** a constant source of water can be added to the model. Select the icon and change the amount of water you want to apply. In the dropdown menu you can change the unit. You can also change the duration of the discharge. Click **PLACE ON MAP** and click a location on the map that should be the source. The water will start flowing from this location over the 2D domain. It is the modelling equivalent of a 2D lateral. 
When you press the **Play** button, the intervention will become active.

.. figure:: image/d3.6_discharge.png
	:alt: Discharge tool

	Discharge tool.

If you made a mistake when creating discharge, you can **delete** before you activate it. After you have started your simulation, you can **stop** the discharge while its status is 'active', when your simulation is paused. The discharge will then only have had an effect during it's runtime and not for the previously set duration time.

.. _pump_tool_guide:

Pumping tool
^^^^^^^^^^^^^

With the **Pump tool**, a constant sink of water can be added to the model. Select the icon and change the amount of water you want to pump out of the model. In the dropdown menu you can change the unit. You can also change the duration of the pumping. Click **PLACE ON MAP** and click a location on the map that should be the pump. The water will be pumped out from the 2D domain from this location (1D pumps should be added in the schematisation).
The water that is taken out of the model will not flow back into the model and is considered a loss. It is the modelling equivalent of a negative 2D lateral. 
When you press the **Play** button the intervention will become active.

If you made a mistake when creating a pump you can **delete** before you activate it. After you have started your simulation, you can **stop** the pump while its status is 'active', when your simulation is paused. The pump will then only have had an effect during its runtime and not for the previously set duration time. 


.. _rain_tool_guide:

Rain tool
^^^^^^^^^^

Through the **Rain tool** icon, rainfall can be added to the model. The following rain event types are available:

* **Constant**: a homogeneous event in both space and time across the entire model range.
* **Radar**: use historical rainfall data (only available in the Netherlands).
* **Design**: use a design event. This event is homogeneous over the entire model area and heterogeneous in time.

These three options for adding rainfall all cover the entire model area.

When choosing a **Constant** type of precipitation, the rain intensity (in mm/h) and duration of the rain must be defined. The rain intensity is uniform and constant in the given time frame.

The option **Radar** is currently only available in the Netherlands and uses historical rainfall data that is based on radar rain images. Providing temporally and spatially varying rain information. The Dutch Nationale Regenradar is available for all Dutch applications for organisations that have this module in their contract. On request, the information from other radars (worldwide) can be made available to 3Di as well. In order to apply this type of rain a historical time frame needs to be set. 

When choosing the option **Design**, a number between 3 and 16 must be selected. These numbers correlate to predetermined rain events, with differing return periods, that fall homogeneous over the entire model. Numbers 3 to 10 originate from `RIONED <https://www.riool.net/bui01-bui10>`_ and are heterogeneous in time. Numbers 11 to 16 have a constant rain intensity. When selecting a design rain the total rainfall and duration information will change in the tab.

For a more detailed description on rainfall, see: :ref:`rain`.

When the rainfall is active a cloud icon appears on the top right of the screen. Information about the rainfall event can be accessed by keeping the rainfall tab open. Active and past (inactive) events are shown in this tab 

.. figure:: image/d3.2_rainfall.png
	:alt: Rainfall event

	Rainfall tool.


.. _wind_tool_guide:

Wind tool
^^^^^^^^^^^

A compass card appears after clicking on the **Wind tool** icon. By clicking in the compass card a homogeneous wind field with a specific direction and speed can be set up for the whole model in the 2D domain. This direction can also be filled in numerically. The strength and duration of the wind can be changed. Because the wind is constant for the whole model you only need to press **CREATE**. When the wind is active a wind icon appears on the top right of the screen.

.. figure:: image/d3.6_wind.png
	:alt: Wind speed, direction and duration

	Wind tool.

Once you have created a wind event, you can press **EDIT**. This lets you either **STOP WIND** or after altering the fields **UPDATE EXISTING WIND**.

.. _raster_edit_tool:

Raster-edit tool
^^^^^^^^^^^^^^^^^^

The **Raster-edit tool** lets you edit the elevation raster (DEM) by pressing **DRAW ON MAP** and drawing a polygon and setting a constant elevation level (in mMSL) for that polygon. After you have drawn your polygon, you can **CONFIRM** the polygon and your raster edit will be active for the rest of the simulation. You can also **EDIT DRAWING** and change the shape of your polygon.  

.. figure:: image/d3.6_raster_edits.png
	:alt: Raster edits

	Raster edit tool.



.. _flood_barrier_tool:

Flood barrier tool
^^^^^^^^^^^^^^^^^^^^

A flood barrier can prevent a certain area from flooding. To see the flood barriers tool in action, you can watch the `Floodbarriers preview <https://www.youtube.com/watch?v=by4MS5DdEgY>`_ on Youtube.

Click on the **Flood barrier tool** icon |flood_barrier_icon| at the left of the screen. The flood barrier tool appears.

.. |flood_barrier_icon| image:: image/d3.6_flood_barrier_icon.png

.. figure:: image/d3.6_flood_barrier.png
	:alt: Flood barrier tool.

	Flood barrier tool.

You can set the height in the elevation box. 

- The height is in meters Mean Sea Level (m MSL). If the waterlevel in the flow link crossing the flood barrier exceeds this height the water will flow over the flood barrier. 

Press the DRAW ON MAP button to draw the shape of the flood barrier on the map.

.. figure:: image/d3.6_flood_barrier_draw_on_map.png
	:alt: Flood barrier tool - start creating flood barrier.

	Flood barrier tool - start creating flood barrier.

Click on the map to set the first point. The flood barrier is created by selecting points on the map. Every new point selected on the map creates a line connecting with the previous point. All points together form the flood barrier. 

.. figure:: image/d3.6_flood_barrier_first_point_selected.png
	:alt: Flood barrier - first point selected.

	Flood barrier - first point selected.

During the creation, you can go back to the previous point or cancel the entire flood barrier.
Cancel the last point by clicking on the |flood_barrier_cancel_point| on the map or clicking UNDO LAST POINT in the flood barrier tool (on the left).
Cancel the entire flood barrier by pressing CANCEL in the flood barrier tool.

.. |flood_barrier_cancel_point| image:: image/d3.6_flood_barrier_cancel_point.png

.. figure:: image/d3.6_flood_barrier_multiple_points_selected.png
	:alt: Flood barrier - multiple points selected.

	Flood barrier - multiple points selected.

Confirm the flood barrier by pressing the |flood_barrier_confirm_flood_barrier| on the map or CONFIM in the flood barrier tool.

.. |flood_barrier_confirm_flood_barrier| image:: image/d3.6_flood_barrier_confirm_flood_barrier.png

.. figure:: image/d3.6_flood_barrier_created.png
	:alt: Flood barrier created.

	Flood barrier created.

Adding a discharge point
------------------------
With the discharge tool a constant source of water will be added to your model.
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. 
The water that is added to the 2D surface of your model and will flow in constantly from that point.


Adding a pump station
---------------------
With the pump tool a constant sink will be added to your model. 
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. The water that is taken out of the model will not flow back into the model and is considered a loss. 

DEM edit/ Raster edit
---------------------

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
