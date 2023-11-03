Tutorial 6: Analysing 1D and 2D simulation results
==============================================

Introduction
-------------
In this tutorial, we are going to examine the results of a simulation. The schematization is pre build. The simulation results will be analysed using the :ref:`3Di Results Analysis plugin <_analysing_results>`  in the :ref:`3Di Modeller Interface <mi_what_is>`. At the end of this tutorial, you have acquired some hands on expertise for analysing the movement of water within a 3Di model.

Our area of interest is Langaa, a small railway town located in central Denmark. Langaa is situated between raised agricultural lands to the western side and the Gudena River to the eastern side of the town. The urban area has a seperated sewer system. The wastewater sewer inclines towards a pumping station, and the rainwater sewer has two outlets close to the Gudena River. While this tutorial represents a real-world area, it is important to note that some processes have been simplified for the purpose of this tutorial.

Case study
-------------
Several houses located next to the Vaethvey road are vulnerable to flooding. Recently, the inhabitants living in 21, 23, 25, 27 en 29 have reported heavy inundation after a 40mm rainfall event. Vaethvey road 21-29 is our study area. Now the municipality wants to reproduce this inundation with a hydrodynamic model, to gain insight in the flood properties such as floodextent, floodvolume, and floodduration. The municipality als wants to know where the floodwater originates from. All this isight will help to come up with potential measurements.  


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

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM around the city of Langaa.


Running a simulation 
----------------------

We will now start a simulation with the 3Di model you have created in the 3Di Modeller Interface: 

#) In the 3Di Models and Simulations panel, click *Simulate* (|simulate|) > *New simulation*.  

#) Select your model and simulation template and click *Next*. A dialog box opens with several options for your simulation.  

#) Check the box *Include precipitation* (keep *Include initial conditions* and *Include boundary conditions* checked). Click *Next*.

#) Give your simulation the name e.g. *Demo Langaa 40mm constant rainfall in 1 hour*. Click *Next*.

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

Now we are going to load your simulation results into the Modeller Interface using the 3Di Results Analysis plugin:

#) In the 3Di Results Analysis toolbar, click *3Di Results Manager*. The 3Di Results Manager panel now opens.

#) In the 3Di Results Manager panel, click on the *Add 3Di grids or results* button.

#) Select your simulation and click *Load simulation results*, or dubble click on the name of your simulation.

Now your simulations results are loaded in the Modeller Interface and shown in your *Layers panel*.


Checking the flow summary
----------------------

In order to gain more insight in the simulation, we check out the flow summary. 

#) Go to the results-folder of your schematisation in the working directory. Open the document *flow_summary.log*.

First, you are going to check if the total rainfall volume in the *flow_summary.log* matches the rainfall event (40mm in one hour).

#) Knowing the rainfaill intensity (40mm), we still need the area for calculating the rainfall volume. Right-click on the *Digital elevation model*-layer and choose *properties*. Under the *information* tab, you can find the width and height of the layer in pixels. Furthermore, under *pixel size* you can find the size of the pixels in meters. Combine this information to calculate the area of the DEM and the total rainfall volume. 

Secondly, you are going to volume balance the better understand de functioning of the model.

#) Draw your own water balance, indicating the inflow, volume change, and outflow. Alternatively you can use the empty balancy below:

|langaa_waterbalans_leeg|

#) Now fill in the waterbalance with the numbers you find in the *flow_summary.log*. Check the water balance yourself; do the numbers add up? 

The filled-in water balance can be found below:

|langaa_waterbalans_antwoord|

.. TO Do: Martine om .ppt bestand vragen van de afbeeldingen om m3 netjes te schrijven en af te ronden om minder decimalen


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

Now we are going to take a first look on the movement of water on surface by visualising the flow pattern:

#)	First, we are going the load the results from your simulation. Open the 3Di result Manager by clicking on the *3Di results manager* icon (PLAATJE). 
 
#)	Click on *ADD 3Di Grid or Results* (PLAATJE green *plus*-sign). A pop-up screen appears where you can select the simulation results. Then click on *Load simulation result*. The results will now be added to your screen.

#)	Now click on *3Di result aggregation* (PLAATJE) in the 3Di Results Analysis toolbar. A pop-up screen will appear.
 
#)	In the *input* tab, the result is selected automatically.

#)	Under *preset*, you can select different aggregation results. For now, select *Flow pattern*. If you are interested, you can play around with the different other options later. Press *OK*. The flow pattern will now be derived and visualized in your screen. 

#)	You can zoom in on the flow pattern to discern the individual arrows. As you can see, the direction of the arrow indicates the direction of the flow. Furthermore, the color of the arrow is an indicator for the relative discharge.

#)	Zoom out again to see the general flow pattern in the model area. Look at the elevation map and the flow pattern; note that the water flows from the higher areas towards the lower areas and a large part eventually ends up in the river.


Finding the maximum inundation depth
----------------------

We are going to use the Value Tool to view the inundation depth in our study area using your maximum waterdepth raster.

#) First we have to make sure the maximum waterdepth raster is visible. In the Layers panel, check the layer *max_waterdepth_interpolated*. 

#) In the Attributes Toolbar, click on the Value Tool plugin (PLAATJE ICOON). Now the Value Tool panels opens.

#) Now zoom in to our study area and hoover with your mouse over the inundation. In the Value Tool panel you can read the raster values i.e. the maximum water depth. Find that the inundation is up to 75 cm. 


Plotting waterlevels
----------------------

#) In the 3Di Result Analysis Toolbar, click on the Time series plotter icon. Now the Value Tool panels opens. Now the 3Di Time series plotter panel opens.

#) In the 3Di Time series plotter panel, click on *Pick nodes/cells*. 

#) Click on a 2D surface water node in the study area on a inundated location. Now a graph appears for the selected 2D node.

#) Select Waterlevel in the upperleft drop down menu of the 3Di Time series plotter panel.


Watershed delineation for a flooded area
----------------------

To better understand why an area gets flooded and to design appropriate measures to decrease flood risks in the future; we want to know where the water in the flooded area comes from. We will now use the Watershed Tool to answer this question. The Watershed Tool allows you to determine the upstream and downstream catchment at any point or area. Follow the steps below to use the watershed tool:

#) First we have to make sure the maximum waterdepth raster is still visible. In the Layers panel, check the layer *max_waterdepth_interpolated*. 

#)	Now, open the Watershed tool (PLAATJE) in the 3Di Results Analysis toolbar.
 
#)	In the Watershed tool, first define the Input. Select yout results under *3Di results*.

#)	Under *Settings*, you can adjust the period for which you want to carry out the watershed analysis by adjusting the start and end time. Furthermore, you can adjust the threshold. If there is a net flow from the upstream element to the target node(s) above the defined threshold, the upstream element is included in the catchment. For now, you do not need to change the settings.

#)	The next step is to define the target nodes. Click on *Click on canvas* and select the nodes in our study area (Vaethvey road 21-29).
 
The tool automatically calculates the upstream catchment area for the nodes that you selected. The result of the analysis is depicted in the figure below. By choosing *Clear results*, the catchment will disappear and you can choose different nodes to derive the upstream catchment for.  

#)	Now click *Downstream* instead of *Upstream* to derive the downstream catchment of your selected nodes. The result gives us a indication on how the flood volume is drained during and after the event.


Calculation the flood volume
----------------------

Lastly, we are going to use the water balance-tool to determine the flood volume for in our study area.

In the schematization, you can see that a grid refinement was implemented in the area of the town that gets flooded: our study area (Vaethvey road 21-29). 
 
#)	Click on Water balance tool (PLAATJE) in the 3Di Results Analysis toolbar.  
 
#)	Choose *Select polygon* and click on the grid refinement area. Choose *grid refinement area (study_area)* in the popup menu. The tool will now automatically calculate and visualize the water balance for this area.

#)	In the water balance, you can choose to show both discharges and volumes. The tool is automatically set to discharge. Now change to volume by using the dropdown menu and choose the *m3 cumulative* option. 
 
#)	In the graph, the cumulative volumes of water for different components in the model are displayed. At the right side you can activate and deactivate different options, to visualize different flow components. Hover over the different components to see which ones are indicated in the graph. 

#)	The main component that is of interest in this question is *2D flow*. Notice that the graph displays both a positive and negative cumulative 2D Flow. This is caused by the fact that the 2D flow is both entering (positive) and leaving (negative) the study area. The net 2D flow is represented by the dotted red line, representing the *volume change 2D*. Use your mouse to zoom in on the y-axis, you can check the net 2D volume change at the end of the simulation. Check that the floow volume is about 3200 m3. 

.. |langaa_waterbalans_leeg| image:: /langaa_waterbalans_leeg.png
	:scale: 100%

.. |langaa_waterbalans_antwoord| image:: /image/langaa_waterbalans_antwoord.png
	:scale: 100%

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