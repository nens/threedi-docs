Obstacles and levees
=============================================

Basic idea
-----------
The subgrid technique used in 3Di allows for a very detailed description of the elevation. However, the subgrid technique does not recognizes all narrow elements within a cell as blocking. Only when these are located at the cell edges they are detected and will block flow. When an element can be defined as narrow depends on the dimensions of the computational cell. Examples of narrow elements can be levees, residential blocks or quay walls. There are several methods for dealing with these elements. One can always refine the computational grid, however, this can be unnecessarily give an increase in the computation cost, but blocking a flow can be essential for a correct result. 3Di offers two different methods to achieve this. It can either be done by general obstacle detection, or by adding an obstacle at a specific location. To elaborate, when using general obstacle detection, the modeler only gives an obstacle height, which the 3Di computational core uses to determine obstacle locations itself. Using the latter method, a modeler can add an obstacle with a specific location and height.  

In practice these two methods can have a different outcome. The explicitly defined obstacles are much stricter in closing 2D flow lines. For some situations this is necessary, however it can also result in an ‘angular’ flow domain which might result in additional friction. The ‘general’ obstacle detection is on the other hand, not always strict enough, but it does not require any work of the modeler. Moreover, it is also possible to use both options in one model. In this case, when both methods block a flow line, the explicitly defined obstacle is dominant over the general approach.  


General obstacle detection
--------------------------
The aim of the obstacle routine is to define obstacle locations based on elevation differences in the elevation layer. As this routine can be used by only defining an obstacle height, this function is easy to use by the modeler. However, in practice this method is not always strict enough, with ‘leaking’ obstacles as a result. Also, the routine may place flow obstacles at undesired locations due to local elevation variations.

The obstacle routine searches for a flow route from one location to another in the direction of the flow velocity within a so called momentum domain. Examples of the momentum domains in x- and y-direction are shown with blue and pink planes in Figure 1. The modeler determines the minimum level of an observed obstacle. This height is relative to the local bottom height. If there is an elevation difference within a computational cell that exceeds the given obstacle height, the flow routine will search for a pathway between one edge of the momentum domain to the other edge. It will try to find a route to reach the other end of the domain for various water levels. When only a route can be found for higher water levels than the input minimal level, the cell will be marked as one that contains an obstacle. The flow link is activated when the water level exceeds the height at which the other end of the cell can be reached. 


.. figure:: image/b6_gridwithsearchroutine.png
   :scale: 50%
   :alt: virtual_conservation_box
   :align: right
   
   Figure 1: A computational grid for 2D flow including local grid refinement. The momentum domains in x- (pink) and y-direction (blue) are indicated by the planes. The schematic obstacle that is found in the digital terrain model is indicated with a green line. The dark green lines show the route found in the various momentum domains (the blue lines). The flow lines indicated as domains that contain an obstacle are represented by the red lines. The blue circles show locations where one might want an obstacle to be defined, but remains open using this routine.
   

There are two exceptions to the this flow routine. First, if the elevation increases with a constant slope, this is recognized by the routine. Also, a slope is recognized when the difference between the minimum and maximum levels at the edges of a computational cell is larger than the obstacle height. 


Explicitly defined obstacles
-----------------------------

If the model wishes to include an obstacle that may not be detected by the calculation grid or doesn't exist in the elevation model it can be given explicitly. These obstacles are given by a line segment and an elevation. These lines and elevations are placed over the quadtree. The routine checks which 2D links cross the obstacle line. For those links that are crossed the obstacle height is used instead of the elevation height for Flow computation. The figure below shows an example of an obstacle line in green.

.. figure:: image/b6_gridwithobstacles.png
   :scale: 50%
   :alt: virtual_conservation_box
   :align: right

   Figure 2: A computational grid for 2D flow including local grid refinements. The momentum domains in x- (pink) and y-direction (blue) are indicated by the planes. The obstacle elements are given with a green line and the flow links with a dashed blue line. The flow links closed by the obstacle are marked with a thick red line.  

In the computational core a levee and obstacle are dealt with the same way. However, defining them is slightly different. Levees are a separate category of obstacle, because they need more variable characteristics than obstacles.
 
More details on how to use obstacles, levees and breaches can be found in :ref:`flood_model`.
