.. _3dinetcdf:

Results 3Di
===========

The results of a simulation are written to a `NetCDF <https://en.wikipedia.org/wiki/NetCDF>`_ file called `results_3di.nc`, which follows the `CF Conventions <http://cfconventions.org/>`_ . The CF convention stipulates that the 2D and 1D mesh data are stored in separate parts of the file. The results_3di.nc file contains snapshots of values of all relevant flow variables (1D and 2D). The output timestep, i.e. the interval at which these snapshot values are written to the NetCDF file, is set at the start of the simulation.

The file size is determined by the output time step, the size of the model (number of nodes and flowlines), and the duration of the simulation.

In addition to these snap shots, 3Di can generate aggregated results. More about this can be found in :ref:`aggregationnetcdf`. More about the results of the water quality can be found :ref:`wq_netcdf`


Flow results are split between node and line variables. Node variables include volumes, water levels and all the source and sink terms. Flowline variables include velocities, discharges and wet cross-section areas. A full overview is given below.

2D Mesh Cell/Node variables
---------------------------

First the meta information of the computational grid is defined.

**Coordinates**

  Mesh2DFace_xcc: x-coordinate of the center of the computational cell

  - Name: Flow Face 2D center x coordinate
  - Unit: [m]

  Mesh2DFace_ycc: y-coordinate of the center of the computational cell

  - Name: Flow Face 2D center y coordinate
  - Unit: [m]

  Mesh2DFace_zcc: The deepest point in either the surface water cell or the groundwater cell

  - Name: Flow Face 2D center z coordinate
  - Unit: [m MSL]

  Mesh2DContour_x: x-coordinates of the location of the edge of the cell

  - Name: List of x-coordinates forming Face
  - Unit: m

  Mesh2DContour_y: y-coordinates of the location of the edge of the cell

  - Name: List of y-coordinates forming Face
  - Unit: m


**Attributes** Some administrative information


  Mesh2DNode_id:  IDfrom the computational core

  - Name: Node Identifier

  Mesh2DFace_sumax: Maximum surface area in a computational cell

  - Name: Total cell surface
  - Unit: m2

  Mesh2DNode_type: Type of 2D computational cell

  - Name: Type of 2D mesh node/face
  - Types: surface_water_2d, grounwater_2d, groundwater_2d, open_water_boundary_2d, groundwater_boundary_2d

**Dimensions** Length of the arrays

  nMesh2D_nodes:

  - Name: Number of 2D mesh nodes/faces.


**Flow Variables** These are the variable that are defined in the cell centers.

 Mesh2D_s1: Water level, depending on the node type, it is the surface or the groundwater level.

  - Name: waterlevel
  - Unit: m MSL

  Mesh2D_vol: water volume in a cell

  - Name: Water volume
  - Unit: m3

  Mesh2D_su: current wet surface area

  - Name: Wet surface area
  - Unit: m2

  Mesh2D_ucx: Interpolated flow velocity in the cell center in x-direction

  - Name: Flow velocity in x direction in cell center
  - Unit: m/s


  Mesh2D_ucy: Interpolated flow velocity in the cell center in y-direction

  - Name: Flow velocity in y direction in cell center
  - Unit: m/s


  Mesh2D_rain: Current amount of rain in computational cell

  - Name: Rain
  - Unit: m3/s

  Mesh2D_q_lat: Point discharge in computational cell

  - Name: Lateral discharge
  - Unit: m3/s

  Mesh2D_infiltration_rate_simple: Current amount of infiltration in computational cell

  - Name: Infiltration rate
  - Unit: m3/s

Mesh2D_leak: Current amount of leakage in computational cell.

  - Name: Leakage rate
  - Unit: m3/s

Mesh2D_intercepted_volume: Amount of intercepted volume

    - Name: intercepted_volume
    - Unit: m3

Mesh2D_q_sss: Current amount of surface sources and sinks discharge in computational cell.

  - Name: Surface sources and sinks discharge
  - Unit: m3/s

2D Mesh Line variables
----------------------

The meta information, that defines the structure for the line variables, is mentioned first.

**Coordinates**

  Mesh2DLine_xcc:

  - Name: Flow line 2D center x coordinate.
  - Unit = m

  Mesh2DLine_ycc:

  - Name: Flow line 2D center y coordinate.
  - Unit = m

  Mesh2DLine_zcc:

  - Flow line 2D center z coordinate.
  - Unit = m

**Attributes**


  Mesh2DLine_type:

  - Name: Type of Cell edge
  - Types: open_water_2d, open_water_obstacles_2d, vertical_infiltration_2d, groundwater_2d, open_water_boundary_2d, groundwater_boundary_2d

**Dimensions**

  nMesh2D_lines:

  - Name: Number of 2D Mesh lines.

**Flow variables**


  Mesh2D_u1:
  This variable, in case of Horton-based infiltration and groundwater flow, also consists of the vertical flow and the groundwater flow. This depends on the Line Type. This also yields for most of the other line variables.

  - Name: Flow velocity on 2D flow line
  - Unit: m/s

  Mesh2D_q:

  - Name: Discharge on flow line
  - Unit: m3/s

  Mesh2D_au:

  - Name: Wet cross-sectional area
  - Unit: m2

  Mesh2D_up1:

  - Name: Flow velocity in interflow layer
  - Unit: m/s


  Mesh2D_qp:

  - Name: Discharge in interflow layer
  - Unit: m3/s

1D Mesh Node variables
----------------------

The results for the 1D variables are structured in a similar way. Note that embedded nodes do not have a 1D water level, volume etc information. This information can be found in the 2D results.

**Coordinates**

  Mesh1DNode_xcc:

  - Name: Node 1D x coordinate
  - Unit: m

  Mesh1DNode_ycc:

  - Name: Node 1D y coordinate
  - Unit: m

  Mesh1DNode_zcc:

  - Name: Node 1D z coordinate
  - Unit: m MSL

**Attributes**

  Mesh1DNode_id:

  - Name: Node Identifier

  Mesh1DNode_sumax:

  - Name: Total cell surface
  - Unit: m2

  Mesh1DNode_type:

  - Types = node_without_storage_1d, open_water_with_storage_1d, open_water_boundary_1d

**Dimensions**

  nMesh1D_nodes:

  - Name: Number of 1D mesh nodes


**Node variables**

  Mesh1D_s1: Waterlevel in 1D Node

  - Name: Waterlevel
  - Unit: m MSL

  Mesh1D_vol: Water Volume in a cell

  - Name: Water volume
  - Unit: m3

  Mesh1D_su: Current wet surface area

  - Name: Wet surface of 1D Node
  - Unit: m2

  Mesh1D_rain:  Inflow in 1D from rain or dry wetter discharge

  - Name: Inflow in 1D from rain
  - Unit = m3/s

  Mesh1D_q_lat: Point source/sink flux in 1D cell

  - Name: Lateral discharge in/from 1D cell
  - Unit = m3/s

1D Mesh Line variables
----------------------

**Coordinates**

  Mesh1DLine_xcc:

  - Name: Flow line 1D x center coordinate
  - Unit: m

  Mesh1DLine_ycc:

  - Name: Flow line 1D center y coordinate
  - Unit: m

  Mesh1DLine_zcc:

  - Name: Flow line 1D z center coordinate
  - Unit = m MSL

**Attributes**

  Mesh1DLine_id:

  - Name: Line identifier

  Mesh1DLine_type:

  - Types: embedded_1d, isolated_1d, connected_1d, long_crested_structure_1d, short_crested_structure_1d, double_connected_1d, from_node_with_storage_1d2d, from_node_without_storage_1d2d, potential_breach_1d2d, groundwater_1d2d, boundary_1d

**Dimensions**

nMesh1D_lines:

  - Name: Number of 1D Mesh lines

**Flow variables**

  Mesh1D_u1:Flow velocity on 1D flow line, including 1D2D connections.

  - Name: Flow velocity on 1D flow line
  - Unit: m/s

  Mesh1D_q:

  - Name: Discharge on 1D flow line
  - Unit: m3/s

  Mesh1D_au:

  - Name: Wet cross-sectional area
  - Unit: m

  Mesh1D_breach_depth:

  - Name: Breach depth on 1D2D connection
  - Unit: m

  Mesh1D_breach_width:

  - Name: Breach width on 1D2D connection
  - Unit: m

Pump variables
--------------

**Coordinates**

  Mesh1DPump_xcc:

  - Name: Start point Pump 1D x-coordinate
  - Unit: m

  Mesh1DPump_ycc:

  - Name: Start point Pump 1D y-coordinate
  - Unit: m

**Attributes**

  Mesh1DPump_id:

  - Name: Pump identifier

**Dimensions**

  nPumps:

  - Name: Number of 1D pumps

**Flow variables**

  Mesh1D_q_pump:

  - Name: Pump discharge
  - Unit: m3/s

