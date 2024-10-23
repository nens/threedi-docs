.. _schema_300:

Database schema 300
===================

A 3Di schematisation consists of rasters, vector layers and settings. The vector data and settings are stored in a database file. This database file contains a fixed set of tables, each with a fixed set of columns of a fixed type. This set of tables, columns, and data types is called the `database schema <https://en.wikipedia.org/wiki/Database_schema>`_.

Changes are made to the 3Di database schema, e.g. when new features require additional tables or columns. Each new version of the database schema is numbered; you can find the schema version in the :ref:`schema_version` table. The current schema version is 219. Changes to the database schema are automatically applied to your schematisation, by means of so-called *migrations*. 3Di uses this mechanism so that even years old schematisations can be seamlessly used today. 

Other than in the case of new features, we generally keep the database schema the same as much as we can. However, over the years, a growing number of wishes for optimizing the database schema has been collected. We are now implementing all these changes. They will be released as one series of migrations, migrating your schematisation from schema version 219 to 300, so that you need to update your scripts and workflows only once.

The migration to database schema 300 also includes a switch to GeoPackage as file format, instead of Spatialite.

This page aims to answer :ref:`db_300_faq` on this topic and provides a :ref:`db_300_migration_guide`

.. _db_300_faq:

Frequently asked questions
--------------------------

- :ref:`db_300_planning`
- :ref:`db_300_scripts`
- :ref:`db_300_existing_script`
- :ref:`db_300_api`
- :ref:`db_300_sql_geopackage`
- :ref:`db_300_views`
- :ref:`db_300_why_geopackage`
- :ref:`db_300_why_new_schema`
- :ref:`db_300_try_it_out`
- :ref:`db_300_migration_guide`

.. _db_300_planning:

When will this development be finished?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The definition of the new database schema (version 300) is final and can be downloaded here: :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

- A new version of the 3Di Modeller Interface that is based on the new database schema will be released on **January 28th, 2025**

- In the meantime, the migrations (220 to 300) will be released to the 3Di server one by one. See :ref:`release_notes_api` for updates on which migrations have been released. 

.. _db_300_scripts:

I don't use scripts, what will be the impact for me?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not use scripts (e.g. SQL or Python) to interact with the 3Di schematisation files, the impact will not be very big. The migration from the "old" spatialites to the "new" geopackages will be automatic, in the same way that until now small changes in the database schema are automatically implemented when you open the schematisation in the 3Di Modeller Interface. 

However, some changes will have an impact when you are modelling manually; please read the :ref:`db_300_migration_guide` for more information.

.. note::
    Some things will actually become much easier, such as schematising structure control. Making yourself familiar with what will change will make you a more effective modeller!

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

No, the new schema will not contain any views. Run the schematisation checker to identify any attributes that are NULL that are not allowed to be NULL.


.. _db_300_why_geopackage:

Why does 3Di switch to GeoPackage?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- GeoPackage is increasingly becoming a new standard for the storage of GIS vector data, while the further development and maintenance of Spatialite is uncertain.

- Some useful tooling that is available for GeoPackage is not available for Spatialite. For example, `geodiff <https://github.com/MerginMaps/geodiff>`_, which allows you to gain insight into differences between GeoPackages and transfer them from one GeoPackage to another.

- Storing data in a Geopackage often takes up much less disk space then storing the same data in a Spatialite.

.. _db_300_why_new_schema:

What are the advantages of changing the database schema?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Making *Load from Spatialite* / *Save to Spatialite* unnecessary, which you now have to do frequently (and might forget sometimes) in the Schematisation Editor.

- The schematisation checker will work on the data that you edit. Currently, the Schematisation Editor converts the data from the 3Di Spatialite to another format, you edit this converted data, and the Schematisation Editor converts it back to the Spatialite. But the Schematisation Checker check the data in the Spatialite. Some errors reported by the schematisation checker are difficult to interpret for this reason. For example, if there is an error in the table v2_cross_section_definition, while that layer does not exist in the layers that the Schematisation Editor adds to the project.

- Many layers, such as v2_pipe, do not have their own geometry in database schema 219. To view them on the map, the spatialite used views (e.g. v2_pipe_view), but these are not editable. The 3Di Schematisation Editor adds these geometries when converting the data from the spatialite. With the new database schema, these conversions will not be necessary anymore.

- The same applies to cross-section data. In the new database schema, pipes, culverts, weirs, orifices, and cross-section locations will have attributes defining the cross-section directly, instead of referring to a cross-section definition in another table. This makes it possible to edit cross-section data directly. The 3Di Schematisation Editor also uses this approach, but will no longer need to convert the data back and forth.
 
- It will allow us to add coordinates to ERROR/WARNING/INFO messages from the schematisation checker, so they can be located on the map, if applicable.

- It will make schematising structure control much easier: more visual and more intuitive.

- It is no longer required to add a manhole to a connection node to specify the 1D2D exchange type (isolated/connected/embedded)
    
- A cleaner database schema, including
    
    - Removal of all "v2" prefixes in all table names
    
    - Removal of all old remnants of the database schema that 3Di used before "v2"
    
- Table and column names that better express what they mean, for example "minimum_cell_size" instead of "grid_space". This is particularly helpful for new users.
    
- The functionally identical 0D inflow methods "v2_surface" and "v2_impervious_surface" are merged into one method

- Dry weather flow, which is functionally separate from 0D surface inflow, is now defined in separate layers.
    
- Consistency between database schema and API, for example in naming tables and columns, options such as "interpolate" for the time series of laterals and boundary conditions, the grouping of settings, etc.
    
- Consistent and correct use of English, for example "pump" instead of "pumpstation"

.. _db_300_try_it_out:

Can I try out the new database schema while it is still under development?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, this is possible. We process the schema migrations in groups (e.g. "settings", "inflow", "1D", etc.) and release versions of the python package ``threedi-schema`` every time we have completed such a group. This Python package has functionality to migrate a schematisation to a higher version, see the `threedi-schema GitHub repository <https://www.github.com/nens/threedi-schema>`_.

Note that schematisations that have been migrated to a schema version higher than 219 are not yet usuable in the 3Di Modeller Interface. From January 28th 2025, the 3Di Modeller Interface will be compatible with schema version 300.

.. _db_300_migration_guide:

Migration guide
---------------

This migration guide describes the changes from database schema version 219 to database schema 300.

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

General changes
^^^^^^^^^^^^^^^

- All tables have been renamed to remove the *v2* prefix; e.g. *v2_numerical_settings* is renamed to *numerical_settings*.

- All geometry columns have been renamed from "the_geom" to "geom", following current (informal) conventions.

- All tables that have a geometry (in the new schema) also have a code, display name, and tags.

- Instead of using latitude/longtitude coordinates (WGS84, EPSG:4326) to define geometries, the data uses a local, projected coordinate system (set by model_settings.epsg_code). This has several benefits:

    - Measurements can be done in meters instead of degrees

    - Spatial schematisation checks no longer need to project the data before performing the check, making them faster and in some cases more accurate

    - The data as it appears on the map canvas in the 3Di Modeller Interface is exactly the same as what is used by 3Di. This is expected to fix some hard-to-solve issues with 2D boundary conditions not being located at the correct location, even though they seem to be exactly in the right location on the map.

    - It simplifies the routines used by 3Di to convert schematisation data to 3Di models, by eliminating the need to reproject the data to a projected CRS.

Tags
^^^^

A new feature is the option to add *tags* to each schematisation object. You can define tags in the schematisation, and assign any number of these tags to each feature.

This is useful for administration of data sources and assumptions. For example, if you define a tag "Source: asset management system", you can assign this tag to all pipes that are imported from the asset management system; pipes that are have been edited manually can be given the tag "Manually edited", etc.

Settings
^^^^^^^^

Tables in database schema 219:

- v2_aggregation_settings
- v2_global_settings
- v2_groundwater
- v2_interflow
- v2_numerical_settings
- v2_simple_infiltration
- v2_vegetation_drag

Tables in database schema 300:

- aggregation_settings
- groundwater
- initial_conditions
- interception
- interflow
- model_settings
- numerical_settings
- physical_settings
- simple_infiltration
- simulation_template_settings
- time_step_settings
- vegetation_drag_2d

.. note::
    For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

The most important changes are:

- References to raster files were relative paths, starting from the location of the Spatialite (e.g. "rasters/dem.tif"). In schema 300, it should just be the file name ("dem.tif").

- Settings tables are no longer referenced from the global settings (e.g. v2_global_settings.simple_infiltration_settings_id -> v2_simple_infiltration.id). Instead, a boolean field switches the specific process on or off (e.g. use_simple_infiltration).

- The settings that were grouped in the global settings table are split up into several tables that are consistent with (i) the grouping in the API, and (ii) the distinctions between settings that are required to generate a 3Di model vs. the settings that are required to generate a simulation template. The contents of the global settings table can now be found in:

    - Model settings: contains settings that are used when generating a 3Di model. A further categorisation within this table (which will be reflected in the attribute forms) General model settings, Computational grid, Subgrid, Processes, Other

    - Physical settings: same as in the API, currently contains only advection-related parameters

    - Time step settings: same as in the API, contains settings related to simulation time step and output time step

    - Simulation template settings: contains settings that are used when generating the simulation template

    - Initial conditions: defines the initial (ground)water levels to be used in the simulation template

    - Interception: defines the interception that is used in the 3Di model

- Obstacles have three new attributes to finetune which types of flowlines they affect: 2D, 1D2D open water, and/or 1D2D closed system. For this reason, it matters in which cases 3Di identifies a node as "open water" node, and subsequently sets the flowline type of 1D2D flowlines connecting to such nodes to "open water". Before database schema 300, all nodes without a storage area where regarded as open water. The new default is to regard all nodes that connect to at least one channel as open water. To make the migration backwards compatible, it is still possible to use the old method, by setting the new attribute *node_open_water_detection* in the model settings to 1. In the migration, this is automatically done to be backwards combatible. It is recommended to manually set it to 0 after the migration.
    
0D Inflow
^^^^^^^^^

Tables in database schema 219:

- v2_impervious_surface
- v2_impervious_surface_map
- v2_surface
- v2_surface_map
- v2_surface_parameters

Tables in database schema 300:

- dry_weather_flow
- dry_weather_flow_map
- dry_weather_flow_distribution
- surface
- surface_map
- surface_parameters

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

- The two methods of schematisating 0D inflow (using "surfaces" and "impervious surfaces") are merged into a single method. The surface types available for *impervious surface* will still be available as prepopulated entries in the *surface parameters* table.

- Dry weather flow is moved to a separate layer (with Polygon geometry), with its own mapping

- The intra-day distribution of dry weather flow over the 24 hours of the day is no longer fixed, but can be defined in the *dry weather flow distribution* table.

- If *Use 0D inflow* in the *Global settings* was set to 1, the data from the *Impervious surface* and *Impervious surface map* tables will be used, and data from *Surface*, *Surface map*, and *Surface parameters* will be discarded during the migration to schema version 300. If *Use 0D inflow* was set to 2, it will be the other way around.  


Boundary conditions and laterals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tables in database schema 219:

- v2_1d_boundary_conditions
- v2_1d_lateral
- v2_2d_boundary_conditions
- v2_2d_lateral

Tables in database schema 300:

- boundary_condition_1d
- boundary_condition_2d
- lateral_1d
- lateral_2d

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

The most important changes are:

- Option to specifiy the time units (seconds, minutes, or hours). Before this field was introduced, the time units where always interpreted as minutes.

- Option to switch temporal interpolation on and off

- For laterals, the option to specify an offset (the lateral will start *offset* seconds after the start of the simulation)

- 1D boundary condition and 1D lateral now have a geometry (point)

Structure control
^^^^^^^^^^^^^^^^^

Tables in database schema 219:

- v2_control
- v2_control_delta
- v2_control_group
- v2_control_measure_group
- v2_control_measure_map
- v2_control_memory
- v2_control_pid
- v2_control_table
- v2_control_timed

Tables in database schema 300:

- measure_map
- measure_location
- memory_control
- table_control

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

The changes to structure control are significant. The schema is strongly simplified, and some important changes have been made to facilitate a much more user friendly workflow. Structure control can be shown and edited on the map, because all layers involved now have a geometry.

The workflow for schematising structure control now works as follows:

#. Add a *Measure location* (point geometry) to a connection node
#. Add a *Memory control* or a *Table control* (point geometry) to a structure
#. Add a *Measure map* (line geometry) from the measure location to the memory control
#. Make sure that *Use structure control* in the simulation template settings table is switched on

Other changes:

- Timed control has been removed from the schematisation, because at the time of schematisation, it is not yet known what time period the simulation(s) will cover. Timed control can still be defined in a simulation and saved in a simulation template.

- The concept of *Control groups* is removed for the sake of simplicity

- *Measure groups* are no longer a separate entity; measurement locations are grouped implicitly by mapping them to the same control.

- The tables *Control delta* and *Control PID* were not used and have been removed. If you are interested in these types of structure control, please get in touch about the possibilities for implementing them.

2D
^^

Tables in database schema 219:

- v2_dem_average_area
- v2_grid_refinement
- v2_grid_refinement_area
- v2_obstacle

Tables in database schema 300:

- dem_average_area
- grid_refinement_area
- grid_refinement_line
- obstacle

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

The changes to these tables will be minimal. The most important changes will be:

- Obstacles have three new attributes to finetune which types of flowlines they affect: 2D, 1D2D open water, and/or 1D2D closed system. 1D2D flowlines that are categorized in "open water" or "closed system" depending on the type of the 1D node. 3Di identifies 1D nodes as "open water" if at least one channel is connected to it.

    .. note::
        Before database schema 300, all 1D nodes without a storage area where regarded as open water. The new default is to regard all nodes that connect to at least one channel as open water. To make the migration backwards compatible, it is still possible to use the old method, by setting the new attribute *node_open_water_detection* in the model settings to 1. In the migration, this is done automatically, to be backwards combatible. It is recommended to manually set it to 0 after the migration.
        
- *Grid refinement* has been renamed to *Grid refinement line*, to make its equivalence with *Grid refinement area* clearer.

- *Refinement level* has been renamed to *grid_level*, consistent with the renaming of *kmax* to *nr_grid_levels*

1D2D
^^^^

Tables in database schema 219:

- v2_exchange_line
- v2_potential_breach

Tables in database schema 300:

- exchange_line
- potential_breach

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

The most important changes is that instead of defining a maximum breach depth defined relative to the exchange level, the potential breach now has an attribute *Final exchange level*, which defines the level (in m MSL) to which the breach will grow downward. The *Exchange level* has been renamed to *Initial exchange level*.

1D
^^

Tables in database schema 219:

- v2_channel
- v2_connection_nodes
- v2_cross_section_definition
- v2_cross_section_location
- v2_culvert
- v2_manhole
- v2_orifice
- v2_pipe
- v2_pumpstation
- v2_weir
- v2_windshielding

Tables in database schema 300:

- channel 
- connection_node
- cross_section_location
- culvert
- material
- orifice
- pipe
- pump
- pump_map
- weir
- windshielding_1d
- obstacle

For a complete and detailed overview of the changes in each of the tables and columns, see the :download:`Migration guide spreadsheet <other/3Di database schema 219 to schema 300.xlsx>`

There are quite a few relevant changes in these tables: 

- A new table *Material* has been introduced, which allows you to define friction coefficients for wall materials of pipes, culverts, orifices, or weirs. It is also still possible to directly set the friction coefficient of these objects; if the friction type and friction value for an object are filled in, the material is ignored. 

- The *Manhole* layer has been merged with the *Connection node* layer, and the attributes that describe the manhole dimensions (shape, width, length) have been removed, as they were used for administrative purposes only.

- The *v2_pumpstation* layer has been split into *Pump* and *Pump map*. The pump contains all the properties of the pump, the pump map can be added to let the water be pumped to a connection node within the model domain. A pump without a pump map is equivalent to a v2_pumpstation with an empty connection_node_end_id.

- Layers that referred to connection nodes but did not have a geometry of their own, will now have a geometry:

    - Orifice
    - Pipe
    - Pump and Pump map
    - Weir

- The table *Cross-section definition* has been removed; cross-section information will directly be defined as attributes of pipes, cross-section locations, weirs, orifices, and culverts

- Cross-section data for *Tabulated rectangle*, *Tabulated trapezium*, and *YZ* will be stored in a text field (cross_section_table) as a CSV-style table, instead of in the width and height fields;

- Some fields have been renamed:

    - calculation_type -> exchange_type
    - dist_calc_points -> calculation_point_distance
    - connection_node_start_id -> connection_node_id_start
    - connection_node_end_id -> connection_node_id_end
    - invert_level_start_point -> invert_level_start
    - invert_level_end_point -> invert_level_end
    - drain_level -> exchange_level
    - manhole_indicator -> visualisation
