.. _tutorial3_2dflowmodel:

Tutorial 3: 2D flow model for sloping terrain
=============================================

Introduction
------------
In this tutorial, you will build a basic 2D flow model in mountainous terrain using the :ref:`3Di Modeller Interface <mi_what_is>`. This tutorial will also introduce spatially variable friction and infiltration. At the end of this tutorial, you will have a basic working model that you can run simulations with.

The selected area is that of Lake Mead in the USA, just east of Las Vegas. The lake is enclosed between the mountains of Nevada, Utah, and Arizona. The area is characterized by strong elevation differences and steep slopes. Due to the steep slopes, it can not be assumed that the water level in a cell is uniform, which is a basic assumption in the :ref:`subgridmethod`. Therefore, different settings are required, which will be explored in this tutorial. For further information on how this works in 3Di, see :ref:`limiters`.

.. note::
	The data and simulation results from this tutorial cannot be used to draw conclusions of the real-world location that was the inspiration for this tutorial. The raster files that describe the variation of friction and infiltration have been highly simplified for the purpose of this tutorial.  


Learning objectives
-------------------

You will learn the following in this tutorial:

* Insight in the relevant settings for sloping terrain
* Using spatially varying friction
* Using spatially varying infiltration

Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-03.zip>`_.


Creating a new schematisation
-----------------------------
The first step is to create a new :ref:`schematisation`.

#) Open the 3Di Modeller Interface and click the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

    .. note::
        If this is the first time you use 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a  schematisation name, such as 'Tutorial Lake Mead <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now. Since we are creating a schematisation from scratch, select the *Create new Spatialite* option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.


#) Fill in the following Schematisation settings:

	* The coordinate reference system: is read from the DEM file and filled in automatically (EPSG:32612, UTM zone 12N)

	* Digital elevation model: browse to the DEM file you have downloaded (Mead_DEM.tif)

	* Computational cell size: 400

	* The model area is predominantly: Sloping

	* No 1D flow

	* No 0D flow

	* Friction type: Manning

	* Friction file: Browse to the fricton file (Mead_friction.tif) file you have downloaded

	* Global 2D friction coefficient: 0.06

	* Simulation timestep: 30 s

	* Typical simulation duration: 12-24 hours

#) Click *Create schematisation*. A popup message will tell you that the the schematisation was created. Copy the path that is shown in the popup message.


By choosing the option "The model area is predominantly sloping", the relevant *numerical settings* will be set to values suitable for calculating flow over slopes. The following parameters are set automatically; for more in-depth discussion of these parameters, see :ref:`limiters`.


	.. csv-table:: Numerical settings values specific for sloping terrain
		:header: "Setting", "Value", "Comments"

		"limiter_grad_1d", "1"
		"limiter_grad_2d", "0"
		"limiter_slope_crossectional_area_2d", "3", "For sloping areas"
		"limiter_slope_friction_2d", "1", "For sloping areas"
		"thin_water_layer_definition", "0.3", "Value in meters"
		"frict_shallow_water_correction", "3", "For sloping areas"




Viewing the schematisation
--------------------------

You will now add the schematisation in your 3Di Modeller Interface project and add a background map for reference. This will allow you to check if the schematisation looks as you expect.

#) If you have not copied the path to the spatialite in the previous step, take the following steps. At the top of the 3Di Models & Simulations panel, click the name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button (|load_from_spatialite|). Paste the path to the spatialite and click *Open*.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM, located just east of Las Vegas. In the Layers panel, in the group *Model rasters*, the layer *Friction coefficient [-]* should also be present.



.. _tut_slope_uploading:

Uploading the schematisation
----------------------------

The next step is to check the schematisation, upload it as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors that make it impossible to generate a valid 3Di model and simulation template. It will also provide guidance in the form of warnings or info messages, to help you improve the schematisation. If you have followed the instructions in this tutorial, the schematisation checker should not produce any errors, warnings or info level messages.

#) Continue to the next screen. Here you have to fill in a commit message that describes the changes your have made relative to the previous revision. As this is the first revision of this schematisation, you can instead give provide a short description of what you upload. For example: "Default settings, DEM and friction only".

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

#) At the top of the 3Di Models & Simulations panel, click the (blue, underlined) name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation/rasters*. This is the location where the infiltration raster should be copied to.

#) Open another Windows Explorer window and browse to the location where you downloaded the data for this tutorial.

#) Copy the file *Mead_infiltration.tif* to the *work in progress/schematisation/rasters* folder.

Filling in the Simple infiltration settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#) In the *Layers* panel, in the *Settings* group, click the *Simple infiltration settings* layer

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left, then click the *Add feature* button (|add_feature|). Fill in the following values from the table below and click *OK*:

	.. csv-table:: Simple infiltration settings
		:name: inf_settings_tut3
		:header: "Setting", "Value for this tutorial", "Comments"

		"id", "1", "Must match the simple_infiltration_settings_id in the v2_global_settings_table"
		"display_name", "infiltration"
		"infiltration_rate", "30", "in mm/day; when using an infiltration rate raster, this value will only be used as fallback value for NODATA pixels"
		"infiltration_rate_file", "rasters/Mead_infiltration.tif", "Do not forget to copy the raster to the correct location before uploading."
		"max_infiltration_capacity", "0.1", "100 mm of total infiltration"
		"max_infiltration_capacity_file", "NULL", "A global value is used for this parameter"
		"infiltration_surface_option", "Whole surface", "See the note below"

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

.. note::
   The *infiltration_surface_option* determines which pixels within a cell contribute to infiltration. In flat areas, infiltration is typically computed for all pixels when it is raining, and for wet pixels only when it is not raining. In sloping cells, only the pixels at the bottom of the cell would be regarded as wet, even when the water flows over the whole surface as sheet flow. In such cases, it is more appropriate to always compute infiltration for all pixels in the cell. See :ref:`infiltration` for further details.

Reference the Simple infiltration settings in the Global settings table
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now you need to reference this *Simple infiltration settings* record in the *Global settings* table.

#) In the *Layers* panel, under *Settings*, right-click the *Global settings* layer > *Open attribute table*

#) Click *Switch to form view* in the bottom right corner.

#) Click *Toggle editing mode* (|toggle_editing|).

#) In the tab *Settings IDs*, fill in the ID (1) of the *Simple infiltration settings* record you have just created.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

To make a new revision that includes these edits, you need to save the changes to the spatialite and upload them.

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite* (|save_to_spatialite|). Wait for this process to finish.

#) Upload a new revision, in the same way you did before (see :ref:`tut_slope_uploading`).


Setting the initial water level
-------------------------------

According to our elevation map, Lake Mead is located at around 340 m above mean sea level (MSL).
The deepest point of Lake Mead has a depth of 160 m at full capacity.
Therefore, we set the initial water level to a global value of 500 m MSL. This parameter can be set in the *Global settings* table.

.. note:: 
   It is also possible to set a spatially varying initial water level, by using an initial water level raster. This is very similar to how you set the spatially varying infiltration rate. An important difference is that initial water levels are set on the cell level, rather than on the pixel level. Multiple initial water level pixels can be in the same cell, so you need to instruct 3Di how to aggregate this data. There are 3 options: minimum, maximum, and average. See :ref:`initial_water_levels` for more information.
   
#) In the *Layers* panel, under *Settings*, right-click the *Global settings* layer > *Open attribute table*

#) Click *Switch to form view* in the bottom right corner.

#) Click *Toggle editing mode* (|toggle_editing|).

#) Switch to the tab *Terrain information*.

#) Set the *initial_waterlevel* to 500. This value is in m MSL.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

To make a new revision that includes these edits, you need to save the changes to the spatialite and upload them.

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite*. Wait for this process to finish.

#) Upload a new revision, in the same way you did before (see :ref:`tut_slope_uploading`).


Congratulations! You have completed the 2D flow model for sloping area. 


.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |load_from_spatialite| image:: /image/pictogram_load_from_spatialite.png
	:scale: 80%

.. |toggle_editing| image:: /image/pictogram_toggle_editing.png
    :scale: 80%

.. |add_feature| image:: /image/pictogram_addfeature.png
	:scale: 80%

.. |save_to_spatialite| image:: /image/pictogram_save_to_spatialite.png
	:scale: 80%