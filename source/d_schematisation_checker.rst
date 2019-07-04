Schematisation Checker
======================

The schematization checker analyses your 3Di model database (.sqlite file) for completeness and consistency between tables. With the checker you can make sure most model errors are caught before sending the model to the INP server for model generation. 


Usage
^^^^^

1. Start *QGIS*
2. Add a connection to the model database (*Layer* -> *Data Source Manager*, Select *SpatiaLite* on the left and create a *'New’* connection or connect to an existing connection)
3. Open the schematization checker by opening the *Toolbox* in the 3Di Plugin, select *Step 1: check data*, select *schematisation_checker.py*
4. Select the SpatiaLite connection of the model database and the location where to store the output of the schematisation checker. Click *run* to run the schematisation checker. Click *open* to open the output.

The output is a comma seperated value file which can be opened in Excel. It contains 6 columns: *id, table, column, value, description and check*:

- **id: identification number of the row where a check encounters an error.
- **table: the table in which the error occurs.
- **column: the column which contains the error.
- **value: the current value in the cell
- **description: description of the error
- **check: the type of check that found the error, described below

What is checked?
^^^^^^^^^^^^^^^^

There are currently different general checks applied on all tables and columns of the model database. These checks are:

- TypeCheck
- NotNullCheck
- ForeignKeyCheck
- EnumCheck
- UniqueCheck
- GeometryCheck
- GeometryTypeCheck

Apart from the general checks on the database data and structure there are more 3Di specific checks:

- BankLevelCheck
- CrossSectionShapeCheck
- TimeSeriesCheck
- Use0DFlowCheck


TypeCheck
---------
Every cell in every table will be checked if the type of the entered value is correct. A cell is expected to either contain:

- integer (-4, 0,1,2, etc…)
- real (3.6, -5.2)
- text
- varchar (text of limited length)
- geometry (point, linestring or polygon)
- bool (true or false)
- datetime (2019-07-02 14:27+02:00)

EnumCheck
---------
Some cells expect specific values. For example, the type of a boundary condition is either 1, 2, 3 or 5 (respectively water level, velocity, discharge or Sommerfeld). Any value other than the enumerated values will result in an EnumCheck error.

NotNullCheck
------------
If a cell is NULL it does not have a value at all. For some cells this is allowed, but others cells are obliged to contain a value. If this obligation is not met, a NotNullCheck error is given
n.b. An empty text or varchar does not equal NULL

ForeignKeyCheck
---------------
Many tables contain foreign key columns which refer to other tables. An example is the column *connection_node_start_id* in the table *v2_channel*. This column refers to the column *id* in the table *v2_connection_node*. If a channel is entered with *connection_node_start_id = 1*, there should be an entry in the table *v2_connection_nodes* with *id = 1*. If this is not the case a ForeignKeyCheck error will be given.

UniqueCheck
-----------
Some values have to be unique. An example is the name column in *v2_global_settings*. If multiple rows are entered with the same name, a UniqueCheck error will be given.

GeometryCheck
-------------
If an entered geometry is invalid the GeometryCheck error will be returned. The most occurring reason for invalid geometries is self-intersection of polygons.

GeometryTypeCheck
-----------------
This check makes sure the geometry type (point, linestring or polygon) is consistent with the expected geometry type.

BankLevelCheck 
--------------
Check if the *bank_level* of *v2_cross_section_locations* is not NULL when the channel it is connected to is *connected* or *double_connected*.

CrossSectionShapeCheck
----------------------
Check if all cross section shapes are valid.
Depending on the type of shape the definition has to follow certain requirements.

Rectangle
~~~~~~~~~
A width is required, a height is optional. All supplied dimensions should be positive decimal numbers.

Circle
~~~~~~
Only a width is required, should be a positive decimal number.

Egg
~~~
Only a width is required, should be a positive decimal number.

Tabulated rectangle or trapezium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A list of widths and heights are required. The lists should contain only positive decimal numbers seperated by spaces and contain the same amount of values. The first value of *height* should always be 0. The list of heights should be in increasing order.

TimeseriesCheck
---------------
Check if timeseries are correctly entered and the timesteps are the same as all other timesteps in the same table.

Use0DFlowCheck
--------------
If 0D flow is configured in the global settings, there should be at least 1 (impervious) surface in the model.
