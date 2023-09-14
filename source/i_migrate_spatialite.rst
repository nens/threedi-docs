.. _migrate_spatialite:

Migrate spatialite
------------------

When new features are introduced, new tables or new columns are added to the 3Di spatialite database. Tables and columns may also be removed or renamed. The definition of all tables, columns, and data types is called the *database schema*. If there is a new version of the database schema, older spatialites need to be *migrated* to this newer version. This migration will add or delete the tables and columns that have been changed. Tools in the 3Di Modeller Interface only work when the spatalite has the lastest database schema version and will ask you to migrate the spatialite if needed.

Sometimes it may be necessary to separately migrate the spatialite database. The :ref:`3Di Processing Algorithm<3di_processing_toolbox>` *Migrate spatialite* can be used for this. Access this processing algorithm via *Main menu* > *Processing* > *Toolbox* > *3Di* > *Schematisation* > *Migrate spatialite*.

The schema version shows the database schema version. The database schema is the definition of all tables, columns, and data types. If changes to the database schema are made, tools in the 3Di Modeller Interface will ask you to migrate the spatialite to the newer database schema version. This migration will add or delete the tables and columns that have been changed.

To execute the processing algorithm, open the tool, browse to the spatialite file and click *Run*.