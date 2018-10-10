How to perform a dem edit on the live site
==========================================

A DEM (Digital Elevation Model) edit is a tool in our live site, it allows to adjust the height of the bathymetry. This can be done at any time during the simulation. 

.. figure:: image/d_dem_edits.png
   :alt: Dem edits

To edit the bathymetry of the model, make sure the DEM-layer is activated. This can be done by first clicking on 'Map layers' (globe icon), then open the layer group 'Foreground' and then activate the DEM-layer by clicking on 'DEM'.  
By clicking the pencil icon in the lower left corner of the screen, edits in the DEM can be made. The slider on the right of the icons can be used to set the new height of the DEM. This is the absolute value in meters relative to sea level. The polygon icon on the left side of the screen can be used to draw a polygon on the DEM which is used to indicate the location of the DEM-edit. When clicking this icon a cursor showing the text 'Click to start draw polygon' pops up. A polygon can be drawn by clicking multiple vertices on the DEM and closing it by clicking on the first point again. The DEM edit is immediately committed when finishing the polygon. The result can be checked using the 'Cross profile' tool.

.. figure:: image/d_draw_dem_polygon.png
   :alt: Performing a dem edit
   
A DEM edit is also possible via our API: `3di.lizard.net/api/v1/docs/ <https://3di.lizard.net/api/v1/docs/>`_.  , thereby allowing external applications to perform a DEM edit as well. However, the steps performed by ‘process results’ do not take the DEM edit into account.  Take this into consideration when interpreting the results. 