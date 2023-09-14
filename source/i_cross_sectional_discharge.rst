.. _cross_sectional_discharge:

Cross-sectional discharge tool
------------------------------

The cross-sectional discharge tool is one of the :ref:`3di_processing_toolbox`. Access the tool via *Main menu* > *Processing* > *Toolbox* > *3Di* > *Post-process results* > *Cross-sectional discharge*

The tool calculates total net discharge that passes a given line. The result will be written to a field specified by *output field name*. This field will be created if it does not exist.

The sign (positive/negative) of the output values depends on the drawing direction of the cross-section line. Positive values indicate flow from the left-hand side of the cross-section line to the right-hand side. Negative values indicate flow from right to left.

Parameters
^^^^^^^^^^

Gridadmin file
""""""""""""""

HDF5 file (\*.h5) containing the computational grid of a 3Di model

Results 3Di file
""""""""""""""""

NetCDF (\*.nc) containing the results of a 3Di simulation

Cross-section lines
"""""""""""""""""""

Lines for which to calculate the total net discharge passing that line

Start time
""""""""""

If specified, all data before start time will be excluded. Units: seconds since start of simulation.

End time
""""""""

If specified, all data after end time will be excluded. Units: seconds since start of simulation.

Subset
""""""

Limit the analysis to flowlines in a specific flow domain.

1D Flowline types to include
""""""""""""""""""""""""""""

Further filtering of specific 1D flowlines. This setting does not affect 2D or 1D/2D flowlines.

Output field name
"""""""""""""""""

Name of the field in the cross-section lines layer to which total net discharge will be written.

Outputs
^^^^^^^

Total net discharge per cross-section line
""""""""""""""""""""""""""""""""""""""""""

This result will be written to the cross-section lines layer, in a field specified by output field name. This field will be created if it does not exist.

Intersected flowlines
"""""""""""""""""""""

Flowlines that are included in the analysis. The styling will indicate if there is positive (left-hand side to right-hand side of the cross-section line) or negative net flow through each of these flowlines.

Time series
"""""""""""

Table (CSV file) with time series of net flow over each cross-section line. 

.. note::
   
   Tip: use the DataPlotly QGIS plugin to visualize these time series.
