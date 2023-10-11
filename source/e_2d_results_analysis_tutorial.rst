.. Dit is een comment

.. _dit_is_een_header_link:


Tutorial 6: Analysing 1D and 2D simulation results
==============================================

Introduction
-------------
In this tutorial, we are going to examine the results of a simulation. The schematization is pre build. The simulation results will be analysed using the :ref:`3Di Results Analysis plugin <_analysing_results>`  in the :ref:`3Di Modeller Interface <mi_what_is>`. At the end of this tutorial, you have acquired some hands on expertise for analysing the movement of water within a 3Di model.

Our area of interest is Langaa, a small railway town located in central Denmark. Langaa is situated between raised agricultural lands to the western side and the Gudena River to the eastern side of the town. The urban area has a seperated sewer system. The wastewater sewer inclines towards a pumping station, and the rainwater sewer has two outlets close to the Gudena River. While this tutorial represents a real-world area, it is important to note that some processes have been simplified for the purpose of this tutorial.

Case study
-------------

Several houses located next to the Vaethvey road are vulnerable to flooding. Recently, the inhabitants living in 21, 23, 25, 27 en 29 have reported heavy inundation after a 40mm rainfall event. Vaethvey road 21-29 is our study area. Now the municipality wants to reproduce this inundation with a hydrodynamic model, to gain insight in the flood properties such as floodextent, floodvolume, and floodduration. The municipality als wants to know where the floodwater originates from. All this isight should help to come up with potential measurements.  


Learning objectives
--------------------
You will learn the following in this tutorial:

Downloading your simulation results
Checking the flow summary
Composing the maximum waterdepth raster
Analysing the flow pattern
Finding the maximum inundation depth
Plotting waterlevels
Watershed delineation for a flooded area
Calculation the flood volume


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

.. waarom niet de DEM op de achtergrond?

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM around the city of Langaa.


Running a simulation 
----------------------

We will now start a simulation with the 3Di model you have created in the 3Di Modeller Interface: 

#) In the 3Di Models and Simulations panel, click *Simulate* (|simulate|) > *New simulation*.  

#) Select your model and simulation template and click *Next*. A dialog box opens with several options for your simulation.  

#) Check the box *Include precipitation* (keep *Include initial conditions* and *Include boundary conditions* checked). Click *Next*.

#) Give your simulation the name e.g. *Demo Langa 40mm constant rainfall in 1 hour*. Click *Next*.

#) Set the duration of your simulation to 4 hours. Click *Next*.

#) Accept the Boundary conditions as they are by clicking *Next*.

#) Accept the Initial conditions as they are by clicking *Next*.

#) Fill in the following parameters for Precipitation and then click *Next*.

    * Type of precipitation: choose *Constant*
    * Start after: 1 hrs
    * Stops after: 2 hrs
    * Intensity: 40 mm/h

#) Accept the simulation settings as they are by clicking *Next*. 

#) Check the summary of your simulation and click *Add to queue*.  

Your simulation will start as soon as a calculation node is available for your organisation. Note: the number of available calculation nodes depends on your 3Di subscription. 

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.

It is also possible to simulate your model with 3Di Live. This is explained previous tutorials.


Downloading the simulation results
----------------------

We will now download the results of your simulation to your working directory which is a local folder: 

#) In the 3Di Models and Simulations panel, click *Results* (|simulate|).

#) Select your simulation and click *Download*. A download progress bar now appears. This progress bar colors green when the downloading of your simulation results is finished.  

#) You can now find your simulation results in your working directory. The working directory is a local folder which you have defined during your Modeller Interface installation, e.g. C:\3Di_schematisations. Your can find or change this folder by clicking *Plugins* in the Main Menu > *3Di Models and Simulations* > *Settings* and then click on the *Browse* button.


Opening the simulation results
----------------------

Now we are going to load your simulation results into the Modeller Interface using the 3Di Results Analysis plugin

#) In the 3Di Results Analysis toolbar, click *3Di Results Manager*. Now the 3Di Results Manager panel opens.

#) In the 3Di Results Manager panel, click on the *Add 3Di grids or results* button.

#) Select your simulation and click *Load simulation results*, or dubble click on the name of your simulation.

Now your simulations results are loaded in the Modeller Interface and shown in your *Layers panel*.


Checking the flow summary
----------------------

In order to gain more insight in the model simulation, you can check out the flow summary. Go to the results-folder and open the document ‘flow_summary.log’.

a) Check the volume of rainfall in the log-document and translate the number back to a rainfall-intensity. Does this match the rainfall that we put on the model before the start of the model? (Hint: use the DEM-raster elevation to calculate the area. If you right-click on the ‘Digital elevation model’-layer, you can choose properties. Under the ‘information’ tab, you can find the width and height of the layer in pixels. Furthermore, under ‘pixel size’ you can find the size of the pixels in meters. If you combine this information, you can calculate the area of the elevation layer.)

b) Check out the description of the volume balance in the document and complete the figure below with the different components and the corresponding numbers. Check the water balance yourself; do the numbers add up? The filled-in water balance can be found at the end of this tutorial.

c) What is the default time step of the simulation? And the minimum time step? See that this time steps are not the same, and the minimum time step in this simulation is lower than the default time step. The model needs to calculate with a smaller time step, because otherwise the simulation becomes unstable.



Composing the maximum waterdepth raster
----------------------

In this step, we are going build a raster showing the maximum 2D waterdepth for each gridcel. 

#) Open the *Processing Toolbox*  by clicking *Processing* in the Main Menu > *Toolbox*. The  Processing Toolbox panel now opens. 

#) In the Processing Toolbox panel, click on *3Di* > *Post-process results* > then dubble click on *Maximum water depth/ level raster*. 

Now a new panel opens where we can define the settings for the maximum waterdepth raster that we are going to creat.  

#) Select your gridadmin.h5 file by clicking on de browse button browse to your working directory folder (e.g. C:\3Di_schematisations) > Demo model Langaa > revision 1 > results >  Demo Langa 40mm constant rainfall in 1 hour > gridadmin.h5.

#) Select your simulation results by clicking on de browse button, then browse to your working directory folder > Demo model Langaa > revision 1 > results >  Demo Langa 40mm constant rainfall in 1 hour > results_3di.nc.

#) Select the DEM (Digital Elevatil Model) by clicking on de browse button under DEM. Then browse to your working directory folder > Demo model Langaa > work in progress > schematisation >  rasters > Elevation_model_Langaa.tif.

#) Set the Interpolation mode to *Interpolated water depth*.

#) Set the destination file path for water depth/level raster by clicking the browse button. Browse to your working directory C:\3Di_schematisations) > Demo model Langaa > revision 1 > results and write the File name max_waterdepth_interpolated.tif.

#) Click on the *run* button.

When finished, the raster will automaticaly appear in the layers panel. Now we are going to add a basis styling to this raster:

#) Dubble click on raster name in the layer panel to open the Layer Properties window.

#) In the layer properties window, click on the left on the Symbology tab.

#) Set Render type to Singleband pseudocolor.

#) Set color ramp to Blues.

#) Fill in 0.05 as Min value and 0.5 as Max value, the unit is meters.

#) Click *OK*.


Analysing the flow pattern
----------------------
Martine?


Finding the maximum inundation depth
----------------------

We are going to use the Value Tool to view the inundation depth in our study area using your maximum waterdepth raster.

#) First we have to make sure the maximum waterdepth raster is visible. In the Layers panel, check the layer max_waterdepth_interpolated. 

#) In the Attributes Toolbar, click on the Value Tool plugin. Now the Value Tool panels opens.

#) Now zoom in to our study area and hoover with your mouse over the inundation. In the Value Tool panel you can read the raster values i.e. the maximum water depth. Find that the inundation is op to 75 cm. 


Plotting waterlevels
----------------------

#) In the 3Di Result Analysis Toolbar, click on the Time series plotter icon. Now the Value Tool panels opens. Now the 3Di Time series plotter panel opens.

#) In the 3Di Time series plotter panel, click on *Pick nodes/cells*. 

#) Click on a 2D surface water node in the study area on a inundated location. Now a graph appears for the selected 2D node.

#) Select Waterlevel in the upperleft drop down menu of the 3Di Time series plotter panel.


Watershed delineation for a flooded area
----------------------

Martine?


Calculation the flood volume
----------------------

Martine?





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