.. _3dinetcdf:

Results 3Di
=================

The results of a simulation are written to file. The result file is created using NetCDF, which is a set of software libraries and self-describing, machine-independent data formats that support the creation, access, and sharing of array-oriented scientific data. The set of libraries can be used by multiple tools and programming languages, such as matlab, python and excel, to extract the data from the netcdf data formats.

The 3Di Plugin visualizes the information stored in this file. An overview of the data format in the output file is given in this chapter, to help users in reading data from file. To facilitate users in the direct access to the results from the output file, users can make use of the python package *threedigrid*. Which can be downloaded from `https://pypi.org/project/threedigrid <https://pypi.org/project/threedigrid/>`_. This package helps to link the output data to the input data.

During the spring release of 2018 the output file has been changed. The changes include a change in name from *subgrid_map.nc* to *results_3di.nc* and changes to the data format within the output file. An overview of both data formats is presented below.

These files consist of all relevant variables that are necessary to analyze the results of a simulation. The user defines the output time step. The snapshots of the flow are saved at these intervals. Note, that the output time step in combination with the size of the model will define the size of the output file. In addition to these snap shots, 3Di can generate aggregated results. More about this can be found in  :ref:`aggregationnetcdf`.


Data format *results_3di.nc*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The current output NetCDF file consists of all flow variables of the 1D and the 2D mesh. The results file is constructed according to the `CF Conventions <http://cfconventions.org/>`_ . In this data format, the 2D and 1D mesh are split, so each part of the mesh has its own result and mesh variable. A description of all the flow and mesh variables for the 1D and 2D mesh are given below.

For the results in the 1D and in the 2D domain, results are split between node and line variable. Node variables are typically, variables related to volumes. This concens volumes, water levels and all the source and sink terms. Line variables are related to flow variables, in other words velocities and discharges. This distiction is also clear in the 3Di Plugin and in the contsruction of the result files.

2D Mesh Cell/Node variables:
----------------------------

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

**Dimensions** Lenght of the arrays

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

2D Mesh Line variables:
-----------------------

The meta information, that defines the structure for the line variables is mentioned first.

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

1D Mesh Node variables:
-----------------------

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

1D Mesh Line variables:
-----------------------

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

Pump variables:
---------------

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

Data format *subgrid_map.nc*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the file called: subgrid_map.nc exists the following information:

Information of the grid
________________________

-	X-coordinates of the 2D computational cell corner points (FlowElemContour_x)

		- size[4,n2dtot]

		- dimension [m]

-	Y-coordinates of the 2D computational cell corner points (FlowElemContour_y)

		-	size [4,n2dtot]

		-	dimension [m]

-	X-coordinates 1D en 2D computational cell center point (FlowElem_xcc)

		-	size [number of computational nodes]

		-	dimension [m]

-	y-coordinates 1D en 2D computational cell center point (FlowElem_ycc)

		-	size [number of computational nodes]

		-	dimension [m]

-	Maximum surface area computational cell (sumax)

		-	size [number of computational nodes]

		-	dimension [m2]

-	Connections between computational points in 1D network (FlowLine_connections)

		-	size [2,number of flow lines]

		-	dimension [-]

-	Connections by a pump (PumpLine_connections)

		-	size [2,number of pumps]

		-	dimension [-]

-	(projected_coordinate_system (projected_coordinate_system)

		-	size [1]

		-	dimension [-]

-	Deepest point of a computational cell (bath)

		-	size [number of computational nodes]

		-	dimension [m MSL]

-	Potential breaches

		-	size [number of potential breaches]

		-	dimension [-]


Mapping administration:
__________________________

-	Mapping of input and out put of connection nodes (node_mapping)

		-	size [2,number of connection nodes]

		-	dimension [-]

-	Mapping of input and out put of connection lines (channel_mapping)

		-	size [2,number of flow lines]

		-	dimension [-]

Variables computed per computational cell:
_____________________________________________

-	Time (time)

		-	size [number of time steps]

		-	dimension [s]

-	Water level (s1)

		-	size [number of computational nodes]

		-	dimension [m MSL]

-	Volume in a computational cell (vol)

		-	size [number of computational nodes]

		-	dimension [m3]

-	Wet surface areas computational cell (su)

		-	size [number of computational nodes]

		-	dimension [m2]

-	Velocity interpolated in cell centre in x-direction (ucx)

		-	size [number of computational nodes]

		-	dimension [m/s]

-	Velocity interpolated in cell centre in y-direction (ucy)

		-	size [number of computational nodes]

		-	dimension [m/s]

-	Rain per computational cell (rain)

		-	size [number of computational nodes]

		-	dimension [m3/s]

-	Lateralen per computational cell (qlat)

		-	size [number of computational nodes]

		-	dimension [m3/s]

-	Infiltration per computational cell (infiltration)

		-	size [n2dtot]

		-	dimension [m3/s]

Variable per line:
_____________________

-	Velocity (u1)

	-	size [number of flow lines]

	-	dimension [m/s]

-	Discharge (q)

	-	size [number of flow lines]

	-	dimension [m3/s]

-	Wet Cross-Sectional area (au)

	-	size [number of flow lines]

	-	dimension [m2]

- Velocity in interflow layer (up1) (if defined)

	-	size [number of flow lines]

	-	dimension [m/s]

- Discharge in interflow layer (qp) (if defined)

	-	size [number of flow lines]

	-	dimension [m3/s]

Variables concerning pumps:
____________________________

-	Discharge (q_pump)

-	size [Number of pumps]

-	dimension [m3/s]

Some numbers:
______________________

-	computational cells in 2D (nFlowElem2D)

	-	  [n2dtot]

-	computational cells in 1D (nFlowElem1D)

	-	  [n1dtot]

-	computational cells concerning 2D boundary conditions (nFlowElemBound2d)

	-	  [n2dobc]

-	computational cells concerning 1D boundary conditions  (nFlowElemBound1d)

	-	  [n1dobc]

-	total computational cells (nFlowElem)

	-	  [number of computational nodes]

-	Flowlines in 2D Domain (nFlowline2D)

	-	  [l2dtot of liutot+livtot]

-	Flowlines in 1D Domain (nFlowline(1D)

	-	  [l1dtot]

-	1D2D Connections (nFlowline1D2D)

	-	  [infl1d]

-	Flowlines concerning 2D boundary conditions (nFlowline2DBound)

	-	  [n2dobc]

-	Flowlines  concerning 1D boundary (nFlowline1DBound)

	-	  [nodobc-n2dobc]

-	Total number of flowlines  (nFlowline)

	-	  [number of flow lines]

-	Number of Pumps (nPumps)

	-	  [jap1d]

-	Number of potential breaches (nBreaches)

	-	  [levnms]
