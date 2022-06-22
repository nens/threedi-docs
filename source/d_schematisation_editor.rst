.. _schematisation_editor:

Using the Schematisation Editor
===============================


Introduction
^^^^^^^^^^^^
The schematisation editor is a powerful tool that simplifies the process of building and editing schematisations. 
It automates certain tasks of the regular workflow, which enables the user to build schematisations faster while reducing the chance of making errors.
Currently, the Schematisation Editor is still in its beta phase. Eventually, the goal is to completely replace the 3Di Toolbox by the editor. 

Unlike the regular workflow, where a spatialite format is used for the storage of data, the Editor uses the *geopackage* format. 
As the integration of the Schematisation Editor is not completely finished yet, and we want to prevent having two parallel database formats, it is required to switch back and forth between the two formats each time the Editor is used and the changes are saved.
We do realize that this workflow might feel somewhat confusing or cumbersome to new users, but the high demand for the tool made us deliberately choose to release the beta version.
Once the integration of the Schematisation Editor is completely finished, the 3Di Toolbox will be replaced by the Schematisation Editor. 
With this change, the geopackage format will be the new standard for both editing and uploading.


Installation
^^^^^^^^^^^^
The easiest way to install the Schematisation Editor is by installing the newest version of the :ref:`Modeller Interface <MI_installation>`. 
If you prefer using QGIS, the Schematisation Editor can be installed by:

    #) Making sure that in the Plugins > Manage and Install Plugins > Settings the '*Show also experimental plugins*' box is checked;
    #) Searching '*3Di Schematisation Editor*' in the Plugin Management Screen, and pressing the *Install Plugin* button.
    #) Make sure that '*Enable macros*' is set to '*Always*' in Settings > Options > General > Project files. 


Loading & Saving
^^^^^^^^^^^^^^^^
.. note::
    When loading the data from a spatialite, one might receive an error on the version of the database schema. This can easily be fixed by migrating the spatialite via Processing > Toolbox > 3Di > Schematisation > Migrate spatialite.


Creating new features (digitizing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pasting features from external data sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Editing feature attributes
^^^^^^^^^^^^^^^^^^^^^^^^

Editing feature geometries
^^^^^^^^^^^^^^^^^^^^^^^^^^

Deleting features
^^^^^^^^^^^^^^^^^

