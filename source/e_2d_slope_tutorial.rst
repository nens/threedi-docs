.. _tutorial3_2dflowmodel:

Tutorial 3: 2D flow model over sloped terrain with multiple rasters
===================================================================

Introduction
------------
In this tutorial, you will build a basic 2D flow model in mountainous terrain. We will edit an existing schematisation, and this tutorial will introduce spatially variable friction and infiltration. These raster files that describe the variation of these parameters have been highly simplified for the purpose of this tutorial. As with any other component of the tutorials, the data and outcomes cannot be used to draw conclusions of the real-world location that was the inspiration for this tutorial. 
At the end of this tutorial, you will have a basic working model that you can run simulations with.

The selected area is that of Lake Mead in the USA, just east of Las Vegas. The lake is enclosed between the mountains of Nevada, Utah, and Arizona. The area is characterized by strong elevation differences and steep slopes. Due to the steep slopes, it can not be assumed that the water level in a cell is uniform, which is a basic assumption in the :ref:`subgrid_method`. Therefore, different settings are required, which will be explored in this tutorial. For further information on how this works in 3Di, see :ref:`limiters`.

Learning objectives
-------------------

You will learn the following in this tutorial:

* Insight in the relevant settings for sloping terrain.
* Using spatially varying friction
* Using spatially varying infiltration

Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-02.zip>`_.

-------------------------------------------------------

Creating a new schematisation
-----------------------------

The first step is to create a new :ref:`schematisation`. The first revision of your schematisation will contain two raster: the digital elevation model (DEM; mandatory for all models that contain 2D) and the friction coefficients raster. The friction raster defines the bottom roughness, i.e. the amount of shear stress that the surface exerts on water flowing over it. The DEM and the friction raster can be added to the schematisation in the *New simulation* wizard.

#) Open the 3Di Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

    .. note::
        If this is the first time you use 3Di Models and Simulation panel, you will need to go through `some steps to set it up <setting_up_models_and_simulations>`.

#) Click the New button (|newschematisation|) and fill in a **unique** schematisation name, such as 'Tutorial Lake Mead <your_name>' and select your organisation. The schematisation will be saved in the online model database of this selected organisation. Tags are optional. Since we are creating a schematisation from scratch, the *Create new Spatialite* option should be selected for the Spatialite option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.

#) In the section *2D Flow*, browse to the DEM (Mead_DEM.tif) file you have downloaded. The coordinate reference system (EPSG:32612, UTM zone 12N) is read from the DEM file and filled in automatically.

#) Fill in the following settings:
- Computational cell size: 400
- The model area is predominantly: Sloping
- No 1D flow
- No 0D flow
- Friction type: Manning
- Friction file: Browse to the fricton file (Mead_friction.tif) file you have downloaded
- Global 2D friction coefficient: 0.06
- Simulation timestep: 30 s
- Typical simulation duration: 12-24 hours

#) Click *Create schematisation*. A popup message will tell you that the the schematisation was created. Copy the path that is shown in the popup message.


Viewing the schematisation
--------------------------

You will now add the schematisation in your 3Di Modeller Interface project and add a background map for reference. This will allow you to check if the schematisation looks as you expect.

#) If you have not copied the path to the spatialite in the previous step, take the following steps. At the top of the 3Di Models & Simulations panel, click on the name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button. Paste the path to the spatialite and click *Open*.

#) Add a background map from OpenStreetMap by clicking Main Menu > Web > Quick Map Services > OSM > OSM Standard.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM, located just east of Las Vegas. In the Layers panel, in the group *Model rasters*, the layer *Friction coefficient [-]* should also be present.



.. _tut_uploading:

Uploading the schematisation
----------------------------

The next step is to check the schematisation, upload its as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors that make it impossible to generate a valid 3Di model and simulation template. It will also provide guidance in the form of warnings or info messages, to help you improve the schematisation. If you have followed the instructions in this tutorial, the schematisation checker should not produce any errors, warnings or info level messages.

#) Continue to the next screen. Here you have to fill in a commit message that describes the changes your have made relative to the previous revision. As this is the first revision of this schematisation, you can instead give provide a short description of what you upload. For example: "Default settings, DEM only".

#) Click *Start upload*. Check if it is the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

    .. note::
        By default, this page of the upload wizard is set to *UPLOAD AND PROCESS*, so that a 3Di model and simulation template will be generated automatically after the upload. When you start using the upload wizard regularly, you may sometimes want to upload data without generating a new 3Di model from it. In that case, choose the *UPLOAD ONLY* option.

Your 3Di model is now ready for simulation!  


Adding spatially varying infiltration
-------------------------------------

You will now create a new revision, that also includes infiltration settings. 3Di offers two ways to use infiltration in the 2D domain: Horton infiltration, in which the infiltration rate changes over time, or *simple infiltration*, in which the infiltration rate is constant over time. To use Horton infiltration, a groundwater layer needs to be present in the model. In this tutorial, we will use *simple infiltration*. 

When using simple infiltration, the process is defined by two parameters: the infiltration rate (in mm/d) and the maximum infiltration (in m). The maximum infiltration is the the soil's capacity to store water before ponding starts. Both parameters can either be defined globally (the same value is used in the entire model domain) or using a raster file (taking spatial variation of these parameters into account by specifying a value for each pixel).

Infiltration rasters are added to the model in two steps. First, the raster needs to be moved or copied to the correct location. Second, the raster needs to be referenced from the *Simple infiltration settings* table.

Putting the raster in the right location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- At the top of the 3Di Models & Simulations panel, click on the name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation/rasters*. This is the location where the infiltration raster should be copied to.

- Open another Windows Explorer window and browse to the location where you downloaded the data for this tutorial.

- Copy the file *Mead_infiltration.tif* to the *work in progress/schematisation/rasters* folder.

Filling in the *Simple infiltration* settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#) In the *Layers* panel, in the *Settings* group, click the *Simple infiltration settings* layer

#) Click the *Toggle editing mode* button in the *Digitizing toolbar*, then click the *Add record* button. Fill in the following values and click *OK*:

.. csv-table:: General
    :name: inf_settings
    :header: "Setting", "Value for this tutorial", "Comments"

    "id", "1", "Must match the simple_infiltration_settings_id in the v2_global_settings_table"
    "display_name", "infiltration"
    "infiltration_rate", "30", "in mm/day; when using an infiltration rate raster, this value will only be used as fallback value for NODATA pixels"
    "infiltration_rate_file", "rasters/Mead_infiltration.tif", "Do not forget to copy the raster to the correct location before uploading."
    "max_infiltration_capacity", "0.1", "100 mm of total infiltration"
	"max_infiltration_capacity_file", "NULL", "A global value is used for this parameter"
    "infiltration_surface_option", "Whole surface", "See :ref:`infiltration`"

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

Reference the *Simple infiltration settings* from the *Global settings* table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you need to reference this *Simple infiltration settings* record from the *Global settings* table.

#) In the *Layers* panel, under *Settings*, right-click the *Global settings* layer > *Open attribute table*

#) Click *Switch to form view* in the bottom right corner.

#) Click *Toggle editing mode* in the top right corner.

#) In the tab *Settings IDs*, fill in the ID (1) of the *Simple infiltration settings* record you have just created.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

To make a new revision that includes these edits, you need to save the changes to the spatialite and upload them.

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite*. Wait for this process to finish.

#) Upload a new revision, in the same way you did before (see :ref:`tut_uploading`).


Setting the initial water level
-------------------------------


----------------------------------------------------------------------------------------------------------------------------------------------


You now have a model with a spatially varying elevation, friction, and infiltration, but the model settings are representative for flat areas. 

Modify the settings for mountain environments
+++++++++++++++++++++++++++++++++++++++++++++


We will modify the settings file, which was created for a flat area, such that it can be applied to sloping areas instead.
Here we will only discuss the settings that must be changed.
A full overview of all settings can be found at :download:`the database overview <pdf/database-overview.pdf>`

First, we will set the numerical settings. Modify the numerical settings via the v2_numerical_settings table.

A.	Right-click the v2_numerical_settings table.
B.	Select **Open attribute table**.
C.	Select **Switch to form view**. [1] 
D.	Select **Toggle editing mode**. [2] 
E.	Select the tab “Limiters”. [3] 
F.	Set the limiter values as in the table below. [4] 

.. csv-table:: Limiters
    :header: "Setting", "Value", "Comments"

    "limiter_grad_1d", "1"
    "limiter_grad_2d", "0"
    "limiter_slope_crossectional_area_2d", "3", "For sloped areas"
    "limiter_slope_friction_2d", "1", "For sloped areas"

.. image:: image/08_numerical1.png
    :alt: Setting numerical limiters

G.	Select the tab “Thresholds”
H.	Set the thin_water_layer_definition to 0.3. This value is in meters.
I.	Select the tab “Miscellaneous”
J.	Set the frict_shallow_water_correction to 3.  

Second, we will change how infiltration is computed in the model.
In flat areas, infiltration is typically computed in the wet subgrid cells only.
This method does not work in mountainous terrain, where the elevation differences within a cell are large.
Therefore, the infiltration will be computed over the whole surface.
This is implemented through the “infiltration_surface_option”.
Documentation on the infiltration settings can be found at :ref:`infiltration`.

A.	Right-click the v2_simple_infiltration table.
B.	Select **Open attribute table**.
C.	Select **Switch to form view**. [1] 
D.	Select **Toggle editing mode**. [2] 
E.	Set the infiltration_surface_option to 1. [3] 

.. image:: image/09_infiltration.png
    :alt: Setting infiltration options

Complete the location-specific settings
++++++++++++++++++++++++++++++++++++++++

Lake Made is a large lake with an area of 640 km2 at maximum capacity.
This leads to an extensive model domain of approximately 90 by 110 km.
The grid and the output settings are adjusted to account for the large model domain.
The initial water level will also be modified to match the elevation of the lake.

First, we will set the grid cell size and the table step size to improve the calculation speed of the model.
The grid cell size will be set to 400 m in accordance with the large domain.
The table step size controls at which vertical resolution properties (other than elevation) are translated from the subgrid domain to the computational domain.
A table step size of 10 m is selected for this model. This is very coarse for a typical 3Di model, but it is justified here due to the large elevation differences at the subgrid level.
Both properties are part of the global settings.

A.	Right-click the v2_global_settings table.
B.	Select **Open attribute table**.
C.	Select **Switch to form view**. [1] 
D.	Select **Toggle editing mode**. [2] 
E.	Select the tab “Grid”. [3] 
F.	Set the grid_space to 400. This value is in meters. [4] 
G.	Set the table_step_size to 10.  This value is in meters. [5] 
H.	Keep the global settings table open.


.. image:: image/10_grid_settings.png
    :alt: Changing grid settings

According to our elevation map, Lake Mead is located at around 340m above sea level.
The deepest point of Lake Mead has a depth of 160 m at full capacity.
Therefore, we set the initial water level at 500m.

A.	Select the tab “Terrain Information”.
B.	Set the initial_waterlevel to 500. This value is in meters.
C.	Keep the global settings table open

The discharge of precipitation into Lake Mead takes a long time due to the large model domain.
The number of time steps and the time between model outputs is increased to reflect the slow time scale.
More time steps and a larger output time step are selected to account for the slower drainage. 

A.	Select the tab “Time”.
B.	Set the nr_timesteps to 1440. This amounts to a model duration of 12 h, as the time step is 30 s.
C.	Set the output_time_step to 900.  This value is in seconds.
D.  Save you changes.

The aggregation time step is also set to 900 s. This has already been set correctly in your .sqlite. 

With the completion of the location-specific settings, we have built a basic working 2D flow model for mountainous terrain. 
