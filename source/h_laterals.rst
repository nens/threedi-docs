.. _laterals:

Laterals
========

Laterals refer in 3Di to point sources and sinks. They can occur in the 1D and in the 2D surface domain. They are treated as any source and sink term, but laterals have a specific location and can vary in time. When one, for example, uses the *tap*-icon in 3Di Live, one adds a lateral.  When adding lateral to the 1D and/or the 2D domain, the time series can be added to the related tables in the spatialite database.

.. note::
   Negative laterals extract water from the model. If less water is available in the node or cell then what is to be extracted, 3Di will limit the extraction. Just before the cell becomes dry, the extraction discharge will be less than the extraction in the lateral time series. This is done to guarantee stability and capture reality better.
   
   *A Surface-Subsurface Model; balancing speed, accuracy and reality. Stelling and Volp (to be published)*