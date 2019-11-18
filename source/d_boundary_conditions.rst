Boundary Conditions
======================

Sometimes it is necessary to limit a model's extent. On the outer edges of the model boundary conditions can be specified to specify the interaction with the rest of the world. Boundary conditions are used to describe the behavior of the system outside the domain of interest. Boundary conditions can be present in both the 1D and 2D domain. There are four types of boundaries: waterlevel, discharge, velocity and waterlevel slope (Sommerfield) over time. 

- Waterlevel [mNAP]: The user submits a constant or alternating waterlevel at the edge of the model area. Examples are the waterlevel behind a sewer spillway, an alternating tidal elevation or river waterdepth.

- Discharge [m3/s]: The user submits a constant or alternating volume of water which either enters or leaves the model per second. Positive values specify flow into the model and negative values out of the model. Examples are the upstream discharge of a river or sewer water which is pumped into the pumped drainage area of interest. 

- Velocity [m/s]: The user submits a constant or alternating flow velocity into or out of the model. Like the discharge values positive velocities flow into the model while negative values flow out of the model. Examples are the same as with discharge.

- Waterlevel slope (Sommerfield) [m/m]: The user submits a constant or alternating slope of the waterlevel, which drives a discharge into or out of the model. Examples are: tidal waves where flow velocity is driven by the slope of the wave. 

1D Boundaries
-------------------------
Boundary conditions for the 1D system are placed on connection nodes. They can be placed on connection nodes that are connected to a single isolated channel or structure, so not on an embedded or connected channel/sewersystem component. All boundary conditions must have exactly the same time intervalls!! Check the different types of boundary conditions available in the Database overview. Please note that a boundary cannot be placed directly on a pumpstation. 

To create the boundary a list of timesteps (seconds) and values is provided. Between the values the boundary condition is interpolated. The timeseries should always exceed the simulation time. Often this is accomplished by adding "99999,0" at the end. In QGIS it is not possible to add a new line in the attribute table. Therefore you should either compose the timeseries in a text-editor and copy paste it into the field, or compose the timeseries through the field calculator and use "\\n" to create a new line.

2D Boundaries
-------------------------
A 2D boundary can be used to specify the edges of the 2D domain. The boundary should exactly coincide with the edge of the raster and thus works best with straight rasters or through converting the raster outline to a shapefile. Just like with the 1D boundaries there are waterlevel, discharge, velocity and Sommerfield boundaries. A boundary is specified as a list of time (seconds) and values (dependend on boundary type) i.e.:

0,10
9999,10

Between the values the boundary condition is interpolated. The timeseries should always exceed the simulation time. Often this is accomplished by adding "99999,0" at the end. In QGIS it is not possible to add a new line in the attribute table. Therefore you should either compose the timeseries in a text-editor and copy paste it into the field, or compose the timeseries through the field calculator and use "\\n" to create a new line.
