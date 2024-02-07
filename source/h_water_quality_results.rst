.. _wq_netcdf: 

Water quality results 3Di
=========================

The water quality results of a simulation are written to a `NetCDF <https://en.wikipedia.org/wiki/NetCDF>`_ file called *water_quality_results_3di.nc*, which follows the `CF Conventions <http://cfconventions.org/>`_ . The CF convention stipulates that the 2D and 1D mesh data are stored in separate parts of the file. The *water_quality_results_3di.nc* file contains snapshots of concentrations at nodes (1D and 2D). The output timestep, i.e. the interval at which these snapshot values are written to the NetCDF file, is set at the start of the simulation. 

Water quality results can be retrieved from the nodes in the 1D and 2D. The amount of variables in the netcdf depends on the amount of added substances in the model. An overview of the configuration of the variables is given below.

**Water quality Variables 2D**.

 Mesh2D_substance_1_2D: Concentration of substance 1 at the specified node.

  - Name: substance_1_2D
  - Unit: substance per m3

 Mesh2D_substance_2_2D: Concentration of substance 2 at the specified node.

  - Name: substance_2_2D
  - Unit: substance per m3

 Mesh2D_substance_*n*_2D: Concentration of substance *n* at the specified node.

  - Name: substance_*n*_2D
  - Unit: substance per m3


**Water quality Variables 1D**.

 Mesh2D_substance_1_2D: Concentration of substance 1 at the specified node.

  - Name: substance_1_1D
  - Unit: substance per m3

 Mesh2D_substance_2_2D: Concentration of substance 2 at the specified node.

  - Name: substance_1_1D
  - Unit: substance per m3

 Mesh2D_substance_*n*_2D: Concentration of substance *n* at the specified node.

  - Name: substance_*n*_1D
  - Unit: substance per m3
