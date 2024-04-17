.. _schema_300:

Database schema 300
===================

A 3Di schematisation consists of rasters, vector layers and settings. The vector data and settings are stored in a database file. This database file contains a fixed set of tables, each with a fixed set of columns of a fixed type. This set of tables, columns, and data types is called the `database schema <https://en.wikipedia.org/wiki/Database_schema>`_

Sometimes, changes are made to the 3Di database schema, e.g. when new features require additional tables or columns. Each change in the database schema is numbered; you can find the schema version in the :ref:`schema_version` table. Changes to the database schema are automatically applied to your schematisation, by means of so-called 'migrations'. 

Apart from new features, the database schema is kept the same as much as possible. However, over the years, a growing number of wishes for optimizing the database schema has been collected. These changes are implemented all at once, migrating your schematisation to schema version 300 all at once. The reason to do this in one single release is so that users that use SQL, Python, or other automated methods need to do a large update of their scripts only once.

The migration to database schema 300 also includes a switch to GeoPackage as file format, instead of Spatialite.

This page aims to answer frequently asked questions on this topic.

Frequently asked questions
--------------------------

- :ref:`db_300_why_new_schema`
- :ref:`db_300_why_geopackage`
- :ref:`db_300_views`
- :ref:`db_300_sql_geopackage`
- :ref:`db_300_api`
- :ref:`db_300_existing_script`
- :ref:`db_300_scripts`
- :ref:`db_300_planning`


.. _db_300_planning:

When will this development be finished?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of March 2024, the expectation is that this development will be completed in the second quarter of 2024. At this point, it is still difficult to make a precise assessment of the release date. The estimate will be refined when as we proceed.

.. _db_300_scripts:

I don't use scripts, what will be the impact for me?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For 'normal'/'manual' use the impact will not be very big. The migration from the "old" spatialites to the "new" geopackages will be automatic, in the same way that until now small changes in the database schema are automatically implemented when you open the schematization in the 3Di Modeller Interface. 

However, the following things *will* have an impact when you are modelling manually:

- References to raster files were relative paths, starting from the location of the Spatialite (e.g. "rasters\dem.tif"). In schema 300, it should just be the file name ("dem.tif").

- The ``aggregation_variable`` in the aggregation settings table now uses the same variable names as are used in the computational core (and in threedigrid). The list below shows how each variable is renamed:

    - discharge -> q
    - flow_velocity -> u1
    - pump_discharge -> q_pump
    - rain -> rain
    - waterlevel -> s1
    - wet_cross-section -> au
    - wet_surface -> su
    - lateral_discharge -> q_lat
    - volume -> vol
    - simple_infiltration -> infiltration_rate_simple
    - leakage -> leak
    - interception -> intercepted_volume
    - surface_source_sink_discharge -> q_sss

- Some attribute names have changed; the most important ones are:

	- grid_space -> minimum_cell_size
	- kmax -> nr_grid_levels
	- dist_calc_points -> calculation_point_distance_1d

- Specific hydrological or hydraulic processes could be switched on or off by setting or removing a reference in the global settings; this has been replaced by a boolean (True/False) attribute. E.g. to switch off the use of simple infiltration, v2_global_settings.simple_infiltration_settings_id could be set to NULL. In schema 300, set use_simple_infiltration to False.

- Groundwater flow and groundwater storage can be switched on and off independently by setting ``use_groundwater_flow`` or ``use_groundwater_storage``. Note that you can only use groundwater flow if you also use groundwater storage. You *can* use groundwater storage without using groundwater flow.

.. _db_300_existing_script:

Can I keep using my existing SQL or Python scripts?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SQL or Python scripts that communicate with the Spatialite will need to be modified to continue working. For example, this code snippet:

.. code-block:: sql

   UPDATE v2_global_settings 
   SET name = 'a pretty name',
       grid_space = 20,
	   kmax = 3
   ;
   
   DELETE FROM v2_grid_refinement_area;


Needs to be rewritten to:


.. code-block:: sql

   UPDATE simulation_template_settings SET name = 'a pretty name';
   
   UPDATE model_settings 
   SET minimum_cell_size = 20,
	   nr_grid_levels = 3
   ;
   
   DELETE FROM grid_refinement_area;


For a detailed overview of all schema changes, see :ref:`db_300_migration_guide`.

We roll out all changes from database schema 219 to 300 all at once, so that this major adjustment to scripts and tooling is a one-time action, rather than a longer period of rolling out new changes.


.. _db_300_api:

Do I need to make changes to my scripts that interact with the 3Di API?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, this development will not affect the 3Di REST API. Uploading and downloading schematisations, starting simulations, downloading results, etc. will still work exactly the same way.

.. _db_300_sql_geopackage:

Can I still run SQL on the GeoPackage?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, GeoPackage supports the same SQL dialect as Spatialite.

.. _db_300_views:

Can I still use the views in the Spatialite to check for foreign key errors?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, the new schema will not contain any views. Run the schematisation checker to identify any attributes that are NULL but should have a value.


.. _db_300_why_geopackage:

Why does 3Di switch to GeoPackage?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-GeoPackage is increasingly becoming a new standard for the storage of GIS vector data, while the further development and maintenance of Spatialite is uncertain.

- Some useful tooling that is available for GeoPackage is not for Spatialite. For example, geodiff, which allows you to gain insight into differences between GeoPackages and transfer them from one GeoPackage to another.

.. _db_300_why_new_schema:

What are the advantages of changing the database schema?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Making *Load from Spatialite* / *Save to Spatialite* unnecessary, which you now have to do frequently (and might forget sometimes) in the Schematisation Editor.

- The schematisation checker then works on the data that you edit; Currently you edit the data converted to GeoPackage by the Schematization Editor, but check the Spatialite. This sometimes means that errors reported by the schematization checker are difficult to trace. For example, if there is an error in v2_cross_section_definition that does not exist in the Schematization Editor file.

- Enable direct editing by adding a geometry to all layers that currently have it via a view, such as v2_pipe_view. And by linking information about cross-sections directly to the features to which that cross-section belongs (pipe/culvert/weir/orifice/cross-section location), instead of in a separate table v2_cross_section_definition. This already works this way via the Schematisation Editor.

- It will allow us to add coordinates to ERROR/WARNING/INFO messages from the schematisation checker, so they can be located on the map, if applicable.

- It will make schematising structure control much easier: more visual and more intuitive.

- Being able to specify the different aspects of 1D2D exchange, storage and advection more explicitly and independently of each other, by:

    - Specify the exchange width specifically
	
    - Make exchange type (isolated/connected/embedded) an attribute of connection node instead of manhole, so that it is no longer necessary to place manholes purely to set the exchange type.
	
- A cleaner database schema, including:
	
    - Remove the "v2_" prefixes in all table names
    
	- Delete all old ("v1_") tables.
    
- Table and column names that better express (also for new users) what they mean (for example "minimum_cell_size" instead of "grid_space")
    
- Merging the (functionally almost identical) 0D inflow schematizations "v2_surface" and "v2_impervious_surface"
    
- Consistency between database schema and API, for example in naming tables and columns, options such as "interpolate" with Laterals time series, grouping of settings.
    
- Consistent and correct use of English, for example "pump" instead of "pumpstation"

.. _db_300_try_it_out:

Can I try out the new database schema while it is still under development?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, this is possible. We process the schema migrations in groups (e.g. "settings", "inflow", "1D", etc.) and release versions of the python package ``threedi-schema`` every time we have completed such a group. This Python package has functionality to migrate a schematisation to a higher version, see <https://www.github.com/nens/threedi-schema>`_.

Note that schematisations that have been upgraded with versions of threedi-schema that are higher than the one used in the 3Di Modeller Interface will not be usable in the 3Di Modeller Interface anymore (until the version of threedi-schema in the 3Di Modeller Interface is updated accordingly).

.. _db_300_migration_guide:

Migration guide
---------------

This migration guide describes the changes from database schema version 219 to database schema 300.

.. note::
    
	This migration guide is a work in progress. It will be updated and extended during development.

General changes
^^^^^^^^^^^^^^^

- All tables have been renamed to remove the "v2_" prefix; e.g. ``v2_numerical_settings`` is renamed to ``numerical_settings``.

- All geometry columns have been renamed from "the_geom" to "geom", following current (informal) conventions.

Tags
^^^^

A new feature that will be introduced is *tags*. You can define tags in the schematisation, and assign any number of these tags to each feature.

This is useful for administration of data sources and assumptions. For example, if you define a tag "Source: asset management system", you can assign this tag to all pipes that are imported from the asset management system. Pipes that are digitized by hand can be given the tag "Source: digitized by hand".


Settings
^^^^^^^^

For a complete and detailed overview of the changes in the settings tables, see <other/db_schema_300_settings.xlsx>`_


The settings that were grouped in the global settings table are split up into several tables that are consistent with (i) the grouping in the API, and (ii) the distinctions between settings required to generate the 3Di model and settings required to generate a simulation template. The contents of the global settings table can now be found in:

- **Model settings**: contains settings that are used when generating a 3Di model. A further categorisation within this table (which will be reflected in the attribute forms) is:

    - General
    - Computational grid
    - Subgrid
    - Processes
    - Other

- **Physical settings**: same as in the API, currently contains only advection-related parameters

- **Time step settings**: same as in the API, contains settings related to simulation time step and and output time step

- **Simulation template settings**: contains settings that are used when generating the simulation template

- **Initial conditions**: defines the initial (ground)water levels to be used in the simulation template

- **Interception**: defines the interception that is used in the 3Di model

The ``aggregation_variable`` in the aggregation settings table now uses the same variable names as are used in the computational core (and in threedigrid). The list below shows how each variable is renamed:

- discharge	-> q
- flow_velocity -> u1
- pump_discharge -> q_pump
- rain -> rain
- waterlevel -> s1
- wet_cross-section -> au
- wet_surface -> su
- lateral_discharge -> q_lat
- volume -> vol
- simple_infiltration -> infiltration_rate_simple
- leakage -> leak
- interception -> intercepted_volume
- surface_source_sink_discharge -> q_sss

References to raster files were relative paths, starting from the location of the Spatialite (e.g. "rasters\dem.tif"). In schema 300, it should just be the file name ("dem.tif").

Settings tables are no longer referenced from the global settings (e.g. v2_global_settings.simple_infiltration_settings_id -> v2_simple_infiltration.id). Instead, a boolean field switches the specific process on or off (e.g. use_simple_infiltration).

0D Inflow
^^^^^^^^^

- The two methods of schematisating 0D inflow (using "surfaces" and "impervious surfaces") will be merged into a single method. The surface types available for "impervious surface" will still be available, as predefined settings.

- Dry weather flow will be moved to a separate layer (with Point geometry), with its own mapping

- It will be possible to define the distribution of dry weather flow over the 24 hours of the day in the schematisation.

- Option to add tags to each feature

Boundary conditions and laterals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- New: option to specifiy time units, interpolation, and/or offset (for laterals)

- New: option to add tags to each feature


Structure control
^^^^^^^^^^^^^^^^^

Structure control is simplified and the needed tables are given geometries, so they can be schematised, visualised, and edited on the map.

- Add geometries to timed, table, and memory control
- Measurements are schematisated using a *Measure location* (point geometry) and mapped to a table or memory control using a *Measure map* (line geometry)
- The concept of *control groups* is removed for the sake of simplicity
- *Measure groups* are no longer a separate entity; measurement locations are grouped implicitly by mapping them to the same control.

2D
^^

The changes to *Dem average area*, *Obstacle*, *Grid refinement* and *Grid refinement area* will be minimal. The most important changes will be:

- New: option to add tags to each feature
- Some changes in names of tables and columns

1D2D
^^^^

There will be some impactful changes to the schematisation of 1D2D exchange, but this is mainly governed by attributes of schematisation objects in the 1D category.

The changes to *Exchange line* and *Potential breach* will be minimal. The most important changes will be:

- New: option to add tags to each feature
- Some changes in names of tables and columns

1D
^^

- Pipe, Weir, and Orifice will have their own geometry.
- *Calculation type* will be replaced by two columns: *Exchange type* and *Exchange width*
- *Manhole* will no longer have an *Calculation type*; this will be moved to *Connection node* (as *Exchange type* and *Exchange width*)
- The table *Cross-section definition* will be removed; cross-section information will directly be defined as attributes of pipes, cross-section locations, weirs, orifices, and culverts
- *Manhole* attributes that are purely intended for administrative purposes will be removed: shape, width, length, and surface_level
- *Pipe* attributes that are purely intended for administrative purposes will be removed: material
- *Pumpstation* will be renamed to *Pump*. Instead of an optional "connection_node_end_id", there will be a separate layer "Pump map"





