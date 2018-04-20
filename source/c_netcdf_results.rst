Results in the NetCDF
========================


The raw results of 3Di, or snap shots of the flow variables are stored in a NetCDF-file. This is a common file type, for which there are several standars packages in matlab, python and excell availble to extrct the data from it. It is also the file from which the 3Di plugin recieves its information.

In  the file called: Subgrid_map.nc exists the following information:

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

-	Deepenst point of a computational cell (bath)

		-	size [number of computational nodes]
	
		-	dimension [m MSL]

-	Potential breaches

		-	size [number of potential breaches]

		-	dimension [-]
	

Mapping adminstratie:
__________________________
-	Mapping of input and out put of connection nodes (node_mapping)
	
		-	size [2,number of connection nodes]
	
		-	dimension [-]

-	Mapping of input and out put of connection lines (channel_mapping)
	
		-	size [2,number of flow lines]
	
		-	dimension [-]
	
Variabeles computed per computational cell:
_____________________________________________
-	Time (time)

		-	size [number of timesteps]
		
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
	
Variabelen per line:
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

Variabels concerning pumps:
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
