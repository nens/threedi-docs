Choose for 1D or 2D
===================

An important modelling choice is choosing between 1D or 2D flow. This "how to" aims to provide some guidelines when making such choices. While in some situations there is cleare a 'best' option, there are also many situations where the 'best' choice really depends on the specific modelling objectives, performance requirements and data availability.

2D if possible, 1D if needed
----------------------------

The :ref:`subgrid method<subgrid_method>` makes it possible to describe open water channels at a very high resolution in the 2D domain. If you have experience with hydrodynamic modelling with software that does not use subgrid, you may be used to schematising waterways in 1D as soon as they are narrower than the 2D computational cell size. This is often not necessary in 3Di. Realizing this may save you a lot of time and reduce the complexity of the schematisation, which also makes analysis easier.

Reasons to use 1D
-----------------
However, there are still some very good reasons to use 1D elements:

**1D models for very fast simulations.** Models that contain *only* 1D elements usually have much fewer nodes than 2D or 1D-2D models and will therefore run very fast. If your use case requires simulations to be finished within seconds or minutes, or you want to simulate very long periods, or a large number of events, this may be a good option. The trade-off is that you simplify reality much more than in a model with 2D. The routes that the water can take is strongly limited by the schematisation; this is particularly relevant for extreme rain or discharge events, when water will not always follow the man-made or expected routes, take shortcuts or start flowing in opposite directions. 

**Large upstream or downstream areas in 1D.** If the runoff from a large upstream area affects your area of interest, but you are not interested in the exact details of how water flows through that upstream area, 1D may be a good option. You model the area of interest in 2D, but strongly simplify the schematisation of the upstream area, by using a combination of 1D flow and :ref:`0D inflow<0d_rain>`. In a similar way, this can also be relevant downstream. To avoid having a model boundary close to the area of interest, you may extend the 1D schematisation downstream, e.g. to a weir where flow is known to be (super)critical.

**Pipes and other closed structures.** Flow through structures with a closed cross-section can only be schematised using 1D elements. This also allows for the flow to become pressurized once the pipe is full. Examples of this are sewerage systems or culverts.

**Hydraulic structures.** Flow through hydraulic structures, such as weirs or sluice gates, is calculated accurately using weir formulas. When using an :ref:`orifice` or :ref:`weir`, 3Di uses a weir formula to calculate the flow through the structure (see :ref:`weirs_and_orifices`).  

**Channels too narrow for the subgrid resolution**

**Strongly winding or meandering channels**

Connected or embedded
---------------------


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



When to use 1D, when to use 2D
------------------------------
A water system consists often of small channels, ditches and pipes. These are difficult to model in 2D, and therefore they are schematised using the 1D network options in 3Di.

Some considerations for 1D elements
-----------------------------------

Every method has advantages and disadvantages. This is also true for choices considering the 1D types. It depends on the application, where the balance lies:

- considering *connected* types, the seperate dealing of the 1D and 2D domain in the same geographic area results in an overlapping volume domain. This means that the volume above a 1D channel, is counted twice.

- For embedded 1D elements, the specific handling of the 1D information is strongly related to the 2D resolution. However, there is no double counting of volume and no increase in computational cost.

- In general, use 1D models for applications that are truely 1D with respect the rest of the domain. Use it for elements that are narrow with respect to the 2D resolution and all will be fine. In those cases the advantages are great, and the disadvantages will remain small.


When to use connected
---------------------
For applications where one has an extended 2D domain including, various essential small scale features, 1D connected elements will improve the model results. Ditches, canals and manholes can be schematised using the 1D connected elements. Hereby, locally increasing the total resolution of the model.

When to use embedded
--------------------
The option to add 1D elements to the 2D domain will effectively increase your resolution and offers the possibility to take small elements into account. However, adding computational points will affect the computational effort. A middle ground could be the use of embedded 1D elements. In such case the information of the 1D elements is integrated with the information of the 2D domain. The number of computational points is not increased, but the number of velocity points is.

Using 1D vs. 2D
---------------
While modelling think of the type of 1D channel type that fits the watercourses in the study area best. For small ditches in an area without elevation, where the flow velocity is low it is sometimes useful not to use 1D channels. Digging ditches in the elevation map will probably lead to sufficient drainage and will make it possible to use bigger calculation cells.