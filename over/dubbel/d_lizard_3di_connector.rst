.. _lizardintegration:

Lizard-3Di integration
=========================

.. note::
    This section will be extended in the near future. 
	
	


3Di Scenario Archive
---------------------

After simulating with 3Di, the scenario can be processed to several rasters to visualize your results. These rasters can be viewed using the Lizard portal and in the 3Di Modeller Interface using WMS. *Note: these post-processed results are only available for Lizard subscription holders.*

The following results are available: 

**Water levels:**
Water level relative to mean sea level (m) at a certain time step or maximum water level per calculation cell. 

**Water depth:**
Water depth (m) relative to surface level (water level minus surface level). Surface level is defined by the DEM used by the model. 

**Rainfall:**
Rain intensity per calculation cell (mm/h).

**Maximum flow velocity:**
Maximum flow velocity per calculation cell (m/s). Can for example be used for flood damage estimations. 

**Rise velocity:** 
Rate of rise (m/s), defined by the difference in water level per second. Can for example be used for flood damage estimations. 

**Flood hazard rating:**
Rating used to indicate the degree of danger caused by flooding. 
The flood hazard rating is calculated as follows: 

HR = d * (v + 0.5) + DF

| Where:
| HR = (flood) Hazard Rating
| d = depth of flooding (m)
| v = flow velocity (m/s)
| DF = debris factor 

When water depth is smaller than or equal to 0.25 than DF = 0.5, else DF = 1. 


Load rasters in 3Di Modeller Interface using WMS
-------------------------------------------------
To view post-processed results from your 3Di scenario in the 3Di Modeller Interface follow the following steps: 

| 1. Find the scenario UUID in the scenario management screen of your Lizard portal. Go to ``{yourportal}.lizard.net``, click on **Management > Data > 3Di Scenarios** and search for your scenario. After opening, you can copy the UUID from the URL. 

| 2. Compose WMS url. Fill out the name of the Lizard portal you are using and the UUID of your scenario in the following URL: 
| ``https://{yourportal}.lizard.net/wms/scenario_{UUID of scenario}/?request=getcapabilities``

| For example: 
| https://demo.lizard.net/wms/scenario_c30ef7f2-c871-4d70-a087-8f078f9ebafd/?request=GetCapabilities

| 3. In the 3Di Modeller Interface connect to the Lizard WMS server using the Data Source Manager. 
| a) Choose WMS/WMTS as data source.
| b) Create a new connection.
| c) Give your scenario a name and copy the URL composed in the previous step. 
| d) Under *Authentication* choose *Basic*.
| e) You need to use a personal API key. If you do not have one yet, you can create one in the Lizard management portal. Go to yourportal.lizard.net, go to **Management > Personal API keys > +New Item.** Use *__key__* as username and the personal API key you created as password. See the `Lizard documentation <https://docs.lizard.net/d_apitechnical.html#apiauthenticationanchor>`_ for more information. 
| f) Click *OK* to save the connection. 

.. figure:: image/d_wms_connection.png
    :alt: Create WMS connection in QGIS

4. When the connection is created, several layers appear (expand the *Title*-section to view full names of the layers). The layers can be added to the project by selecting them and clicking *Add*. 

.. figure:: image/d_wms_layers_3di.png
    :alt: 3Di WMS layers

| 5. The water depth, water level and rain rasters can also be viewed as timeseries.
| a) A temporal raster is indicated by a small clock icon in the layer panel.
| b) Activate the *Temporal Controller* by clicking the clock sign on the toolbar.
| c) Turn on *Fixed range temporal navigation* or *Animated temporal navigation*.
| d) Choose for which time step of your simulation you want to see the water level or depth. 

.. figure:: image/d_wms_temporal_controller_rasters.png
    :alt: Temporal Controller WMS layers
	











