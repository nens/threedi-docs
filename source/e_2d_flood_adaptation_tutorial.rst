Tutorial 5: Flood Adaptation measures
======================================

Introduction
-------------
In this tutorial we will create a flood and apply flood adaptation measures to a 3Di model during a simulation in :ref:`3Di Live <3di_live_introduction>`.

The selected area is the town Strand in Western Cape, South Africa. The river Lourens runs past this city and will be flooded in this tutorial.

Learning objectives
--------------------
You will learn the following in this tutorial:

* Creating a template from a schematisation.
* Adding discharge to a river during a simulation.
* Adding a flood barrier during a simulation. 


Preparation
-----------
Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-05.zip>`_.

.. Checken dat Wolf zipje erop heeft gezet.


Creating a new schematisation
------------------------------
Follow these steps to convert the existing Spatialite to a :ref:`schematisation`:

#) Unpack the starter package and save the contents into a folder. The dataset that you downloaded for this tutorial contains an partially configured .sqlite database, a digital elevation model (DEM) and a initial water level raster.

#) Open the 3Di Modeller Interface.

#) Click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a schematisation name, such as 'Tutorial 2D flow adaptation <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now.

#) Since we are creating a schematisation from an existing Spatialite, select the *Choose file* option. Select the Strand - Western Cape.sqlite file you downloaded and click *Create schematisation*.


Viewing the schematisation
--------------------------
The schematisation must be imported in the 3Di Modeller Interface to view and modify its contents. The schematisation can be loaded by following these steps:

#) At the top of the 3Di Models & Simulations panel, click on the (blue, underlined) name of your schematisation. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button (|load_from_spatialite|). Paste the path to the spatialite and click *Open*.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM and schematisation located over the town Strand.


Uploading the schematisation
----------------------------
We will now upload the schematisation as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next* twice.

#) Fill in a commit message. As this is the first revision of this schematisation, you can give provide a short description of what you upload. For example: "Initial upload".

#) Click *Start upload*. Check if it is the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

Your 3Di model is now ready for simulation! 


Starting the simulation with discharge in 3Di Live
---------------------------------------------------

Now we have created a model, we need to add a forcing to the model. In this case we are going to add a discharge into the Lourens river:

#) :ref:`Load <loading_model_3di_live>` the created model in the 3Di Live.

#) Add a discharge to the Lourens river.

    * Click the :ref:`discharge_tool_3di_live` button (|discharge_tool|).
    * Set the *Amount of water* to 30 m3/s. 
    * Set the *Duration* to 24 hours.  
    * Click *Place on Map* and place the discharge point on the map in near the Broadway Boulevard bridge.

#) Click the *Play* button at the top centre.

#) Pause the simulation after 1 hours of simulated time (01:00)

#) Zoom in to the areas that are starting to flood. 

#) Use the :ref:`point_selection_tool` (|selection_tool|) to click on the flooded area. In the panel at the right, graphs are displayed that show how the situation is developing in this location: the water level (in m MSL), water depth (relative to the DEM) and rain intensity are shown.

#) Now use the :ref:`line_selection_tool` (|line_selection_tool|) to draw a side view of the flooded area. Notice how the water level changes as the simulation progresses. 

#) Make a screenshot of the inundation you see on the map after 1 hours (CTRL + Print Screen) and paste this into a new paint or word document.  

#) Use the line selection tool to determine the waterlevel of the inundated area and write it down.


Create a simulation template from your schematisation
------------------------------------------------------
To store the schematisation with the discharge you added, the schematisation can be saved as a template. This is very useful if you want to reuse the schematisation with the same particular settings. This is especially useful for comparing a schematisation with and without flood adaptation measures or saving a schematisation with a lot of additional forcings (discharge, rain, wind, etc.) for later use.

#) Click *Restart simulation* in the user menu (|user_menu|). 

#)	Select *Store results instead of restarting*

#)	Select *Create simulation template from simulation*

#)	Chose a template name (Like: 'Discharge 30m/s for 24 hours') and make sure the boxes: include events, include initials and include settings are checked. Then click *Store results*


Adding a barrier to your simulation
------------------------------------
Before placing the barrier you should analyse where it should be placed.

Analyse where the barrier should be placed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we would like to place a barrier to reduce the inundation, we need to analyse the elevation of the inundated area and need to find an area on the map where the water enters the area and analyse if we could place a barrier on this location. 

In the previous simulation you saw that there was some inundation in the urban area adjacent the Lourens river. In this part of the tutorial, we are going to try to reduce this inundation in the urban area. To do this, in real life we would create a barrier with sandbags or a mobile barrier in the current landscape to increase the hight of the riverbank, so the water can't enter the urban area. In 3Di live we can simulate this using the flood barrier tool.
In real life, if we want to place barriers, roads are a very useful location due to their even surface and the easy access for the supply of the barrier materials.

#) :ref:`Load <loading_model_3di_live>` your model in the 3Di Live.

#) Select the template you just created, and click *Start*.

#) Use the :ref:`line_selection_tool` (|line_selection_tool|) to analyse the elevation of the riverbank in the inundated urban area.

#)	Use the Line-selection tool to analyse the elevation of the De Ruyter Street (in the south west of your modelled area).

    The Line-selection tool shows that there is a low point in the De Ruyter Street around the area where the river started inundating the urban area. If we would place a barrier at this place, we could reduce most of the flooding. Unfortunately, there are some buildings that are outside of the barriers. 

#) Try using the Line-selection tool to find a location for the barrier that saves more houses than placing the barrier on the De Ruyter Street, but which would also be a realistic location of a barrier.

    The most logical thing to do to save all the houses, is placing the barrier between the houses and the river, but if we take a closer look at the satellite image, we can see that there are four walls surrounding the different gardens of these houses. In a crisis, it takes too much time to first break down these walls and then place a barrier. The De Beers Road however is a realistic area to place the barrier and can be a fine addition to save the houses between the De Beers Road and the Beach Road could be saved by adding a barrier around the houses.



Add a barrier to your simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As you have seen earlier in this tutorial, the inundation without a barrier reaches a level of 2.35 mMsl. To make sure the barrier is high enough, place a barrier with a height of 2.5 mMsl at the designated area. Now that we know where the barrier needs to be placed and how high the barrier needs to be, it is time to add it to our simulation:


#) Click the :ref:`flood_barrier_tool_3di_live` button (|barrier_tool|).

#)	Fill in the height of 2.5 mMsl.

#)	Click *Draw on map*.

#)	Draw a barrier on the map with the location shown in the figure below. If you are finished drawing, click on *Confirm*. 

#)	Select the barrier using the Selection tool to check if the height is correct and see what the length of the placed barrier is.

#)	Start the simulation and let it run for 1 hour.

#)	To make a quick comparison, make a screenshot of the results and past this next to the screenshot of the model without barrier.

.. figure:: image/t_05_location_barrier.png
   :alt: Location of the barrier

   Location of the barrier.


.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |load_from_spatialite| image:: /image/pictogram_load_from_spatialite.png
	:scale: 80%

.. |discharge_tool| image:: /image/pictogram_discharge_tool.png
    :scale: 80%

.. |line_selection_tool| image:: /image/pictogram_line_selection_tool.png
    :scale: 75%

.. |selection_tool| image:: /image/pictogram_selection_tool.png
    :scale: 80%

.. |user_menu| image:: /image/pictogram_user_menu.png
    :scale: 60%

.. |barrier_tool| image:: /image/pictogram_barrier_tool.png
    :scale: 80%

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%