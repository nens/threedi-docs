.. _aggregationnetcdf:

Aggregated output
=================

Results for a 3Di simulation are written in a results file called *results_3di.nc* (previously *subgrid_map.nc*). This file contains the flow information (snap shots) at different times in the simulation. The interval at which this information is written, is defined by the user via the parameter *output_time_step*. 

Aggregated results over certain intervals during the simulation can be very useful. For instance, the aggregated results are the input for the water balance tool in QGIS. For a consistent water balance, the results of various snap shots is not enough in case of an output time step which is larger than the computational time step. For this purpose, an aggregated results file is available called *aggregate_ results_3di.nc* (previously *flow_aggregate.nc*). The structure of the file is very similar as the other result file. Each Mesh variable (s1, u1, etc.) described in the results section can be aggregated. The configuration for this aggregation file is available in the models spatialite and the table is called v2_aggregation_settings. The configuration and its options are explained below. The layout of the table is:

.. figure:: image/aggregation_table.png
   :alt: Table layout aggregation options

Configuration options
---------------------

In the spatialite a table can be filled to configure variables and their aggregation methods to acquire the desired aggregation results. The possible flow variables and their specific inputs are described along with all the possible aggregation methods. Users can determine multiple aggregation options for each *flow_variable* as long as the *aggregation_method* is not used twice for the same flow_variable.

var_name
^^^^^^^^

A user-defined variable name to distinguish between aggregated configuration of variables for user administration only. This setting is mandatory.

flow_variable
^^^^^^^^^^^^^

The different flow variable for which to determine aggregated results are. The flow variables for input to generate aggregated results are:

* waterlevel
* flow_velocity
* discharge
* volume
* pump_discharge
* wet_cross-section
* lateral_discharge
* wet_surface
* rain
* simple_infiltration
* leakage
* interception

aggregation_method
^^^^^^^^^^^^^^^^^^

The different aggregation methods that can be used on a flow variable are:

* max: maximum value of the variable in the configured interval (time step).
* min: minimum value of the variable in the configured interval (time step).
* avg: average value of the variable in the configured interval (time step).
* cum: This is integration over time of the variable [dt * variable]. For instance, the cumulative net discharge across a flow line in the configured interval.
* cum_positive: This is integration over time of the variable [dt * variable] in positive direction. For instance, the cumulative net discharge in positive direction across a flow line in the configured interval.
* cum_negative: This is integration over time of the variable [dt * variable] in negative direction. For instance, the cumulative net discharge in negative direction across a flow line in the configured interval.
* current: the value at the output time

time step
^^^^^^^^

Time step is the interval in seconds for writing and determining the aggregated flow results. In the example above, the maximum water level is determined over every 600 seconds. The minimum water level is determined over a period ov 500 seconds. 

aggregation_in_space
^^^^^^^^^^^^^^^^^^^^
This setting is not yet implemented and is therefore always *False*.

Output format in result file
-----------------------------

The variable name of the aggregated flow results in the *aggregate_ results_3di.nc* are named based on the chosen flow variable and the chosen aggregation method:

The flow variable chosen in the flow_variable field is converted to the flow_variable naming of threedi concatenated with the aggregation method. This convention look like this:
<threedi_flow_variable>_<aggregation _method> 
Every aggregated results has it’s own time variable in the aggregated result file at which the aggregated flow results were written. This variable will be named based on the following convention:
time_<aggregation_variable>

The translation between the input flow variable name and the format in the the output file is given in the table below:

* waterlevel - s1
* flow_velocity - u1
* discharge - q
* volume - vol
* pump_discharge - q_pump
* wet_cross-section - au
* lateral_discharge - q_lat
* wet_surface - su
* rain - rain
* simple_infiltration - infiltration_rate_simple
* leakage - leak
* interception - intercepted_volume

An example of the output name is::

  flow_variable: s1
  aggregation_method: max
  output_name: Mesh2D_s1_max and Mesh1D_s1_max
  time_name: time_s1_max

QGIS plugin: water balance tool
-----------------------------------

To use the water balance tool in the 3Di QGIS plugin you must set a specific set of aggregation settings. These settings are listed below.

.. csv-table:: Aggregation settings for water balance tool
   :file: other/water_balance_aggregation_settings.csv
   :widths: 5, 10, 20, 15, 15, 20
   :header-rows: 1
  