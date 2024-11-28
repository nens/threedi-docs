.. _tutorial7_1d2dmodel:

Tutorial 7: Creating an integral 1D2D urban drainage model
==========================================================

Introduction
------------

In this tutorial, you will use the :ref:`3Di Modeller Interface <mi_what_is>` to build an integral 1D2D urban drainage model of the xtt..., in xtt.... The purpose of the model is to analyse urban drainage patterns and pluvial flooding in the city. This model will include flow above and below ground: rain on the 2D grid and on buildings, overland flow, flow into the sewer system (from buildings and from the surface) and flow through the sewer system.  

For the sewer system, you will use open data from xtt... You will import these data using the vector data importer and use two different processing algorithms to automatically add information to 1D objects. 

Although the model will represent a real-world area, some processes will be simplified for the sake of this tutorial. Please keep this in mind while analysing the results of your simulations.

A similar model is built in this `webinar <https://www.youtube.com/watch?v=YhJzzI7gBq0>`.


Learning objectives
-------------------

In this tutorial you will:

* Create a new schematisation
* Use the vector data importer to add 1D objects to a schematisation in batch
* Use expressions to infer culvert characteristics in the attribute table
* Use a processing algorithm to infer the manhole bottom level from pipes
* Add impervious surfaces to a schematisation and use a processing algorithm to map them to connection nodes 
* Upload a schematisation


Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.

* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.

* Download the xtt... DEM. 

* Add the model bounds GeoPackage (regina_model_boundaries.gpkg) to the project.

Creating a new schematisation
-----------------------------

Follow these steps to create a new :ref:`schematisation`:

#) Open the 3Di Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations panel.

    .. note::
        If this is the first time you use the 3Di Models and Simulation panel, you will need to go through :ref:`some steps to set it up<setting_up_models_and_simulations>`. http://localhost:62677/e_2d_flood_tutorial.htmlhttp://localhost:62677/a_how_to.html

#) In the *Schematisation* section of the 3Di Models and Simulations panel, click the *New* button (|newschematisation|). The *New schematisation* wizard is shown.

#) Fill in a  schematisation name, such as 'Tutorial 7 <your_name>'. Select the organisation you want to be the owner of the new schematisation (most users have rights for only one organisation). Tags are optional, you can leave this field empty for now. Since we are creating a schematisation from scratch, select the *Create new Spatialite* option. Click *Next*.

#) Read the explanation on the second page of the *New schematisation* wizard. Click *Next*.

#) In the section *2D Flow*, browse to the DEM (.tif) file you have downloaded. The coordinate reference system (EPSG:2957) is read from the DEM file and filled in automatically.

#) Fill in the following settings:

	* Computational cell size: 10

	* The model area is predominantly: Sloping

	* Check 1D flow 

	* Check 0D flow and do not change the inflow parameters type

	* Friction type: Manning

	* No friction file

	* Global 2D friction coefficient: 0.03

	* Simulation timestep: 10 s

	* Typical simulation duration: 0-3 hours

#) Click *Create schematisation*. A popup message will ask you if you want to load the schematisation data from the associated Spatialite file. Click *Yes*.

Viewing and editing the schematisation
--------------------------------------

The schematisation is added to your 3Di Modeller Interface project. You will now add a background map for reference. This will allow you to check if the schematisation looks as you expect.

#) Add a background map from OpenStreetMap by clicking *Web* in the Main Menu > *Quick Map Services* > *OSM* > *OSM Standard*.

#) In the *Layers* panel, reorder the layers such that the OpenStreetMap layer is below the 3Di schematisation.

You should now see the DEM, located in Regina.

You will now change some default settings and save the changes to the spatialite.

#) Open the *Global settings* attribute table. Make sure to use the form view; you can change the view on the bottom right. 

#) Click the *Toggle editing mode* button (|toggle_editing|) in the top left corner.

#) Click the *Grid* tab and set *kmax* to 3. For explanation on the grid size and grid refinements, see :ref:`computational_grid_2d_domain`.

#) Click the *Terrain information* tab and set initial_waterlevel to 568. Note that it is also possible to supply an initial water level raster to specify an initial water level for each cell; in this tutorial we use a global value, for simplicity.

#) Click the *Toggle editing mode* button and save your edits to this table.

#) In the 3Di Schematisation Editor toolbar, click *Save to Spatialite* (|save_to_spatialite|). Wait for this process to finish.


Uploading the schematisation
----------------------------

The next step is to check the schematisation, upload it as a first :ref:`revision` and process it into a :ref:`threedimodel`. All these steps are covered by the upload wizard.

#) Click the upload button (|upload|) in the 3Di Models and Simulations panel.

#) In the dialog that has appeared, click *New upload* and click *Next*.

#) Click *Check schematisation*. This will check your schematisations for any errors. A schematisation that contains errors cannot be processed into a 3Di model and simulation template. The schematisation checker may also produce warnings or info level messages. These help you to improve the schematisation. If you have followed the instructions in this tutorial, the schematisation checker should not produce any errors, warnings or info level messages.

    .. note::
       Please do not ignore warnings. These are given for schematisation choices that are usually wrong and negatively impact the performance of you model. It will still be possible to generate a model from a schematisation with warnings, and there may also be special cases where your schematisation choice is intentional and you deliberately ignore the warning. If the performance of you model is sub-par, please fix any warnings before reaching out to the :ref:`servicedesk`.

#) Continue to the next screen. Here you have to fill in a commit message that describes the changes you have made relative to the previous revision. As this is the first revision of this schematisation, you can instead provide a short description of what you upload. For example: "Default settings, DEM only".

#) Click *Start upload*. Check if the upload is successful and if the uploaded data is successfully processed into a 3Di model.  

    .. note::
        By default, this page of the upload wizard is set to *UPLOAD AND PROCESS*, so that a 3Di model and simulation template will be generated automatically after the upload. When you start using the upload wizard regularly, you may sometimes want to upload data without generating a new 3Di model from it. In that case, choose the *UPLOAD ONLY* option.

.. _tut_import_vector_data:

Import vector data from open data source 
----------------------------------------

Right now, you have a schematisation and model of your first version, which only contains the DEM and some global settings. To make this an integral model, you will now add the manholes, culverts and pipes to your schematisation. To do this, you need to add the relevant layers from the open data to your project. The open data is made available through an ArcGIS REST Server. To add a connection to this service, make sure you can see the Browser panel. 

#) In the Browser panel, right-click *ArcGIS REST Servers* and select *New Connection...*

#) Fill in the following settings: 

    * Name: name of your choice, for example "Regina Storm Sewer Network". 

    * URL: https://opengis.regina.ca/arcgis/rest/services/OpenData/StormSewerNetwork/MapServer

#) Click *Ok*.

You are now able to see all layers from the server in the Browser panel. You will add the manholes, culverts and pipes layers to the project after applying filters to select the desired features within the model bounds.

#) Manholes:

    * Double-click the vector layer *Manhole* from the ArcGIS REST Server to add it to the project.
  
    * Right-click the layer and select *Filter...*

    * Under *Provider Specific Filter Expression*, type: "SUBTYPENAME" IN ('Interceptor', 'Manhole', 'ManholeChamber').

#) Pipes:

    * Double-click the vector layer *Storm Sewer Line* from the ArcGIS REST Server to add it to the project.

    * Rename the layer to "Pipe".

    * Right-click the layer and select *Filter...*

    * Under *Provider Specific Filter Expression*, type: "SUBTYPENAME" IN ('Main', 'Trunk'). This way, you only keep the pipes and filter out other types, such as culverts.

#) Culverts:

    * Double-click the vector layer *Storm Sewer Line* from the ArcGIS REST Server to add it to the project.

    * Rename the layer to "Culvert".

    * Right-click the layer and select *Filter...*

    * Under *Provider Specific Filter Expression*, type: "SUBTYPENAME" = 'Culvert'.

You now have three vector layers in your project, which contain the features that make up the sewer system in Regina. As you can see, there are also features outside of the model bounds.  
You will use the *Select by Location* tool on each of these layers in order to select features within the model bounds. Follow these steps for all three layers:

#) Click *Select by Location*.

#) Fill in the following settings:

    * Select features from: select the layer Manhole

    * Where the features: are within.

    * By comparing to features from: regina_model_boundaries.

    * Modify current selection by: creating new selection.

#) Click *Run* to create the selection.

Now you have selected the relevant Manhole features, you are ready to import them into the schematisation.

#) Repeat these steps for the *Pipe* and *Culvert* layers, to select the relevant features from those layers.

You will now import the Manholes, Pipes and Culverts to the 3Di Schematisation.

#) Manholes: Click *Import schematisation objects* in the Schematisation Editor panel and select *Manholes*. Fill in the following settings:
  
    * Source manhole layer: select your filtered manhole layer.

    * Check *Selected features only* to only import the features within the model bounds.

    * Check *Create connection nodes*.

    * Check *Snap within* and fill in 0.10 meters.

    * Now set the method, source attributes and default values for the manhole fields:

    .. csv-table:: Import manholes settings
        :name: import_manholes_settings
        :header: "Field name", "Method", "Source attribute", "Default value"

        "ID", Auto, -, -
        "Code", Attribute, OBJECTID, -
        "Display name", Attribute, OBJECTID, -
        "Calculation type", Default, -, Connected
        "Shape", Default, -, Square
        "Width [m]", Default, -, 1.0
        "Length [m]", Default, -, 1.0
        "Bottom level [m MSL]", Ignore, -, -
        "Surface level [m MSL]", Attribute, RIMELEVATION, -
        "Drain level [m MSL]", Attribute, RIMELEVATION, -
        "Sediment level [m MSL]", Ignore, -, -
        "Manhole indicator", Default, -, Inspection
        "Zoom category", Default, -, Medium low visibility
        "Connection node ID", Auto, -, -
        "Exchange thickness [m]", Ignore, -, -
        "Hydraulic conductivity in [m/d]", Ignore, -, -
        "Hydraulic conductivity out [m/d]", Ignore, -, -

    * You are also creating connection nodes. To set the method, source attributes, and default values for these, click the *Connection nodes* tab and fill in the table:

    .. csv-table:: Import manholes settings: connection nodes
        :name: import_manholes_settings_connection_nodes
        :header: "Field name", "Method", "Source attribute", "Default value"

        "ID", Auto, -, -
        "Code", Attribute, OBJECTID, -
        "Initial water level [m]", Ignore, -, -
        "Storage area [m2]", Default, -, 1.0

The values for the ID fields are autogenerated, such that each attribute has a unique ID. With the method *Attribute*, the value from the selected field from the source table is filled in. The method *Default* allows you to set a default value in the target table. Finally, *Ignore* results in a NULL value in the target table. 
In this case, we used the attribute *OBJECTID* from the imported manholes to set the *Code* and *Display name* in the schematisation's manhole layer. Every manhole has calculation type "Connected" and is square with a width of 1 m. 
We ignored the bottom levels, because we will obtain those later, based on the pipes' invert levels. Try to find out for yourself how the values in the other fields are determined.  

    .. note::
        You don't have to fill in this table each time. You can save these configurations by clicking *Save as template...*. Next time you would like to import a manhole layer with the same format, simply select the saved JSON file after clicking *Load template...*.


#) Pipes: Click *Import schematisation objects* in the Schematisation Editor panel and select *Pipes*. Fill in the following settings:

    * Source pipe layer: select your filtered pipe layer.

    * Check *Selected features only* to only import the features within the model bounds.

    * Check *Create manholes* and *Create connection nodes*. The tool will create new manholes and connection nodes if these are not found within the snapping distance of a pipe end.

    * Check *Snap within* and fill in 0.10 meters.

    * Now set the method, source attributes and default values for the pipe fields: 

    .. csv-table:: Import pipe settings
        :name: import_pipe_settings
        :header: "Field name", "Method", "Source attribute", "Value map", "Default value"

        "ID", Auto, -, -, -
        "Code", Attribute, OBJECTID, -, -
        "Display name", Attribute, OBJECTID, -, -
        "Calculation type", Default, -, -, Isolated
        "Calculation point distance [m]", Default, -, -, 1000.0
        "Invert level start point", Attribute, STARTELEVATION, -, -
        "Invert level end point", Attribute, ENDELEVATION, -, -
        "Friction value", Attribute, MATERIAL, xtt see below (paste table below), -
        "Friction type", Default, -, -, Manning
        "Material", Ignore, -, -, -
        "Sewerage type", Default, -, -, Storm drain
        "Zoom category", Default, -, -, Medium low visibility
        "Connection node start ID", Auto, -, -
        "Connection node end ID", Auto, -, -
        "Cross section shape", Default, -, -, Circle
        "Cross section width [m]", Attribute, DIAMETER, -, -
        "Cross section height [m]", Ignore, -, -, -
        "Cross section table", Ignore, -, -, -
        "Exchange thickness [m]", Ignore, -, -, -
        "Hydraulic conductivity in [m/d]", Ignore, -, -, -
        "Hydraulic conductivity out [m/d]", Ignore, -, -, -

    * You are also creating connection nodes. To set the method, source attributes and default values for these, click the *Connection nodes* tab and fill in the table:

    .. csv-table:: Import pipe settings: connection nodes
        :name: import_manholes_settings_connection_nodes
        :header: "Field name", "Method", "Source attribute", "Default value"

        "ID", Auto, -, -
        "Code", Attribute, OBJECTID, -
        "Initial water level [m]", Ignore, -, -
        "Storage area [m2]", Default, -, 1.0

    * You are also creating manholes. To set the method, source attributes and default values for these, click the *Manholes* tab and fill in the table:

    .. csv-table:: Import pipe settings: manholes
        :name: import_pipe_settings_manholes
        :header: "Field name", "Method", "Source attribute", "Default value"

        "ID", Auto, -, -
        "Code", Attribute, OBJECTID, -
        "Display name", Attribute, OBJECTID, -
        "Calculation type", Default, -, Connected
        "Shape", Default, -, Square
        "Width [m]", Default, -, 1.0
        "Length [m]", Default, -, 1.0
        "Bottom level [m MSL]", Ignore, -, -
        "Surface level [m MSL]", Ignore, -, -
        "Drain level [m MSL]", Ignore, -, -
        "Sediment level [m MSL]", Ignore, -, -
        "Manhole indicator", Default, -, Inspection
        "Zoom category", Default, -, Medium low visibility
        "Connection node ID", Auto, -, -
        "Exchange thickness [m]", Ignore, -, -
        "Hydraulic conductivity in [m/d]", Ignore, -, -
        "Hydraulic conductivity out [m/d]", Ignore, -, -

.. note::
    This time, you used a value map to infer the friction value from the material. 

#) Culverts: Click *Import schematisation objects* in the Schematisation Editor panel and select *Culverts*. Fill in the following settings:

    * Source culvert layer: select your filtered culvert layer.

    * Check *Selected features only* to only import the features within the model bounds.

    * Check *Create manholes* and *Create connection nodes*. The tool will create new manholes and connection nodes if these are not found within the snapping distance of a culvert end.

    * Check *Snap within* and fill in 0.10 meters.

    * Now set the method, source attributes and default values for the culvert fields: @Leendert hier ben ik gebleven



.. images:

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%

.. |newschematisation| image:: /image/pictogram_newschematisation.png
    :scale: 80%

.. |addresults| image:: /image/pictogram_addresults.png

.. |upload| image:: /image/pictogram_upload_schematisation.png
    :scale: 80%

.. |load_from_spatialite| image:: /image/pictogram_load_from_spatialite.png
    :scale: 80%

.. |simulate| image:: /image/pictogram_simulate.png
    :scale: 80%

.. |toggle_editing| image:: /image/pictogram_toggle_editing.png
    :scale: 80%

.. |add_feature| image:: /image/pictogram_addfeature.png
    :scale: 80%

.. |save_to_spatialite| image:: /image/pictogram_save_to_spatialite.png
    :scale: 80%
    