.. _tutorial2_2dflatmodel:

Tutorial 2: Creating a 2D model
===============================

Introduction
------------

In this tutorial, you will build a 2D model of the Laugharne and Pendine Burrows, in Carmarthenshire (Wales). The burrows enclose a flat area of reclaimed salt marshes that are currently used as farmland.

Although the model will represent a real-world area, some processes will be simplified for the sake of this tutorial. Please keep this in mind while analysing the results of your simulations.


Learning objectives
-------------------
In this tutorial you will:

* Become familiar with the modelling workflow in 3Di
* Learn how to create a new schematisation
* Learn how to use the schematisation checker
* Learn how to upload a new revision and creating a 3Di model
* Learn how to start simulations in the 3Di Modeller Interface

Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.

* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.

* Download the `Digital Elevation Model (DEM) for the Burrows area <https://demo.lizard.net/media/3di-tutorials/3di-tutorial-01.zip>`_ [#dem_attribution]_. 



Creating a new schematisation
-----------------------------

The first step is to create a new :ref:`schematisation`

#) Open the 3Di Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

    .. note::
        If this is the first time you use 3Di Models and Simulation panel, you will need to go through `some steps to set it up <setting_up_models_and_simulations>`.

#) Click the New button (|newschematisation|) and fill in a **unique** schematisation name, such as 'Tutorial 2 <your_name>' and select your organisation. The schematisation will be saved in the online model database of this selected organisation. Tags are optional. Since we are creating a schematisation from scratch, the *Create new Spatialite* option should be selected for the Spatialite option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.

#) In the section *2D Flow*, browse to the DEM (.tif) file you have downloaded. The coordinate reference system (EPSG:27700) is read from the DEM file and filled in automatically.

#) Fill in the following settings:
- Computational cell size: 64
- The model area is predominantly: Flat
- No 1D flow
- No 0D flow
- Friction type: Manning
- No friction file
- Global 2D friction coefficient: 0.06
- Simulation timestep: 30 s
- Typical simulation duration: 0-3 hours

#) Click *Create schematisation*. A popup message will tell you that the the schematisation was created. Copy the path that is shown in the popup message.


Viewing the schematisation
--------------------------

You will now add the schematisation in your 3Di Modeller Interface project and add a background map for reference. This will allow you to check if the schematisation looks as you expect.

#) If you have not copied the path to the spatialite in the previous step, take the following steps. At the top of the 3Di Models & Simulations panel, click on the name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button. Paste the path to the spatialite and click *Open*.

#) Add a background map from OpenStreetMap by clicking Main Menu > Web > Quick Map Services > OSM > OSM Standard.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM, located in southern England.

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

.. _tut_run_simulation:

Running a simulation 
--------------------

You will now start a simulation with the 3Di model you have created. 

#) In the 3Di Models and Simulations panel, click *Simulate* > *New simulation*.  

#) Select your model and simulation template and click *Load model*. A new dialog opens with several options for your simulation.  

#) Check the box for *Include precipitation*

#) Give your simulation a name and click next

#) Set the duration of your simulation to 4 hours. 

#) Use the default Initial conditions. Click next.  

There are several options to define a precipitation event for your simulation. In the drop-down menu, one can choose Constant, Custom, Design, Radar and Forecast events. 

Define a Constant rain event of 40 mm/h during the first two hours. Click *Next*. 

Accept the simulation settings as they are by clicking *Next*. 

Check the summary of your simulation and click Add to queue.  

Your simulation will start as soon as a calculation node is available for your organisation. Note: the number of available calculation nodes depends on your 3Di subscription. 

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.


Adding infiltration
-------------------

We will now add infiltration to the model you have just created. In this tutoriaul, you will set a global infiltration rate, that applies to the entire model domain. It is also possible to use a spatially variable infiltration rate by providing a infiltration rate raster file. 

To do this, you need to create a *Simple infiltration settings* record and reference it from the *Global settings*.

Follow these steps:

#) In the *Layers* panel, under *Settings*, click on the *Simple infiltration settings* layer > *Open attribute table*

#) Click the *Toggle editing mode* button in the toolbar, and then the *Add record* button. Fill in the following values and click *OK*:

.. csv-table:: General
    :name: inf_settings
    :header: "Setting", "Value for this tutorial", "Comments"

    "id", "1", "Must match the simple_infiltration_settings_id in the v2_global_settings_table"
    "display_name", "infiltration"
    "infiltration_rate", "360", "in mm/day; uniform silty sand is assumed in this tutorial"
    "infiltration_rate_file", "NULL", "Only used for spatially varying infiltration rates"
    "max_infiltration_capacity_file", "NULL", "infinite infiltration capacity is assumed in this tutorial"
    "infiltration_surface_option", "Rain", "See :ref:`infiltration`"

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

Now you need to reference this *Simple infiltration settings* record from the *Global settings* table.

#) In the *Layers* panel, under *Settings*, right-click the *Global settings* layer > *Open attribute table*

#) Click *Switch to form view* in the bottom right corner.

#) Click *Toggle editing mode* in the top right corner.

#) In the tab *Settings IDs*, fill in the ID (1) of the *Simple infiltration settings* record you have just created.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

To make a new revision that includes these edits, you need to save the changes to the spatialite and upload them.

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite*. Wait for this process to finish.

#) Upload a new revision, in the same way you did before (see :ref:`tut_uploading`).


Running a simulation with infiltration
--------------------------------------

With the model that includes infiltration, run the same simulation as before (see :ref:`tut_run_simulation`).


Using the same model in the browser
-----------------------------------

Note that the models you have created are stored online. You can use them in 3Di Live and view them in the 3Di Management pages. 

To use the model in 3Di Live:

#) Go to `www.3di.live <www.3di.live>`, log in and type the name of your schematisation in the search bar.

#) Select the model you want to use; #1 is the first revision (without infiltration) and #2 is the second revision (with infiltration). Click *Start*

To view the model on 3Di Management:

#) Go to `management.3di.live <management.3di.live>`, and log in (if needed) 

#) Click on *Schematisations*

#) Type the name of your schematisation in the search bar

#) In the list, click on your schematisation 

#) On this page, you see the details of the last revision of your schematisation. You can switch to older revisions by clicking *Choose other revisions*

#) Under *3Di Model of this revision* > *Simulation templates*, you can start a 3Di Live simulation with this model, by clicking on the button with three horizontal lines > *Run on live site*


.. |modelsSimulations| image:: /image/e_modelsandsimulations.png
    :scale: 90%

.. |newschematisation| image:: /image/e_newschematisation.png
    :scale: 90%

.. |addresults| image:: /image/e_addresults.png

.. |upload| image:: /image/e_tut1upload.png
    :scale: 90%


.. rubric:: Footnotes

.. [#dem_attribution] The digital elevation model contains United Kingdom public sector information licensed under the Open Government Licence v2.0.