.. _a_how_to_vegetation:

How to deal with vegetation and its parameters 
==============================================

Local flow velocities are strongly affected by vegetation. In case of flooding applications, dense vegetation can alter routes for flooding, affect the arrival times of floods, but also by slowing down the flow, it allows more time for infiltration and water buffering. In fluvial or in estuarine flow modelling, it affects the route, it determines the shear stresses, which is crucial information for determining sedimentation and erosion patterns. Having a correct indication of the flow patterns is vital information to preserve, improve and ensure the conditions for various animal and plant species. 

There are various methods available to take the effects of vegetation into account, also in 3Di. The options available in 3Di are selected to ensure a correct capturing of the physics, or at least as good as possible. Keep in mind, that the incorporation of vegetational effects in large scale hydrodynamic models is still a very empirically based field. However, in recent years the ecological value of vegetation in in our society has increased, but also the combine this ecological value with the affects on the hydrodynamics. Where vegetation allows for a strong flow reduction from which protectional measures can benefit. 


Choosing the right method for schematising vegetation
-----------------------------------------------------

Choosing the right method for schematising vegetation depends on the application, the purpose of the model results and the availability of data. Providing generic guidelines is difficult and asks for some expert judgement. However, here are some thoughts to keep in mind:

* **Low vegetation** Low vegetation is vegetation that has the height of the underlying bottom roughness. Generally, as soon as such an area gets wet, it is submerged and the height of the vegetation is in the same order of magnitude as the accuracy in height of the bathymetry values. Under these conditions it is advantageous to model the vegetation as a bottom roughness. That means for 3Di models, setting either Manning or Chézy values.

* **Medium to high vegetation** In case the vegetation height is higher than the roughness layer at the bed, it can be advantageous to model the drag using the method the vegetation drag formulation in 3Di. Thereby, 3Di can take automatically care of the spatial variability and the changing water level conditions. This is especially important when measurement data is limited, and the system can only be calibrated under very specific conditions. This method aims at capturing the physics, so the prediction capability improves.

* **Dense vegetation** In case the vegetation is very dense, it is questionably whether in such a case the drag force can be represented by such a formulation. Under these conditions, where flow is actually going through a porous medium, we are investigating whether the flow is not better simulated by a porosity layer. This is under investigation and the results will be published. More information can be found at Volp et al 2023, NCK Days and the paper that will be submitted in the Journal of hydraulic engineering. 


Setting the right values for the vegetation parameters
------------------------------------------------------

The correct values for the vegetation parameters depend on the species, the growth stadium and the season. The stem diameter, the height and the number of stems can be measured relatively easy, at least, compared to the drag coefficient. In the last decade, more and more measurements have been performed to define these values. Unfortunately, there is not a general overview of these values per species. However, the paper of Vargas-Luna 2015 can give a nice starting point. In the formulation in 3Di, it is generally ok to start with a discharge coefficient set to 1. Depending on the data you have of the area, it allows a more detailed calibration and tuning to the local conditions. The other parameters can be derived from land-use maps and ecological maps. 