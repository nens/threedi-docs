.. _mi_analysing_results_introduction:

Analysing results in the 3Di Modeller Interface
===============================================

The 3Di Modeller Interface offers a range of tools to visualise and analyse computational grids and simulation results. These tools are available from the *3Di Results Analysis toolbar* and from the 3Di section in the *Processing Toolbox*.

These tools relate the time series of the flow variables (water levels, volumes, velocities, discharges, etc.) that are stored in the :ref:`output files<outputs>` to the nodes and flowlines in the :ref:`computational_grid`. 

.. _3di_results_manager:

3Di Results Manager
-------------------

To add computational grids and simulation results to your project, open the *Results Manager* from the toolbar (|addresultstoolbar|). Click |addresults| in the upper right corner to search for the simulation results you want to analyse. You can choose from all simulation results that have been downloaded to your local 3Di working directory. Alternatively, switch to the *Browse* tab to browse for gridadmin.h5 or results_3di.nc files in other locations. Select the desired results file and click either *Load computational grid* or *Load simulation results*. Both options will load the computational grid into the Layers panel, but the latter option is required to see the results. You can also double click on a row to add the items to your project.

If multiple simulations have been run with the same 3Di model, the computational grid will be loaded once and both simulation results will be connected to the same computational grid.

To remove a computational grid or simulation result, select the item you want to remove and click |removeresults| in the upperright corner.

Under **General settings** you can select whether or not the simulation start times are aligned (based on the simulation with the earliest start time) in case you have loaded multiple sets of results.

In the **Visualisation settings** you can select the flowline and node variables you want to view. By checking the *Relative* checkbox the node results are visualised as change relative to the initial values (t0). The results are loaded in your computational grid (see :ref:`temporal_controller_layers_panel`). The visualisation through time is handled by the :ref:`temporal_controller`.

Visualising results on the map canvas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the results are visible (|opened_eye|) they are loaded into the corresponding layers of the computational grid in the Layers panel.
The results are automatically styled based on the ranges of the values. 

.. TODO: Once the labels/aliases of the flowlines have been 'fixed' the filters under 2) can be added, with a screenshot and example (as was previously done).

1) The 1D-node results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.
2) The flowline results that correspond to the selected flowline variable in the *Visualisation settings* of the Results Manager. The results can by filtered to only show the specific flowlines you are interested in. To do this right click the ‘flowline_results’ layer (whose name corresponds to the chosen variable) and choose ‘Filter...’. The Query Builder will open. Double click ‘line_type’ in the box **Fields** and click ‘Sample’ or 'All' to see which types are available. In the box below you can specify the types of flowlines you want to see.
3) The 2D-computational cell results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.

.. image:: /image/i_temporal_controller_layers.png
	:scale: 30%
	:alt: Temporal Controller - Layers panel

.. |closed_eye| image:: /image/pictogram_temporal_controller_load_results_closed_eye.png
	:scale: 100%
	
.. |opened_eye| image:: /image/pictogram_temporal_controller_load_results_opened_eye.png
	:scale: 100%


.. _temporal_controller:

Temporal controller
^^^^^^^^^^^^^^^^^^^

When you load your results the Temporal Controller will automatically appear at the top of your screen (if it was not already visible). With the Temporal Controller you can see and analyse the results through time. The Temporal Controller is a native feature of QGIS and can also be utilised in combination with other results tools. To use this tool, you first need to click the |closed_eye| in front of the desired results in the *Results Manager*. If you have loaded more than one set of results, the |opened_eye| shows the set that is used in the visualisation. Click the |opened_eye| again to stop visualisation of the results.

The results are visualised on the flowlines, 1D nodes and 2D computational cells (see :ref:`3dinetcdf` for more information on the possible flow-variables).

Temporal Controller panel
~~~~~~~~~~~~~~~~~~~~~~~~~
	
1) Pause or play the animation of the results through time.
2) Skip to next frame.
3) Skip to last frame.
4) Move the slider to visualise the results at different timesteps.
5) Check to automatically reset and repeat the animation endlessly when running the animation.
6) The temporal range that is used for the visualisation. Note that the default range that is shown is the range used in the simulation.
7) The steps per frame. Here the steps frame are shown every 300 seconds. Note that this shouldn't be smaller than the used output timestep in the simulation.
8) The units that correspond to the number of steps [6].
9) Export the results as png's for every or any timestep.

.. image:: /image/i_temporal_controller.png
	:alt: Temporal Controller panel

.. |addresultstoolbar| image:: /image/i_3di_results_analysis_toolbar_results_manager.png
	:scale: 25%

.. |addresults| image:: /image/pictogram_add_results.png
	:scale: 90%	
	
.. |removeresults| image:: /image/pictogram_remove_results.png
	:scale: 90%	

.. |temporalcontroller| image:: /image/i_temporal_controller.png
	:scale: 90%	
		
.. _logfile:

Log file
--------

Clicking the (|loggingtoolbar|) saves the logging of your results analysis to your computer. By clicking the underlined path to the text file in the pop-up windows you can open the log file. This can provide helpful information about what went wrong in case of an error.

Also, it can be send as an attachment to our :ref:`servicedesk` at servicedesk@nelen-schuurmans.nl in case of errors.

.. |loggingtoolbar| image:: image/i_3di_results_analysis_toolbar_logging.png
	:scale: 25%