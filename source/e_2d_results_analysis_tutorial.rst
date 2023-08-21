.. Dit is een comment

.. _dit_is_een_header_link:


Tutorial 6: Analysing 1D and 2D simulation results
==============================================

Introduction
-------------
In this tutorial, you are going to examine the results of simulation depicting the flow of rainfall into both a river and a sewer system. The schematization is pre build. The simulation results will be analysed using the :ref:`3Di Results Analysis plugin <_analysing_results>`  in the :ref:`3Di Modeller Interface <mi_what_is>`. At the end of this tutorial, you have acquired the expertise to analyze the movement of water within your model.

Our area of interest is Langaa,a small railway town located in central Denmark. Langaa is situaed between raised agricultural lands to the western side and the Gudena River to the eastern side of the town. The urban area has a seperated sewer system. The wastewater sewer inclines towards a pumping station, and the rainwater sewer has two outlets close to the Gudena River. While this tutorial represents a real-world area, it is important to note that some processes have been simplified for the purpose of this tutorial.


Learning objectives
--------------------
You will learn the following in this tutorial:

AANPASSEN

* Adding 1D channels to a model.
* Adding boundary conditions to a 1D channel.
* Adding a linear obstacle to a model.
* Creating a potential breach event.
* Simulating the model with an active breach event.

Preparation
------------
Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-04.zip>`_. AANPASSEN 

.. TODO: zip updaten via Wolf 

Unzip the dataset for this tutorial and save the contents in your download folder. The dataset that you downloaded for this tutorial contains a 3Di schematisation (.sqlite extension) including a digital elevation model raster (DEM) for the place Langaa. The DEM is located in the folder named "rasters". 


Creating a new schematisation
------------------------------
The first step is to create a new :ref:`schematisation`:

#) Open the 3Di Modeller Interface.

#) Click the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel. If this is the first time you use the 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a schematisation name, such as 'Tutorial analysing simulation results Langaa <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now. Since you will use a pre build schematisation, select the *Choose file* option. Select the schematisation *Demo model Langaa.sqlite* extension) from your dowload folder.

#) Click *Create schematisation*. A popup message will tell you that the schematisation was created successfully. Copy the path that is shown in the popup message and paste it somewhere (e.g. in an empty text file).


Uploading the schematisation
----------------------------
We will now upload the schematisation as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog box that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors that would make it impossible to generate a valid 3Di model and simulation template. It should not produce any errors, warnings or info level messages. Click *Next*.

#) Fill in a commit message. As this is the first revision of this schematisation, you can give provide a short description of what you upload. For example: "Langaa schematisions without changes".

#) Click *Start upload*. Check whether the upload is successful and the schematisation is successfully processed into a 3Di model.  


Viewing the schematisation
--------------------------
We will load the schematisation in the 3Di Modeller Interface to view (and eventually modify) its contents. The schematisation can be loaded by following these steps:

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button (|load_from_spatialite|). Paste the previously copied path to the spatialite and click *Open*.

    If you have not copied the path to the spatialite, click the (blue, underlined) name of your schematisation at the top of the 3Di Models & Simulations panel. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM around the city of Langaa.


Running a simulation 
----------------------

You will now start a simulation with the 3Di model you have created in the 3Di Modeller Interface: 

#) In the 3Di Models and Simulations panel, click *Simulate* (|simulate|) > *New simulation*.  

#) Select your model and simulation template and click *Next*. A dialog box opens with several options for your simulation.  

#) Check the box *Include precipitation* (keep *Include initial conditions* and *Include boundary conditions* checked). Click *Next*.

#) Give your simulation a name. Click *Next*.

#) Set the duration of your simulation to 4 hours. Click *Next*.

#) Accept the Boundary conditions as they are by clicking *Next*.

#) Accept the Initial conditions as they are by clicking *Next*.

#) Fill in the following parameters for Precipitation and then click *Next*.

    * Type of precipitation: choose *Design*
    * Start after: 1 hrs
    * Design number: 10

#) Accept the simulation settings as they are by clicking *Next*. 

#) Check the summary of your simulation and click *Add to queue*.  

Your simulation will start as soon as a calculation node is available for your organisation. Note: the number of available calculation nodes depends on your 3Di subscription. 

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.

It is also possible to simulate your model with 3Di Live. This is explained previous tutorials.


Downloading the simulation results
----------------------

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.


Opening the simulation results
----------------------


----------------------
----------------------
----------------------
----------------------
----------------------



.. |load_from_spatialite| image:: /image/pictogram_load_from_spatialite.png
	:scale: 80%

.. |toggle_editing| image:: /image/pictogram_toggle_editing.png
    :scale: 80%

.. |add_line| image:: /image/pictogram_addline.png
    :scale: 80%

.. |add_point| image:: /image/pictogram_addpoint.png
    :scale: 80%

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |save_to_spatialite| image:: /image/pictogram_save_to_spatialite.png
	:scale: 80%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |Simulate| image:: /image/pictogram_simulate.png
    :scale: 80%
.. check zipje!! (nieuw zipje kan reinout of wolf online zetten voor je)