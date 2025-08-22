.. _basic_modelling_concepts:

Schematisations, Models & Simulations 
=====================================

In the 3Di modelling workflow, you make a *schematisation* and upload it to the server. On the server, a *3Di model* is generated. You can run *simulations* with this 3Di model, adding initial conditions, forcings and events. All this information can also be stored in a *simulation template*. 

This section explains these and related concepts in detail. The figure below provides an overview of the concepts discussed. 

.. figure:: image/a_modelling_concepts_schema.png
   :alt: A schematic overview of the 3Di Workflow modelling concepts

   A schematic overview of the 3Di Workflow modelling concepts.

.. _schematisation:

Schematisation
--------------

A *schematisation* is a simplified representation of a specific area and situation. It is the data you work with locally and the way to make edits to your 3Di model. It contains all data and parameters that 3Di needs to generate a computational grid and subgrid tables. The data format of the schematisation is a geopackage (.gpkg file) and one or several rasters. If it is a schematisation without 2D, the schematisation will not contain any rasters. A geopackage is a sqlite database file, extended with functionality for GIS data. The 3Di geopackage contains the schematisation's GIS vector data (points, lines, and polygons) and settings tables. See :ref:`schematisation_objects` for more details.

The schematisation database file also contains data that is not used to generate the 3Di model, but stored in a simulation template (see below for further details). This applies to all data that is not required for the creation of the computational grid and the subgrid tables:

- Physical, numerical, time step, aggregation and simulation template settings 

- Time series of boundary conditions and laterals

- Initial water levels (in the connection node and initial conditions layers, and the initial water level raster)

.. _revision:

Revision
--------

When you make changes to a schematisation and upload these changes, a new *revision* is created. This can be seen as an improved or updated version of the schematisation. It still represents the same specific area and situation, but is a better version of that representation.

A schematisation can have as many revisions as you like. All revisions will be stored on the server (unless you intentionally delete it).

.. _threedimodel:

3Di Model
---------
For each revision, a so called *3Di model* can be generated. A 3Di model only exists on the server and can not be downloaded or used locally. A 3Di model is the required format (i.e. a computational grid and subgrid tables) of the data for the calculation core to run a calculation.
 
There are limits to the number of 3Di models that can be stored on the server at the same time. There is a limit per schematisation (usually 3) and a limit to the total number of 3Di models for you whole organisation (the limit depends on the contract). If you want to generate a 3Di model while either of these limits has been reached, one 3Di model needs to be deleted first.

.. note::
   Please note that when deleting a 3Di Model, the revision of the schematisation will **not** be removed. This means that a deleted 3Di Model can be re-generated at any time, as long as the schematisation has no more than 3 existing 3Di Models.
   
When generating a 3Di model, a simulation template is also generated from the spatialite. See :ref:`schematisation` for details. 

.. _simulation_and_simulation_templates:

Simulations and simulation templates
------------------------------------

In a *simulation* the 3Di model is combined with simulation settings, initials, forcings and/or events. Simulation settings consist of physical, numerical, timestep, and aggregation settings. Initial conditions can be initial water levels in 1D and/or 2D, or :ref:`saved_states`. Settings and initials have to be set before starting the simulation.

Forcings can be boundary conditions, rain, laterals, surface sources and sinks, leakage, or wind. Events include breaches, changing properties of hydraulic structures, breaches, raster edits and obstacle edits. Forcings and events can be added to the simulation before it is started, but can also be added or changed while the simulation is already running.

.. todo::
   add reference to page about initial conditions when that has been written. 
   add references to all these pages
 

When the simulation has been created, a *simulation template* can be made from it. This can be done before or after the simulation has run. A simulation template is basically a copy of the simulation, which refers to the model and scenario settings that were used for the simulation. The power of a simulation template is that it can be used to start another, identical simulation, with the option to change specific settings, initials, forcings or events.

.. figure:: image/a_modelling_concepts_visual.png
   :alt: A visual overview of the 3Di Workflow modelling concepts
   
   A visual overview of the 3Di Workflow modelling concepts.
