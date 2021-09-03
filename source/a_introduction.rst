Introduction
============

3Di is a process-based, hydrodynamic model for flooding, drainage and other water management studies. It can be used for the computation of water flow in 1D and 2D. The software is developed by a consortium of Stelling Hydraulics, Deltares, TU Delft and Nelen & Schuurmans. With 3Di it is possible to make fast simulations while using a high level of detail. 3Di allows the user to interact with the model during a simulation. One can interactively influence the simulation by changing the rainfall, wind force and model components like cross-sections, breaches and pump capacities.

Background
----------

The 3Di engine is based on state-of-the-art numerical schemes. The engine makes use of a so-called subgrid method. This technique includes high resolution information in coarse resolution computations. This guarantees both accuracy and efficiency. The 3Di engine includes a whole range of processes, including surface run-off, 1D and 2D surface water and groundwater flow. Moreover, it can deal with 1D sewer flow and structures like pumps, weirs and culverts. 3Di deals with numerous external forcings, like precipitation from radar images and wind. These unique characteristics makes 3Di suitable for climate impact studies, flood studies and hydraulic design of open channel and sewer networks.

The 3Di engine is developed by Prof. dr. ir. G. S. Stelling, who worked on the subgrid technique in close collaboration with Prof. dr. ir. V. Casulli. Most of the techniques used within the 3Di engine are published in scientific papers.


Introduction video
--------------------

A short introduction to threedi is given in this video:

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/BvS8ijgUvuc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


3Di Ecosystem
----------------

3Di is completely cloud-based. Simulations are run in the cloud, model building is done on the laptop using the Modeller Interface. All interaction with the calculation core is done using an API. An API is an Application Programming Interface, and it enables software applications to talk with one another. The API is the connection between our user interfaces and the calculation core. Next to that, it is also possible as a user to interact with the API directly. This is for more advanced users, familiar with programming languages. 

.. figure:: image/d_api_3di_ecosystem.png
    :alt: 3Di Eco system

Modeller Interface
^^^^^^^^^^^^^^^^^^

The Modeller Interface is the interface where users build models, adjust models, start simulations and analyze results. The Modeller Interface is a customized QGIS installation with dedicated plugins for the use of 3Di. Thanks to this setup users can use the benefit of all processing power of QGIS combined with tools supporting 3Di. Since a 3Di schematization consists of a compact database (currently spatialite format) and rasters users have a great deal of freedom in building the model. And when finished there is no import/export necessary, the spatial dataset is the schematization. 

.. figure:: image/a_intro_modeller_interface.png
    :alt: 3Di Modeller Interface
	
In short:

- QGIS Technology, use the power of hundreds of GIS processing tools
- Combine web maps (aerial, topo, osm and may others) and model schematizations
- Powerful styling options (almost unlimited styling options)
- Highly customizable interface
- Option for building own plugins to interact with model (results)


Live site
^^^^^^^^^^^

The live site is the interface where users have live insight in the results of their simulation. Not only that, they can also interact with it. This interface is perfect to create a shared understanding of the watersystem

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/k9heL89ZF1E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Model databank 
^^^^^^^^^^^^^^^^^^

Editing is done on a laptop or computer using the Modeller Interface or QGIS, storage is in the cloud. When uploading a model it is stored in the model databank. Users upload their model with a description of the adjustment being made. Other users can synchronize their models on their own laptop and continue working with the improved version. Every version of the model is being stored in the cloud. It’s super easy to browse back and download a previous version.

Within 3Di the data governance structure is set-up per organisation. People from within the same organisation can see all models that belong to their entity. 

Sharing the model with other outside your organisation is also possible. There are two ways to organize this:

- external people get access to the 3Di subscription, have read and write access to the models and can run them
- external people download the 3Di models and use their own subscription for running simulation


3Di API 
^^^^^^^^
	
3Di has a completely API setup. Not only that: the API is accessible for users. It is a more advanced way of modelling, but it enables great flexibility and can speed up projects. The benefits of using the 3Di API is:

- Batch calculating
- Automated testruns & results checking & adjusting a model and run it again
- Run 3Di in an operational setting 
- Use Jupyter Notebooks to run, download en analyze 3Di simulations. Examples can be found on the : `threedi github repository <https://github.com/threedi/scripts-nens/tree/master/Notebooks%203Di%20-%20API%20v3%20-%20VD>`_
- Use other applications 



The current production API of 3Di is v3. For previous versions of the API check this section :ref:`api_v1`

Where to start?
--------------- 

This document presents some tutorials and a description of the methods used in 3Di. This document will help the novice as well as the experienced 3Di-user. For the novice it contains background information and key points for creating a first model, while for the experienced user it will serve as a reference work. The manual contains the following sections:

* The sections under *Tutorials* is the place to start if you want to get going with existing models and changing them. In these section we also describe how to get insight in the results and some best practices. 

* The section *Problem Solving* consists of a list that contains the most common Error messages including how to fix them. We also update here some known issues. 

* In the sections under *Physics*, the concepts behind the 3Di engine are explained in detail. Read these sections to get to know the processes and the computations of 3Di.

* In the final part, *Model Concepts* clusters a series of numerical methods used by 3Di.

Information about courses, examples, demonstrations and how to contact us can be found on: https://3diwatermanagement.com/.

