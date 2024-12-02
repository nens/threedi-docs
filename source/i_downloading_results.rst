.. _mi_download_res:

Downloading results
====================

There are two options for downloading simulation results:

- :ref:`dl_via_models_simulations`, within 7 days

- :ref:`dl_via_lizard_plugin`, if your subscription includes the Scenario Archive

.. _dl_via_models_simulations:

Download via 3Di Models and Simulations panel
---------------------------------------------

Simulation results can be downloaded using the :ref:`models_simulation_panel`. To download results:

#) Activate the *3Di Models and Simulation panel* by clicking the pictogram (|modelsSimulations|) in the toolbar.
#) Click the *Results* icon (|download_results|).
#) Select the results you want to download and click *Download*.

The results will be downloaded to your local 3Di working directory, so that you can find them easily when loading them via the :ref:`3Di Resuls Manager<3di_results_manager>`

The files that are downloaded in this way are the :ref:`Raw results<outputs>`. To download automatically post-processed results, such as maximum water depth rasters, see :ref:`dl_via_lizard_plugin`.

.. note::
    Results are only available for download from the 3Di Models and Simulations panel for 7 days after a simulation has finished.

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%
	
.. |download_results| image:: /image/pictogram_download_results.png
	:scale: 60%

.. _dl_via_lizard_plugin:

Download via the Lizard plugin
------------------------------

If you have stored simulation results in the :ref:`scenario_archive`, you can download them using the `Lizard plugin <https://docs.lizard.net/b_lizardplugin.html>`_.

Instructions for storing simulation results in the Scenario Archive can be found here:

- In the 3Di Modeller Interface, see :ref:`this section<simulate_api_qgis_post_processing>`
- In 3Di Live, see :ref:`this section<store_results>`
- If you have already run a simulation, find it on :ref:`threedi_management` and post-process the results. Note that this last option is only available within 7 days after you have run the simulation.

.. note::
    This option is only available if your subscription includes the Scenario Archive.
