Sewerage
============

To model the sewerage system you will need different types of structures and perhaps a larger level of detail than available in your 2D raster-files. The manholes form the base of your sewerage model, because this is where the 1D-sewerage flow can interact with the 2D-surface flow. This tutorial shows you what steps you need to take to add these elements to an existing model. The first thing you must do is activate 1D flow in the global settings. Also consider the following parameters in the global or numerical settings:

* advection_1d

* max_angle_1d_advection

* max_degree

* use_of_nested_newton


Manholes
------------------------
Manholes define the locations where the 1D sewerage system can interact with the surface. Each manhole must have a volume and refer to a connection node, which determines the geographical location.

To add a manhole consider the following steps:

#. First, load these tables from the spatialite database if you haven’t already:

    a. v2_connection_nodes (point geometry)
	


Pipes
------------------------



Pumpstations
------------------------



Weirs
------------------------



Orifices
------------------------



Manholes
------------------------

