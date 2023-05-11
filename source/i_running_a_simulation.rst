.. _simulate_api_qgis:

Running a simulation
=====================

To perform a simulation using the Modeller Interface, we will utilize the 3Di Models and Simulation plugin. This section offers valuable insights into the various options available for your specific :ref:`scenario <add_scenario_info>`.


.. todo:
    dit stuk moet ik nog helemaal checken of het wel klopt en up to date is.

.. _start_up_api_qgis:

Start up the "3Di Models and Simulations"
-----------------------------------------

Open the Modeller Interface. Click on **Plug-ins** from the menu bar and open the dropdown menu. Click on **"3Di Models and Simulations"** to start up the plugin.
For a guide on how to install the Modeller Interface or the"3Di Models and Simulations" see :ref:`3di_instruments_and_downloads`.

.. figure:: image/d_openplugin.png
   :alt: Open the 3Di Models and Simulations plugin


.. _load_model_api_qgis:

Load model
------------

Load your model by clicking **start** in the "3Di Models and Simulations". In the pop-up window (wizard) choose **Load from Web**.

**Note:** If you are using 3Di outside of the Netherlands you need to change the Base API. See: :ref:`plugin_settings` on how to do this.

.. TODO: *screenshot toevoegen*

.. figure:: image/d_qgisplugin_apiclient_start.png
    :alt: Load from web

.. figure:: image/d_qgisplugin_apiclient_login.png
    :alt: Load from web

Users that have access to run simulations for more than one organisation will get a menu in which they choose the organisation:

.. figure:: image/d_qgisplugin_apiclient_login_choose_organisation.png
    :alt: Choose organisation

Now choose **only simulate** (only option available at the moment):

.. figure:: image/d_qgisplugin_apiclient_choose_simulate.png
    :alt: Choose simulate


Choose the model that you like to run simulations on, and click **Load model**:

.. figure:: image/d_qgisplugin_apiclient_login_choose_model.png
    :alt: Choose simulate

On load of the model the following files are retrieved from the server:

- cells
- breaches (only when present in your model)

.. figure:: image/d_qgisplugin_load_model_cells_breaches.png
    :alt: Loaded model with Cells and Breach

Cells represent the computational grid comprised of computational cells. This file can help analyze modelling results when used in an overlay with the model schematization.
For theoretical information, see :ref:`grid`.

Breaches can be used for breach calculations. The number of the breach as shown in the map canvas is the number required in the wizard. Alternatively, you can also select a breach before starting the wizard, see :ref:`addleveebreaches`. This breach will then be used in the calculation. For theoretical information, see :ref:`breaches`.

Note: if the files have been downloaded before the Modeller Interface will use the cached version.


Simulate
----------

To start a simulation, click on the **SIMULATE** button. Next, the following window will be shown:

.. figure:: image/d_qgisplugin_apiclient_runningsimulations.png
    :alt: Choose simulate

This window shows an overview of current simulations for the specific organisation. In this panel simulations can be started and stopped.

To stop a simulation, select the simulation you want to stop and click on **Stop Simulation**.

To start a simulation you can either use **Load template** or **New simulation**. Both options will enable you to fill in scenario information and start a simulation.


.. _add_scenario_info:

Add scenario information
----------------------------

Using **Load template** enables you to re-use a previously stored scenario template. All the previous defined settings are automatically filled into the scenario information. This information can still be edited, before you run the simulation.

Selecting **New Simulation** will start a simulation with a new scenario that still needs to be filled in. After clicking 'new simulation' the start screen of the wizard is shown:

.. figure:: image/d_qgisplugin_apiclient_start_screen_new_simulation.png
    :alt: Choose new simulation

In this window the various options, to be used in the simulation calculation, can be defined.


Boundary conditions:
Not configurable yet. Boundary conditions are taken from the spatialite directly.

:ref:`simulate_api_qgis_initial_conditions`:
To define the use of a (previously) saved state or initial water levels in 1D, 2D or Ground water.

:ref:`simulate_api_qgis_laterals`:
To select laterals to use in the model.

:ref:`simulate_api_qgis_breaches`:
To select a breach to open in the model.

:ref:`simulate_api_qgis_precipitation`:
To define precipitation in the model.

:ref:`wind_apiclient`:
To define wind in the model.

:ref:`simulate_api_qgis_multi_sim` (becomes available when using either breaches or precipitation):
To define multiple simulations with rainfall or breaches. Useful when simulating multiple events on the same model.

:ref:`generate_api_qgis_saved_state`:
To save the end result of the simulation as a saved state.

:ref:`simulate_api_qgis_post_processing`:
This is a feature that is only available for users of organisations that have a Lizard account. It enables you to store the results in the cloud and it triggers automated post-processing of water depth, water levels, time of arrival, flood hazard rating and damage estimations maps.
See :ref:`simulate_api_qgis_post_processing` on how to use post-processing.


**Check** the options you want to be used in the calculations of your simulation, and click **Next**.

The next step is to name the simulation. You and other users within your organisation will be able to find this simulation and its results based on the name. It can also be used to look up simulations later.

Adding tags can clarify for other users what your simulation calculated or can be used to assign a simulation a certain project name or number.

.. figure:: image/d_qgisplugin_apiclient_new_simulation.png
    :alt: Choose new simulation

The first step in any simulation is choosing the duration of the simulation:


.. figure:: image/d_qgisplugin_apiclient_choose_duration.png
    :alt: Choose duration

The next steps depend on the selection of options from the initial screen of the wizard. Unchecked options will be omitted by the wizard.


.. _simulate_api_qgis_initial_conditions:

Initial conditions
"""""""""""""""""""""

Initial conditions either refer to the use of saved state file, or the use of initial water level in 1D, 2D or groundwater (2D).

.. figure:: image/d_qgisplugin_apiclient_initialconditions_start.png
    :alt: Choose initial conditions

1D options:

- Predefined: this refers to the initial water level as defined in the column initial_waterlevel in the connection nodes in the spatialite.
- Global value: this would be a generic initial water level value in m MSL which is applied in all 1D nodes of the model.

2D Surface Water options:

- Raster: this refers to the initial water level raster as uploaded with the model to the model database.
- Aggregation settings: This can min, max or average
- Global value: this would be a generic initial water level value in m MSL which is applied in all 2D nodes of the model.


2D Groundwater options:

- Raster: This refers to the initial water level raster as uploaded with the model to the model database.
- Global value: This would be a generic initial water level value in m MSL which is applied in all 2D ground water nodes of the model.


.. _simulate_api_qgis_boundary_conditions:

Boundary conditions
"""""""""""""""""""

If the 3Di model contains boundary conditions, a timeseries for each boundary condition will be included in the simulation template. On the 'boundary conditions' page of the simulation wizard, you can upload CSV files to replace the boundary conditions that are included in the simulation template. You can only replace *all* boundary conditions. For example, if your model contains two 1D boundary conditions and five 2D boundary condition, the CSV file for the 1D boundary conditions should contain time series for both of the two 1D boundary conditions and the CSV file for the 2D boundary conditions should contain time series for all five 2D boundary conditions. The simulation wizard will merge them into a single JSON file that is sent to the API


Boundary conditions CSV file format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The CSV file input should have the following columns:

- "id": integer; is the id of the corresponding row in the v2_1d_boundary_conditions table in the spatialite
- "timeseries": a CSV-formatted text field: pairs of time step (in minutes or seconds) and value (in m\ :sup:`3`/s, m, or m/m, depending on the boundary condition type). The timestep is separated from the value by a comma and lines are separated from one another by a newline.

Example (as a table):

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


Options
^^^^^^^

If you have selected the option "Upload file(s)", you have two configuration options:


Units
#####

Here you can set the time units used in your CSV file (hours, minutes, or seconds). The default is minutes, because this is the time unit that is used in the 3Di spatialite.


Interpolate
###########


If this option is checked, the value between time steps will be linearly interpolated. For example, consider the following time series:

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

Editing a time series for a single boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run a simulation in which only one or a few boundary conditions have a different time series, take the following steps. The instructions are for 1D Boundary conditions; for 2D Boundary conditions, the same instructions apply. 

- Load your schematisation
- In the Layers panel, right click on the layer *1D Boundary condition* > *Export* > *Save features as..*
- For *Format*, choose *Comma Separated Value [CSV]*
- Choose a *File name* to save the file to
- Click *Select fields to export and their export options*
- Make sure only the checkboxes for the fields *id* and *timeseries* are checked
- Under *Geometry* > *Geometry type* choose *No Geometry*
- Under *Layer options*, make sure the *Separator* is 'comma'
- Save the file
- Open the file in a text editor to edit the values and save the CSV file.
- In the simulation wizard, on the *Boundary conditions* page, choose the option "Upload file(s)" and browse for the edited CSV file you just saved.
     

Running a model without boundary conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the 3Di model contains boundary conditions, you can only run a simulation if a time series is specified for each one of them. To run a simulation without boundary conditions, you will need to remove them from your schematisation and generate a new 3Di model. 


.. _simulate_api_qgis_laterals:

Laterals
""""""""""

Laterals can be uploaded using .csv format for either 1D or 2D. For a more detailed description on laterals, see: :ref:`laterals`.

.. figure:: image/d_qgisplugin_apiclient_laterals_start.png
    :alt: Choose laterals

The CSV file format is generated by a right-mouse click on table: v2_1d_lateral. Then choose export --> save features as --> Select csv as output format. Choose a filename and location to store and click OK. the file should be like this:

.. figure:: image/d_qgisplugin_apiclient_laterals_export_csv_example.png
    :alt: Export laterals as csv

*Important note: Units in the CSV are seconds (for time steps) and m3/s (for the flows).*

.. _simulate_api_qgis_breaches:

Breaches
"""""""""

A breach can be selected using the menu below:

.. figure:: image/d_qgisplugin_apiclient_breaches.png
    :alt: Breaches

When choosing the model to calculate in a breaches file was downloaded from the server. The number of the breach as shown in the map canvas is the number required in the wizard. Alternatively, you can also select a breach before starting the wizard. This breach will then be used in the calculation.

For a description on breaches, see: :ref:`breaches`.


.. _simulate_api_qgis_precipitation:

Precipitation
"""""""""""""""

There are several options to define a precipitation event for your simulation. In the drop-down menu, one can choose Constant, Custom, Design and Radar events. For all events an offset can be defined. The offset is the duration between start simulation and the start of the rainfall event.

.. figure:: image/d_qgisplugin_choose_type_of_precipitation.png
    :alt: Choose type of precipitation

When choosing a **Constant** type of precipitation, the stop after and rain intensity (in mm/h) must also be defined. The stop after is the duration between the start of the simulation and the end of the rain event. The rain intensity is uniform and constant in the given timeframe. The rain intensity preview provides the rain intensity throughout the simulation in the form of a histogram.

.. figure:: image/d_qgisplugin_apiclient_rain_constant.png
    :alt: Choose constant rain

When choosing the option **Custom**, the event is defined in a CSV-file. The format is in minutes, and the rainfall in mm for that time step. Please keep in mind that the duration of the rain in the custom format cannot exceed the duration of the simulation. The interpolate option will gradually change the rain intensity throughout a time series. Without the interpolate function the rain intensity will stay constant within a time step and will make an abrupt transition to the next time step.

.. figure:: image/d_qgisplugin_apiclient_rain_custom.png
    :alt: Choose custom rain

.. figure:: image/d_qgisplugin_apiclient_csv_format.png
    :alt: Example CSV

When choosing the option **Design**, a design number between 1 and 16 must be filled in. These numbers correlate to predetermined rain events, with differing return periods, that fall homogeneous over the entire model. Numbers 1 to 10 originate from `RIONED <https://www.riool.net/bui01-bui10>`_ and are heterogeneous in time. Numbers 11 to 16 have a constant rain intensity:

Rain 11 statistically occurs once every 100 years. The duration of this event is 1 hour with a constant rain intensity of 70 mm/h. (T= 100.0 year, V=70 mm, Standard rain event (local) from Delta Programme 2019).

Rain 12 statistically occurs once every 250 years. The duration of this event is 1 hour with a constant rain intensity of 90 mm/h. (T=250.0 year, V=90 mm, Standard rain event (local) from Delta Programme 2019).

Rain 13 statistically occurs once every 1000 years. The duration of this event is 2 hours, with a constant rain intensity of 80 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (local) from Delta Programme 2019).

Rain 14 statistically occurs once every 100 years. The duration of this event is 48 hours, with a constant rain intensity of 2.5 mm/h. (T=100.0 year, V=120 mm, Standard rain event (regional) from Delta Programme 2019).

Rain 15 statistically occurs once every 250 years. The duration of this event is 48 hours, with a constant rain intensity of 2.7 mm/h. (T=250.0 year, V=130 mm, Standard rain event (regional) from Delta Programme 2019).

Rain 16 statistically occurs once every 1000 years. The duration of this event is 48 hours, with a constant rain intensity of 3.4 mm/h. (T=1000.0 year, V=160 mm, Standard rain event (regional) from Delta Programme 2019).


These so-called design rain events are time series, which are traditionally used to test the functioning of a sewer system in the Netherlands.

.. figure:: image/d_qgisplugin_apiclient_rain_design.png
    :alt: Choose design rain

**Radar - NL Only** is only available in the Netherlands and uses historical rainfall data that is based on radar rain images. Providing temporally and spatially varying rain information. The Dutch `Nationale Regenradar <https://nationaleregenradar.nl/>`_ is available for all Dutch applications. On request, the information from other radars can be made available to 3Di as well.

.. figure:: image/d_qgisplugin_apiclient_rain_radar.png
    :alt: Choose radar rain


.. _simulate_api_qgis_multi_sim:

Multiple simulations
"""""""""""""""""""""
This option becomes available when using either breaches or precipitation. You can define multiple simulations with different rainfall or breaches. Useful when simulating multiple events on the same model.


.. _wind_apiclient:

Wind
"""""""

Wind in 3Di applies to 2D surface water. Read more about wind and the physics used by 3Di here: :ref:`wind_effects`.

You can choose between a Constant or a Custom type of wind. For both events an offset and a drag coefficient can be defined. The offset (start after) is the duration between the start of the simulation and the start of the wind event. The drag coefficient has a default value of 0,005. By increasing the drag coefficient, you increase the influence of the wind.

When choosing a **Constant** wind event, the stop after, wind speed and direction must also be defined. The stop after is the duration between the start of the simulation and the end of the wind event.
The (meteorological) wind direction is defined as the direction from which the wind originates, measured in degrees clockwise from due north. Therefore, wind blowing toward the south has a direction of 0 degrees. You can either use the wind rose to depict which way the wind is blowing, or enter the direction manually.

.. figure:: image/d_qgisplugin_apiclient_wind_constant.png
    :alt: Choose Constant wind

When choosing a **Custom** wind, the CSV format is minutes, wind speed in m/s and wind direction, both for that time step. The interpolate options will gradually change the wind speed or wind direction throughout a time series. Without the interpolate functions the wind speed and wind direction will stay constant within the time steps and will make an abrupt transition to the next time step.

.. figure:: image/d_qgisplugin_apiclient_wind_custom.png
    :alt: Choose Custom wind

.. figure:: image/d_qgisplugin_apiclient_wind_csv.png
    :alt: Example CSV wind

After choosing all the settings check the overview, press **Next** and **Add to Queue**. The simulation will start up when there is a session available on the servers within your organisation.

.. figure:: image/d_qgisplugin_apiclient_preview_simulation.png
    :alt: Overview new simulation


.. _generate_api_qgis_saved_state:

Generate saved state after simulation
""""""""""""""""""""""""""""""""""""""
To save the end result of the simulation as a saved state. A saved state file can be used as an initial condition. For more information, see: :ref:`state_files`.

.. _simulate_api_qgis_post_processing:

Post-processing in Lizard
----------------------------

Storing your results in Lizard and automated post-processing is only available for users of organisations with a Lizard account.
This function will generate maps of water depth for each output time step, a maximum water depth for the whole simulation water levels for each output time step, a maximum water level for the whole simulation, time of arrival, flood hazard rating and damage estimations.
The damage estimations are only available in the Netherlands. Contact us at servicedesk@nelen-schuurmans.nl if you like to use this option and don't have access yet.



.. figure:: image/d_qgisplugin_apiclient_postprocessing_lizard.png
    :alt: Example CSV

**Basic processed results** stores the 3Di output files in the Lizard platform:

- Result NetCDF (containing actual values)
- Aggregate NetCDF (availability and content dependent on user settings. required for water balance tool in Modeller Interface)
- Grid administration (gridadmin.h5 file. required to load NetCDF results in Modeller Interface)
- Calculation core logging (A zip containing logfiles)

As a service, the following maps are available in Lizard:

- water depth maps per output time step
- maximum water depth map
- flood hazard rating
- rise velocity
- water level
- max water level
- max velocity
- rainfall

All maps can be downloaded as GTiff, either via the interface `<https://demo.lizard.net/>`_ or via the lizard API.

When **Arrival time map** is checked a map with arrival time is being calculated showing the time of arrival of water per pixel in hours.

**Damage estimation** is only available in the Netherlands: automated estimate of damage as a result of flooding. Takes into account water depth and duration of flood. Result is the following damage maps:

- Water depth (WSS)
- Damage (direct)
- Damage (indirect)
- Total damage

And a damage summary in csv format. For more information check the documentation here: https://docs.lizard.net/e_catalog.html#results



.. _simulate_api_qgis_results:

Results
----------

For information on how to get, view and analyze results, see :ref:`mi_download_res` and :ref:`view_analyze_mi`.



Old table
-----------

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
