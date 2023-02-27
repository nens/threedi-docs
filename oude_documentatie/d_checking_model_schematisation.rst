.. _checking_model:

Checking the model schematisation
===================================

It is very useful to check your model schematisation before uploading. It can raise errors and let you solve them early on, or it can raise warnings, which you might want to solve.

*Checking the model schematisation can only be done with plugins in QGIS designed for 3Di models, which come pre-installed with the Modeller Interface.
For information how to download the Modeller Interface or the seperate plugins, please visit* :ref:`3di_instruments_and_downloads`.

.. todo:: 
    de schreenshots moeten worden aangepast + de uitleg. En er moet nog verwezen worden naar algemene uitleg plugin.
    

.. _rasterchecker:

Raster checker
^^^^^^^^^^^^^^
The *Raster checker* is launched since the QGIS 3.4.5 version of the Plugin and now available for the LTR version. This tool checks the rasters for your 3Di model schematisation. The tool verifies for example:

- The correct nodata value

- Consistent projection between rasters

- Alignment of all rasters


The principe of the raster checker is to check if your model will calculate. It does not validate on logical values and if elements are connected. 


The RasterChecker checks your rasters based on the raster references in your sqlite. 
This is done for all v2_global_setting rows. 

**The following checks are executed:**

-- Per individual raster: -- 

- 1: Are all filenames of rasters within one setting_id unique? (3Di can handle this, but the RasterChecker not).

- 2: Do the referenced rasters (in all v2_tables) exist on your machine?

- 3: Is the raster file extension .tif / .tiff?

- 4: Is the raster filename valid? (no special characters, no space, max one '.' and '/')

- 5: Is the raster single- (not multi-) band?

- 6: Is the raster nodata value -9999?

- 7: Does the raster have a projected coordinate system (unit: meters)?

- 8: Is the raster data type float 32?

- 9: Is the raster compressed? (compression=deflate)

- 10: Does the pixelsize have max three decimal places?

- 11: Are the pixels square?

- 12: Are there no extreme pixel values? (dem: -10kmMSL<x<10kmMSL, other rasters have their own limits)

-- All rasters per setting_id at once: -- 

- 13: Is the cumulative number of pixels of all rasters per setting_id lower than 1.000.000.000?

-- Raster comparison: -- 

- 14: Is the projection equal to the dem projection?

- 15: Is the pixel size equal to the dem pixel size?

- 16: Is the number of data/nodata pixels equal to the dem.

- 17: Is the number of rows-colums equal to the dem?

-- Pixel allignment: -- 

- 18: Are pixels correctly aligned (data and nodata locations) with the dem?



**How to use the raster checker?**

To use the *Raster checker*, set up a connection with the SQlite of your model. 

1) Open the *Data Source Manager* under the drop down menu *Layer* on top of the screen. 
2) Go to *SpatiaLite* and click *New*. Browse to the location of your model Sqlite and open it. 
3) Now you can close the *Data Source Manager* window.

.. figure:: image/d_qgisplugin_load_sqlite.png
    :alt: Data Source Manager


4) The *Raster checker* can be accessed by opening the Toolbox. 
5) The *Raster checker* can be found under *Step 1 - Check data*. By double clicking *raster_checker.py* the *Raster checker* is opened in a seperate window. 

.. figure:: image/d_qgisplugin_activate_rasterchecker.png
    :alt: Data Source Manager

6) Under *Model schematisation database* you can choose the spatialite of your model. 
7) Click *OK* to start the *raster checker*. When the tool is finished the following message pops-up:

.. figure:: image/d_qgisplugin_rasterchecker_done.png 
    :alt: Raster checker Done

8) The log-file of the raster checker can be found at the same location as the location of the SQlite. The log-file can be opened with a text editor such as Notepad. The log-file looks similar to:

.. figure:: image/d_qgisplugin_rasterchecker_log_header.png
    :alt: Rasterchecker Done

Here, one can also find the overview of the 18 checks that are performed. 

9) The performed checks are numbered 1 to 18. This number is called a *check_id*. 
10) Under sub-heading *Found following raster references*, there is a list with the rasters used in your model schematisation.

Further down in the log-file, the outcome of the *raster checker* for each raster is shown.

.. figure:: image/d_qgisplugin_rasterchecker_log_checks.png
    :alt: Rasterchecker Feedback

11) The first column, named *level*, shows the importance of the notification (info, warning or error). Errors need to be solved.
12) The second column, named *setting_id*, refers to the id of the row in the v2_global_settings table of the sqlite, where the raster reference can be found. 
13) The third column contains the *check_id*. 
14) The fourth column is the *feedback*, it contains the outcome of the specific verification check. 
15) If one of your rasters is not aligned with the DEM (bathymetry file), check_id 18 will give an error. Make sure all your rasters have the same extent and and have nodata pixels at the same location. 

.. _schematisationchecker:

Schematisation checker
^^^^^^^^^^^^^^^^^^^^^^^^^

The *schematisation checker* analyses your 3Di model database (.sqlite file) for completeness and consistency between tables. 
With the checker you can make sure most database errors are found before sending the model to the 3Di servers for model generation. 

In order to use the *schematisation checker* follow these steps:

1. Start the Modeller Interface
2. Add a connection to the model database (*Layer* -> *Data Source Manager*, Select *SpatiaLite* on the left and create a *'New'* connection or connect to an existing connection)
3. Open the *schematization checker* by opening the *Toolbox* in the 3Di Plugin, select *Step 1: check data*, select *schematisation_checker.py*
4. Select the SpatiaLite connection of the model database and the location where to store the output of the schematisation checker. Click *run* to run the schematisation checker. Click *open* to open the output.

The output is a comma seperated value file, which can be opened in, for example, Excel. It contains 6 columns: *id, table, column, value, description and check*:

- **id**: identification number of the row where a check encounters an error.
- **table**: the table in which the error occurs.
- **column**: the column which contains the error.
- **value**: the current value in the cell
- **description**: description of the error
- **check**: the type of check that found the error, described below

**What is checked?**

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

**TypeCheck** Every cell in every table will be checked if the type of the entered value is correct. A values in cell is expected to be a(n): 
- integer (-4, 0,1,2, etc…)
- real (3.6, -5.2)
- text
- varchar (text of limited length)
- geometry (point, linestring or polygon)
- bool (bolean, true or false)
- datetime (2019-07-02 14:27+02:00)

**EnumCheck** Some cells expect specific values. For example, the type of a boundary condition is either 1, 2, 3 or 5 (respectively water level, velocity, discharge or Sommerfeld). Any value other than the enumerated values will result in an EnumCheck error.

**NotNullCheck** If a cell is *NULL* it id empty. For some cells this is allowed, but others cells are obliged to contain a value. If this obligation is not met, a NotNullCheck error is given.

n.b. An empty text or varchar does not equal NULL.

**ForeignKeyCheck** Many tables contain foreign key columns which refer to other tables. An example is the column *connection_node_start_id* in the table *v2_channel*. This column refers to the column *id* in the table *v2_connection_node*. If a channel is entered with *connection_node_start_id = 1*, there should be an entry in the table *v2_connection_nodes* with *id = 1*. If this is not the case a ForeignKeyCheck error will be given.

**UniqueCheck** Some values have to be unique. An example is the name column in *v2_global_settings*. If multiple rows are entered with the same name, a UniqueCheck error will be given.

**GeometryCheck** If an entered geometry is invalid the GeometryCheck error will be returned. The most occurring reason for invalid geometries is self-intersection of polygons.

**GeometryTypeCheck** This check makes sure the geometry type (point, linestring or polygon) is consistent with the expected geometry type.

**BankLevelCheck** Check if the row *bank_level* of *v2_cross_section_locations* table is not NULL, when the corresponding channel is of the type *connected* or *double_connected*.

**CrossSectionShapeCheck** Each type of cross-section shape requires certain input. This check verifies if all cross-section shapes are well posed: 

- *Rectangle*: A width is required, a height is optional. The dimensions should be positive decimal numbers.
- *Circle*: Only a "width" is required. This is diameter of the circle and should be a positive decimal number.
- *Egg*: Only a "width" is required. The height is 1.5 times the width. This value should be a positive decimal number.
- *Tabulated rectangle or trapezium*: A list of widths and heights are required. The lists should contain only positive decimal numbers seperated by spaces and contain the same amount of values. The first value of *height* should always be 0. The height list should be increasing. In case the width is set to 0 m at the heighest increment, the cross-section is closed. 

**TimeseriesCheck** This check verifies if time series are correctly defined. It checks whether the time steps in that table are all the same. 

**Use0DFlowCheck** If 0D flow is configured in the global settings table, there should be at least 1 (impervious) surface defined in the model.