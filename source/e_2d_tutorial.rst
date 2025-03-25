.. _tutorial2_2dflatmodel:

Tutorial 2: Creating a 2D model
===============================

Introduction
------------

In this tutorial, you will us the :ref:`3Di Modeller Interface <mi_what_is>` to build a 2D model of the Laugharne and Pendine Burrows, in Carmarthenshire (Wales). The burrows enclose a flat area of reclaimed salt marshes that are currently used as farmland.

Although the model will represent a real-world area, some processes will be simplified for the sake of this tutorial. Please keep this in mind while analysing the results of your simulations.



Learning objectives
-------------------
In this tutorial you will:

* Become familiar with the modelling workflow in 3Di
* Create a new schematisation
* Use the schematisation checker
* Upload a new revision and create a 3Di model
* Start simulations in the 3Di Modeller Interface

Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.

* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.

* Download the `Digital Elevation Model (DEM) for the Burrows area <https://demo.lizard.net/media/3di-tutorials/3di-tutorial-02.zip>`_ [#dem_attribution]_. 


Creating a new schematisation
-----------------------------

Follow these steps to create a new :ref:`schematisation`:

#) Open the 3Di Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

    .. note::
        If this is the first time you use 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a  schematisation name, such as 'Tutorial 2 <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Project and Tags are optional, you can leave these fields empty for now. Since we are creating a schematisation from scratch, select the *Create new Geopackage* option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.

#) In the section *2D Flow*, browse to the DEM (.tif) file you have downloaded. The coordinate reference system (EPSG:27700) is read from the DEM file and filled in automatically.

#) Fill in the following settings:

	* Computational cell size: 64

	* The model area is predominantly: Flat

	* No 1D flow

	* No 0D flow

	* Friction type: Manning

	* No friction file

	* Global 2D friction coefficient: 0.06

	* Simulation time step: 30 s

	* Typical simulation duration: 0-3 hours

#) Click *Create schematisation*. 

    A popup message will tell you that the the schematisation was created, asking you if you want to add it to the project. 

#) Click *Yes*

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the *Layers* panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM, located in southern Wales.

.. _tut_uploading:

Uploading the schematisation
----------------------------

The next step is to check the schematisation, upload it as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors. A schematisation that contains errors cannot be processed into a 3Di model and simulation template. The schematisation checker may also produce warnings or info level messages. These help you to improve the schematisation. If you have followed the instructions in this tutorial, the schematisation checker should not produce any errors, warnings or info level messages.

	.. note::
	   Please do not ignore warnings. These are given for schematisation choices that are usually wrong and negatively impact the performance of you model. It will still be possible generate a model from a schematisation with warnings, and there may also be special cases where your schematisation choice is intentional and you deliberately ignore the warning. If the performance of you model is sub-par, please fix any warnings before reaching out to the servicedesk.

#) Continue to the next screen. Here you have to fill in a commit message that describes the changes your have made relative to the previous revision. As this is the first revision of this schematisation, you can instead provide a short description of what you upload. For example: "Default settings, DEM only".

#) Click *Start upload*. Check if it is the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

    .. note::
        By default, on this page of the upload wizard, the checkbox *Make 3Di model* is checked, so that a 3Di model and simulation template will be generated automatically after the upload. When you start using the upload wizard regularly, you may sometimes want to upload data without generating a new 3Di model from it. For example, when the schematisation still contains errors. In that case, uncheck the *Make 3Di model* checkbox.

Your 3Di model is now ready for simulation!  

.. _tut_run_simulation:

Running a simulation 
--------------------

You will now start a simulation with the 3Di model you have created. 

#) In the 3Di Models and Simulations panel, click *Simulate* (|simulate|) > *New simulation*.  

#) Select your 3Di model and simulation template and click *Next*. A new dialog opens with several options for your simulation.  

#) Check the box for *Include precipitation*. Click *Next*.

#) Give your simulation a name. Click *Next*.

#) Set the duration of your simulation to 4 hours. Click *Next*.

#) Accept the Boundary conditions as they are by clicking *Next*.

#) Use the default Initial conditions. Click *Next*.

#) Define a Constant rain event during the first two hours with an intensity of 40 mm/h. Click *Next*. 

#) Accept the simulation settings as they are by clicking *Next*. 

#) Check the summary of your simulation and click *Add to queue*.  

Your simulation will start as soon as a calculation node is available for your organisation. Note: the number of available calculation nodes depends on your 3Di subscription. 

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.

Adding infiltration
-------------------

We will now add infiltration to the model you have just created. In this tutorial, you will set a global infiltration rate, that applies to the entire model domain. 

.. note::
   It is also possible to use a spatially variable infiltration rate by providing an infiltration rate raster file. This will be shown in :ref:`tutorial 3 <tutorial3_2dflowmodel>`.

To add infiltration to the model, you need to create a *Simple infiltration settings* record and reference it from the *Global settings*.

Follow these steps:

#) In the *Layers* panel, under *Hydrological processes*, click the *Simple infiltration* layer

#) Click *Switch to form view* in the bottom right corner.

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left corner, then click the *Add Feature* button (|add_feature|). Fill in the values from the table below (:ref:`inf_settings`) and click *OK*.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

	.. csv-table:: Simple infiltration settings
		:name: inf_settings
		:header: "Setting", "Value for this tutorial", "Comments"

		"ID", "1", ""
		"Infiltration rate [mm/d]", "360", "Uniform silty sand is assumed in this tutorial"
		"Infiltration rate file", "NULL", "Only used for spatially varying infiltration rates"
		"Infiltration surface option", "0: Whole surface when raining", "See :ref:`infiltration`"
		"Max. infiltration volume [m]", "NULL", "Infinite infiltration capacity is assumed in this tutorial"
		"Max. infiltration volume file", "NULL", "Infinite infiltration capacity is assumed in this tutorial"


Now you need to enable *Use simple infiltration* in the *Model settings* table.

#) In the *Layers* panel, under *Settings*, right-click the *Model settings* layer > *Open attribute table*

#) Click *Switch to form view* in the bottom right corner.

#) Click *Toggle editing mode* |toggle_editing| in the top left corner.

#) In the tab *Processes*, check the box for *Use simple infiltration*

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.


To make a new revision that includes these edits, you need to upload a new revision, in the same way you did before (see :ref:`tut_uploading`).


Running a simulation with infiltration
--------------------------------------

With the model that includes infiltration, run the same simulation as before (see :ref:`tut_run_simulation`).


Online access
-------------

Note that the models you have created are stored online. You can use them in 3Di Live and view them in the 3Di Management pages. 

To use the model in 3Di Live:

#) Go to `www.3di.live <www.3di.live>`_, log in and type the name of your schematisation in the search bar.

#) Select the model you want to use; #1 is the first revision (without infiltration) and #2 is the second revision (with infiltration). Click *Start*


To view the model on 3Di Management:

#) Go to `management.3di.live <management.3di.live>`_, and log in (if needed) 

#) Click on *Schematisations*

#) Type the name of your schematisation in the search bar

#) In the list, click on your schematisation 

#) On this page, you see the details of the last revision of your schematisation. You can switch to older revisions by clicking *Choose other revisions*

#) Under *3Di Model of this revision* > *Simulation templates*, you can start a 3Di Live simulation with this model, by clicking on the button with three horizontal lines > *Run on 3Di Live*




.. rubric:: Footnotes

.. [#dem_attribution] The digital elevation model contains United Kingdom public sector information licensed under the Open Government Licence v2.0.


.. images:

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |addresults| image:: /image/pictogram_addresults.png

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%

.. |simulate| image:: /image/pictogram_simulate.png
    :scale: 80%

.. |toggle_editing| image:: /image/pictogram_toggle_editing.png
    :scale: 80%

.. |add_feature| image:: /image/pictogram_addfeature.png
	:scale: 80%
