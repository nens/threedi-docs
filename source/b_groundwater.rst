Groundwater
===========

We are aiming at a modelling method that can handle short term effects of heavy precipitation and inundation including the interaction with groundwater. For the computational of surface flow detailed information about the topography and the land use is often available. The information about the soil is often much less accurate and detailed. This favors a scenario-approach when dealing with groundwater flow, to investigate the sensitivity of areas to flooding and hindrance originating from groundwater. This approach requires a fast numerical model that can integrate the effects of the sewer system, surface water and overland flow.
   
.. figure:: image/b_grw_largescaleoverview.png
   :scale: 30%
   :alt: largescale_figure
   :align: right

   Overview of large scale groundwater concepts (1) 
   
   
Flow in the subsurface is very complex on a large scale, as also the effects on smaller scales can have a significant effect. In order to take all processes into account, models with significant computational times are required, even when surface flow, sewer systems and other processes are neglected. A schematic overview of some of the large scale processes are given in Figure 1. Number I indicates surface flow and overland flow. From the surface, Number II, water can infiltrate or exfiltrate to and from the subsurface where is can flow further in the horizontal or the vertical direction (Number III). From thereon several aquifers can overlap and interact with each other. As they are separated by (semi-) impervious layers, they can exist under different pressures. The interaction can occur in both up- and downward direction (Numbers IV and V).  Moreover, different zones within one aquifer can be distinguished, consisting of a zone of saturation and the zone of acration. In addition, within one aquifier the soil characteristics vary over time and space (Numer VI). To limit the modelling domain and the number of processes to be taken into account, the current method for modelling groundwater flow, is focused on the processes in the top aquifer of the subsurface layer. In the section below, while using Figure 2 the key concepts of the groundwater model and the assumptions made are illustrated.


Groundwater concepts
-----------------------
The physical groundwater concepts on which this groundwater method is based, are thoroughly described in the book of *Jacob Bear and Arnold Verruijt, Modeling Groundwater Flow and Pollution*. Based on the numbers and letters shown in Figure 2, the key concepts and assumption of the groundwater model are illustrated. The aim is to simplify the processes involved in the top aquifer, but to preserve enough accuracy for reliable simulations of the surface interaction.


.. figure:: image/b_grw_overview.png
   :scale: 40%
   :alt: master_figure
   :align: right
   
   
   
.. figure:: image/b_grw_overview_ass.png
   :scale: 40%
   :alt: master_figure
   :align: right   

   Overview of groundwater concepts (2)




1. When only looking at the top aquifer in a system, only one phreatic surface can be defined. This is the level at which the pressure is atmospheric (assumed zero) and the soil is assumed fully saturated. 

2. Above the phreatic surface is the vadose water zone. There is some of the pore space is actually occupied by water, although the soil is not fully saturated. In the right graph, the saturation of the soil is plotted with depth. As can be seen, the change in gradient can be quite steep and is often approximated by a step function. The step-size depends on various issues including the characteristics of the soil. Note, that in the vadose water zone, pressures are negative, which allows the water to go upwards (capillary fringe). 

3. However, when one would place a well, one will find the water level at the phreatic surface. At the top of the capillary water, the water table is defined. In many applications it is valid to approximate the groundwater table at the top of the capillary fringe by assuming the soil to be saturated below this level and completely dry above it. This assumption is called the capillary fringe approximation and gives in combination with surface water flow,  a two-layer system.  When the :math:`h_c` \ is much smaller than the thickness of the aquifer, the capillary fringe can be neglected. Than, the water table and the phreatic surface are at the same level. This is indicated by the Letter *A*  in the bottom panel of the Figure 2. 
  
4. The main flow in an aquifer follows the phreatic surface, therefore the phreatic surface is considered to be a stream line as well. Within an aquifer the slope of the phreatic surface is generally small. It is often much smaller than 1 ( :math:`i<<1` ) [Dupuit (1863)]. In cases where this yields, one can assume the streamlines to be horizontal, and use only the horizontal Darcy equations to compute the flow, based on the groundwater level gradients, defined by the height of the phreatic surface. This implies the assumption of hydrostatic pressure within the aquifer. This assumption is called the Dupuit approximation (Letter *B*  in the bottom panel of the Figure 2.)
 
5. The Dupuit approximation can be locally valid, while in other regions it can be invalid. Number *5*  indicates an example where the incline of the streamlines is higher. The dashed red line indicates where the Dupuit assumption is invalid. In stationary cases, one can apply the so-called Dupuit-Forchheimer discharge formula to compute the outflow from groundwater to surface water. The computation of the discharge is still quite accurate, even though the ground water levels deviate.  In regions further than ones or twice the :math:`\Delta h`, the solution approximates again the actual solution. In 3Di (Letter *C* ), the Dupuit-Forchheimer discharge formula is at these interfaces not applied, as they are often not a priori known. However, for practical purpose this is often only a local deviation.
   
6. The storage capacity in the soil is naturally very important, as it determines the volume that can be added and extracted from the soil. However, the storage capacity and the saturation of the soil is related to very complex processes. This deals with the pores, the distribution of pores and the molecular behaviour of water interacting with the soil.  Not everything can be extracted, therefore we differ between porosity, the specific yield and the specific retention. Where the porosity is the actual porosity, the specific yield is also known as the effective porosity and is a measure for the area where water can be added or extracted. Whereas, the specific retention is representative for the areas within the pores where water cannot be added nor extracted, for example in isolated pores. These values are actually also dependent on the local pressure distribution and partly also whether the pores where previously filled or dry. For simplicity, all these processes are simplified by defining a phreatic storage capacity that is a measure for the effective storage in this layer (Letter *D* ). Although, this is a strong simplification of reality, the detailed structures in the soil at this level of detail are generally unknown.  
  
7. In case of a porous surface layer, surface water will be flowing downward due to gravity, depending on the pressure gradient, the saturation and the hydraulic connectivity. As seen in the graph, there will be a saturated front flowing dpownward. There is a difference between the infiltration rate and the effective infiltration velocity. The infiltration rate is the rate in which the surface water level decreases. The effective infiltration velocity is the velocity of the front of the saturated zone. Due to differences in porosity the effective velocity can vary with depth. The vertical flow can be described by a Darcy-like formulation in the vertical:

.. math::
   :label: inf_press

	q(x,y,z,t) = -\kappa(x,y,z) \frac{\partial \phi}{\partial z}
	
where :math:`\phi` is the hydraulic head. This equation is seemingly simple, but the hydraulic head and the hydraulic connectivity are both dependent on the saturation of the soil. Due to the complexity of the infiltration processes, there are various formulations for infiltration, such as Green and Ampt, Horton and Philip infiltration. There are several differences between does formulations, however, they share that the infiltration rate is initially higher and decreases more or less exponentially to an equilibrium rate. For now, only the Horton-based infiltration, see :ref:`grwhortoninfiltration`, is implemented, which is a formulation, originally, for ponded infiltration only. The formulation described by Horton (1875-1945) takes into account that when the soil contains more water, the infiltration rate will decrease. This can be seen in the graph in Figure 2 at label *E*.

8. Within the soil, multiple aquifers can exist within one domain. Such aquifers are separated by (semi) impervious layers, but these can leak. To simulate the potential interaction between these layers, it is possible to add a bottom boundary condition for flow. This can represent the possible effect of deeper groundwater layers (See Figure 2 at label *E* ).
   
9. The soil water zone is the layer just below the surface. Often this is a fully saturated area, but the processes in this layer are heavily affected by the vegetation, precipitation and evaporation. Therefor, often the simulation of this layer is difficult. In case of heavy precipitation, this layer becomes saturated in a sort time. In such case, a user can simulate this layer with use of the interflow layer (Figure 2 at label *F* ).


.. _grwhortoninfiltration:

Horton based infiltration
-----------------------------------
Mentioned above, the infiltration proces is rather complex, therefore many models use a parametrization for this proces. In 3Di, a horton based infiltration is chosen. Three variables determine the infiltration rate in time. It is based on the notion that the infiltration rate decays to an equilibrium value. Mathematically:

.. math::
   :label: inf_horton

	f(x,y,t) = f_{equ}(x,y)+(  f_{ini}(x,y)-f_{equ}(x,y))e^{-t/T(x,y)}

in which :math:`f` is the infiltration rate varying in time and space, :math:`f_{equ}` and :math:`f_{ini}` are the equilibrium and the initial infiltration rates, respectively. The decay period :math:`T` determines the time that the infiltration rate reaches its equilibrium. An example of the decay function is shown in Figure 3. 

.. figure:: image/b_grw_inf_rate.png
   :scale: 100%
   :alt: Horton infiltration
   :align: right   

   Infiltration rate according to Horton; with :math:`f_{equ}=300.0` mm/day and :math:`f_{ini}=100.0` mm/day and :math:`T=3.0` days.    (2)


The infiltration rate will start its decay as soon as the cell becomes wet. Currently there is no process that the infiltration rate will restore the rate to its initial value. This would happen in real life when an are becomes dry again due to runoff or evaporation.   
   
   
Input
~~~~~~~~~~~~
For the use of Horton infiltration, one chooses indirectly to take a groundwater level into account. This to ensure a limit to the infiltration, when the groundwater level reaches the surface. To take the storage capacity of the soil into account one needs to define the impervious surface layer and the phreatic storage capacity, as well. The three Horton parameters, the impervious surface layer and the preatic storage capacity can be defined globally and spatially varying. In case one uses the spatially varying option a user needs to define a method for analysing the rasters (taking the minimum, maximum or the average in a cell). You can download the complete overview of tables that 3Di uses in the spatialite database :download:`here <pdf/database-overview.pdf>`.

Output
~~~~~~~~~~~ 



.. _grwflow:

Groundwater flow 
--------------------

Input
~~~~~~~~~~~~

Output
~~~~~~~~~~~ 

.. _grwleakage:

Sources and Sincs, Leakage
-----------------------------

Input
~~~~~~~~~~~~

Output
~~~~~~~~~~~ 



