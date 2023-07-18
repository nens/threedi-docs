.. _edit_schematisation:

Editing your schematisation
============================

The following edits of your schematisation are possible in the Modeller Interface:

* :ref:`creating_new_feature`
* :ref:`pasting_features_external_data`
* :ref:`edit_feature_attributes`
* :ref:`edit_feature_geometries`
* :ref:`deleting_features`

The following features have been added to assist you in editing your schematisation:

* **Drop-down menus**: To facilitate the selection of appropriate values, we have introduced drop-down menus for attributes with multiple value options in tables. This feature proves useful, for instance, when choosing a shape for a cross-section definition.
* :ref:`automated_fill`: Certain fields are automatically filled-in to streamline the schematisation process, providing helpful assistance.
* **Highlighting mandatory fields**: When adding a new feature, mandatory fields that require input will be highlighted in orange, ensuring they are easily identifiable.
* **Multi-line fields for time series**: Multi-line fields are specifically designed for editing time series data. You can edit the time series for :ref:`simulate_api_qgis_boundary_conditions`, :ref:`simulate_api_qgis_laterals`, :ref:`simulate_api_qgis_precipitation` and :ref:`wind_apiclient`.

|

**Activate the plugin**

Make sure you activate the plugin by clicking on 'Plugins' in the menu bar > 'Manage and Install Plugins...' > Check the box of the 3Di Schematisation Editor.

.. _creating_new_feature:

Creating new Features 
-----------------------

To create a new feature:

#) Select the layer in the Layers panel.
#) Press the 'Toggle Editing' button (|toggleEditing|).
#) Click on 'Add Point-' (|addPoint|), 'Add Line-' (|addLine|) or 'Add Polygon Feature' (|addPoly|), depending on what kind of feature you want to add.
#) Left click on the map to add a Point feature. When adding Line or Polygon features, add multiple locations by left clicking and finish by right clicking.
#) Fill in the Attribute Form. The orange fields are required to fill in. The other fields are optional. Press 'OK' to finish the process.
#) When you are finished with adding the features, disable 'Toggle Editing' and save your schematisation to Spatialite.

.. _3di_feature_notes:

Notes on the 3Di Features
""""""""""""""""""""""""""
Please check out these notes to correctly add 3Di features to the schematisation.

* **Channel**: A channel can exist of 2 or more vertices. The *connection nodes* and the *Cross Section Location* are added automatically. Do not forget to fill in the required Feature Attributes for the Cross Section Location.

* **Cross Section Location**: Should be placed on top of a channel vertex, (not on the start or end vertex).

* **Culvert**: The culvert can also exist of 2 or more vertices and the *connection nodes* are added automatically.

* **Orifice**: An orifice can only consist of 2 vertices. The *connection nodes* are added automatically.

* **Pipe**: To draw a single pipe, the geometry must have exactly 2 vertices. A line with more than 2 vertices will be split into several pipes. Check out the tip below to add a trajectory of multiple pipes.

* **Pump**: The geometry of a pump must have exactly 2 vertices. The *connection nodes* are added automatically. For external pumps, which pump water out of the model domain, the *Pumpstation (without end node)* should be used. For internal pumps, which pump water between two nodes within the model domain, the *Pumpstation (with end node)* should be used.

* **Weir**: The weir consists of exactly 2 vertices, and the *connection nodes* are added automatically.

* **(Impervisous) Surfaces**: First draw the (impervious) surface polygon(s), then add (impervious) surface map lines. These should start on the impervious surface polygon and end at the connection node to which it is mapped.


.. tip::
    In order to digitize **a trajectory of multiple pipes**, first digitize the manholes, fill in the bottom levels, and then draw the pipe trajectory over these manholes by adding a vertex at each of the manholes. 
    The pipes that are generated will use the manhole's bottom levels as invert levels and the *connection nodes* and *manholes* will be added automatically.

.. _addleveebreaches:

Add levee breaches
^^^^^^^^^^^^^^^^^^^

.. VRAAG: is dit een logische plek hiervoor? Zou dit niet meer een tutorial zijn?
.. Ik heb deze tekst zelf niet geschreven, maar heb het idee dat hij nu al veroudert is met v2_ en referenties naar de 3Di toolbox.

Levee breaches can be created in 3Di-models that contain a connected *v2_channel* 
(*calculation_type* = 102) and a *v2_levee*-structure. For more information on the 
theory behind levee breaches in 3Di, see :ref:`breaches`.

Before adding levee breaches, please make sure that the data in *v2_levee*-table is 
correctly filled out. For simulating breaches, 3Di requires the *crest_level* of the 
levee in m MSL **(a)**, the *material* of the levee **(b)** and the *max_breach_depth* 
relative to the crest level in meters **(c)**.

.. image:: image/d_qgisplugin_breach_info_v2_levee_table.png

.. NOTE:: 
    adding levee breaches should generally be the last step in the modelling process. When connected points belonging to a channel are moved across a levee in order to simulate a breach, they are assigned a *calculation_pnt_id* that refers to the id number of the old calculation point. Any changes that affect the amount of calculation/connected points or the location of calculation points (like adding a new *v2_channel*) will lead to changes in the id numbers of the calculation points, and hence, to moved connected points referring to the wrong calculation points.

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


|

.. _pasting_features_external_data:

Pasting Features from external data sources
---------------------------------------------

Features can be copy-pasted from external data sources into the :ref:`Schematisation Editor <schematisation_editor>`. 
Check out the `QGIS Documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/attribute_table.html>`__ for how to work with the attribute table.

.. Note::
    Please note that when pasting features from external sources, the perks of the Schematisation Editor will not be applied to the features. 

|

.. _edit_feature_attributes:

Editing Feature Attributes
----------------------------

There are two options available for editing feature attributes:

1. Via the **Attribute Table**:
   
   - Right-click the layer in the Layers panel.
   - Select 'Open Attribute Table'.
   - Click the 'Toggle Editing' button located in the top left corner.
   - Make the necessary edits within the table.
   - Click 'Save Edits' in the top left corner to save your changes.


2. Using the **Identify Feature** option:
   
   - Select the desired feature layer.
   - Enable the 'Identify Feature' (|idendifyFeature|) option.
   - Click on a feature on the map.
   - A window will open displaying the attributes of the selected feature, along with the attributes of all related features.
   - Explore the different tabs within the window to access the related feature attributes.

|

.. _edit_feature_geometries:

Editing Feature Geometries
----------------------------

For editing the geometries of features, the 'Vertex tool' can be used, see the `QGIS documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#vertex-tool>`__. On top of the standard QGIS functionalty, the :ref:`Schematisation Editor <schematisation_editor>` provides extra functionalities:

    - When moving a node, all connected features will move along.
    
    - Changing the start/end vertex of a line feature (e.g. pipe, channel, culvert, orifice, weir, pump (impervious) surface map) allows you to connect the line to another connection node.

|

.. _deleting_features:

Deleting Features
-------------------

To learn more about deleting features, refer to the `QGIS documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#deleting-selected-features>`_ for general instructions. When using the Schematisation Editor, you will encounter the following options:

* 'Delete this feature only': This option deletes only the selected features. It may result in an invalid schematisation, but can be useful when removing a specific part of the model.
* 'Delete all referenced features': Choosing this option will delete all connected features along with the selected ones. Your schematisation is likely to remain valid when using this option.
* 'Cancel': Selecting this option will cancel the deletion process and leave the features unchanged.


.. |toggleEditing| image:: /image/pictogram_toggle_editing.png
    :scale: 90%

.. |addPoint| image:: /image/pictogram_addpoint.png

.. |addLine| image:: /image/pictogram_addline.png

.. |addPoly| image:: /image/pictogram_addpolygon.png

.. |idendifyFeature| image:: /image/pictogram_identify_features.png

|

.. _automated_fill:

Automated field fill 
----------------------

Some fields are automatically filled to assist in making your schematisation. Here is an overview of the fields that are filled automatically:

- The cross-section location fetches the corresponding channel-id automatically
- Channels and culverts automatically fill connection node ids when drawing between nodes with `snapping <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#snapping-on-custom-grid>`_.
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
