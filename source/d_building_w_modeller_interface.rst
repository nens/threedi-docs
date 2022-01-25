.. _qgisplugin:


Building and adjusting a model with the Modeller Interface
===========================================================

Introduction
^^^^^^^^^^^^^
The Modeller Interface (MI) will help you with building 3Di models locally. 




.. _importsufhyd:

Import from SUF-HYD
^^^^^^^^^^^^^^^^^^^

SUF-HYD is a Dutch standardised format for transferring data of sewerage systems for hydraulic analyses. This tool allows an automated import of the sewerage data in the 3Di model database. 

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

.. _view_model_results:
    
View and edit 3Di model schematisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After loading your 3Di model schematisation, there are several ways to inspect your model. We have added the following features to assist you in viewing and editing the model schematization:

- Multiple styles per layer
- Drop down menus
- Immediate validation
- Automated field fill
- Multi-line fields for time series 

.. _multiplestyles:


**Multiple styles per layer**


The multiple styles per layer can help you when analysing your model. The different styles depict aspects of the layer you might be interested in, without cluttering your schematization with too much information at once. 

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
