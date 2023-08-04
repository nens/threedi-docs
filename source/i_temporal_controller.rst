.. _temporal_controller:

Temporal Controller
===================

With the Temporal Controller you can see your results through time. The Temporal Controller is a native features of QGIS and is also usedful with other results tools. To use this tool on the full extent of your model, you first need to click the (|closed_eye|) in front of your results in the *Results Manager*. If you have loaded more than one set of results, the |opened_eye| shows the set that is used in the visualisation.

The results are visualised on the flowlines, 1D nodes and 2D computational cells (see :ref:`3dinetcdf` for more information on the possible flow-variables).

Temporal Controller panel
---------------------------
	
1) Pause or play the animation of the results through time.
2) Skip to next frame.
3) Skip to last frame.
4) Check to automatically reset and repeat the animation endlessly.
5) The temporal range that is used for the visualisation. Note that the default range that is shown is the range used in the simulation.
6) The steps per frame. Here the steps frame are shown every 300 seconds. Note that this shouldn't be smaller than the used output timestep in the simulation.
7) The units that correspond to the number of steps [6].
8) Export the results as png's for every or any timestep.


.. image:: /image/i_temporal_controller.png
	:alt: Temporal Controller panel

Results in Layers panel
-----------------------

Once the results are visible (|opened_eye|) they are loaded into the corresponding layers of the computational grid in the Layers panel.
The results are automatically styled based on the ranges of the values. 

1) The 1D-node results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.
2) The flowline results that correspond to the selected flowline variable in the *Visualisation settings* of the Results Manager.
3) The 2D-computational cell results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.

.. image:: /image/i_temporal_controller_layers.png
	:scale: 30%
	:alt: Temporal Controller - Layers panel

.. |closed_eye| image:: /image/i_temporal_controller_load_results_closed_eye.png
	:scale: 100%
	
.. |opened_eye| image:: /image/i_temporal_controller_load_results_opened_eye.png
	:scale: 100%

