.. _sssdischarges:

Surface source and sink 
=============================

3Di does not cover all processes that can affect a water system. To allow users to add and extract water from the 2D surface domain, the Surface Sources and Sinks function is implemented. It allows users to define their own source and sink rates related to a certain process. An example would be to capture evaporation effects. These rates are treated similar to the other source and sink terms. 


Input
^^^^^^^^^^

The *Surface sources and sinks* is part of the scenario forcings, it forces the system to react to the input and it can differ per simulation. Therefor, the input is is not part of your schematisation, but is set in the API call. A more elaborate explanation about API calls and the specified input can be found :ref:`apicalculations` and on the site https://3di.lizard.net/api/v1/calculation/start/.

In this first release, one can only use the option to add a time-series containing uniform values. In the near future, options to add temporally and spatially variating raster values will be released. In addition to those option, also an option for interpolation of these rates will become available. The input rates are defined in *m/s*, and will automatically scaled with the grid size.

Output
^^^^^^^^^^

The actual surface source and sink discharges per computational cell are recorded in the 3di_results.nc file :ref:`3dinetcdf`. Especially, in case of extraction of water, the quantities can differ from the input values in case the cell becomes nearly empty. In addition to these results, one can also generate aggregated results :ref:`aggregationnetcdf`. The positive and negative cumulated results are required in case for using the water balance tool.

