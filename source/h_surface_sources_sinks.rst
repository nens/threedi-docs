.. _sssdischarges:

Surface sources and sinks
=========================

Processes like evaporation or seepage can be included in a 3Di simulation using the *Surface sources and sinks*. This add and/or extracts water from the 2D surface domain. These source and sink terms can represent any hydrological process, evaporation being the most common use case. The way it works is similar to a :ref:`2D lateral<laterals>`, with the difference that the surface sources and sinks are applied on an area, while laterals are applied to a point location.


Input
^^^^^

The *Surface sources and sinks* are a forcing, which are included in the :ref:`simulation template<simulation_and_simulation_templates>`. They cannot be defined in the spatialite, they are not yet included in the simulation wizard. To use *Surface sources and sinks*, you will need to start your simulation via a script that uses :ref:`a_api`.

Input can be supplied in various formats:

- Constant: a constant value for a specific duration, applied to the entire model domain

- Time series: a value that varies over time, applied to the entire model domain. This time series can be supplied in the API call, as NetCDF, or retrieved from Lizard.

- Spatio-temporal variation: a value that varies spatially and over time, supplied as a NetCDF file or as a temporal raster from Lizard.

The input rates are defined in *m/s*, and will automatically be converted to m³ by multiplying it by each cell's surface area.

Output
^^^^^^^^^^

The actual surface source and sink discharges per computational cell are recorded in the :ref:`3dinetcdf` file. In addition to these results, one can also generate  :ref:`aggregated results<aggregationnetcdf>`. The positive and negative cumulative results are required for using the :ref:`water_balance_tool`.


.. note::
   Surface *sinks* (i.e. negative values in the time series) extract water from the model. If less water is available in the node or cell then what is to be extracted, 3Di will limit the extraction. Just before the cell becomes dry, the extraction rate will be less than the extraction rate in the user input. This is done to guarantee stability and capture reality better.
   
   *A Surface-Subsurface Model; balancing speed, accuracy and reality. Stelling and Volp (to be published)*
 
