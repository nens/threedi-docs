.. 3Di documentation master file, created by
   sphinx-quickstart on Fri Jun  9 12:35:04 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to 3Di's documentation!
===============================

3Di is a process-based, hydrodynamic model for flooding, drainage and other water management studies. It can be used for the computation of water flow in 1D and 2D. The software is developed by a consortium of Stelling Hydraulics, Deltares, TU Delft and Nelen & Schuurmans. With 3Di it is possible to make fast simulations while using a high level of detail. 3Di allows the user to interact with the model during a simulation. One can interactively influence the simulation by changing the rainfall, wind force and model components like cross-sections, breaches and pump capacities.

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/BvS8ijgUvuc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	
*A short introduction to 3Di is given in this video*

Introductie van schematisatie en scenario is samen een simulatie.

The 3Di Ecosystem is composed of four main components; a computational core, an *application programming interface* (API), a modeller interface and a 3Di Live site. The computational core actually computes the water flow. The API enables other applications and user interfaces to interact with the computational core. The computational core and the API run on specialized servers to ensure computational power. We develop and maintain two user interfaces the Modeller Interface and the 3Di livesite. Operational models can also interact directly via the API with the computational core. Naturally,  users who are familiar with programming languages can make their own interface or script to automatically calibrate or add their own controls to their simulation.

TODO: Noem de modellendatabank en voeg die ook toe in je plaatje


.. figure:: image/d_api_3di_ecosystem.png
   :alt: 3Di Ecosystem
	
   The 3Di Ecosystem


.. toctree::
   :maxdepth: 1
   :caption: 3Di Ecosystem
   :name: 3Di Ecosystem

   a_introduction
   a_where_to_start
   a_releasenotes
   a_contributors
   
  
.. toctree::
   :maxdepth: 1
   :caption: User manual
   :name: user_manual
   :numbered: 3

   d_building_a_model
   d_checking_model_schematisation
   d_adding_running_scenario
   d_viewing_analyzing_results
   d_problem_solving


.. toctree::
   :maxdepth: 1
   :caption: Tutorials
   :name: tutorials
   :numbered:
   
   d_workflow_tutorial
   d_2d_tutorial
   d_2d_slope_tutorial

.. toctree::
   :maxdepth: 2
   :caption: Installation manual
   :name: instalation_manual
   
   f_3di_instruments_and_downloads
   d_threedi_portal

.. toctree::
   :maxdepth: 2
   :caption: Physics
   :name: basic_principles
   :numbered:

   b_massconservation
   b_flow
   b_sources_sinks
   b_levees_obstacles_breaches
   b_wind
   b_interception

.. toctree::
   :maxdepth: 2
   :caption: Model concepts
   :name: Model_concepts
   :numbered:

   b_grid
   c_numerics
   c_control
   c_calculation_grid_data
   c_results
   c_aggregate_results
   c_state_files


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
