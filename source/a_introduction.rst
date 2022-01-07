Modeller Interface
^^^^^^^^^^^^^^^^^^

The Modeller Interface is the interface for the hydrology experts. This interface is used to build models, edit models, start simulations and analyse results. The Modeller Interface is a customised QGIS installation with dedicated plugins for the use of 3Di. 
This setup allows users to benefit of all processing power of QGIS combined with custom made tools supporting 3Di. Since a 3Di schematisation consists of a compact database (currently spatialite format) and rasters users have a great deal of freedom in building their model. 
And when finished there is no import/export necessary, the spatial dataset is the schematisation. 

.. figure:: image/a_intro_modeller_interface.png
   :alt: 3Di Modeller Interface
   
   An example of a schematisation in de Modeller Interface.   
	
	
We have chosen QGIS as our supporting platform to build, edit and analyse the 3Di models and the results for the following reasons:

- QGIS Technology allows you to use the power of hundreds of GIS processing tools
- Combine web maps (aerial, topo, osm and may others) and model schematisations
- It offers almost unlimited styling options styling options
- It is a highly customisable interface
- Option for building own plugins to interact with model (results)
- It is an open source platform. 




  .. todo::
		mooi verhaaltje over onze visie en samenwerking met lutra en de donaties.
		


3Di Live
^^^^^^^^

The 3Di Live Site is the interface where users have live insight in the results of their simulation. Not only that, they can also interact with it. This interface is perfect to create a shared understanding of the watersystem. 
Scientific papers on this can be found `here <https://www.researchgate.net/publication/285586163_Interactive_use_of_simulation_models_for_collaborative_knowledge_construction_-_The_case_of_flood_policy_decision-making>`_

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/k9heL89ZF1E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
*A short introduction of 3Di.live*


3Di API 
^^^^^^^^

The 3Di API is the center of the 3Di Ecosystem as it allows all interactions of users and forcings. The 3Di API is accessible for users. It is a more advanced way of modelling, but it gives you lots of flexibility and can speed up projects. 
We give here some examples of applications, where it can be usefull to interact directly using the API.

- Batch simulations: run hundred different rain events
- Automated testruns & results checking & adjusting a model and run it again
- Run 3Di in an operational setting 
- Use Jupyter Notebooks to run, download and analyse 3Di simulations. Examples can be found on the : `threedi github repository <https://github.com/threedi/scripts-nens/tree/master/Notebooks%203Di%20-%20API%20v3%20-%20VD>`_
- Design your own control for weirs or other structures

The current production API of 3Di is v3. 

Model database
^^^^^^^^^^^^^^^

The Modeller Interface or QGIS is used to build and edit you model schematisation on your own computer. However, the 3Di models are stored in the cloud, to enable version control. When uploading a model it is stored in the so-called *3Di Model Database*. Users upload their model with a description of the adjustment being made. 
Colleagues can synchronise their models on their own laptop and continue working with the improved version. Every version of the model is being stored in the cloud. It is super easy to browse back and download a previous version.

Within 3Di the data governance structure is set-up per organisation. People from within the same organisation can see all models that belong to their entity. Sharing the model with people outside your organisation is also possible. There are two ways to organize this:

- external people get access to the 3Di subscription, have read and write access to the models and can run them
- external people download the 3Di models and use their own subscription for running simulation

