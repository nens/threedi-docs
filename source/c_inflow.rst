.. _inflow:

Inflow
============

Rainfall-runoff can be schematized using surfaces. The runoff from these surfaces that flows into the 1D network is called '0D inflow' in 3Di. 0D inflow can be combined with rainfall-runoff in the 2D domain (0D-1D-2D model) or be used with 1D only (0D-1D model). It is also possible to use 0D inflow without having a 1D network, by connecting the inflow to an embedded node (0D-2D model).

The amount of runoff that results from the rainfall on each surface is calculated by the 0D inflow module. There are two different 0D inflow modules. One uses 'surfaces', the other one 'impervious surfaces'.


Schematisation
--------------
- In the v2_global_settings table, the parameter use_0d_inflow must be set to 1 (for 'impervious surface' 0D inflow) or 2 (for using 'surface' 0D inflow). If you do not want to use 0D inflow, set it to 0.
- Add polygon features to either the v2_surface or v2_impervious_surface tables (depending on the setting you have chosen in the global settings). The feature's attributes describe the rainfall-runoff process for the surface. These parameters are explained in more detail below.
- Add entries to the v2_surface_map or v2_impervious_surface_map. Each row in this table contains the id of the surface (e.g. 23), the id of the connection node (e.g. 542) it and a percentage (e.g. 100). This means that 100% of the runoff produced by surface 23 is added to the volume at connection node 542.
- Runoff from a (impervious) surface can be distributed over multiple connection nodes. For example, the runoff from surface 23 can be distributed over connection nodes 542 and 543 by creating two mappings from surface 23, one to each connection node, each with a percentage of 50.


0D inflow using surfaces
--------

To offer more flexibility it is also possible to define your own set of parameters that characterize the inflow of a surface. This can be achieved by using surface parameters. In this case the surface can be modelled by a v2_surface instance that then is linked to connection nodes just the same way as described above but with its own mapping table called v2_surface_map.

The parametrisation of your specific surface-type can be set in the v2_surface_parameters table. For an overview of the available parameters check out the :ref:`database-overview`.


0D inflow using impervious surface
------------------

A surface often is an urban construction like the roof of a building with its typical characteristics. For this use case 3Di has a set of pre-defined impervious surfaces (from the dutch NWRW-inloop model). The surface itself is modelled by a v2_impervious_surface instance that can be linked to connection nodes by v2_impervious_surface_map instances where the percentage attribute controls the inflow distribution. 

The figure below shows an overview of the parameters available.

.. figure:: image/surface_runoff_parameters.png
   :alt: Surface Runoff parameters

   Overview of surface run-off parameters

The parametrisation for the impervious surface types is fixed. It uses the following parameters:
    
.. list-table:: Parameters Impervious Surface
   :widths: 50 30 30 30 30 30 30 30
   :header-rows: 1

   * - Surface description
     - outflow_delay (/min)
     - surface_storage (mm)
     - infiltration boolean
     - Max infiltration capacity (mm/h)
     - Min infiltration capacity (mm/h)
     - Time factor reduction of infiltration capacity (/h)
     - Time factor recovery of infiltration capacity (/h)
   * - gesloten verharding, hellend
     - 0.5
     - 0.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - gesloten verharding, vlak
     - 0.2
     - 0.5
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - gesloten verharding, vlak uitgestrekt
     - 0.1
     - 1.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - open verharding, hellend
     - 0.5
     - 0.0
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * - open verharding, vlak
     - 0.2
     - 0.5
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * - open verharding, vlak uitgestrekt
     - 0.1
     - 1.0
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * - dak, hellend
     - 0.5
     - 0.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - dak, vlak
     - 0.2
     - 2.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - dak, vlak uitgestrekt
     - 0.1
     - 4.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - onverhard, hellend
     - 0.5
     - 2.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1
   * - onverhard, vlak
     - 0.2
     - 4.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1
   * - onverhard, vlak uitgestrekt
     - 0.1
     - 6.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1


