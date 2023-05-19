.. _simulate_api_qgis:

Running a simulation
#######################

To perform a simulation using the Modeller Interface, we will utilize the :ref:`models_simulation_plugin`. This section offers valuable insights into the various options available for your specific :ref:`scenario <scenario_info>`.


To start a simulation:
=========================

#) Open the 3Di Modeller Interface
#) Activate the '3Di Models and Simulation panel' by clicking on the pictogram (|modelsSimulations|) in the toolbar.
#) Click on the 'Simulate' icon.
#) Click on 'New Simulation'.
#) Select the model you want to simulate. If you have access to more than one organisation, choose the organisation that billing should go to. Then click on 'Next'.
#) A panel with different scenario options will now appear, check the options you want to be used in the calculations of your simulation:

    * Initial condition

      * :ref:`simulate_api_qgis_initial_conditions`: To define the use of initial water levels in 1D, 2D or Ground water or a (previously) saved state.

    * Forcings

      * :ref:`simulate_api_qgis_boundary_conditions`: Boundary conditions are taken from the spatialite directly.
      * :ref:`simulate_api_qgis_laterals`: Select laterals to use in the model.
      * :ref:`dry_weather_flow`: Include dry weather flow in your model.
      * :ref:`simulate_api_qgis_precipitation`: Define precipitation in the model.
      * :ref:`wind_apiclient`: Define wind in the model.
      * Raster edits
      * Leakage
      * Sources and sinks
      * Local or time series rain
      * Obstacle edits

          .. VRAAG: De opties die ik nu niet heb beschreven; zijn die in gebruik? Ik heb meerdere modellen geprobeerd maar ik kon ze nooit aanklikken

    * Events

      * :ref:`sim_structure_controls`: Modify hydraulic structure parameters.
      * :ref:`simulate_api_qgis_breaches`: To select a breach to open in the model.

    * Other options

      * :ref:`generate_api_qgis_saved_state`: To save the end result of the simulation as a saved state.
      * :ref:`simulate_api_qgis_post_processing`: This is a feature that is only available for users of organisations that have a Lizard account. It enables you to store the results in the cloud and it triggers automated post-processing of water depth, water levels, time of arrival, flood hazard rating and damage estimations maps.
      * :ref:`simulate_api_qgis_multi_sim` (becomes available when using either breaches or precipitation): To define multiple simulations with rainfall or breaches. Useful when simulating multiple events on the same model.

#) Name the simulation. Users within your organisation will be able to find this simulation and its results based on the name. Adding 'Tags' can clarify for other users what your simulation calculated or can be used to assign a simulation a certain project name or number.
#) Set the 'Duration' of the simulation.
#) The next steps depend on the selection of options from the initial screen of the wizard (step 6). Unchecked options will be omitted by the wizard. All possible options are explained below under :ref:`scenario_info`.
#) Set the Simulation Settings. Here you can overwrite the settings in the SQLite if that is necessary.
#) Start the simulation by clicking on 'Add to queue'. 

.. VRAAG: wat moet ik nog over de simulations settings uitleggen



You can follow the progress of your simulation by clicking on the 'Simulate' icon in the '3Di Models and Simulations' panel. You can also terminate your simulation by clicking on 'Stop Simulation'. 

Once the simulation is done the results will be available for 7 days. For information on how to get, view and analyze results, see :ref:`mi_download_res` and :ref:`view_analyze_mi`.



.. _scenario_info:

Scenario information
=========================


.. _simulate_api_qgis_boundary_conditions:

Boundary conditions
---------------------

* **From simulation template**: If the 3Di model contains boundary conditions, a timeseries for each boundary condition will be included in the simulation template. 

* **Upload files(s)**: You can upload CSV files to replace the boundary conditions that are included in the simulation template. 

  * Upload a CSV file.
  * Set the time units used in your CSV file (hours, minutes, or seconds). The default is minutes (mins), because this is the time unit that is used in the 3Di spatialite.
  * If the option 'Interpolate' is checked, the value between time steps will be linearly interpolated. For example, consider the following time series:

    .. list-table:: Timeseries example for interpolation
      :header-rows: 1

      * - time [hours]
        - discharge [m\ :sup:`3`/s]
      * - 0
        - 0
      * - 1
        - 16
      * - 3
        - 10

    If *interpolate* is checked, the discharge after half an hour will be 8 m\ :sup:`3`/s. If it is not checked, the discharge after half an hour will be 0 m\ :sup:`3`/s.


.. Note:: You can only replace *all* boundary conditions. For example, if your model contains two 1D boundary conditions and five 2D boundary condition, the CSV file for the 1D boundary conditions should contain time series for both of the two 1D boundary conditions and the CSV file for the 2D boundary conditions should contain time series for all five 2D boundary conditions. The simulation wizard will merge them into a single JSON file that is sent to the API



Editing a time series for boundary conditions
"""""""""""""""""""""""""""""""""""""""""""""""

To run a simulation in which only one or a few boundary conditions have a different time series, take the following steps. The instructions are for 1D Boundary conditions; for 2D Boundary conditions, the same instructions apply. 

- Load your schematisation
- In the Layers panel, right click on the layer '1D Boundary condition' > 'Export' > 'Save features as..'
- For 'Format', choose 'Comma Separated Value [CSV]'
- Choose a 'File name' and location to save the file to
- Click 'Select fields to export and their export options'
- Make sure only the checkboxes for the fields 'id' and 'timeseries' are checked
- Under 'Geometry' > 'Geometry type' choose 'No Geometry'
- Under 'Layer options', make sure the 'Separator' is 'comma'
- Click 'Ok' to save the file
- Open the file in a text editor to edit the values and save the CSV file
- You can now select the edited CSV file under the option "Upload file(s)" when adding scenario information

| **Boundary conditions CSV file format**
| The CSV file input should have the following columns:

- "id": integer; is the id of the corresponding row in the 1D Boundary Conditions table in the spatialite
- "timeseries": a CSV-formatted text field: pairs of time step (in minutes or seconds) and value (in m\ :sup:`3`/s, m, or m/m, depending on the boundary condition type). The timestep is separated from the value by a comma and lines are separated from one another by a newline.

Example as a table:

.. list-table:: Boundary conditions CSV file format
   :header-rows: 1

   * - id
     - timeseries
   * - 4
     - 0,1.2

       99999,1.2
   * - 5
     - 0,2.1

       99999,2.1
   * - 6
     - 0,1.3

       99999,5.6
   * - 7
     - 0,8.2

       99999,1.0
   * - 8
     - 0,63.307

       99999,63.307

Text example::

    id,timeseries
    "4","0,1.2
         99999,1.2"
    "5","0,2.1
         99999,2.1"
    "6","0,1.3
         99999,5.6"
    "7","0,8.2
         99999,1.0"
    "8","0,63.307
         99999,63.307"

     

Running a model without boundary conditions
"""""""""""""""""""""""""""""""""""""""""""""

If the 3Di model contains boundary conditions, you can only run a simulation if a time series is specified for each one of them. To run a simulation without boundary conditions, you will need to remove them from your schematisation and generate a new 3Di model. 

|

.. _simulate_api_qgis_initial_conditions:

Initial conditions
-------------------

Initial conditions either refer to the use of saved state file, or the use of initial water level in 1D, 2D or groundwater (2D):

1D options:

- Global value: a generic initial water level value in m MSL which is applied in all 1D nodes of the model.
- From Spatialite: the initial water level as defined in the column initial_waterlevel in the connection nodes in the spatialite.


2D Surface Water options:

- Global value: a generic initial water level value in m MSL which is applied in all 2D nodes of the model.
- Online Raster: the initial water level raster as uploaded with the model to the model database.
- Local Raster: a local the initial water level raster.
- Aggregation method: this can mean, min or max.



2D Groundwater options:

- Global value: a generic initial water level value in m MSL which is applied in all 2D groundwater nodes of the model.
- Online Raster: the initial water level raster as uploaded with the model to the model database.
- Local Raster: a local the initial water level raster.
- Aggregation method: this can mean, min or max.

.. VRAAG: moet er nog meer uitleg bij de aggregation method?

|

.. _simulate_api_qgis_laterals:

Laterals
------------

Laterals can be uploaded using .csv format for either 1D or 2D. For a more detailed description on laterals, see: :ref:`laterals`.

* Select the 'Type of laterals:'
* Upload a CSV file
* Set the time units used in your CSV file (hours, minutes, or seconds). The default is minutes (mins), because this is the time unit that is used in the 3Di spatialite
* If the option 'Interpolate' is checked, the value between time steps will be linearly interpolated. 
* Check the option 'Overrule single laterals', to exclude certain laterals in your model

.. VRAAG: klopt mijn uitleg over 'Overrule single laterals'


| **Follow these steps to generate the CSV file:**
| The instructions are for 1D laterals; for 2D laterals, the same instructions apply. 

- Load your schematisation
- In the Layers panel, right click on the layer '1D lateral' > 'Export' > 'Save features as..'
- For 'Format', choose 'Comma Separated Value [CSV]'
- Choose a 'File name' and location to save the file to
- Click 'Select fields to export and their export options'
- Make sure only the checkboxes for the fields 'id', 'connection_node_id' and 'timeseries' are checked
- Under 'Geometry' > 'Geometry type' choose 'No Geometry'
- Under 'Layer options', make sure the 'Separator' is 'comma'
- Click 'Ok' to save the file
- You can now select the CSV file under the option "Upload file(s)" when adding scenario information


*Important note: Units in the CSV are seconds (for time steps) and m3/s (for the flows).*

|

.. _dry_weather_flow:

Dry weather flow
-----------------

Dry weather flow (DWF) is the average daily flow to a waste water treatment works during a period without rain, and can be added as a CSV file:

* 'Upload dry weather flow CSV'
* If the option 'Interpolate' is checked, the value between time steps will be linearly interpolated. 
* If the option 'CSV contains 24 hour time series' is checked, 24-hour timeseries are assumed to start and end at midnight. The simulation start and end time will determine which part of the timeseries is used.


The dry weather flow that you add to your simulation, will be processed as lateral discharge. If lateral discharges on the same connection nodes already exists, the dry weather flow will be added to these lateral discharges.


**Follow these steps to generate the dry weather flow CSV file:**

- Click on 'Processing' in Menu bar and then 'Toolbox'
- Click on '3Di' > 'Dry weather flow' > 'DWF Calculator'
- Set the 'Input spatialite'
- Set a name and location to save the file under 'Output CSV'

  - 'Input spatialite': valid spatialite containing the schematisation of a 3Di model
  - 'Start time of day': at which hour of the day the simulation is started (HH:MM:SS)
  - 'Simulation duration': amount of time the simulation is run (hours)
  - 'DWF progress file': timeseries that contains the fraction of the maximum dry weather flow at each hour of the day. 

      | Formatted as follows:
      | '0, 0.03'
      | '1, 0.015'
      | ...
      | '23, 0.04'
      | Defaults to a pattern specified by Rioned.

  - 'Output CSV': csv file to which the output 1d laterals are saved. This will be the input used by the API Client.

|

.. _simulate_api_qgis_precipitation:

Precipitation
--------------

There are several options to define a precipitation event for your simulation. In the drop-down menu, one can choose 'Constant', 'Custom', 'Design' and 'Radar - NL Only' events. 


Constant

* 'Start after:' defines an offset. The offset is the duration between start simulation and the start of the rainfall event.
* 'Stop after:' the duration between the start of the simulation and the end of the rain event.
* 'Intensity:' The rain intensity (in mm/h) is uniform and constant in the given time frame. The rain intensity preview provides the rain intensity throughout the simulation in the form of a histogram.


Custom

* 'Start after:' defines an offset. The offset is the duration between start simulation and the start of the rainfall event.
* 'Values:' the event is defined in a CSV or NetCDF file. The default format is in minutes, and the rainfall in mm for that time step. Please keep in mind that the duration of the rain in the custom format cannot exceed the duration of the simulation. Here is and example of the format of a CSV file:

  .. figure:: image/d_qgisplugin_apiclient_csv_format.png
      :alt: Example CSV

* 'Units:' select the units of the uploaded file.
* 'Interpolate:' will gradually change the rain intensity throughout a time series. Without the interpolate function the rain intensity will stay constant within a time step and will make an abrupt transition to the next time step.


Design

* 'Start after:' defines an offset. The offset is the duration between start simulation and the start of the rainfall event.
* 'Design number:' a design number between 1 and 16 must be filled in. These numbers correlate to predetermined rain events, with differing return periods, that fall homogeneous over the entire model. Numbers 1 to 10 originate from `RIONED <https://www.riool.net/bui01-bui10>`_ and are heterogeneous in time. Numbers 11 to 16 have a constant rain intensity:

    | Rain 11 statistically occurs once every 100 years. The duration of this event is 1 hour with a constant rain intensity of 70 mm/h. (T= 100.0 year, V=70 mm, Standard rain event (local) from Delta Programme 2019).
    | Rain 12 statistically occurs once every 250 years. The duration of this event is 1 hour with a constant rain intensity of 90 mm/h. (T=250.0 year, V=90 mm, Standard rain event (local) from Delta Programme 2019).
    | Rain 13 statistically occurs once every 1000 years. The duration of this event is 2 hours, with a constant rain intensity of 80 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (local) from Delta Programme 2019).
    | Rain 14 statistically occurs once every 100 years. The duration of this event is 48 hours, with a constant rain intensity of 2.5 mm/h. (T=100.0 year, V=120 mm, Standard rain event (regional) from Delta Programme 2019).
    | Rain 15 statistically occurs once every 250 years. The duration of this event is 48 hours, with a constant rain intensity of 2.7 mm/h. (T=250.0 year, V=130 mm, Standard rain event (regional) from Delta Programme 2019).
    | Rain 16 statistically occurs once every 1000 years. The duration of this event is 48 hours, with a constant rain intensity of 3.4 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (regional) from Delta Programme 2019).

    These so-called design rain events are time series, which are traditionally used to test the functioning of a sewer system in the Netherlands.



Radar - NL Only 

This option is only available in the Netherlands and uses historical rainfall data that is based on radar rain images. Providing temporally and spatially varying rain information. The Dutch `Nationale Regenradar <https://nationaleregenradar.nl/>`_ is available for all Dutch applications. On request, the information from other radars can be made available to 3Di as well.

* 'Start after:' defines an offset. The offset is the duration between start simulation and the start of the rainfall event.
* 'Stop after:' the duration between the start of the simulation and the end of the rain event.

|

.. _wind_apiclient:

Wind
------

Wind in 3Di applies to 2D surface water. You can choose between a 'Constant' or a 'Custom' type of wind. Read more about wind and the physics used by 3Di here: :ref:`wind_effects`.

Constant

* 'Start after:' defining an offset for the drag coefficient. The offset is the duration between the start of the simulation and the start of the wind event.
* 'Stop after:' the duration between the start of the simulation and the end of the wind event.
* 'Windspeed:' the constant windspeed that will be added for the given time range (in m/s or km/h).
* 'Drag coefficient:' by increasing the drag coefficient, you increase the influence of the wind. It has a default value of 0,005.
* 'Direction:' the (meteorological) wind direction is defined as the direction from which the wind originates, measured in degrees clockwise from due north. Therefore, wind blowing toward the south has a direction of 0 degrees. You can either use the wind rose to depict which way the wind is blowing, or enter the direction manually.


Custom

* 'Start after:' defining an offset for the drag coefficient. The offset is the duration between the start of the simulation and the start of the wind event.
* 'Drag coefficient:' by increasing the drag coefficient, you increase the influence of the wind. It has a default value of 0,005.
* 'Values:' upload a CSV in the format minutes, wind speed in m/s and wind direction, both for that time step.Here is and example of the format of a CSV file:

  .. figure:: image/d_qgisplugin_apiclient_wind_csv.png
    :alt: Overview new simulation

* the 'Interpolate' options will gradually change the wind speed or wind direction throughout a time series. Without the interpolate functions the wind speed and wind direction will stay constant within the time steps and will make an abrupt transition to the next time step.

|

.. _sim_structure_controls:

Structure controls
-------------------

Structure controls provide the capability to modify hydraulic structure parameters within a water system by leveraging flow variables. These flow variables serve as triggers for actions on a structure, based on predefined rules specific to the type of control employed. For a comprehensive understanding, visit the :ref:`structures` and the :ref:`control` pages.


To incorporate structure controls, there are two methods: utilizing a simulation template or uploading a JSON file. When using a simulation template, you have four options:

* File structure controls
* :ref:`Table structure controls <table_control>`
* :ref:`Memory structure controls <memory_control>`
* Timed structure controls
  

.. VRAAG: De andere dingen stonden nog niet uitgelegd in de documentatie. Klopt dit stukje nu een beetje?

|

.. _simulate_api_qgis_breaches:

Breaches
---------

The dimension of a breach in a levee can be added to determine the flow through the breach and subsequently the flood. For a description on breaches, see: :ref:`breaches`.

If you choose a model that incorporates breaches for simulation, a breaches file will be downloaded from the server and added to the layers panel when you select the desired model. The breaches will be visible in the map view. When adding a breach to your simulation the following parameters need to be filled in:

* 'ID of breach:' select the ID of the breach to be used in the simulation.
* 'Initial width:' specify the initial width of the breach.
* 'Duration till max depth:' determine the duration of the breach until it reaches its maximum depth.
* 'Start after:' defining an offset for the breach. The offset is the duration between the start of the simulation and the start of the breach event.
* 'Max breach depth:' set the maximum depth that the breach can reach.
* 'Discharge coefficient positive/negative:' these coefficients are utilized in the discharge formulation. Depending on the flow direction, the coefficients may vary.

.. VRAAG: Klopt deze uitleg zo? heb ik hem aangepast.


|

.. _generate_api_qgis_saved_state:

Generate saved state after simulation
----------------------------------------------

When you check this option the end result of the simulation will be saved as a saved state. A saved state file can be used as an initial condition. For more information, see: :ref:`state_files`.

|

.. _simulate_api_qgis_post_processing:

Post-processing in Lizard
----------------------------

Storing your results in Lizard and automated post-processing is only available for users of organisations with a Lizard account.

Checking the **'Post-Processing in Lizard'** function will generate the following maps:

- water depth maps per output time step
- maximum water depth map for the whole simulation
- flood hazard rating
- rise velocity
- water level for each output time step
- maximum water level for the whole simulation
- max velocity
- rainfall

The Basic processed results are stored the 3Di output files in the Lizard platform:

- Result NetCDF (containing actual values)
- Aggregate NetCDF (availability and content dependent on user settings. required for water balance tool in Modeller Interface)
- Grid administration (gridadmin.h5 file. required to load NetCDF results in Modeller Interface)
- Calculation core logging (A zip containing logfiles)

All maps can be downloaded as GTiff, either via the interface `<https://demo.lizard.net/>`_ or via the lizard API.


**'Arrival time map'**: calculates a map showing the time of arrival of water per pixel in hours

**'Damage estimation'**: automated estimate maps of damage as a result of flooding. This option takes into account water depth and duration of flood, resulting ing the following damage maps:

- Water depth (WSS)
- Damage (direct)
- Damage (indirect)
- Total damage
- And a damage summary in csv format. For more information check the documentation here: https://docs.lizard.net/e_catalog.html#results

.. Note:: The damage estimations are only available in the Netherlands. Contact us at servicedesk@nelen-schuurmans.nl if you like to use this option and don't have access yet.

|

.. _simulate_api_qgis_multi_sim:

Multiple simulations
--------------------------
This option becomes available when using either breaches or precipitation. You can define multiple simulations with different rainfall or breaches. Useful when simulating multiple events on the same model.

|
|

Old table
-----------

.. VRAAG: Is dit nog steeds relevant om in de documentatie te hebben? En zo ja dan zou ik de titel verduidelijken.

The most used API options are included in the newest version of the plugin. Important consideration is a difference between API v1 and v3 how initial waterzylevels, laterals and boundaries are handled. The current status is as follows:

============================= =========================== =========================================== ==================================
Forcings                        Live site                  "3Di Models and Simulations" Wizard         OpenAPI Client
============================= =========================== =========================================== ==================================
Boundary conditions            SQLite                      SQLite                                      SQLite, can be overwritten (a)
Initial water level 2D         SQLite, always 'max'        Add raster/global in wizard                 Add raster/global to simulation
Initial water level 1D         SQLite                      Add predefined/global in wizard             Add predefined to simulation
Initial water level GW         SQLite                      Add predefined/global in wizard             Add predefined to simulation
Laterals  1D and 2D            Not used                    Add in wizard with CSV (b)                  Add CSV
Breaches                       Open in gui                 Open breach using wizard                    Open breach
Precipitation                  Add using live site         Add using wizard (c)                        Add to simulation
Wind                           Add using live site         Add using wizard                            Add to simulation
Control Structures             Not used from SQLite        Not used from SQLite                        Add to simulation
DWF (inflow)                   Not used from SQLite        Add as laterals, use dwf calculator         Add to simulation as lateral CSV
Settings                       SQLite                      SQLite                                      SQLite, can be overwritten
============================= =========================== =========================================== ==================================


This is a temporary situation, simulation templates will be implemented on our servers. In these templates users will be able to predefine the forcings and settings that users want to use in a model. A model can contain multiple simulation templates

**(a):** When overwriting the boundary conditions, both 1D and 2D need to be supplied

**(b):** When using the laterals as a CSV note that units of the laterals in the wizard are expected in m3/s

**(c):** CSV files can contain up to 300 entries

This means that for *boundary conditions* nothing changes between API v1 and v3. Values are taken from the spatialite. The following requirements still hold for the boundary conditions:

- number of entries have to be exactly the same
- time has to be the same value (e.g. al time series have 0, 10, 20, 40 as time. It is not possible to have a boundary condition with the time as 0,15,20,40)

*Initial water levels* are taken from the spatialite if the users selects this in the wizard, see the section on initial conditions below for a 'how to'.

*Laterals* are not taken into account when added to the spatialite. The user has to add them to the API call for them to be taken into account. See the section on laterals below for a 'how to'.

*DWF (inflow)* In API v1 inflow on connection nodes is being calculated based on nr of inhabitants per impervious surface and the mapping to the connection nodes. In API v3 users can calculate the inflow separately using the dwa calculator tool. The output of this tool is a csv with lateral inflow. This csv can be used in the "3Di Models and Simulations". In this approach is more transparant and generic usable for different countries.




.. |modelsSimulations| image:: /image/e_modelsandsimulations.png
    :scale: 90%
