Sewerage
============

To model the sewerage system you will need different types of structures. A sewerage model can be purely the sewerage system itself (1D), or it can interact with the surface (1D/2D). This tutorial shows you what steps you need to take to add these elements to an existing model. The first thing you must do is activate 1D flow in the global settings. Also consider the following parameters in the global or numerical settings:

* manhole_storage_area

* advection_1d

* max_angle_1d_advection

* max_degree

* use_of_nested_newton


Manholes
------------------------
Manholes define the locations where the 1D sewerage system can interact with the surface. Each manhole must have a volume and refer to a connection node.

To add a manhole consider the following steps:

#. First, load these tables from the spatialite database if you haven’t already:

    a. v2_connection_nodes (point geometry)
	
#. Each manhole needs to be linked to a connection node, which determines its geographical location.

#. Furthermore, each manhole must have dimensions. You have several option to define these dimensions, check the :ref:`database-overview` for more details. Note that manholes do not refer to the cross section definition table (as do the structures). The drain_level details the elevation at which the manhole can interact with the 2D-rasters and water can flow in our out of the manhole. This is only used in case of connected manholes.
	
#. The manholes must have manhole_indicators (what kind of manhole it is) and calculation_type. The calculation_type defines whether, and how, the water can flow in or out of the manhole.

#. In case of a purely 1D sewerage model, the manhole storage area has to be defined in the global settings. This determines the size of the 'cylinder' that is used as a substitute to determine the volume at street level when the water rises above the drain_level in case of connection manholes.


Structures
------------------------
Sewerage structures in 3Di are always a connection between two connection nodes, without their own geometry. 3Di supports four types of structures in sewerage systems:

#. Pipe

#. Weir

#. Orifice

#. Pumpstation

Check out het :ref:`database-overview` for how use the structure attributes. Below, some specific details are listed.

* The shape of the pipe, weir and orifice is stored in the cross section definition table. So make sure you have some available before you start adding these structures.

* To add a structure you have to define the correct start and end connection node id in the sqlite tables. You must work in the v2_structure table, editing in views is not supported.

* The pumpstation pumps from the start node to the end node. You can choose how it is controlled using the *type* attribute. It is possible to leave the end node blank ('NULL'). In that case the pumpstation pumps water 'out of the model' and functions as a boundary condition. This could, for example, simulate the final pumpstation that pumps the water to the sewage treatment plant.


Impervious surfaces
------------------------
It is also possible to use a pure 1D-sewerage model without any 2D component. If that is the case make sure you activate "use_0d_inflow" in the global settings. 
In this case you force the '0d-surfaces' into the sewerage system. This is done by linking the '0d-surfaces' (v2_impervious_surface) to a connection node (using v2_impervious_surface_map), check the :ref:`database-overview` for more details.


