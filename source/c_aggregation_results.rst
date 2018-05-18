Aggregated output
=================

Results for a 3Di simulation are normally written in a results file called *results_3di.nc* (previously *subgrid_map.nc*). This file contains the flow information (Snap Shots) at different times in the simulation. The interval at which these flow information are written is defined by the user via the parameter *output_time_step*. 
Aggregated results from certain intervals during the simulation can be very useful. For this purpose an aggregated results file is available called *aggregate_ results_3di.nc* (previously *flow_aggregate.nc*). The configuration for this aggregation file is available in the models spatialite and the table is called v2_aggregation_settings. The configuration with its options will be explained below. The layout of the table is:

.. figure:: image/aggregation_table.png
   :alt: Table layout aggregation options

Configuration options
---------------------

var_name
^^^^^^^^

A user-defined variable name to distinguish between aggregated configuration of variables. This setting is mandatory.

flow_variable
^^^^^^^^^^^^^

Flow variable for which to determine aggregated results. The flow variables for which to determine aggregated results are:

* discharge
* flow_velocity
* infiltration
* pump_discharge
* rain
* volume
* waterlevel
* wet_cross-section
* wet_surface
* lateral_discharge

aggregation_method
^^^^^^^^^^^^^^^^^^

The different aggregation methods that can be used on a flow variable are:

* max = maximum value of variable in timestep (configurated interval)
* min = minimum value of variable in timestep (configurated interval)
* avg = average value of variable in timestep (configurated interval)
* cum = This is integration over time of variable [dt * variable]. For instance cumulative net volume across flowline in timestep (configurated interval)
* cum_positive = This is integration over time of variable in positive direction [dt * variable]. For instance cumulative volume across flowline in positive direction for timestep (configurated interval)
* cum_negative = This is integration over time of variable in negative direction [dt * variable]. For instance cumulative volume across flowline in negative direction for timestep (configurated interval)

time step
^^^^^^^^

Timestep is the interval in seconds for writing and determining the aggregated flow results. An example is when the maximum waterlevel needs to be determined every 300 seconds. Every 300 seconds the maximum waterlevel in that interval is determined at the end of this interval. Users can determine for each for each *flow_variable* multiple aggregation options as long as the given *var_name* is different. However, each combination of *aggregation_method* in combination to a *flow_variable* can only occur once.

aggregation_in_space
^^^^^^^^^^^^^^^^^^^^^^
This setting is not yet implemented and is therefore always *False*.

Output layout
-------------

The variable name of the aggregated flow results in the *aggregate_ results_3di.nc* is named based on the following convention:

<flow_variable>_<aggregation _method> 

Every aggregated results has it’s own time variable in the aggregated result file at which the aggregated flow results were written. This variable will be named based on the following convention:
time_<aggregation_variable>
