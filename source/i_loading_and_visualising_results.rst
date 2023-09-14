.. _loading_visualising_results:

Loading and visualising results in the 3Di Modeller Interface
=============================================================

.. _3di_results_manager:

Loading simulation results
--------------------------

To add computational grids and simulation results to your project, open the *Results Manager* from the toolbar (|addresultstoolbar|). Click |addresults| in the upper right corner to search for the simulation results you want to analyse. You can choose from all simulation results that have been downloaded to your local 3Di working directory. Alternatively, switch to the *Browse* tab to browse for gridadmin.h5 or results_3di.nc files in other locations. Select the desired results file and click either *Load computational grid* or *Load simulation results*. Both options will load the computational grid into the Layers panel, but the latter option is required to see the results. You can also double click on a row to add the items to your project.

If multiple simulations have been run with the same 3Di model, the computational grid will be loaded once and both simulation results will be connected to the same computational grid.

To remove a computational grid or simulation result, select the item you want to remove and click |removeresults| in the upperright corner.

Under **General settings** you can select whether or not the simulation start times are aligned (based on the simulation with the earliest start time) in case you have loaded multiple sets of results.

In the **Visualisation settings** you can select the flowline and node variables you want to view. By checking the *Relative* checkbox the node results are visualised as change relative to the initial values (t0).

.. _visualising_results:

Visualising results on the map canvas
-------------------------------------

To visualise the simulation results on the map canvas, click the |closed_eye| icon. This changes the styling of the computational grid layers, to show the flow variables chosen under *Visualisation settings*. The value ranges in the styling are based on the value distributions of these variables over the entire simulation. 

By default, the last time step is visualised. Use the :ref:`temporal_controller` to navigate through time. 

.. TODO: Once the labels/aliases of the flowlines have been 'fixed' the filters under 2) can be added, with a screenshot and example (as was previously done).

1) The 1D node results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.
2) The flowline results that correspond to the selected flowline variable in the *Visualisation settings* of the Results Manager. The results can by filtered to only show the specific flowlines you are interested in. To do this right click the ‘flowline_results’ layer (whose name corresponds to the chosen variable) and choose ‘Filter...’. The Query Builder will open. Double click ‘line_type’ in the box **Fields** and click ‘Sample’ or 'All' to see which types are available. In the box below you can specify the types of flowlines you want to see.
3) The 2D computational cell results that correspond to the selected node variable in the *Visualisation settings* of the Results Manager.

.. image:: /image/i_temporal_controller_layers.png
	:scale: 30%
	:alt: Temporal Controller - Layers panel

.. |closed_eye| image:: /image/pictogram_temporal_controller_load_results_closed_eye.png
	:scale: 100%
	
.. |opened_eye| image:: /image/pictogram_temporal_controller_load_results_opened_eye.png
	:scale: 100%

.. |addresultstoolbar| image:: /image/i_3di_results_analysis_toolbar_results_manager.png
	:scale: 25%

.. |addresults| image:: /image/pictogram_add_results.png
	:scale: 90%	
	
.. |removeresults| image:: /image/pictogram_remove_results.png
	:scale: 90%	

