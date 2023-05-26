.. _schematisation_editor:

3Di Schematisation Editor plugin
=================================

The 3Di Schematisation Editor is a powerful tool that simplifies the process of building and :ref:`editing schematisations <edit_schematisation>`. It automates certain tasks of the regular workflow, which enables the user to build schematisations faster while reducing the chance of making errors. 

The plugin comes pre-installed with the Modeller Interface and may need to be :ref:`updated <updating_plugin_schem_editor>`.

Functionality
--------------

The Schematisation Editor offers several key advantages:

* Seamless Integration: Load your schematisation from both a Geopackage and a Spatialite into the Modeller Interface effortlessly.
* Enhanced Visualization: Experience improved visualization of your schematisation. Gain a clearer understanding of the data by effectively presenting all relevant information.
* Streamlined Editing: Enjoy a streamlined editing process as your edits are directly incorporated into all appropriate layers of your schematisation. This ensures consistency and saves time by eliminating the need for manual adjustments.
* Convenient Saving: Easily save your edits to a Spatialite database, allowing for efficient data storage and retrieval. Your modifications are securely preserved for future use and analysis.

.. Note::  
    * In the regular workflow, schematisation data is stored in a *spatialite (.sqlite)* . The Schematisation Editor stores this data in a *geopackage (.gpkg)*. The database *schema* (the names and data types of tables and columns) of this geopackage also differs from the spatialite database schema. The Schematisation Editor loads the data from the spatialite into a geopackage; you make your edits in the geopackage, and when you have finished editing, save your changes to the spatialite. 
    
    * Currently, the Schematisation Editor is released as 'experimental' plugin. In a future release, we expect to replace the spatialite by the geopackage entirely (for editing as well as uploading), so that this loading and saving will no longer be necessary. Functionality for viewing and editing schematisations will be removed from the 3Di Toolbox plugin. The Schematisation Editor will remain 'experimental' until this has been completed.

Overview of the Schematisation editor toolbar
-----------------------------------------------

.. figure:: image/d_schematisation_editor_options.png
   :alt: Menu of the schematisation editor

   The Schematisation Editor options menu.

* **Open geopackage**: Loads your schematisation in the Modeller Interface, directly from the geopackage.
* **Load from Spatialite**: Load your schematisation in the Modeller Interface, by loading the data from the spatialite into a geopackage. The Schematisation Editor automatically performs the transformation and saves the *.gpkg*-file in the same folder and with the same name as the spatialite.
* **Save to Spatialite**: Saves the data back to the spatialite from which you loaded it. Do not forget to save your changes to the spatialite *before* uploading the spatialite to a new revision!
* **Save As**: Gives you the option to select another spatialite to save your data to. 
* **Remove 3Di Model**: Removes the schematisation layers from your project. 

Overview of the Schematisation editor processing toolbox
---------------------------------------------------------

The Schematisation editor toolbox can be reached by clicking on 'Processing' in the menubar > 'Toolbox' > '3Di Schematisation Editor'.

Here you can find the option 'Generate exchange lines' under the option '1D2D'. This processing algorithm generates exchange lines for (a selection of) channels. The resulting exchange line's geometry is a copy of the input channel's geometry, at user specified distance from that channel (the GIS term for this is 'offset curve'). The resulting exchange lines is added to the exchange line layer, and the attribute 'channel_id' refers to the channel it was derived from.

* Input channel layer: Usually this is the Channel layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the fields 'id' and 'calculation_type' can be used as input.
* Distance: Offset distance in meters. A positive value will place the output exchange line to the left of the line, negative values will place it to the right.
* Exchange lines layer: The layer to which the results are written. Usually this is the 'Exchange line' layer that is added to the project with the 3Di Schematisation Editor. Technically, any layer with a line geometry and the field 'channel_id' can be used.