.. _scenario_archive:

Scenario Archive
================

.. note::
    This option is only available if your subscription includes the Scenario Archive.

The Scenario Archive (Lizard) is used to store and view scenarios.

You can access the Scenario Archive here: https://demo.lizard.net/. For instructions on how to use the Scenario Archive, see the `Lizard documentation <http://docs.lizard.net>`_, for example, the sections about finding scenarios in the `Catalog <https://docs.lizard.net/e_catalog.html#scenarios>`_, and the section about the `Viewer <https://docs.lizard.net/e_viewer.html>`_. 

Scenario's that are stored in the Scenario Archive can also be accessed in the 3Di Modeller Interface, using the `Lizard plugin <https://docs.lizard.net/d_qgisplugin.html>`

A 3Di scenario consists of one or more of the following components:

- :ref:`Raw results<outputs>`
- :ref:`basic_processed_results`
- :ref:`arrival_time`
- :ref:`damage_estimation`

.. _basic_processed_results:

Basic processed results
-----------------------

Basic processed results are:

Water level (timeseries)
^^^^^^^^^^^^^^^^^^^^^^^^

Water level (m MSL) relative to datum (usually mean sea level, MSL), for each output timestep. The water level data per computional cell is spatially interpolated to the pixel resolution. 

Max water level
^^^^^^^^^^^^^^^

Maximum water level (m MSL) relative to datum (usually mean sea level, MSL). The maximum water level data per computional cell is spatially interpolated to the pixel resolution. 

Water depth (timeseries)
^^^^^^^^^^^^^^^^^^^^^^^^
Water depth (m) relative to surface level (water level minus surface level), for each output timestep. Surface level is defined by the DEM used by the model. The water level data per computional cell is spatially interpolated to the pixel resolution. 

Max water depth
^^^^^^^^^^^^^^^

Maximum water depth (m) relative to surface level (maximum water level minus surface level). Surface level is defined by the DEM used by the model. The maximum water level data per computional cell is spatially interpolated to the pixel resolution.

Flood hazard rating
^^^^^^^^^^^^^^^^^^^

Rating used to indicate the degree of danger caused by flooding. 
The flood hazard rating is calculated as follows: 

HR = d * (v + 0.5) + DF

| Where:
| HR = (flood) Hazard Rating
| d = depth of flooding (m)
| v = flow velocity (m/s)
| DF = debris factor 

When water depth is smaller than or equal to 0.25 than DF = 0.5, else DF = 1. 

Rain
^^^^

Rain intensity per calculation cell (mm/h).

Rate of rise
^^^^^^^^^^^^ 

Rate of rise (m/s), defined as how fast the water depth rises from 0 to 1.5 m.

.. math::
   :label: rate_of_rise

   R = \frac{\delta \zeta}{\delta t}

In which: 

| :math:`\delta \zeta` difference in water depth, fixed to 1.5 - 0
| :math:`\delta t` time between the cell getting wet (volume > 0) and reaching a water depth of 1.5 m. The water depth is defined as (water level - lowest DEM pixel in the cell)

Cells that already have a water depth of 1.5 m at the start of the simulation are ignored.

.. note::
    
	This raster is calculated from the :ref:`3dinetcdf`. The temporal resolution (output time step) of this file determines the precision of :math:`\delta t`.


Max flow velocity
^^^^^^^^^^^^^^^^^

Maximum flow velocity per calculation cell (m/s). The flow velocity in the calculation cell is the resultant of the flow velocity x (``ucx``) and y (``ucy``) at the cell center. Can be used for flood damage estimations, for example. 


.. _arrival_time:

Arrival time
------------

.. todo::

    Hier een stukje over schrijven	
	

.. _damage_estimation:

Damage estimation (NL only)
---------------------------

Depending on your location Lizard provides estimates of damage caused by inundation or flooding. To use the damage estimation your study or model area must be within the Netherlands. 

The damages are estimated based on the land-use type, depth of the inundation, year of the month and repair time and are closely linked to the dutch waterschadeschatter.nl. The damage can be used by selecting the 'damage estimation' option and providing the parameters. The land-use map can be viewed in lizard and is fixed. The water depth is derived using the maximum water level and the most recent AHN elevation. The damage estimation does not use the DEM provided in the model.


.. figure:: image/d_store_results.png
   :alt: Store results
   
.. figure:: image/d_store_results2.png
   :alt: Store results 2

The estimated damages are available on a 0.5 m x 0.5 m resolution. Direct, indirect and total damages are available in separate raster layers. In addition, a CSV formatted file with total damages can be downloaded from Lizard.

Further documentation (only in Dutch) can be downloaded from :download:`here <pdf/nabewerking-3di-resultaten-in-lizard.pdf>`. The used damage table are available in :download:`Excel <other/3di-v2.2018-05-15.xlsx>` and :download:`CFG <other/3di-v2.2018-05-15.cfg>` (for use on `waterschadeschatter.nl <https://www.waterschadeschatter.nl>`_. The damage estimation in Lizard was developed together with Hoogheemraadschap Hollands Noorderkwartier.

