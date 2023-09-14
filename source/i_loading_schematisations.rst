.. _load_schematisation:

Loading a schematisation
========================

You can load a :ref:`schematisation revision<revision>` with the :ref:`schematisation_editor_toolbar`:

#. Click on the 'Open 3Di Geopackage' or the 'Load from Spatialite' icon 
#. Select the schematisation you want to load from you local files
#. Click on 'Open'

You schematisation should now be loaded and you should be able to view all the elements in the Layers panel on the left.

.. Note:: 
    You might get the following message: "The selected spatialite cannot be used because its database schema version is out of date. Would you like to migrate your spatialite to the current schema version?". Click 'Yes' and your schematisation should be loaded

.. Note::  
    * In the regular workflow, schematisation data is stored in a *spatialite (.sqlite)* . The Schematisation Editor stores this data in a *geopackage (.gpkg)*. The database *schema* (the names and data types of tables and columns) of this geopackage also differs from the spatialite database schema. The Schematisation Editor loads the data from the spatialite into a geopackage; you make your edits in the geopackage, and when you have finished editing, save your changes to the spatialite.
	

.. _multiplestyles:

Multiple styles per layer
-------------------------

For some schematisation layers, multiple predefined styles are available. These can be helpful to quickly visualise the needed information on the map. 

To switch between stylings: 
1) In the *Layer panel*, right-click the layer you are interested in. 
2) Hold your mouse over *Styles* and the multiple styles will be shown. 
3) Click the style you want to use. The style with the dot next to it is the active style. 

Note: Some styles add a label to the object. Keep in mind when using these stylings that the labels only becomes visible when a certain zoom level is applied. 

The default style depicts the locations of the objects in the layer. The other stylings are explained briefly below.

1D and 2D Boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

=================  =====================================================================================
Style              Description  
=================  =====================================================================================
Timeseries label   The ‘timeseries label’ style adds a label to the default style, depicting the boundary

                   type, and the smallest (min:) and largest (max:) value in the time series.
=================  =====================================================================================



1D and 2D Lateral
^^^^^^^^^^^^^^^^^

=================  =====================================================================================
Style              Description  
=================  =====================================================================================
Timeseries label   The ‘timeseries label’ style adds a label to the default style, depicting the smallest

                   (min:) and largest (max:) value in the time series.
=================  =====================================================================================

When looking at these timeseries keep in mind that the values get rounded off to 2 decimal places, which can make it seem like the values are zero (0.00) when in fact they were not.

Connection node
^^^^^^^^^^^^^^^

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Id                   The ‘id’ style adds a label to the default style, depicting the id of the connection

                     node. This can be useful when connecting other elements to existing connection 

                     nodes.
Initial water level  The ‘initial water level’ style is a categorised styling that represents the connection

                     nodes without an initial water level in the default style and the connection nodes

                     with an initial water level as blue outlined dots with labels that depict the initial 

                     water levels (in m MSL).
Storage area         The ‘storage area’ style depict the storage area of the connection nodes as a ratio 

                     style with a label. The extent of the schematisation corresponds to the size of the 

                     storage area of the connection node. The label depicts the storage area. 
===================  ===================================================================================

 
Manhole
^^^^^^^

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style is a categorised styling depicting the locations and indicators of

                     the manholes. The different manhole indicators have different zoom levels in order

                     to avoid clutter. When zooming into a certain area the local manholes will appear.
Levels               The ‘levels’ style adds a label to the default style, depicting the surface level (s:),

                     the drain level (d:) and the bottom level (b:).
Calculation type     The `’calculation type’ <calculation_types>` style is a categorised styling that depicts the way 3Di calculated the interaction between the manhole and the 2D computational domain.

                     calculated the interaction between a manhole and the 2D computation domain.
Code                 The ‘code’ style adds a label to the default style, depicting the code of the manhole.
===================  =================================================================================== 


Cross section location (view)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Levels               The ‘levels’ style adds a label to the default style, depicting the bank level (bank:),

                     the reference level (ref:) and the difference between the two (diff:).
Cross section        The ‘cross-section’ style adds a label depicting the shape, the maximum width (w:) and  

                     the maximum height (h:) of the cross-section definition. The width (in m) is the 

                     diameter in the case of a circle and the max width in the case of a tabulated profile.
===================  =================================================================================== 


Pumpstation
^^^^^^^^^^^

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


Channel
^^^^^^^

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Calculation type             The `’calculation type’ <calculation_types>` style is a categorized styling that depicts the way    

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

Weir
^^^^

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

Culvert
^^^^^^^

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Levels and flow direction    The ‘levels and flow direction’ style adds arrows and a label to the default

                             style. The  arrows point in the expected flow direction (high to low 

                             invert level) and the label shows the invert level for the start point (s:)  
 
                             and end point (e:) of the culvert.
Calculation type             The `’calculation type’ <calculation_types>` style is a categorized styling that depicts the way  

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

Orifice
^^^^^^^

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


Pipe
^^^^

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Default                      The ‘default’ style is a categorized styling depicting the locations and  

                             sewerage types of the pipes.
Levels and flow direction    The ‘levels and flow direction’ style adds arrows and a label to the default 

                             style. The arrows point in the expected flow direction (high to low   

                             invert level) and the label shows the invert level for the start point (s:) 

                             and end point (e:)  of the pipe.
Calculation type             The `’calculation type’ <calculation_types>` style is a categorized styling that depicts the way 3Di   

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

Obstacle
^^^^^^^^

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

Grid refinement
^^^^^^^^^^^^^^^

===================  ===================================================================================
Style                Description  
===================  ===================================================================================
Default              The ‘default’ style depicts the locations of the grid refinements. The dashed   

                     pattern is based on the refinement level. The number of dots represents the 

                     refinement level.
Refinement levels    The ‘refinement level’ style adds a label to the default style, depicting 

                     the refinement level.
===================  =================================================================================== 


Grid refinement area
^^^^^^^^^^^^^^^^^^^^

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

Impervious surface
^^^^^^^^^^^^^^^^^^

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Surface inclination          The ‘surface inclination’ style is a categorized styling depicting the  

                             locations and the surface inclinations of the impervious surfaces.  
Area and dry weather flow    The ‘area dry weather flow’ style depicts the amount of dry weather flow 

                             in L/d for each impervious surface, calculated 

                             as dry_weather_flow * nr_inhabitants. 
===========================  ============================================================================

Surface
^^^^^^^

===========================  ============================================================================
Style                        Description  
===========================  ============================================================================
Area and dry weather flow    The ‘area dry weather flow’ style depicts the amount of dry weather flow  

                             in L/d for each surface, calculated as dry_weather_flow * nr_inhabitants.
===========================  ============================================================================

