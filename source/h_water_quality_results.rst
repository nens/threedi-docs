.. _wq_netcdf: 

Water quality results 3Di
=================

The results of a simulation are written to a `NetCDF <https://en.wikipedia.org/wiki/NetCDF>`_ file called `results_3di.nc`, which follows the `CF Conventions <http://cfconventions.org/>`_ . The CF convention stipulates that the 2D and 1D mesh data are stored in separate parts of the file. The results_3di.nc file contains snapshots of values of all relevant flow variables (1D and 2D). The output timestep, i.e. the interval at which these snapshot values are written to the NetCDF file, is set at the start of the simulation.

The file size is determined by the output time step, the size of the model (number of nodes and flowlines), and the duration of the simulation.

In addition to these snap shots, 3Di can generate aggregated results. More about this can be found in :ref:`aggregationnetcdf`.