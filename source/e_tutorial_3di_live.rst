.. _tutorial_3di_live:

Tutorial 1: Using 3Di Live
==========================

Introduction
------------

:ref:`3Di Live <3di_live_introduction>` is an intuitive online interface to run 3Di simulations. You can see the simulation's results as it progresses, and interact with the simulation in many ways. 3Di Live can be used to quickly and interactively assess the behaviour of the water system and communicate with stakeholders effectively. Simple edits can also be performed in 3Di Live, such as shutting down a pump, digging a hole for extra storage, or placing a flood barrier to prevent further flooding. 


Learning objectives
-------------------
In this tutorial you will:

- Become familiar with the interface and possibilities of 3Di Live 

- Get a feeling for how to use 3Di Live in your everyday work

The tutorial helps you to explore 3Di Live and its possibilities. We invite you to explore and try out the options available in the user interface. The more you experiment with it, the more you will learn! 

Preparation
-----------

Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.

* At least one 3Di model should be available for your organisation. If this is not the case, you may do :ref:`tutorial 2 <tutorial2_2dflatmodel>` first.

Loading a model
---------------

#) Go to `3di.live <https://www.3di.live/>`_ and log in.

#) Choose a model from the list, or, if you know the name of your model, type the name in the search bar to find it. There may be more than 1 :ref:`revision` available, numbered with #1, #2, etc. Usually, you will want to use the one with the highest revision number, which is the most recent version of that 3Di model.

#) Click *Start*. If multiple :ref:`simulation templates <simulation_and_simulation_templates>` are available for this 3Di model, a list of available simulation templates will be shown for you to choose one. See  for more information.

Exploring the model
-------------------

On the left side of the screen, you find a toolbar. The tools here are used to inspect the model, add forcings (discharge, pump, rain, or wind), or edit the model during the simulation (editing the DEM or adding a flood barrier). The layers button at the bottom-left opens the *Map Layers* panel, where you can change the visualisation to your liking.
 
#)	Open the *Map Layers* (|map_layer|) panel.

#)  Task: find out what the lowest elevation in the DEM is. Hint: Toggle the *Digital Elevation Map* to visible, and use the :ref:`line_selection_tool` (|line_selection_tool|).

#)	Task: find out what the size of the 2D computational cells is (in m²)? Hint: toggle the :ref:`Model grid <visualisation_calculation_layers_3di_live>` to visible and zoom in. Use the :ref:`line_selection_tool` to measure the length of the cells.

Starting the simulation
-----------------------

#) Click the :ref:`rain_tool_3di_live` button (|rain_tool|). In the *Rain* panel, set the settings to a *Constant* rain event with an *Intensity* of 40 mm/h and a *Duration* of 2 hours. 

#) Click *Create*. Below the rain event options, you will now see that your rain event has been added. If you made a mistake, you may still delete this rain event. This is only possible as long as the simulation is still paused.

#) Click the *Play* button at the top centre to start the simulation. 

#) Zoom in to the areas that are starting to flood. 

#) Use the :ref:`point_selection_tool` (|selection_tool|) to click on the flooded area. In the panel at the right, graphs are displayed that show how the situation is developing in this location: the water level (in m MSL), water depth (relative to the DEM) and rain intensity are shown.

#) Now use the :ref:`line_selection_tool` (|line_selection_tool|) to draw a side view of the flooded area. Notice how the water level changes as the simulation progresses.

\
\

If your model also contains 1D elements (such as channels, pipes, or weirs) you see flow through these, visualized with moving dots. The size of the dots represents the discharge, the speed at which they move represents the velocity.

#) Use the :ref:`point_selection_tool` (|selection_tool|) and click on a 1D element to see its properties. You can stop the flow through this 1D element by setting it to *Closed* when the simulation is paused. 

#) Pause the simulation. In the panel at the right side, click *Edit*. Set the status to *Closed*. Click *Confirm*. Click the *Play* button to resume the simulation.

#) Observe the effect of closing this 1D element in the discharge and velocity graphs on the right-hand side.

Many more tools are available for interacting with the simulation. The best way to become familiar with them is to try them out! The user manual section :ref:`3di_live_interactive_tools` gives further explanation about these tools.


Quitting the simulation
-----------------------

Stop the session via the User menu (|user_menu|) > Quit simulation. You will be asked if you want to store the results. This is useful if you want to do further post-processing or analysis of the simulation results, for example in the :ref:`guide_modeller_interface`. For this tutorial, you do not need to store or download the results. If you want to know how this works and what the different options are, see :ref:`store_results`.



.. |map_layer| image:: /image/pictogram_map_layer.png
    :scale: 80%
.. |rain_tool| image:: /image/pictogram_rain_tool.png
    :scale: 80%
.. |line_selection_tool| image:: /image/pictogram_line_selection_tool.png
    :scale: 75%
.. |selection_tool| image:: /image/pictogram_selection_tool.png
    :scale: 80%
.. |user_menu| image:: /image/pictogram_user_menu.png
    :scale: 60%
    


