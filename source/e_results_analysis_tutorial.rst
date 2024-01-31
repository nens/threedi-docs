Tutorial 6: Analysing simulation results
========================================

Introduction
------------

In this tutorial, we explore how you can analyse simulation results using the :ref:`3Di Modeller Interface<mi_what_is>`. This tutorial is a bit longer than the previous tutorials. It has a number of sub-sections:

- :ref:`tut6_simulation`
- :ref:`tut6_impact`
- :ref:`tut6_why`
- :ref:`tut6_quant`


Case study
##########

Our study is Langå, a small railway town located in central Denmark. 

.. image:: /image/e_langaa_overview_map.png
	:scale: 100%
	:alt: Overview of the modelled area: Langå, Denmark

Langå is situated between raised agricultural lands to the west and the Gudena River to the east of the town. The urban area has a seperated sewer system. The sanitary sewer inclines towards a pumping station, and the stormwater sewer has two outlets close to the Gudena River.

Several houses on Vaethvey road (numbers 21-29) are vulnerable to flooding. Recently, the inhabitants living there have reported flood problems after a 40 mm rainfall event. 

.. image:: /image/e_langaa_aoi.png
	:scale: 80%
	:alt: Vaethvey road 21-29, Langå, Denmark

Now the municipality wants to reproduce this inundation with a hydrodynamic model, to gain insight in the flood properties such as flood extent, flood volume, and flood duration. The municipality also wants to know where the flood water originates from. These insights will help the municipal government to design measures to reduce the flood risk.  

.. note::
    While this tutorial represents a real-world area, it is important to note that some processes have been simplified for the purpose of this tutorial and that the situations described in it are hypothetical.


Learning objectives
###################

You will learn the following in this tutorial:

- Downloading simulation results

- Checking the flow summary

- Generaring a maximum inundation depth raster

- Analysing the flow pattern

- Finding the maximum inundation depth

- Plotting water levels

- Watershed delineation for a flooded area

- Calculating the flood volume


Preparation
###########

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/langaa.zip>`_.
* Unzip the dataset for this tutorial and save the contents in your *Downloads* folder.

The dataset that you downloaded for this tutorial contains a 3Di schematisation, consisting of a Spatialite (.sqlite file) and a Digital Elevation Model (.tif file) for the place Langå. The DEM is located in the folder named "rasters".

.. _tut6_simulation:

Running the simulation
----------------------

We will go through a number of steps to run a simulation, to have results that we can analyse. These steps should mostly be familiar if you have already done one or more of the previous tutorials. 

Creating a new schematisation
#############################

The first step is to create a new :ref:`schematisation`:

#) Open the 3Di Modeller Interface.

#) Click the |modelsSimulations| 3Di Models and Simulations. You should now see the 3Di Models and Simulations panel. If this is the first time you use the 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click |newschematisation| *New*. The *New schematisation* wizard is shown.

#) Fill in a schematisation name, such as 'Tutorial analysing simulation results Langaa <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now. Since you will use a pre-built schematisation, select the *Choose file* option. Select the schematisation file *Demo model Langaa.sqlite* from your Downloads folder.

#) Click *Create schematisation*. A popup message will tell you that the schematisation was created successfully.


Uploading the schematisation
############################

We will now upload the schematisation as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the |upload| upload button in the 3Di Models and Simulations panel.

#) In the dialog box that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisation for any errors that would make it impossible to generate a valid 3Di model and simulation template. It should not produce any errors, warnings or info level messages. Click *Next*.

#) Fill in a commit message. This is a short description of the changes you have made relative to the previous revision. As this is the first revision of this schematisation, you can provide a short description of what you upload. For example: "Langå schematision without changes".

#) Click *Start upload*. Check whether the upload is successful and the schematisation is successfully processed into a 3Di model.  


Viewing the schematisation
##########################

We will load the schematisation in the 3Di Modeller Interface to view it. Later in this tutorial we will also make some modifications. The schematisation can be loaded by following these steps:

#) In the 3Di Schematisation Editor toolbar, click the |load_from_spatialite| *Load from Spatialite* button.

#) Double-click the name of the schematisation you want to load.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*. 

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM around Langå.


Running a simulation
####################

We will now start a simulation with the 3Di model you have created in the 3Di Modeller Interface: 

#) In the 3Di Models and Simulations panel, click |simulate| *Simulate*  > *New simulation*.  

#) Select your model and simulation template and click *Next*. A dialog box opens with several options for your simulation.  

#) Check the box *Include precipitation*. Keep *Include initial conditions* and *Include boundary conditions* checked. Click *Next*.

#) Give your simulation a name, e.g. *Demo Langaa 40mm constant rainfall in 1 hour*. Click *Next*.

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

You may also :ref:`follow the simulation in 3Di Live<follow_a_session>`.

.. _tut6_impact:

Assessing the flood impact
--------------------------

Now that we have ran the simulation, we can start analysing. Our first step will be to assess the flood impact: where does it flood, with what depths and for how long?


Downloading the simulation results
##################################

We will now download the results of your simulation to your working directory which is a local folder: 

#) In the 3Di Models and Simulations panel, click *Results* |download_results|.

#) Select your simulation and click *Download*. A download progress bar now appears. This progress bar colors green when the downloading of your simulation results is finished.  

.. note::
  The simulation results are saved in your 3Di working directory. To open this folder, click on the name of the schematisation in the 3Di Models & Simulations panel.


Opening the simulation results
##############################

Our next step is to load the simulation results in the 3Di Modeller Interface.

#) In the :ref:`results_analysis_toolbar`, click the *3Di Results Manager* button |results_manager|. The 3Di Results Manager panel now opens.

#) In the 3Di Results Manager panel, click on the |add_results| *Add 3Di grids or results* button.

#) Select your simulation and click *Load simulation results*, or double click the name of your simulation.

Now your simulations results are loaded in the 3Di Modeller Interface and shown in the *Layers panel*.


Checking the flow summary
#########################

As a first step of gaining insight in the simulation, we will check out the :ref:`flow_summary`. 

#) In the 3Di Models & Simulations panel, click on the name of the schematisation to open the folder where the simulation results are downloaded to. 

#) Open the document *flow_summary.json*.

First, we will check if the total rainfall volume in the *flow_summary.log* matches the rainfall event (40mm in one hour). To be able to calculate this, we need to know the surface area of the model.

#) In the 3Di Modeller Interface, in the Layers panel, right-click on the layer *Digital elevation model* > *Properties*. 

#) Under the *Information* tab, in the *Information from provider* section, you can find the width and height (in pixels), and pixel size (in meters). Combine this information to calculate the area of the DEM and the total rainfall volume. Does it correspond with the total rain on 2D reported in the Flow summary? 

.. note::
   The 3Di Model in this example is atypical in that it is perfectly rectangular. All pixels in the DEM have a value. Most 3Di Models have a boundary that follows hydrogical watershed boundaries. DEM pixels outside of these boundaries are "no data" pixels. In such a case, the method used here for calculating the surface area of the model does not work. Instead, use the QGIS Processing Algorithm "Zonal statics", with an input polygon that covers the entire model domain, and choose "Count" as one of the statistics to calculate.

Secondly, you are going to volume balance the better understand de functioning of the model.

#) Draw your own water balance, indicating the inflow, volume change, and outflow. Alternatively, you can use the empty balance below:

|langaa_waterbalans_leeg|

#) Now fill in the water balance with the numbers you find in the flow summary. Check the water balance yourself; do the numbers add up? Does the difference correspond with the volume error reported in the flow summary?

The filled-in water balance can be found below:

|langaa_waterbalans_antwoord|


Generating the maximum water depth raster
#########################################

In this step, we are going generate a maximum inundation depth map. 

#) Open the *Processing Toolbox* (*Main Menu* > *Processing* > *Toolbox*). 

#) In the Processing Toolbox panel, click on *3Di* > *Post-process results* > then double click *Maximum water depth / level raster*. 

Now a new panel opens where we can define the settings for the maximum water depth raster that we are going to create.  

#) Select your gridadmin.h5 file by clicking on the browse button and browse to your working directory folder (e.g. C:\3Di_schematisations) > Demo model Langaa > revision 1 > results >  Demo Langa 40mm constant rainfall in 1 hour > gridadmin.h5.

#) Select your simulation results file (results_3di.nc). This file is located in the same directory as the gridadmin.h5 file.

#) Select the DEM (Digital Elevation Model) by clicking on the browse button under DEM. Browse to your working directory > Demo model Langaa > work in progress > schematisation >  rasters > Elevation_model_Langaa.tif.

#) Set the Interpolation mode to *Interpolated water depth*.

#) Set the destination file path for water depth/level raster by clicking the browse button. Browse to your working directory > Demo model Langaa > revision 1 > results. 

#) Write the file name max_water_depth_interpolated.tif.

#) Click *Run*.

When finished, the raster will automaticaly appear in the *Layers* panel. Now we are going to add a basic styling to this raster.

#) In the *Layers* panel, double click the layer max_water_depth_interpolated. The Layer Properties window opens.

#) In the layer properties window, the *Symbology* tab (at the left side).

#) Set *Render type* to *Singleband pseudocolor*.

#) Set *Color ramp*/ to Blues.

#) Fill in 0.0 as Min value and 0.5 as Max value. These are units in meters.

We will now make all water depths between 0 and 1 cm transparent.

#) In the *Transparency* tab, under *Custom transparency options*, click the + button.

#) For *From*, fill in 0; for *To*, fill in 0.01.

#) Click *OK*.


Finding the maximum inundation depth
####################################

We are going to use the Value Tool to view the inundation depth in our study area using the maximum water depth raster.

#) First, make sure the maximum water depth raster is visible. In the Layers panel, check the layer *max_water_depth_interpolated*. 

#) In the Attributes Toolbar, click on the |value_tool| Value Tool button. Now the Value Tool panels opens.

#) Now zoom in to our study area; with your mouse, hoover over the inundated area. In the Value Tool panel, you can read the raster values, i.e. the maximum inundation depth. Find that the inundation is up to 75 cm.


How long does the inundation last?
##################################

#) In the 3Di Result Analysis Toolbar, click on the *Time series plotter* icon. Now the 3Di Time series plotter panel opens.

#) In the 3Di Time series plotter panel, click on *Pick nodes/cells*. 

#) Click on a 2D surface water node in the study area in an inundated location. A graph is plotted for the selected 2D node.

#) Select *Water level* in the upperleft drop-down menu of the 3Di Time series plotter panel.

.. _tut6_why:

Why does the inundation occur?
------------------------------

Now that we have established the impact and severity of the flooding, we will look into why it happens at this location. If we know where the water comes from, we know where we can add extra buffer capacity. If we know which routes the water follows, we may be able to change those routes. We may also be able to drain water from the area more quickly.

Analysing the flow pattern
##########################

Now we are going to take a first look into how the water flows through the modelled area, by visualising the flow pattern.

First, we are going the load the results from your simulation. 

#) Click the |results_manager| *3Di Results Manager* icon. 
 
#) Click |add_results| *Add 3Di Grid or Results*. 

#) A pop-up screen appears where you can select the simulation results. Double-click your downloaded results. 

The results will now be added to the project.

#) In the 3Di Results Manager, click the |closed_eye| icon. 

In the layers panel, the node, flowline and cell layers have been renamed to the variable that is visualised. 

#) Toggle the *Node* and *Cell* layers to invisible.

You now see the net cumulative discharge over the whole simulation for each flowline. You may move the time slider in the *Temporal Controller* at the top of the screen to view the results for earlier moments in the simulation. In the 3Di Results Manager panel, you can also change the visualised variable to *Discharge* to get a snapshot of the situation at the time step you have navigated to in the *Temporal Controller*.

Another way to analyse the flow pattern is by using the *3Di Results Aggregation* tool. 

#) Click |resultsaggregationtoolbar| *3Di Result Aggregation* in the *3Di Results Analysis toolbar*. A pop-up screen will appear.
 
#) In the *Input* tab, the simulation result is selected automatically.

#) Under *Preset*, select *Flow pattern*. If you are interested, you can play around with the other presets options later. Click *OK*. The flow pattern will now be derived and thre resulting layer will be added to the project. The layer shows an arrow for each calculation node. 

#) You can zoom in on the flow pattern to discern the individual arrows. As you can see, the direction of the arrow indicates the direction of the flow. The colour of the arrow is scaled with the discharge.

#) Zoom out again to see the general flow pattern in the model area. Look at the elevation map and the flow pattern; note that the water flows from the higher areas towards the lower areas and a large part eventually ends up in the river.


Watershed delineation for a flooded area
########################################

To better understand why an area gets flooded and to design appropriate measures to decrease flood risks in the future, we want to know where the water in the flooded area comes from. We will use the Watershed Tool to answer this question. The Watershed Tool allows you to determine the upstream and downstream catchment at any point or area.

#) First, we have to make sure the maximum water depth raster is still visible. In the Layers panel, check the layer *max_water_depth_interpolated*. 

#)	Now, open the Watershed tool |watershed_tool| in the 3Di Results Analysis toolbar.
 
#)	In the Watershed tool panel, define the *Input*. Select your simulations results under *3Di results*.

#)	Under *Settings*, you can adjust the period for which you want to carry out the watershed analysis by adjusting the start and end time. Furthermore, you can adjust the threshold. If there is a net flow from the upstream element to the target node(s) above the defined threshold, the upstream element is included in the catchment. For now, you do not need to change the settings.

#)	The next step is to define the *Target nodes*. Click *Click on canvas* to activate the map tool. On the map canvas, the nodes in our study area (Vaethvey road 21-29).
 
The tool automatically calculates the upstream catchment area for the nodes that you selected. The result of the analysis is depicted in the figure below. By choosing *Clear results*, the catchment will disappear and you can choose different nodes to derive the upstream catchment for.  

#)	In the *Output* section, check the *Downstream* option and uncheck the *Upstream* option. The result gives us a indication of how the flood volume is drained during and after the event.

.. _tut6_quant:

Quantification of the flood volume
----------------------------------

Now that we know *where* additional storage or buffer capacity would be helpful, we need to estimate how much storage is needed, so that we can use the correct dimensions in the design of our measure.

Calculating the flood volume
############################

Lastly, we are going to use the *Water balance tool* to determine the flood volume in our study area.

In the schematisation, you can see that a grid refinement was added in the area of the town that gets flooded: our study area (Vaethvey road 21-29). 
 
#)	Click the Water balance tool button |water_balance_tool| in the 3Di Results Analysis toolbar.  
 
#)	Choose *Select polygon* and click the grid refinement area. Choose *grid refinement area (study_area)* in the popup menu. The tool will now automatically calculate and visualize the water balance for this area.

.. note::
   You can use any polygon layer as water balance area. If you do not yet have a polygon for your area of interest, create one first. In the main toolbar, click |new_geopackage|, or go to *Main Menu* > *Layer* > *Create new layer* > *New Geopackage Layer*.

#)	In the water balance plot, you can either show discharge (m³/s) or volumes (cumulative discharge, m³). The tool is automatically set to discharge. Now change to volume by using the dropdown menu and choose the *m³ cumulative* option. 
 
#)	In the graph, the cumulative volumes of water for flows are displayed. At the right side, you can activate and deactivate different the flows. Hover over the different components to see which ones are indicated in the graph. 

#)	The main component that is of interest in this question is *2D flow*. Notice that the graph displays both a positive and negative cumulative 2D Flow. This is caused by the fact that the 2D flow is both entering (positive) and leaving (negative) the study area. The net 2D flow (change in storage) is represented by the dotted red line, representing the *volume change 2D*. Use your mouse to zoom in on the y-axis. You can check the net 2D volume change at the end of the simulation. Check that the flow volume is about 3,200 m³. 

.. |langaa_waterbalans_leeg| image:: /image/langaa_waterbalans_leeg.png
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

.. |add_results| image:: /image/pictogram_add_results.png
    :scale: 80%

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |save_to_spatialite| image:: /image/pictogram_save_to_spatialite.png
	:scale: 80%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |simulate| image:: /image/pictogram_simulate.png
    :scale: 80%
	
.. |download_results| image:: /image/pictogram_download_results.png
    :scale: 80%

.. |results_manager| image:: /image/i_3di_results_analysis_toolbar_results_manager.png
    :scale: 25%
	
.. |closed_eye| image:: /image/pictogram_temporal_controller_load_results_closed_eye.png
	:scale: 100%

.. |resultsaggregationtoolbar| image:: image/i_3di_results_analysis_toolbar_aggregation.png
	:scale: 25%

.. |watershed_tool| image:: image/i_3di_results_analysis_toolbar_watershed.png
	:scale: 25%
	
.. |water_balance_tool| image:: image/i_3di_results_analysis_toolbar_waterbalance.png
	:scale: 25%

.. |value_tool| image:: image/value_tool.png
	:scale: 50%

.. |new_geopackage| image:: image/new_geopackage.png
	:scale: 100%

.. check zipje!! (nieuw zipje kan reinout of wolf online zetten voor je)

