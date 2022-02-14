.. _overview_documentation:

.. TODO: *hier een globaler verhaal typen met uitleg hoe de documentatie is opgebouwd met referenties naar de kopjes*
    




Overview documentation
^^^^^^^^^^^^^^^^^^^^^^^

This document presents some tutorials and a description of the methods used in 3Di. This document will help the novice as well as the experienced 3Di-user. For the novice it contains background information and key points for creating a first model, while for the experienced user it will serve as a reference work. The manual contains the following sections:

* The sections under *Tutorials* is the place to start if you want to get going with existing models and changing them. In these section we also describe how to get insight in the results and some best practices. 

* The section *Problem Solving* consists of a list that contains the most common Error messages including how to fix them. We also update here some known issues. 

* In the sections under *Physics*, the concepts behind the 3Di engine are explained in detail. Read these sections to get to know the processes and the computations of 3Di.

* In the final part, *Model Concepts* clusters a series of numerical methods used by 3Di.

Information about courses, examples, demonstrations and how to contact us can be found on: https://3diwatermanagement.com/.


.. _welcome:

Introduction to 3Di
^^^^^^^^^^^^^^^^^^^^^^^^

3Di is a process-based, hydrodynamic model for flooding, drainage and other water management studies. It can be used for the computation of water flow in 1D and 2D. The software is developed by a consortium of Stelling Hydraulics, Deltares, TU Delft and Nelen & Schuurmans. With 3Di it is possible to make fast simulations while using a high level of detail. 
3Di allows the user to interact with the model during a simulation. One can interactively influence the simulation by changing the rainfall, wind force and model components like cross-sections, breaches and pump capacities.

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/BvS8ijgUvuc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	
*A short introduction to 3Di is given in this video*

.. TODO: Introductie van schematisatie en scenario is samen een simulatie.

The 3Di Ecosystem is composed of four main components; a computational core, an *application programming interface* (API), a modeller interface and a 3Di Live site. The computational core actually computes the water flow. The API enables other applications and user interfaces to interact with the computational core. 
The computational core and the API run on specialized servers to ensure computational power. We develop and maintain two user interfaces the Modeller Interface and the 3Di livesite. Operational models can also interact directly via the API with the computational core. 
Naturally,  users who are familiar with programming languages can make their own interface or script to automatically calibrate or add their own controls to their simulation.

.. TODO: Noem de modellendatabank en voeg die ook toe in je plaatje


.. figure:: image/d_api_3di_ecosystem.png
   :alt: 3Di Ecosystem
	
   The 3Di Ecosystem

.. _background:

Background of 3Di
^^^^^^^^^^^^^^^^^

The 3Di engine is based on state-of-the-art numerical schemes. The engine makes use of a so-called subgrid method. This technique includes high resolution information in coarse resolution computations. This guarantees both accuracy and efficiency. The 3Di engine includes a whole range of processes, including surface run-off, 1D and 2D surface water and groundwater flow. Moreover, it can deal with 1D sewer flow and structures like pumps, weirs and culverts. 3Di deals with numerous external forcings, like precipitation from radar images and wind. These unique characteristics makes 3Di suitable for climate impact studies, flood studies and hydraulic design of open channel and sewer networks.

The 3Di engine is developed by Prof. dr. ir. G. S. Stelling, who worked on the subgrid technique in close collaboration with Prof. dr. ir. V. Casulli. Most of the techniques used within the 3Di engine are published in scientific papers.
