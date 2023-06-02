.. _aggregationnetcdf:

Aggregated output
=================

Aggregated results over certain intervals during the simulation can be very useful. For instance, the aggregated results are the input for the water balance tool in QGIS. For a consistent water balance, the results of various snap shots is not enough in case of an output time step which is larger than the computational time step. For this purpose, an aggregated results file is available called *aggregate_ results_3di.nc*. The structure of the file is very similar to the other result file. Each Mesh variable (s1, u1, etc.) described in the results section can be aggregated. Which variables to include in this file is set in the :ref:`aggregation_settings`.

Output format in result file
-----------------------------

The variable name of the aggregated flow results in the *aggregate_results_3di.nc* are a combination of flow variable and  aggregation method: <flow_variable>_<aggregation_method>
Every aggregated results has its own time variable in the aggregated result file at which the aggregated flow results were written. This variable will be named based on the following convention:
<time>_<aggregation_variable>

The translation between the input flow variable name and the format in the output file is given in the table below:

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
* surface_source_sink_discharge - q_sss

An example of the output name is::

  flow_variable: s1
  aggregation_method: max
  output_name: Mesh2D_s1_max and Mesh1D_s1_max
  time_name: time_s1_max

Settings for water balance tool
-------------------------------

To use the water balance tool in the 3Di QGIS plugin you must set a specific set of aggregation settings. These settings are listed under :ref:`waterbalanceactivate`.


  