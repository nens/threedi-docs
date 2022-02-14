Editing a model schematisation with the live site
==================================================

In the live site, you can temporarily adjust values. For example, you can change the pump capacity and weir height, and you can close 1D elements such as channels, pipes, weirs, culverts and orifices.
You can also perform a DEM edit via the raster edil tool. 


The buttons at the mid left of the screen are used to interactively adjust the forcing of the model. Two of these buttons can be used to alter the model:
- Discharge tool
- Pump tool
- The raster edit tool


Adding a discharge point
-------------------------
With the discharge tool a constant source of water will be added to your model.
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. 
The water that is added to the 2D surface of your model and will flow in constantly from that point.


Adding a pump station
-----------------------
With the pump tool a constant sink will be added to your model. 
Select the icon and change the rate (in m3/s) to what you want to apply, then click at a location on the map to point the location. 
This can only be done when your simulation is paused. The water that is taken out of the model will not flow back into the model and is considered a loss. 



DEM edit/ Raster edit
------------------------------------------------

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




