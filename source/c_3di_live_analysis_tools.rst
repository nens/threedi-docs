.. _3di_live_analysis_tools:

Analysis tools
==============

.. _search_bar_ls:

Search bar
----------
The Search Bar enables you to locate assets of your schematisation. You can search for asset type (e.g. pipe), name, code or id.

Realtime results during a simulation
------------------------------------

By default, the **selection tool** (top left) is switched on. With it you can click anywhere on the map to visualize the time series at that location. Default water depth and water level will be shown. If the model contains groundwater that graph is also shown. 

The time series can all be downloaded in CSV format. The points over time that are shown are the points calculated by the 3Di calculation core and are independent from the output time step that the modeller has set.

.. figure:: image/d3.1_point_location.png
    :alt: Point selection

Also the height of a cross section can be displayed with the **Line-selection tool**, together with the water level in that transect. Click the start and end point in any place on the map for the cross section (within the 2D model domain).

.. figure:: image/d3.1_side_view.png
    :alt: Cross section selection

The side view shows the elevation in green and the water in blue. By hovering over the graph with the mouse, exact values can be seen. Keeping this graph open during a flood event will show you how the water level is slowly rising. Note that in the example also groundwater is available in the model indicating an extra blue line. 


.. _selection_tool_guide:

Selection tool
^^^^^^^^^^^^^^^^
By default, the **selection tool** is switched on. With it you can click anywhere on the map to visualise the time series at that location. By default water depth and water level will be shown. If the model contains ground water, that graph is also shown. 

The time series can be downloaded in CSV format. The points in the graphs in :numref:`fig_point_select_tool` are the points calculated by the 3Di calculation core and are independent from the output time step that the modeller has set while following a location. If a location is clicked later during the simulation, the historic values on the graph are the values shown according to the output time step. 

.. note::
	Water depth is not shown for channel nodes

.. _fig_point_select_tool:

.. figure:: image/d3.1_point_location.png
	:alt: Point selection

	Point selection tool.

.. _line_selection_tool:

Line-selection tool
^^^^^^^^^^^^^^^^^^^^

The **Line-selection tool** shows the height of a cross section, together with the water level in that transect. Click the start and end point in any place on the map for the cross section (within the 2D model domain).

.. figure:: image/d3.1_side_view.png
	:alt: Cross section selection

	Line-selection tool.
	
The side view shows the elevation in green and the water in blue. By hovering over the graph with the mouse, exact values can be seen. Keeping this graph open during a flood event will show you how the water level is slowly rising. Note that in the example also groundwater is available in the model indicating an extra blue line (only in those cases where ground water is set up in the schematisation). 



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



