.. _threedigrid:

Threedigrid
===========

The Python package for low level access to the 3DI core administration file and result file.


Features
--------

The package provides the following features:

 - Access to threedicore administration HDF5 file by a single instance of the ``GridH5Admin`` object
 - Access to results NetCDF file via a single instance of the ``GridH5Resultadmin`` object
 - Query/filter the model data by pre-defined subsets and Django style filters
 - Export model data to GIS formats like shapefile, geopackage

Short example
-------------

Example of the result admin in an iPython shell::

    # Import the 3DI result admin 
    In [1]: from threedigrid.admin.gridresultadmin import GridH5ResultAdmin

    # Initalize the gridadmin with a threedicore administration HDF5 file
    # and a result NetCDF file.
    In [2]: ga = GridH5ResultAdmin('gridadmin.h5', 'results_3di.nc')

    # See if the model has groundwater
    In [3]: ga.has_groundwater
    Out[3]: False

    # View 3DI core administration information.
    # For example the line coordinates of the weir with node_id=37225
    In [4]: ga.lines.weirs.filter(id__eq=37225).line_coords
    Out[4]: array([[ 110278.3],
                   [ 517669.1],
                   [ 110276.3],
                   [ 517669.8]]) 

    # Get timeseries 
    # For example s1 for all 1D nodes from 0-40 seconds
    In [5]: ga.nodes.subset('1D_all').timeseries(start_time=0, end_time=40).s1
    Out[5]: array([[  0.00000000e+00,  -9.99900000e+03,  -9.99900000e+03, ..., 
                     -4.00000006e-01,  -4.00000006e-01,  -4.00000006e-01], 
                   [  0.00000000e+00,   5.00051076e+00,   5.00051076e+00, ..., 
                     -4.00000000e-01,  -4.00000000e-01,  -4.00000000e-01]])


Threedigrid Documentation
-------------------------

The full threedigrid documentation can be found via the following link: `Threedigrid documentation <https://threedigrid.readthedocs.io/en/latest/readme.html>`_.




