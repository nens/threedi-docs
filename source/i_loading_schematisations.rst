.. _load_schematisation:

Loading a schematisation
=========================

You can load a schematisation with the the :ref:`schematisation_editor` in the Toolbar:

#. Click on the 'Open 3Di Geopackage' or the 'Load from Spatialite' icon 
#. Select the schematisation you want to load from you local files
#. Click on 'Open'

You schematisation should now be loaded and you should be able to view all the elements in the Layers panel on the left.

.. Note:: 
    You might get the following error message: "The selected spatialite cannot be used because its database schema version is out of date. Would you like to migrate your spatialite to the current schema version?". Press 'Yes' and your schematisation should be loaded

.. Note::  
    * In the regular workflow, schematisation data is stored in a *spatialite (.sqlite)* . The Schematisation Editor stores this data in a *geopackage (.gpkg)*. The database *schema* (the names and data types of tables and columns) of this geopackage also differs from the spatialite database schema. The Schematisation Editor loads the data from the spatialite into a geopackage; you make your edits in the geopackage, and when you have finished editing, save your changes to the spatialite. 