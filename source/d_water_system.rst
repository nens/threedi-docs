Water system
================

To model the water system of a polder you will need different types of structures and perhaps a larger level of detail than available in your 2D raster-files. For this purpose 3Di offers channels and structures that can be linked to the Quadtree. We refer to them as the 1D components. This tutorial shows you what steps you need to take to add these elements to an existing model.
The first thing you must do is activate 1D flow in the global settings. Also consider the following parameters in the global or numerical settings:

* advection_1d

* max_angle_1d_advection

* max_degree

* use_of_nested_newton

Channels
------------------------

To add a channel or network of channel consider the following steps:

#. First, load these tables from the spatialite database if you haven’t already:

    a. v2_channel (line geometry)

    #. v2_connection_nodes (point geometry)

    #. v2_cross_section_location (point geometry)

    #. v2_cross_section_definition (no geometry)

#. Channels are drawn in between connection nodes, so start by adding nodes on the start- and endpoints of your channels. If you wish to add structures later on, make sure to add enough nodes as they are also linked between connection nodes (and thus not placed on top of channels).

#. After saving your edits in QGIS the connection node’s id’s are filled automatically. You can fill out the other attributes of the connection nodes later on.

#. Now draw your channels from connection node to connection node. Make sure you snap the start- and endpoints to the connection nodes and fill out the connection_node_start_id and connection_node_end_id for every channel feature. Then fill all the attribute fields for all channels except id and save.

#. Every channels needs at least one cross section. Start by adding one or multiple cross section definitions in the table v2_cross_section_definition. You have several option to define you profile, check the :ref:`database-overview` for more details. One definition can be used on multiple locations. When you’re done, save. Note that the v2_cross_section_definition id’s are filled.

#. You can place cross sections on channels using the v2_cross_section_location. You may place multiple cross sections on one channel. When placing locations, consider the following:

    a. Cross section locations must be placed on a channel vertex. If you have no vertex available on you channel, add one.

    #. Cross section locations may not be placed on the start- on endpoint of a channel

    #. When placing multiple cross section locations on one channel consider your calculation distance. Make sure you have sufficient calculation points on your channel.

    #. Refer to the correct channel id in the attribute field channel_id.

    #. Refer to the correct definition in the attribute field definition_id

    #. If your channel is of type connected or double connected, make sure to fill out the bank_level. This is the threshold between the water in the channel and that on the 2D surface.

After these steps your channel is complete. If you whish you can fill out the initial water level on the connection nodes. The water level is interpolated between nodes across channel calculation points. If you would like to use an embedded channel, you will find some more requirements below.

Structures
------------------------

Structures in 3Di are always a connection between two connection nodes. 3Di supports four types of structures:

#. Pumpstation

#. Weir

#. Orifice

#. Culvert

Check out het :ref:`database-overview` for how use the structure attributes. Below, some specific details are listed.

* The shape of the weir, orifice and culvert are stored in the cross section definition table. So make sure you have some available before you start adding these structures.

* Culverts are the only structure type that has a geometry, it is a line. This means it can be f.i. curved. The culvert length is derived from it's geometry. All other structures are defined only as a link between nodes. They have no length. 

* To add a structure,  make sure you have two connection nodes available at the end of two channels. Fill in the correct start and end connection node id in the sqlite tables. You must work in the v2_structure table, editing in views is not supported.

* The pumpstation  pumps from the start node to the end node. You can choose how it is controlled using the *type* attribute. 

* If you wish to model several structures that are only connected to each other, for instance a culvert followed by a culvert. You must add storage area to the connection node. Normally the storage area is derived from the cross section of the adjoining channel, but when there is no channel connected to a connection node, by default is has no storage. So add it manually, or your model won't work. 

* You can not place boundary conditions directly on structures.

* Finally, you must make sure that one of the cross section's reference levels near the structure is below the start, crest or invert level of the adjoining structure. 


1D boundary condition
------------------------

Boundary conditions for the 1D system are placed on connection nodes. They can only be placed on connection nodes that are connected to a single isolated channel or pipe. So not on structures or embedded or connected channels. Check the different types of boundary conditions available in the :ref:`database-overview`.

The timeseries field in the spatialite database can only be filled by pasting your timeseries into the spaitialite as QGIS does not allow you to enter a newline. U may use this example::
    
    0,0.000000
    15,1.000000
    30,2.000000
    45,3.000000
    60,2.000000
    99999,2.000000

    
Embedded channels
------------------------

Embedded channels are usefull when you wish to add more detailed profiles to a course raster-file. Also, they are the most efficient way to add channels since they don't add to the numer of calculation points. In fact, the volume in the channel is integrated with that of the 2D calculation grid cell. When modelling embedded channels, consider the following:

* The water level in the embedded channel is always equal to the water level in the underlaying 2D grid cell,

* Embedded channels add extra connections between 2D grid cells that ignore levee's,

* Make sure the embedded channel profile always partially lays below the surface level in you DEM (you can't have floating embedded channels),

* Make sure no more than one channel vertice falls inside a singel raster-file pixel,

* Embedded channels only function when they connect several 2D grid cells, so make sure no embedded channel falls completely inside one 2D grid cell,

* All connection nodes connected to an embedded channel become embedded, so make sure structures or channels of other types that are connected to these connection node cross at leat one 2D grid cell boundary, and

* Do not place boundary conditions directly on embedded channels.
