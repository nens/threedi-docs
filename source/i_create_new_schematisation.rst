.. _create_a_new_schematisation:

Create a new schematisation
============================

New :ref:`schematisations<schematisation>` can be created from the :ref:`models_simulation_panel`.

Creating a new schematisation from scratch
------------------------------------------

To create an entirely new schematisation, go through the following steps:

#. Open the :ref:`models_simulation_panel` (|modelsSimulations|).
#. In the *Schematisation* section, click *New* (|newschematisation|).
#. Choose a schematisation name (obligatory) and tags (optional).
#. If you have rights to more than one organisation, choose the organisation that is to own the new schematisation.
#. In the *Spatialite* section, choose the option *Create new spatialite*.
#. Click *Next*.
#. Fill in other settings, such as the projection and friction type and simulation time step.
#. Click *Create Schematisation*.

A :ref:`schematisation` has now been created on the server. The corresponding folder in your local 3Di working directory contains the spatialite and (if chosen) a DEM and/or friction raster. This data itself has not been uploaded yet. See :ref:`uploading_schematisation` for instructions to upload this data as a new :ref:`revision`.


.. _copying_existing_schematisation:

Copying an existing schematisation
----------------------------------

The *New schematisation* wizard can also be used to copy existing schematisations. This is useful when for example, you have a schematisation of the "current situation" and you want to investigate one or more alternatives for "future situations". In such a case, you can copy the current situation situation and start making changes in the copy, without affecting the original schematisation.

Go through the following steps:

#. Make sure you have :ref:`downloaded<downloading_schematisation>` the schematisation revision you want to create a copy of.
#. Open the :ref:`models_simulation_panel` (|modelsSimulations|).
#. In the *Schematisation* section, click *New* (|newschematisation|).
#. Choose a schematisation name (obligatory) and tags (optional).
#. If you have rights to more than one organisation, choose the organisation that is to own the new schematisation.
#. In the *Spatialite* section, choose the option *Choose file*.
#. Browse to the location where the spatialite is stored that belongs to the schematisation you want to copy. This is usually "<3Di working directory>\<Schematisation name>\work in progress\schematisation\<schematisation name>.sqlite"
#. Click *Create Schematisation*.

A :ref:`schematisation` has now been created on the server. The corresponding folder in your local 3Di working directory contains a copy of the spatialite and all the rasters it references. This data itself has not been uploaded yet. See :ref:`uploading_schematisation` for instructions to upload this data as a new :ref:`revision`.


.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%