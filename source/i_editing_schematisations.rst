.. _edit_schematisation:

Editing schematisations
=======================

This section explains how you can edit the schematisation manually and how you can use Processing Algorithms to make some edits easier.

For manual editing, the following topics are covered:

* :ref:`creating_new_feature`
* :ref:`pasting_features_external_data`
* :ref:`edit_feature_attributes`
* :ref:`edit_feature_geometries`
* :ref:`deleting_features`

The following processing algorithms are available:

* :ref:`generate_exchange_lines`
* :ref:`auto_fill_sewerage_properties`
* :ref:`map_surfaces_to_connection_nodes`
* :ref:`manhole_bottom_level_from_pipes`

The following features have been added to assist you in editing your schematisation:

* **Drop-down menus**: To facilitate the selection of appropriate values, we have introduced drop-down menus for attributes with multiple value options in tables. This feature proves useful, for instance, when choosing a shape for a cross-section definition.
* **Highlighting mandatory fields**: When adding a new feature, mandatory fields that require input will be highlighted in orange, ensuring they are easily identifiable.
* **Multi-line fields for time series**: Multi-line fields are specifically designed for editing time series data. You can edit the time series for :ref:`simulate_api_qgis_boundary_conditions`, :ref:`simulate_api_qgis_laterals`, :ref:`simulate_api_qgis_precipitation` and :ref:`wind_apiclient`.

|

.. _creating_new_feature:

Creating new features 
---------------------

To create a new feature:

#) In the *Layers panel*, select the layer you want to add the feature to.
#) Click *Toggle Editing* |toggleEditing|.
#) Click *Add Point feature* |addPoint|, *Add Line feature* |addLine| or *Add Polygon feature* |addPoly|, depending on what kind of feature you want to add.
#) Left-click on the map canvas to add a Point feature. When adding Line or Polygon features, add multiple locations by left-clicking and finish by right-clicking.
#) Fill in the Attribute Form. The orange fields are required to fill in. The other fields are optional. Click *OK* to finish the process.
#) When you finished adding the features, click *Toggle Editing* |toggleEditing| to stop editing
#) In the :ref:`schematisation_editor_toolbar`, click *Save to Spatialite*.

For instructions specific to each layer, see :ref:`schematisation_objects`.

.. todo::
   Move the following to schematisation objects section
   * **Pump**: The geometry of a pump must have exactly 2 vertices. The *connection nodes* are added automatically. For external pumps, which pump water out of the model domain, the *Pumpstation (without end node)* should be used. For internal pumps, which pump water between two nodes within the model domain, the *Pumpstation (with end node)* should be used.
   
   * **Weir**: The weir consists of exactly 2 vertices, and the *connection nodes* are added automatically.
   * **(Impervious) Surfaces**: First draw the (impervious) surface polygon(s), then add (impervious) surface map lines. These should start on the impervious surface polygon and end at the connection node to which it is mapped.

.. _pasting_features_external_data:

Pasting Features from external data sources
---------------------------------------------

Features can be copy-pasted from external data sources into the schematisation layers. 
Check out the `QGIS Documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/attribute_table.html>`__ for how to work with the attribute table.

.. Note::
    Please note that when pasting features from external sources, the automagic actions of the 3Di Schematisation Editor will not be applied to the features. 

.. _edit_feature_attributes:

Editing Feature Attributes
----------------------------

There are two options available for editing feature attributes:

1. Via the **Attribute Table** (for editing multiple objects at once):
   
   - In the *Layers* panel, right-click the layer > *Open Attribute Table*.
   - In the top left corner, click *Toggle editing* .
   - Make the necessary edits within the table.
   - To batch edit, use the drop-down menu in the top left to select the features to be edited. Fill out a value or expression in the text bar and click *Update all* to edit all objects, or *Update selected* to edit the selected objects. 
   - Click *Save Edits* in the top left corner to save your changes.


2. Using the **Identify Feature** option (for editing specific objects one at a time):
   
   - Select the desired feature layer.
   - Click the *Toggle Editing* button located in the top left corner.
   - Activate the *Identify feature* (|idendifyFeature|) map tool.
   - Click on a feature on the map canvas.
   - A window will open, displaying the attributes of the identified feature, along with the attributes of all related features.
   - Explore the different tabs within the window to access and edit the related feature attributes.
   - Click *Save Edits* in the top left corner to save your changes.

|

.. _edit_feature_geometries:

Editing feature geometries
----------------------------
   
For editing the geometries of features, the 'Vertex tool' can be used, see the `QGIS documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#vertex-tool>`__. On top of the standard QGIS functionalty, the 3Di Schematisation Editor provides extra functionalities:

    - When moving a node, all connected features will move along.
    
    - Changing the start/end vertex of a line feature (e.g. pipe, channel, culvert, orifice, weir, pump (impervious) surface map) allows you to connect the line to another connection node.

|

.. _deleting_features:

Deleting features
-----------------

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


.. _generate_exchange_lines:

Generating exchange lines
-------------------------

A processing algorithm is available to automatically generate :ref:`Exchange lines<exchange_line>`. This processing algorithm can be found via *Main menu* > *Processing* > *Toolbox* > *3Di Schematisation Editor* > *1D2D* > *Generate exchange lines*.

This processing algorithm generates exchange lines for (a selection of) channels. The resulting exchange line's geometry is a copy of the input channel's geometry, at user specified distance from that channel (the GIS term for this is 'offset curve'). The resulting exchange lines is added to the exchange line layer, and the attribute 'channel_id' refers to the channel it was derived from.

* Input channel layer: Usually this is the Channel layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the fields 'id' and 'calculation_type' can be used as input.
* Distance: Offset distance in meters. A positive value will place the output exchange line to the left of the line, negative values will place it to the right.
* Exchange lines layer: The layer to which the results are written. Usually this is the 'Exchange line' layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the field 'channel_id' can be used.

.. _auto_fill_sewerage_properties:

Auto-fill sewerage properties
-----------------------------

The :ref:`3Di processing algorithm<3di_processing_toolbox>` *Guess indicators* estimates the correct values for pipe friction, manhole indicator and manhole area (only for NULL fields) with the overall option to only fill NULL fields.
 
This processing algorithm can be found via *Main menu* > *Processing* > *Toolbox* > *3Di* > *Schematisation* > *Guess indicators*.

.. _map_surfaces_to_connection_nodes:

Map (impervious) surfaces to connection nodes
---------------------------------------------

This processing algorithm can be found via *Main menu* > *Processing* > *Toolbox* > *3Di Schematisation Editor* > *Inflow* > *Map (impervious) surfaces to connection nodes*.

Connect (impervious) surfaces to the sewer system by creating (impervious) surface map features. The new features are added to the (impervious) surface layer directly.

For each (impervious) surface, the nearest pipe is found; the surface is mapped to the the nearest of this pipe's connection nodes.

In some cases, you may want to prefer e.g. stormwater drains over combined sewers. This can be done by setting the stormwater sewer preference to a value greater than zero.

Parameters:

* (Impervious) surface layer: Surface or Impervious surface layer that is added to the project with the 3Di Schematisation Editor.
* (Impervious) surface map layer: Surface map or Impervious surface map layer that is added to the project with the 3Di Schematisation Editor.
* Pipe layer: Pipe layer that is added to the project with the 3Di Schematisation Editor.
* Connection node layer: Connection node layer that is added to the project with the 3Di Schematisation Editor.
* Sewerage types: Only pipes of the selected sewerage types will be used in the algorithm
* Stormwater sewer preference: This value (in meters) will be subtracted from the distance between the (impervious) surface and the stormwater drain. For example: there is a combined sewer within 10 meters from the (impervious) surface, and a stormwater drain within 11 meters; if the stormwater sewer preference is 2 m, the algorithm will use 11 - 2 = 9 m as distance to the stormwater sewer, so the (impervious) surface will be mapped to one of the stormwater drain's connection nodes, instead of to the combined sewer's connection nodes.
* Sanitary sewer preference: This value (in meters) will be subtracted from the distance between the (impervious) surface and the sanitary sewer. See 'stormwater sewer preference' for further explanation.
* Search distance: Only pipes within search distance (m) from the (impervious) surface will be used in the algorithm.

.. _manhole_bottom_level_from_pipes:

Manhole bottom level from pipes
-------------------------------

This processing algorithm can be found via *Main menu* > *Processing* > *Toolbox* > *3Di Schematisation Editor* > *1D* > *Manhole bottom level from pipes*.

Calculate manhole bottom level from the invert levels of pipes or culverts.

For each manhole, the algorithm determines which sides of which pipes (or culverts) are connected to it, and what the invert level is at that side. It than takes the lowest of these invert levels as bottom level for the manhole.

Parameters:

- Manhole layer Manhole layer that is added to the project with the 3Di Schematisation Editor. If "Selected manholes only" is checked, only the selected manholes will be used in the algorithm.
- Pipe layer: Pipe or Culvert layer that is added to the project with the 3Di Schematisation Editor. If "Selected pipes only" is checked, only the selected pipes will be used in the algorithm.
- Overwrite existing bottom levels: If checked, bottom levels will be recalculated for manholes that already have a bottom level filled in.
- Do not raise existing bottom levels: This is only relevant if "Overwrite existing bottom levels" is checked. If checked, bottom levels will only be updated for manholes where the calculated value is lower than the existing value.

