Results in Lizard
=================================

In general, stored results can be downloaded using the 3Di QGIS plugin or viewed and downloaded from the Lizard platform. The 'Basic Results' option includes the following derivations from calculation results for Lizard users: 

* Water level 
* temporal Water depth 
* temporal Waterlevel
* Maximum flow velocity 
* Maximum rate of rise 
* Maximum water depth 
* Flood hazard rating 

The 'damage_estimation' option uses a module called "WaterSchadeSchatter" (currently only available in the Netherlands) which provides two products derived from the maximum water depth:

* Damage estimation map 
* Damage estimation table 

3Di users that have access to Lizard can view and playback stored scenarios through the portal. 

View stored results
---------------------

To view results in Lizard, follow these steps

1. Store your result at the end of your simulation on 3Di.lizard.net

    A. Click you name and click ‘store results’
    B. Choose a name for your scenario (and remember it)
    C. Check basic process results for water depths in Lizard


.. figure:: image/d_store_results.png
   :alt: Store results
   
.. figure:: image/d_store_results2.png
   :alt: Store results 2

2. Wait a while for Lizard to process your results. You will receive an email when all results are available.

3. Go to lizard (delfland.lizard.net) and Log on.

4. Expand the layer view and scroll down to add another layer

.. figure:: image/d_lizard_add_layer.png
   :alt: Lizard add layer

5. Search for your scenario name and select it, then go back

.. figure:: image/d_lizard_add_layer2.png
   :alt: Lizard add layer 2

6. Select your scenario in the layers panel. Here you can view several processed results and download raw results. Select the layer ‘waterdiepte’ (or waterdepth).

.. figure:: image/d_lizard_select_layer.png
   :alt: Lizard select layer

7. Then click the small vizier on the selected layer. This will zoom your view to your model extent and the correct period in time in which your scenario was stored (see time frame at the bottom of your screen).

8. To playback your scenario click the play button. To pause click it again. You will notice that the image will sharpen as soon as you pause playback. You may also click on a point on the map to view a graph of the water depth at that location.

9. Raw results can be downloaded from the menu directly. To download a raster select the export button and select the result you would like. You must choose a spatial projection and resolution. All data within your current view is exported. When the export is ready for download you receive a message in your inbox.

.. figure:: image/d_export_button.png
   :scale: 90%
   :alt: Lizard export button
   :align: center
   
   Lizard export button
   
Stored results can be managed using the following URL: <your-organisation>.lizard.net/management/scenarios

Damage Estimation 
---------------------

Depending on your location Lizard provides estimates of damage caused by inundation or flooding. To use the damage estimation your study or model area must be within the Netherlands. 

The damages are estimated based on the land-use type, depth of the inundation, year of the month and repair time and are closely linked to the dutch waterschadeschatter.nl. The damage can be used by selecting the 'damage estimation' option and providing the parameters. The land-use map can be viewed in lizard and is fixed. The water depth is derived using the maximum water level and the most recent AHN elevation. The damage estimation does not use the DEM provided in the model.


.. figure:: image/d_store_results.png
   :alt: Store results
   
.. figure:: image/d_store_results2.png
   :alt: Store results 2

The estimated damages are available on a 0.5 m x 0.5 m resolution. Direct, indirect and total damages are available in separate raster layers. In addition, a CSV formatted file with total damages can be downloaded from Lizard.

Further documentation (only in Dutch) can be downloaded from :download:`here <pdf/nabewerking-3di-resultaten-in-lizard.pdf>`. The used damage table are available in :download:`Excel <other/3di-v2.2018-05-15.xlsx>` and :download:`CFG <other/3di-v2.2018-05-15.cfg>` (for use on `waterschadeschatter.nl <https://www.waterschadeschatter.nl>`_. The damage estimation in Lizard was developed together with Hoogheemraadschap Hollands Noorderkwartier.

