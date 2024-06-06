.. _release_notes_LS:

3Di Live
--------

.. _release_notes_3di_live_20240605:

June 5th, 2024
^^^^^^^^^^^^^^

- Improved interpolation of 2D flow visualisation between cells (#1594)

- Improve 3Di Live performance of 2D flow visualisation by reducing the redrawing frequency (#1686)

- Show exchange level in Breaches details (#1673)

- The UI for the visualisation of 1D and 2D flow has been improved:

	- It has been made clearer which elements are visible/invisible on the map (#1759)

	- For the 1D flow/2D flow settings, the "down arrow" has been replaced with a "settings" icon (#1761)

- File 2D laterals in the simulation template are now also visible on the map in 3Di Live, similar to non-file 2D laterals (#1757)

- Bugfix: "Billing goes to" dropdown was very slow sometimes (#1785)

- Bugfix: opening breaches in 3Di Live did not work for 3Di models generated after May 30th. This has been fixed now (#1843)


March 26th, 2024
^^^^^^^^^^^^^^^^

- 2D flow is now visualised using traces. The visualisation of 2D flow is based on the flow velocity at the center of the computational grid cells. Note that it does not take into account intra-cell variation of flow velocity or direction. For this reason, you may see flow in dry parts of cells. (#1705, #1703, #1670, #1617, #1682, #1675, #1612, #1576, #1561, #440)

- Hillshade and new colour map in for the DEM (#1671, #1707, #1681, #1677, #1616, #1577)

- Recording option: click on the record button to record the 3Di Live tab in your browser (#1583)

- 1D flow above 2 m/s (or other user-defined threshold) is highlighted (#1558)

- Design of the layers panel has been simplified by putting the flow velocity settings (for 1D and 2D) in a drop-down menu (#1692)
	
- Visibility of assets, breaches and model grid is no longer dependent on zoom level (#1674, #1575)

- Model flowlines are shown only when drawing flood barriers (#1521)

- "Code" is now shown in asset details (#1683)

- Some improvements in spelling & terminology have been made (#1559)	

- Technical change: 3Di Live now uses deck.gl instead of Leaflet (#1562)

- Technical change: 3Di Live now uses Maptiler instead of Mapbox tiles (#1636)

- Bugfix: in some cases, the model grid would not show, no matter what zoom level (#1592)

- Bugfix: in some cases, the point selection tool would not react (#1592)

- Bugfix: The "velocity" graph for Breaches has been fixed (#1520)


January 11th, 2024
^^^^^^^^^^^^^^^^^^

- Model elements and 1D flow are now visualised using WebGL, which improves performance. 1D flow is now visualised with moving waves instead of dots (#1341, #1342).

- The Line selection tool now supports drawing a side view trajectory with a custom path, i.e. with more than 2 vertices. (#1446)

- Option to rescale DEM color scale based on current extent (#853)

- Show days in clock, relevant for simulations longer than 24 hours (#1387)

- When starting a session, the organisation that owns the model is automatically selected in the "Billing goes to" dropdown (#1251)

- When switched on, model grid is shown regardless of zoom level. It is no longer necessary to zoom in. (#1509)

- The labels that are shown when hovering over model elements now show the display name instead of ID (#1505)

- The organisation to which the simulation is billed is now included in the info panel (#1284)

- Enforce "Simulation runner" and "viewer" roles (#437). A user must have "simulation_runner" role in a organisation to be able to start simulations billed to that organisation. A user must have "viewer" role in an organisation to be able to follow simulations of an organisation.

- Round editable values to 2 decimals (#1345)

- The user interface is loaded while loading the 3Di model, instead of after loading the 3Di model (#426)

- Bugfix: Graph data was rounded to 2 decimals, while only the value on the labels should be rounded to two decimals (#1318)

- Bugfix: Simulation could not be started if multiple simulation templates are available (#1330)

- Bugfix: Show names instead of numbers for properties of model elements (e.g. sewerage type) (#1185)

- Bugfix: Nodatavalue was shown as actual value (#434)





October 31st, 2023
^^^^^^^^^^^^^^^^^^

- Correctly show DEMs that contain None, NaN, inf or -inf values (threedi-api #2041)


October 18, 2023
^^^^^^^^^^^^^^^^
- Flood barriers can now always be clicked for more info, also when the Flood barrier tool is not active (#527)

- When hoovering over the Side view plot, the mouse position is indicated on the map (#449)

- DEM value is shown when clicking on the map using the Point tool (#526)

- Asset properties that are in decimal numbers are now rounded to two decimals (#453)

- Display names of assets are ellipsed and full name is shown when hoovering over (#431)

- 3Di Live and 3Di Management are now "domain agnostic", so they can also be hosted on other domains, like 3di.twinn.io (#1245)

- An *Info* panel was added, with details about the simulation and the 3Di model used (#273)

- Values in charts labels are now rounded to 2 decimals (#1168)


September 21, 2023
^^^^^^^^^^^^^^^^^^

- Bugfix: Allow negative and/or decimal number input in weir crest level edit (#949, #432)

April 25th 2023
^^^^^^^^^^^^^^^

- Breaches: a line has been added to the visualisation of breaches in 3Di Live. Discharge and flow velocity are visualized on these lines by moving dots.


March 20th 2023
^^^^^^^^^^^^^^^

- Now gives a message when max number of licenses is reached


November 21th 2022
^^^^^^^^^^^^^^^^^^

**Flood barriers tool**

A flood barrier can prevent a certain area from flooding. You can set the height of the flood barrier.
For more information about the flood barriers tool, you can watch the `Floodbarriers preview <https://www.youtube.com/watch?v=by4MS5DdEgY>`_ on Youtube.

**Added features**

- Show 2D flow lines (new model generation required for this)

**Fixed**

- Link to 3Di documentation under ‘help


August 2022
^^^^^^^^^^^^
- We have hotfixed the waterdepth interpolation to make sure that no water is shown visually before the start of a simulation and to avoid large patches  of interpolated water when zooming out

- Added Icon Forecast

- Implemented the following rasters:

    - ICON-global forecast of precipitation with hourly timestamp

    - ICON-EU forecast of precipitation with hourly timestamp

    - ICON-D2 forecast of precipitation with hourly timestamp


- Icon forecast gives you a global forecast of rainfall for the next 24 hours. More information can be found `here  <https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html>`__:

- Added a rainbarchart to show the amount of precipitation during the simulation time

- Limit the datepicker of forecasted rain to the range of dates that the forecast spans. Mostly 2-7 days.

- Show in the datepicker if there actually is a rain-event on the model extend.

- Improved search functionality. For instance you can now toggle to view all types of sewers when searching on sewers.

- Fixed a bug where a model without a simulation template would stall in the live-site.

- Fixed a bug where the water depth on nodes would display incorrect.

- Fixed a bug where the mouse cursor would change to a hand indicating you would be able to click the element but couldn't.



February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^^^

We have released new versions of 3Di Live.

- Simulation templates are used

October 18th 2021
^^^^^^^^^^^^^^^^^

We have released new versions of 3Di Live

- Saves the organisation you have selected and your previous search term last
- Forms reflect the last action from the user. E.g. for rainfall it doesn't reset to the default value anymore
- Events can be deleted or stopped. For now pumps, discharges, rain and wind are supported

March 23rd 2021
^^^^^^^^^^^^^^^^

We have update 3Di Live with following features:

- Water depth graph now also shows a graph with water depth - 0
- Add a clock time hover
- Add hh:mm at the start of the simulation, to make clear what are the units of the clock
- Add decimal support for discharge (when editing pumps)
- Add minute support for durations
- Ability to select different units when editing a pump discharge

February 22nd 2021
^^^^^^^^^^^^^^^^^^^^

Some bugfixes in 3Di live:

- Rescale DEM coloring based on model
- Correct water depth calculation for manholes
- Close culvert in both directions
- Rate limiter interferes with simulation in spectator mode
- Moving dots for 0D1D models fixed
- Correct handling of wind direction
- Breach editing used wrong id


