.. _outputs:

Outputs
=======

The outputs that are produced directly by 3Di are called *Raw results*. Which of these files are created, depends on the settings used. E.g., if the simulation does not include structure control, no structure_control_actions_3di.nc file will be created.

.. toctree::
   :maxdepth: 1

   h_gridadmin
   h_results
   h_aggregate_results
   h_structure_control_actions
   h_water_quality_results
   h_logging

.. note::
    
	The computional grid file (gridadmin.h5) is created from the schematisation by 3Di and is input for the 3Di computional core. As such it is not an output or result of the simulation, but is needed to open the other files.

