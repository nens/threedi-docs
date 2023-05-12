.. _edit_schematisation:

Editing your schematisation
============================

The following edits are possible:

* :ref:`edit_feature_attributes`
* :ref:`edit_feature_geometries`
* :ref:`creating_new_feature`
* :ref:`deleting_features`
* :ref:`pasting_features_external_data`



The following features have been added to assist you in editing your schematisation:


* **Drop down menus**: To assist you in selecting the proper values, we have added drop down menus for multiple value attributes in tables. This could help for example in selecting a shape for a cross section definition. 

.. CHECK: Ik zou dit kopje weghalen. Spreekt voor zichzelf als je de interface gebruikt.


* **Highlighting obligatory fields**: Fields that are mandatory to fill with be highlighted in orange when you add a new feature.

.. CHECK: Dit is niet meer zo! (de oude tekst) de velden zijn nog wel oranje. Maar heb een cross section location toegevoegd met bijna geen info en daarna met 'Save to Spatialite' opgeslagen en toen klapte hij daar niet op.


* **Multi-line fields for time series**: Multi-line fields are designed for editing time series. In the example of the Figure, the time series of a discharge boundary condition is edited.

    .. figure:: image/d_qgisplugin_vm_timeseries.png
        :scale: 75%
        :alt: Timeseries example


.. _automated_fill:

Automated field fill 
----------------------

Some fields are automatically filled to assist in making your schematisation. Here is an overview of the fields that are filled automatically:

- The cross-section location fetches the corresponding channel-id automatically
- Channels and culverts automatically fill connection node ids when drawing between nodes with `snapping <https://docs.qgis.org/3.4/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#setting-the-snapping-tolerance-and-search-radius>`_.
- Invert level from culverts. If invert level is empty culverts assumes the invert level based on manhole bottom_level 

On top of that, some default values for some of the mandatory fields are set. This helps you build models faster. The following default values will be set, in case they are left blank. The listed values are defaults, so please change them if required for your specific application.

You need to set your QGIS locale to 'English UnitedStates' in order for this functionality to work properly.

.. CHECK: Klopt deze lijst nog? alles heet nog v2.

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
type 							1: pump behavior is based on water levels on the suction side
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



.. _addleveebreaches:

Add levee breaches
--------------------

.. VRAAG: is dit een logische plek hiervoor?

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

1. Set up a connection with the SQLite or PostgreSQL database of your model.
2. Click on the 3Di toolbox and select *Step 3 - Modify schematisation*.
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
