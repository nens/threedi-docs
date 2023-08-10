..  _flood_model:

Tutorial 4: Building a dike breach flood model
==============================================

Introduction
-------------
In this tutorial, you are going to build a model that simulates a flood caused by a potential breach. The model will be built using the :ref:`3Di Modeller Interface <mi_what_is>`. At the end of this tutorial, you will have a basic working model that you can run simulations with.

Our area of interest is the municipality of Nissewaard on the island of Voorne-Putten in the Netherlands. The municipality of Nissewaard consists of urban area and farmland. While this tutorial represents a real-world area, it is important to keep in mind that some processes will be simplified for the purpose of this tutorial.


Learning objectives
--------------------
You will learn the following in this tutorial:

* Adding 1D channels to a model.
* Adding boundary conditions to a 1D channel.
* Add a linear obstacle to a 2D model.
* Create a potential breach event in a 2D model.
* Simulate the model with a breach event.


Preparation
------------
Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-04.zip>`_.

Unzip the dataset for this tutorial and save the contents into a folder. The dataset that you downloaded for this tutorial contains a digital elevation model (DEM) for a part of the Nissewaard municipality. This DEM is called dem_Nissewaard.tif and is located in the folder named "rasters". 

.. TODO: zip updaten!

Creating a new schematisation
------------------------------
The first step is to create a new :ref:`schematisation`:

#) Open the 3Di Modeller Interface.

#) Click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel. If this is the first time you use 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`.

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a schematisation name, such as 'Tutorial dike breach model <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now. Since we are creating a schematisation from scratch, select the *Create new Spatialite* option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.

#) Fill in the following Schematisation settings:

	* The coordinate reference system: is read from the DEM file and filled in automatically (EPSG:28992 - Amersfoort / RD New)

	* Digital elevation model: browse to the DEM file you have downloaded (dem_Nissewaard.tif)

	* Computational cell size: 20

	* The model area is predominantly: Flat

	* Use 1D flow

	* No 0D flow

	* Friction type: Manning

	* Friction file: Leave empty

	* Global 2D friction coefficient: 0.03

	* Simulation timestep: 30 s

	* Typical simulation duration: 3-12 hours

#) Click *Create schematisation*. A popup message will tell you that the the schematisation was created. Copy the path that is shown in the popup message.


Uploading the schematisation
----------------------------
We will now upload the schematisation as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors that make it impossible to generate a valid 3Di model and simulation template. It should not produce any errors, warnings or info level messages. Click *Next*.

#) Fill in a commit message. As this is the first revision of this schematisation, you can give provide a short description of what you upload. For example: "Default settings, DEM only".

#) Click *Start upload*. Check if it is the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

Your 3Di model is now ready for simulation!  


Viewing the schematisation
--------------------------
We will load the schematisation in the 3Di Modeller Interface to view and modify its contents. The schematisation can be loaded by following these steps:

#) If you have not copied the path to the spatialite in the previous step, click on the (blue, underlined) name of your schematisation at the top of the 3Di Models & Simulations panel. Windows Explorer will open; browse to *work in progress/schematisation* and copy the path from the Windows Explorer address bar.

#) In the 3Di Schematisation Editor toolbar, click the *Load from Spatialite* button (|load_from_spatialite|). Paste the path to the spatialite and click *Open*.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the Layers panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM file located south of the Oude Maas.


Adding a dike breach to the schematisation
-------------------------------------------
We now have a schematisation with a DEM file and the essential settings filled in.
First, we will incorporate the 1D elements, including a channel and boundary conditions. Next, we will introduce the 2D elements, particularly a linear obstacle to represent the dike. Finally, the crucial connection between the 1D and 2D aspects will be established through the implementation of a potential breach.

.. _adding_a_channel:

Adding a channel (1D)
^^^^^^^^^^^^^^^^^^^^^
We are going to add a :ref:`channel` to the model at the 'Scheepvaart- en Voedingskannal' in the North of our model area. See the :ref:`t4reference-image` for a reference.

A channel :ref:`flows <channelflow>` from one connection node to another, has a :ref:`calculation type <calculation_types>` and a :ref:`channel geometry <cross_section_of_1d_element>`. These parameters will be filled in, in the following steps:

#) In the *Layers* panel, in the *1D* group, click the *Channel* layer.

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left.

#) Click on the *Add line feature* button (|add_line|).

#) Begin by clicking on a desired starting location for your channel. Next, click along the 'Scheepvaart- en Voedingskannal' and finally on the location where you want the channel to end. Ensure that the channel remains within the Digital Elevation Model (DEM). 

#) Right-click to stop drawing the channel. A popup screen with the Feature Attributes should now appear.

#) Fill in the following parameters in the *channel* tab:

   * ID: filled in automatically
   * Code: give your channel a code so you can identify it later
   * Display name: this is the name the channel will be displayed with in 3Di Live 
   * Calculation type: Connected
   * Distance between calculation points [m]: 15
   * Connection nodes: filled in automatically

#) In the *Connection nodes* tab, fill in the following parameters for both connection nodes:

   * Connection node ID: filled in automatically
   * Node code: give your connection node a code or name so you can later identify it
   * Node initial water level [m]: 3
   * Node storage area [m2]: Leave empty

#) Fill in the following parameters in the *Cross section locations* tab:

   * ID: filled in automatically
   * Code: rectangle_channel
   * Reference level [m]: 0
   * Bank level: 4
   * Friction type: Manning
   * Friction value: 0.026
   * Shape: Open rectangle
   * Width [m]: 50

#) Click *OK*.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

The 'Reference level' corresponds to the bed level of the channel. The 'Bank level' indicates the level at which the channel will :ref:`exchange <1d2d_exchange>` with the 2D field. Initially, it will prioritize this level before considering the elevation of the DEM surrounding the channel or any obstacles. The 'Friction value' for the Manning coefficient, it is derived from the roughness of the grass.

.. _adding_boundary_conditions:

Adding a boundary condition (1D)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order for water to flow through the channel a boundary condition must be added. As the channel is a :ref:`1D object <1d_objects>`, a 1D boundary condition will be added, with the following steps:

#) In the *Layers* panel, in the *1D* group, click the *1D Boundary condition* layer.

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left.

#) Click on the *Add point feature* button (|add_point|).

#) Hover over the end of your channel until you see a pink square. Click on the pink square and fill in the following parameters:

   * ID: filled in automatically
   * Connection node ID: filled in automatically (this id number is related to the previously added connection nodes)
   * Boundary type: Waterlevel
   * Timeseries:

        - 0,3.5
        - 15,3.5
        - 9999,3.5

#) Do the same for the other end of your channel but fill a different Timeseries:

        - 0,3.0
        - 15,3.0
        - 9999,3.0
  
#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

The use of two distinct time series generates a flow within the channel, carrying water from one end to the other. The direction of this flow is determined by the time series' starting points; water will naturally move from a higher water level (3.5) to a lower water level (3.0).


Drawing the dike (2D)
^^^^^^^^^^^^^^^^^^^^^^
Dikes are automatically read from the DEM. However, if the dike is narrow and the computation cells are large, it might be beneficial to draw the dike using a Linear Obstacle. Follow these steps, and reference the DEM and the :ref:`t4reference-image` and draw the obstacle:
       
#) In the *Layers* panel, locate the *2D* group, and select the *Linear Obstacle* layer.

#) Enable editing mode by clicking the *Toggle editing mode* button (|toggle_editing|) located in the top left corner.

#) Click on the *Add line feature* button (|add_line|).

#) To begin drawing the dike, click on a starting location adjacent to the starting point of the channel, aligning it with the visible dike on the DEM. Next, trace the dike along the 'Scheepvaart- en Voedingskannal' visible in the DEM, and finally, select the location where you want the dike to end.

#) Right-click to stop drawing the dike. A popup screen with the Feature Attributes should now appear.

#) Fill in the value '3' for the *crest level* of the dike, then click *OK*.

#)  Click the *Toggle editing mode* button in the toolbar to exit editing mode and save your edits to this layer.

.. _adding_potential_breach:

Potential Breach (1D-2D)
^^^^^^^^^^^^^^^^^^^^^^^^
Now that we have incorporated a connected channel into our model, the next step is to introduce a potential breach location. This breach acts as a link between the 1D and 2D aspects of the model. In our scenario, the potential breach will simulate a dike breach, allowing water from the channel to flow into the fields behind the dike. For more theoretical information on breaches, see: :ref:`breaches`. 

See the :ref:`t4reference-image` for a reference where to draw the potential brach:

#) In the *Layers* panel, in the *1D2D* group, click the *Potential breach* layer.

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left.

#) Click on the *Add line feature* button (|add_line|).

#) Hover over your channel until a pink square appears. Click on the pink square. Now click on the other side of the dike. Right-click to stop drawing.

#) Fill in the following parameters:

   * ID: filled in automatically
   * Code: a name to identify your potential breach
   * Display name: a name to identify your potential breach
   * Exchange level [m MSL]: 4
   * Max breach depth [m]: 1
   * Levee material: Sand
   * Channel ID: filled in automatically

#) Click *OK*.

#) Click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

The 'Exchange level' represents the water level that the channel must reach to initiate a breach and exchange water. Additionally, a breach can also be "opened", similar to creating a hole in a dike. The 'Max breach depth' signifies the maximum depth of this opening, measured from the top of the dike.

.. VRAAG: klopt deze uitleg een beetje?

The final result should look something like this, with the location of the channel (blue), the boundary conditions (purple), the dike obstacle (brown), and the potential breach (black) from the channel to the field behind the dike:

.. _t4reference:

.. _t4reference-image:

.. figure:: image/t_04_reference.png
    :alt: Reference image
    :scale: 50%
    
    Refrence image.


Adding a channel outside of the DEM to the schematisation
-----------------------------------------------------------
A channel can also be added to the schematisation while it is outside of the DEM, so outside of the modelled area. When you want to do this you need to add a :ref:`exchange_line`. This line will link the 1D channel element to the 2D area of the map. Follow these step:


#) Add a channel in the same way as you did in :ref:`adding_a_channel`, but this time the channel may be outside of the DEM.

#) Add the boundary conditions in the same way as you did in :ref:`adding_boundary_conditions`.

#) In the *Layers* panel, in the *1D2D* group, click the *Exchange line* layer.

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left.

#) Click on the *Add line feature* button (|add_line|).

#) draw your exchange line parallel to your channel. Ensure that the exchange line remains within the Digital Elevation Model (DEM). 

#) Right-click to stop drawing the Exchange line. A popup screen with the Feature Attributes should now appear.

#) Fill in the following parameters in the *channel* tab:

    * ID: filled in automatically
    * Code: give a name you can identify it by
    * Exchange level [m]: leave empty
    * Channel ID: ID of the channel outside of the DEM (2)

#) Click *OK* and click the *Toggle editing mode* button in the toolbar and save your edits to this layer.

#) You can add a potential breach in the same way as you did in :ref:`adding_potential_breach`. Make sure to snap the start of the potential breach to the channel and let it end on the DEM behind the exchange line.

.. VRAAG: klopt dit zo?

Uploading a revision
----------------------
The next step is to check the schematisation, upload its as a second :ref:`revision` and process it into a :ref:`threedimodel`. 

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite* (|save_to_spatialite|). Wait for this process to finish.

#) Click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors that make it impossible to generate a valid 3Di model and simulation template.

#) Continue to the next screen. Here you have to fill in a commit message that describes the changes your have made relative to the previous revision. For example: "Added channel with potential breach".

#) Click *Start upload*. Check if it is the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

Your 3Di model is now ready for simulation! The model is now also available on `3Di Live <https://www.3di.live/>`_ and the `management screens <https://management.3di.live>`_.


Running a simulation 
----------------------

You will now start a simulation with the 3Di model you have created in the 3Di Modeller Interface: 

#) In the 3Di Models and Simulations panel, click *Simulate* (|simulate|) > *New simulation*.  

#) Select your model and simulation template and click *Next*. A new dialog opens with several options for your simulation.  

#) Check the box for *Include breaches* (keep *Include initial conditions* and * Include boundary conditions* checked). Click *Next*.

#) Give your simulation a name. Click *Next*.

#) Set the duration of your simulation to 4 hours. Click *Next*.

#) Accept the Boundary conditions as they are by clicking *Next*.

#) Accept the Initial conditions as they are by clicking *Next*.

#) Fill in the following parameters for Breaches and then click *Next*.

    * ID of breach: 1 (if your model only contains 1 breach)
    * Duration till max depth: 0.100 hours
    * Start after: 3600 sec

#) Accept the simulation settings as they are by clicking *Next*. 

#) Check the summary of your simulation and click *Add to queue*.  


The 'Duration till max depth' refers to the time it takes for the breach to reach its maximum depth after it starts forming. The speed at which the maximum width of the breach is attained depends on the material properties. As for the 'Start after' parameter, it is set to begin one hour after the start of the simulation.

Your simulation will start as soon as a calculation node is available for your organisation. Note: the number of available calculation nodes depends on your 3Di subscription. 

In the 3Di Models and Simulations panel, click *Simulate*. An overview is given of all running simulations for your organisation(s). Here you can follow the progress of your simulation.

.. TODO: to acces the results.. (dit nog toevoegen aan deze tutorial?)


Running a simulation with 3Di Live
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is also possible to simulate your model with 3Di Live:

#) Go to `3di.live <https://www.3di.live/>`_.

#) Find your model. It will be available under the name you gave it, followed by the revision number. Click *Start*.

#) Zoom into your channel (blue line) and potential breach (brown line).

#) Click the Play button at the top centre to start the simulation.

#) You can open a breach by clicking on the breach and clicking on the settings button. You can adjust the breach settings when your simulation is paused.



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
    