.. _migrate_spatialite:

Migrate schematisation database
-------------------------------

When new features are introduced, new tables or new columns are added to the 3Di schematisation database. Tables and columns may also be removed or renamed. The definition of all tables, columns, and data types is called the *database schema*. If there is a new version of the database schema, older geopackages need to be *migrated* to this newer version. This migration will add or delete the tables and columns that have been changed. Tools in the 3Di Modeller Interface only work when the geopackage has the lastest database schema version and will ask you to migrate the geopackage if needed.

.. note::
  Before March 2025, the file format for the 3Di database schema was Spatialite (*.sqlite extension). Simply migrate this file to obtain a schematisation database file in geopackage format.

Sometimes it may be necessary to separately migrate the schematisation database. The :ref:`3Di Processing Algorithm<3di_processing_toolbox>` *Migrate schematisation database* can be used for this. Access this processing algorithm via *Main menu* > *Processing* > *Toolbox* > *3Di* > *Schematisation* > *Migrate schematisation database*.

The schema version shows the database schema version. The database schema is the definition of all tables, columns, and data types. If changes to the database schema are made, tools in the 3Di Modeller Interface will ask you to migrate the schematisation database to the newer database schema version. This migration will add or delete the tables and columns that have been changed.

To execute the processing algorithm, open the tool, browse to the geopackage or spatialite file and click *Run*.