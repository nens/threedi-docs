.. _laterals:

Laterals and dry weather flow
=============================

Laterals are point sources and sinks. Each time step, the volume as specified in the supplied time series is added to the volume of the node or cell they are added to. Laterals can be applied in the 1D and in the 2D surface domain. They are treated as any source and sink term, but laterals have a specific location and can vary in time. 

A specific type of laterals is dry weather flow (DWF). DWF is a 1D lateral with one discharge value each of hour of the day. They are used to simulate the wastewater produced by households or industry, which usually follows a pattern that varies troughout the day.

1D laterals, 2D laterals, and dry weather flow can be defined in the schematisation, so that they will be part of the simulation template that is created along with the 3Di model for that schematisation; see :ref:`2d_lateral`, :ref:`1d_lateral`, and, for :ref:`inflow_objects`.

It is also possible to add laterals and DWF to a simulation if they are not already included in the simulation template; to do this from the 3Di Modeller Interface, see :ref:`simulate_api_qgis_laterals` and :ref:`dry_weather_flow`. 

.. note::
   Negative laterals extract water from the model. If less water is available in the node or cell then what is to be extracted, 3Di will limit the extraction. Just before the cell becomes dry, the extraction discharge will be less than the extraction in the lateral time series. This is done to guarantee stability and capture reality better.
   
   *A Surface-Subsurface Model; balancing speed, accuracy and reality. Stelling and Volp (to be published)*