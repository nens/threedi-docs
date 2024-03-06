.. _schema_300:

Database schema 300
===================

A 3Di schematisation consists of rasters, vector layers and settings. The vector data and settings are stored in a database file. This database file contains a fixed set of tables, each with a fixed set of columns of a fixed type. This set of tables, columns, and data types is called the `database schema <https://en.wikipedia.org/wiki/Database_schema>`_

Sometimes, changes are made to the 3Di database schema, e.g. when new features require additional tables or columns. Each change in the database schema is numbered; you can find the schema version in the :ref:`schema_version` table. Changes to the database schema are automatically applied to your schematisation, by means of so-called 'migrations'. 

Apart from new features, the database schema is kept the same as much as possible. However, over the years, a growing number of wishes for optimizing the database schema has been collected. These changes are implemented all at once, migrating your schematisation to schema version 300 all at once. The reason to do this in one single release is so that users that use SQL, Python, or other automated methods need to do a large update of their scripts only once.

The migration to database schema 300 also includes a switch to GeoPackage as file format, instead of Spatialite.

This page aims to answer frequently asked questions on this topic.

.. _db_300_planning:

When will this development be finished?
---------------------------------------

As of March 2024, the expectation is that this development will be completed in the second quarter of 2024. At this point, it is still difficult to make a precise assessment of the release date. The estimate will be refined when as we proceed.

I don't use scripts, what will be the impact for me?
----------------------------------------------------

For 'normal'/'manual' use the impact will not be too bad. The migration from the "old" spatialites to the "new" geopackages will be automatic, in the same way that until now small changes in the database schema are automatically implemented when you open the schematization in the 3Di Modeller Interface.


Can I keep using my existing SQL or Python scripts?
---------------------------------------------------

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

Can I still run SQL on the GeoPackage?
--------------------------------------

Can I still use the views in the Spatialite to check for foreign key errors?
------------------------------------------------------------------------------






Why do we want to switch to GeoPackage?
---------------------------------------

-GeoPackage is increasingly becoming a new standard for the storage of GIS vector data, while the further development and maintenance of Spatialite is uncertain.

- Some useful tooling that is available for GeoPackage is not for Spatialite. For example, geodiff, which allows you to gain insight into differences between GeoPackages and transfer them from one GeoPackage to another.

Why do we want to change the database schema?
---------------------------------------------

- This makes the Load from Spatialite / Save to Spatialite unnecessary, which you now have to do frequently in the Schematization Editor.

- The schematisation checker then works on the data that you edit; Currently you edit the data converted to GeoPackage by the Schematization Editor, but check the Spatialite. This sometimes means that errors reported by the schematization checker are difficult to trace. For example, if there is an error in v2_cross_section_definition that does not exist in the Schematization Editor file.

- Enable direct editing by adding a geometry to all layers that currently have it via a view, such as v2_pipe_view. And by linking information about cross-sections directly to the features to which that cross-section belongs (pipe/culvert/weir/orifice/cross-section location), instead of in a separate table v2_cross_section_definition. This already works this way via the Schematisation Editor.

- Can link notifications from the schematization checker to a location, if applicable.

- Make schematising structure control much easier and more visual.

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

.. _db_300_migration_guide:

Migration guide
---------------

Download migration guides for:

- `Settings <other/db_schema_300_settings.xlsx>`__