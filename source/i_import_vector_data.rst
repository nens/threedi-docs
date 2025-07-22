.. _vector_data_importer:

Import GIS vector data
======================

GIS data can be imported to a schematisation using the 3Di Schematisation Editor's vector data importer.

.. note:: 
   Currently, this is supported for:
   
   - :ref:`culvert`
   - :ref:`orifice`
   - :ref:`weir`
   - :ref:`pipe`
   - :ref:`connection_node`

How to use the vector data importer
-----------------------------------

Use the following steps:

#. Add the vector data you want to import to your project.
#. Load the schematisation you want to import the data to using the :ref:`schematisation_editor_toolbar`.
#. If you have loaded multiple schematisations, choose the correct schematisation in the :ref:`schematisation_editor_toolbar` dropdown menu.
#. In the :ref:`schematisation_editor_toolbar`, click the vector data importer button |importVectorData| and choose the layer you want to import data into.
#. Fill in the fields in the dialog that appears. The options are explained below. 

.. note::
   Do not forget to fill in the fields in the additional tabs. E.g. if you are importing data to the Culvert layer and you check the option *Create connection nodes*, you will also need to fill in their in the *Connection nodes* tab.

Options at the top of the dialog
################################

- **Source layer**: Choose the layer *from* which you want to import features.

- **Selected features only**: Check this box if you only want to import the selected features.

- **Create connection nodes**: Check this box if you want to create connection nodes at the start and end of the schematisation object. If connection nodes are available within *snapping distance* from the start or end vertex of the imported feature, the existing connection node will be used and the start or end vertex will be snapped to the connection node.

Options in the main table
#########################

- **Field name**: Name of the target field.

- **Method**: Method with which the target field should be filled. Choose from the following options.
    
    - Auto: for ID, auto-increment from the current highest value.
    
    - Attribute: read the value from the specified attribute of the source feature. This can be a direct copy, or a value map (see below). If the source feature's attribute value is *NULL*, the *Default* value will be used (if specified).
    
    - Default: use the specified *Default* value.
    
    - Ignore: leave this attribute empty (NULL) in the target feature.
    
    - Expression: use an expression to calculate the attribute value in the target feature
    
- **Source attribute**: the attribute in the source feature to be used when the chosen method is *Attribute*

- **Value map** (optional): when using the method *Attribute* here you can specify how to translate the values encountered in the source layer (e.g. "Manning") to values in the target layer (e.g. 2). 

- **Default value**: value to be used as fallback value when using the method *Attribute* or as value for all target features when using the method *Default*

- **Expression**: expression to be used when using the method *Expression*. This expression will be evaluated for each source feature and the result written to the target feature attribute.

Options at the right-hand side of the dialog
############################################

- **Snap within**: Snapping distance. If connection nodes are available within snapping distance from the start or end vertex of the imported feature, the existing connection node will be used and the start or end vertex will be snapped to the connection node.

- **Save as template**: Save the import settings as a template (JSON file) to be used when importing similar data in the future.

- **Load template**: Load previously saved import settings from a template (JSON file).


Processing algorithm
--------------------

The vector data importer is also available as a set of Processing Algorithms in the :ref:`3di_processing_toolbox`, in the category *3Di Schematisation Editor*.

The processing algorithms work in the same way as when using the graphical user interface explained above, but most of the options are read from the configuration file (JSON) that is supplied.

* **Source layer**: Choose the layer *from* which you want to import features.

* **Import configuration file**: Choose the JSON file that contains the import settings you want to use. The easiest way to create this JSON file is by using the *Save as template* option in the graphical user interface.

* **Target schematisation database**: Choose the schematisation database file (\*.gpkg).

Configuration file (JSON)
-------------------------

This file contains all the settings that determine how the source data is read and interpreted and written to the target geopackage. The easiest way to create such a file and how to use the specific options is by using the *Save as template* option in the graphical user interface.


.. |importVectorData| image:: /image/pictogram_import_vector_data.png
    :scale: 5%
