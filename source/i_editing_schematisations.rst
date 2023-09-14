.. _edit_schematisation:

Editing schematisations
=======================

The following edits of your schematisation are possible in the 3Di Modeller Interface:

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

Features can be copy-pasted from external data sources into the :ref:`Schematisation Editor <schematisation_editor>`. 
Check out the `QGIS Documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/attribute_table.html>`__ for how to work with the attribute table.

.. Note::
    Please note that when pasting features from external sources, the automagic actions of the 3Di Schematisation Editor will not be applied to the features. 

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

Editing feature geometries
----------------------------

For editing the geometries of features, the 'Vertex tool' can be used, see the `QGIS documentation <https://docs.qgis.org/3.28/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#vertex-tool>`__. On top of the standard QGIS functionalty, the :ref:`Schematisation Editor <schematisation_editor>` provides extra functionalities:

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

Generating exchange lines
-------------------------

A processing algorithm is available to automatically generate :ref:`Exchange lines<exchange_line>`. This processing algorithm can be found via *Main menu* > *Processing* > *Toolbox* > *3Di Schematisation Editor* > *1D2D* > *Generate exchange lines*.

This processing algorithm generates exchange lines for (a selection of) channels. The resulting exchange line's geometry is a copy of the input channel's geometry, at user specified distance from that channel (the GIS term for this is 'offset curve'). The resulting exchange lines is added to the exchange line layer, and the attribute 'channel_id' refers to the channel it was derived from.

* Input channel layer: Usually this is the Channel layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the fields 'id' and 'calculation_type' can be used as input.
* Distance: Offset distance in meters. A positive value will place the output exchange line to the left of the line, negative values will place it to the right.
* Exchange lines layer: The layer to which the results are written. Usually this is the 'Exchange line' layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the field 'channel_id' can be used.
