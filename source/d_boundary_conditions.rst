Boundary Conditions
======================

Boundary conditions are used to describe the behavior of the system outside the domain of interest. Boundary conditions can be present in both the 1D and 2D domain. A boundary condition has a location, a type and a value. The type defines the method that is applied to handle the flow. There are four types of boundary conditions: water level, discharge, velocity and water level slope (Sommerfield) over time. Water level values can be defined as a constant or as a time series. 

- *Water level [mNAP]:* The user defines a water level. The computation of the solution will hold the water level at that location fixed at the given values. The flow will adapt to that value. For example, the water level behind a sewer spillway or an alternating tidal elevation.

- *Discharge [m3/s]:* The user defines a discharge. This flux and momentum is applied to the boundaries. It is typically used to define incoming values, for example, the incoming discharge of a river.

- *Velocity [m/s]:* The user defines a velocity into or out of the model. This type of boundary condition is also usually used at locations where water is entering the system.

- *Water level slope (Sommerfeld) [m/m]:* The user fixes the water level gradient at this boundary. This is very convenient at the outgoing boundary. This boundary condition allows the system to go to an equilibrium, and allows disturbances to go out of the system in stead of being reflected.

Boundaries in the 1D network
-----------------------------

Boundary conditions for a 1D network are defined on connection nodes. They can only be defined on connection nodes that have only one connection to the rest of the network.

The boundary is defined in the *v2_1d_boundary_conditions* table. There the user can define the type, the location and the time series. The values of the time series are interpolated between the defined times. A time series must be defined over the full period of the simulation. In QGIS it is not possible to add a new line in the attribute table. Therefore you should either compose the timeseries in a text-editor and copy paste it into the field, or compose the time series through the field calculator and use "\\n" to create a new line. With the *Meuse* Release of the 3Di Plugin, a specific menu came available to assist in editing the values.

The time series for all 1D boundary conditions must be the same. Check the different types of boundary conditions available in the Database overview. Please note that a boundary cannot be placed directly on a pump station. 

Boundaries in the 2D domain
----------------------------

A 2D boundary can be used to specify the flow at the edges of the 2D domain. The boundary should exactly coincide with the edge of the bathymetry raster. The 2D boundaries can only be defined perfectly horizonal or vertical. 

The 2D  boundary condition can be defined in the *v2_2d_boundary_conditions* table. There you can define the type and the (time varying) values. The time series are specified as a list of time (seconds) and values (dependend on boundary type) i.e.:

0,10
9999,10

The values are interpolated between the different times. A time series must be defined over the full period of the simulation. The time series may be longer, but not shorter. In QGIS it is not possible to add a new line in the attribute table. Therefore you should either compose the timeseries in a text-editor and copy paste it into the field, or compose the timeseries through the field calculator and use "\\n" to create a new line. With the *Meuse* Release of the 3Di Plugin, a specific menu came available to assist in editing the values.

There are some tips and tricks to define the location of the 2D boundary condition. 
-  As the boundary condition is defined at the edge of the batymetry raster, it works best with straight rasters.
- It can help to convert the raster outline to a shapefile, that defines the location of the boundary condition.