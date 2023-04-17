.. _1d_objects:

1D Objects
==========

1D Boundary Condition
---------------------

Boundary condition for 1D connection nodes. Boundaries can only be placed on nodes connected to a single channel, culvert, orifice, weir, pipe, or pumpstation.

1D Lateral
----------

Lateral for 1D connection nodes

Channel
-------

Channel lines between connection nodes. All channels must have at least one cross_section_location.

..
    Not sure if this is still all true:
    Embedded channels
    ^^^^^^^^^^^^^^^^^

    Embedded channels are useful when you wish to add more detailed profiles to a course raster-file. Also, they are the most efficient way to add channels since they don't add to the number of computational points. In fact, the volume in the channel is integrated with that of the 2D computational cell. When modelling embedded channels, consider the following:

    * The water level in the embedded channel is always equal to the water level in the underlaying 2D grid cell.

    * Embedded channels add extra connections between 2D grid cells, but ignore obstacles and levees.

    * Make sure the embedded channel profile always partially lays below the surface level in you DEM (you can't have floating embedded channels).

    * Make sure no more than one channel vertice falls inside a single raster-file pixel.

    * Embedded channels only function when they connect several 2D grid cells, so make sure no embedded channel falls completely inside one 2D grid cell

    * All connection nodes connected to an embedded channel become embedded, so make sure structures or channels of other types that are connected to these connection node cross at least one 2D grid cell boundary, and

    * Do not place boundary conditions directly on embedded channels.


Connection node
---------------

Location and ID of nodes between channels, culverts, orifices, weirs, pipes, or pumpstations.

Cross-section location
----------------------

Location of cross-section for channels.

Culvert
-------

Culvert, a connection between connection nodes

Manhole
-------

Sewerage manhole

Pumpstation (without end node)
------------------------------

Pumpstation that pumps water out of the model domain

Pumpstation (with end node)
---------------------------

Pumpstation that transports water from one connection node to another

Orifice
-------

Structure that can be used to schematize e.g. spillways or bridges

Pipe
----

Sewer pipe

Weir
----

Open water weir or sewerage overflow structure