Choose for 1D or 2D
===================

An important modelling choice is choosing between 1D or 2D flow. This "how to" aims to provide some guidelines when making such choices. While in some situations there is cleare a 'best' option, there are also many situations where the 'best' choice really depends on the specific modelling objectives, performance requirements and data availability.

A common pitfall is to let the choice between 1D and 2D depend mainly on data availability, i.e., schematising all waterways and structures for which data is available in 1D. This often lead to sub-optimal results. Take for example a flat area with a lot of small ditches. Adding all these ditches to the schematisation as 1D elements is quite a bit of work, while carving them out in the DEM is simple and will probably capture their function in storage and drainage with sufficient accuracy. This "how to" will help you to make better choices in such situations.


2D if possible, 1D if needed
----------------------------

The :ref:`subgrid method <subgridmethod>` makes it possible to describe open water channels at a very high resolution in the 2D domain. If you have experience with hydrodynamic modelling with software that does not use subgrid, you may be used to schematising waterways in 1D as soon as they are narrower than the 2D computational cell size. This is often not necessary in 3Di. Realizing this may save you a lot of time and reduce the complexity of the schematisation, which also makes analysis easier.

If you are interested in flow that is not strongly dominated by flow in one direction (i.e. along the length of a watercourse), 2D is definitely the best choice. Examples are broad, meandering natural waterways, coasts and estuaries, or flood plains.

If you do not know beforehand which routes the water will take, 2D is also much more suitable. Examples are floods due to dike breaches or overtopped sea walls, or extreme rain events in urban areas. 

Reasons to use 1D
-----------------

However, there are still some very good reasons to use 1D elements (often in combination with 2D):

**1D models for very fast simulations.** Models that contain *only* 1D elements usually have much fewer nodes than 2D or 1D-2D models and will therefore run very fast. If your use case requires simulations to be finished within seconds or minutes, or you want to simulate very long periods, or a large number of events, this may be a good option. The trade-off is that you simplify reality much more than in a model with 2D. The routes that the water can take is strongly limited by the schematisation; this is particularly relevant for extreme rain or discharge events, when water will not always follow the man-made or expected routes, take shortcuts or start flowing in opposite directions. 

**Large upstream or downstream areas in 1D.** If the runoff from a large upstream area affects your area of interest, but you are not interested in the exact details of how water flows through that upstream area, 1D may be a good option. You model the area of interest in 2D, but strongly simplify the schematisation of the upstream area, by using a combination of 1D flow and :ref:`0D inflow<0d_rain>`. In a similar way, this can also be relevant downstream. To avoid having a model boundary close to the area of interest, you may extend the 1D schematisation downstream, e.g. to a weir where flow is known to be (super)critical.

**Pipes and other closed structures.** Flow through structures with a closed cross-section can only be schematised using 1D elements. This also allows for the flow to become pressurized once the pipe is full. Examples of this are sewerage systems or culverts.

**Hydraulic structures.** Flow through hydraulic structures, such as weirs or sluice gates, is calculated accurately using weir formulas. When using an :ref:`orifice` or :ref:`weir`, 3Di uses a weir formula to calculate the flow through the structure (see :ref:`weirs_and_orifices`).  

**Waterways too narrow for the subgrid resolution** If waterways are too narrow to be described within the subgrid resolution (e.g. if only global coverage DEM data with a coarse resolution is available), schematising them in 1D is a good option.

**Strongly winding or meandering water courses** To properly describe the flow through a natural stream with a lot of curves, a fine 2D computational grid would be required. The cross-sections from one cell to the next are determined by the DEM pixel values at the cell boundary only, so any river bends within the cell are ignored. A 1D schematisation of such a channel would describe the actual length of the channel much more precisely. 

Preventing 'double storage'
---------------------------

When combining 1D and 2D domain, extra care should be given to preventing 'double storage'. For example, a water course is schematised in 1D, while it is also present in the DEM. Water can be stored in the 2D cells the channel cuts through, but also in the 1D channel. So the storage capacity is double that of the channel in reality. 

There are several options for preventing this, each with their own merits.

* Use only 2D. If the DEM is accurate enough, you may not need a 1D schematisation of the water course at all. Note that DEMs are often less accurate in the vicinity of waterways, due to the vegetation that is present and the poor LIDAR reflectance of water. It may be needed to carve the channel into the DEM to make the 2D representation more accurate.
* Use 1D with the exchange type :ref:`calculation_type_embedded`. Without adding 1D nodes, the 1D channel will be used to connect 2D cells for the part of the 1D profile that is below the DEM. The volume-storage relations of the 1D channel and the 2D cell will be merged into one, so double counting of storage is not possible. This is especially useful if channel is narrower than the computational cell. 
* Set DEM pixels to NODATA where channels are located, and include the channels' exchange type to (double) connected. If you set the channel exchange type to *double connected* and place *exchange lines* on either side of the channel, water can flow into or out of the channel from both sides. Note that with this solution, it can no longer rain on the water surface in the 2D domain. If the water surface is significant, you may want to add a :ref:`surface` to one or more channel connection nodes. 
* Similar to the previous option, you can use a very high elevation where channels are located. Again, you can use *double connected* with exchange lines on both sides. An advantage is that it can rain directly on the water surface. Disadvantages include that it may lead to interpolation artifacts and it makes it harder to automatically style the DEM properly.

If you use either of the last two options, it is highly recommended to use :ref:`Exchange lines<exchange_line>` to make sure the channel exchanges correctly with the 2D cells at either side.

