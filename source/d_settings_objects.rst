.. _settings_objects:

Settings objects
================

.. _global_settings:

Global settings
---------------

Global settings


.. _aggregation_settings:

Aggregation settings
--------------------

You can set multiple aggregation options for each *flow_variable* as long as the *aggregation_method* is not used twice for the same flow_variable.

Columns
^^^^^^^

var_name
""""""""

A user-defined variable name to distinguish between aggregated configuration of variables for user administration only. This setting is mandatory.

flow_variable
"""""""""""""

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
* surface_source_sink_discharge


aggregation_method
""""""""""""""""""

The different aggregation methods that can be used on a flow variable are:

* max: maximum value of the variable in the configured interval (time step).
* min: minimum value of the variable in the configured interval (time step).
* avg: average value of the variable in the configured interval (time step).
* cum: This is integration over time of the variable [dt * variable]. For instance, the cumulative net discharge across a flow line in the configured interval.
* cum_positive: This is integration over time of the variable [dt * variable] in positive direction. For instance, the cumulative net discharge in positive direction across a flow line in the configured interval.
* cum_negative: This is integration over time of the variable [dt * variable] in negative direction. For instance, the cumulative net discharge in negative direction across a flow line in the configured interval.
* current: Uses the current value of a variable. This is required in case one checks the water balance for variables that are the result of the processes. This is a setting only valid for *volume* and *intercepted_volume*.


time_step
"""""""""

Time step is the interval in seconds for writing and determining the aggregated flow results. In the example above, the maximum water level is determined over every 600 seconds. The minimum water level is determined over a period of 500 seconds.


Simple infiltration settings
----------------------------

Settings for 'simple' infiltration in models without groundwater

Groundwater settings
--------------------

Groundwater settings

Interflow settings
------------------

Interflow settings

.. _numerical_settings:

Numerical settings
------------------

Numerical settings (advanced users)


.. _vegetation_drag:

Vegetation drag settings
------------------------

The *vegetation drag* table contains the input parameters that are used for 2D flow with vegetation. For an in-depth explanation of how 2D flow with vegetation is calculated by 3Di, see :ref:`flow_with_vegetation`. For more information on using vegetation in your 3Di model and choosing the right parameter values, :ref:`a_how_to_vegetation`.

Vegetation drag can only be used with friction type 'Chezy', because the vegetation formulation (initially introduced by Baptist 2005) uses Chezy.

Columns
^^^^^^^

id
""

Unique identifier

height
""""""
Height of the vegetation (m), i.e. the length of the plant stems.  Global value that is used in the entire model domain, used by 3Di if no raster (*height_file*) is supplied.

height_file
"""""""""""
Reference to a raster file containing the *height of the vegetation (m), i.e. the length of the plant stems*. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *height* will be ignored.

stem_count
""""""""""
Density of plant stems (number of stems per m:sup:`2`). Global value that is used in the entire model domain, used by 3Di if no raster (*stem_count_file*) is supplied.

stem_count_file
"""""""""""""""
Reference to a raster file containing the *density of plant stems (number of stems per m:sup:`2`)* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *stem_count* will be ignored.

stem_diameter
"""""""""""""
Mean diameter of plant stems (m). Global value that is used in the entire model domain, used by 3Di if no raster (*stem_diameter_file*) is supplied.

stem_diameter_file
""""""""""""""""""
Reference to a raster file containing a *mean diameter of plant stems (m)* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *stem_diameter* will be ignored.

drag_coefficient
""""""""""""""""

Dimensionless coefficient to linearly scale the drag that vegetation exerts on the water. The drag resulting from vegetation is different for each situation. A large share of this variation is captured by choosing the correct values for stem count, stem diameter and vegetation height. The drag coefficient can be used to account for the other factors that affect the drag. The drag coefficient can also be used as a calibration parameter.

Global value that is used in the entire model domain, used by 3Di if no raster (*drag_coefficient_file*) is supplied.

drag_coefficient_file
"""""""""""""""""""""

Reference to a raster file containing a *drag_coefficient* for each pixel. Values can be varied on the pixel level and will also be used as such by the 3Di computational core. If a raster file is supplied, any global value given in *drag_coefficient* will be ignored.
