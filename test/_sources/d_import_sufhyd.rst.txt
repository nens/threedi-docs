.. _import_sufhyd:

Import from SUF-HYD
^^^^^^^^^^^^^^^^^^^

SUF-HYD is a Dutch standardised format for transferring data of sewerage systems for hydraulic analyses. This tool allows an automated import of the sewerage data in the 3Di model database. 

Before you can use the tool, make sure you have :ref:`downloaded an empty spatialite <empty_database>`. The SUF-HYD data will be imported to this spatialite. Save the Sqlite to a location fo choice on your computer.

The tool can be accessed by :ref:`activating the toolbox <3ditoolbox>` and double clicking 'import_sufhyd.py' under 'Step 2 - Convert and import data' 

1) First, make sure you have a connection with the sqlite you want to import your data to (see the first 3 steps under :ref:`rasterchecker`). 
2) After opening the tool, select a SUF-HYD file and the database (sqlite) to import the data into and click 'OK'

The data from the SUF-HYD will be loaded into the sqlite. A log file of this process can be found at the same location as the SUF-HYD file. This file has the name of your SUF-HYD with a *.hyd.log* extension. You can open this log file with a text editor such as Notepad. This log-file gives a summary of data errors and warnings. 

The following objects are imported:

* Manhole (``*KNP``)
    * The number of inhabitants will be added as an *Impervious surface*.

Note: the shape of the manhole is referred as 'rnd' = round, 'sqr' = square and 'rect' = rectangle

*    Pipe (``*LEI``)

    *    The number of inhabitants will be added as *Impervious surface*
	
*    Pump station (``*GEM``)

    *    If multiple stages are defined, this will be transformed into seperate pumpstations. Up to 10 stages are supported
	
*    Weir (``*OVS``)

    *    Flow direction (str_rch) is translated into discharge coefficients with a value of 0
    *    An end node with boundary condition is not automatically added.
	
*    Orifice (``*DRL``)

    *    Flow direction (str_rch) is translated into discharge coefficients with a value of 0
	
*    Boundary (``*UIT``)

    *    The water level will be the average definition (bws_gem). If not present the summer water level is used and otherwise the winter water level.
	
*    Extra manhole storage (``*BOP``)

    *    The defined storage area is added to a manhole on the bottomlevel of the manhole. The defined bottom_level of the storage (niv_001) is ignored.
    *    Only one storage area is supported
	
*    *Drainage area/ Impervious surface* (``*AFV``)


*    Linkage nodes (``*KPG``)

    *    The 'fictive' linkages (with typ_gkn == 01) are ignored, only real nodes are combined.
    *    The second node (ide_kn2) is removed. Impervious surfaces and pipes linked to the removed node are redirected to the first node. Extra manhole storage will be lost.
