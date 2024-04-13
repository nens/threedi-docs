3Di for developers
==================

All parts of the 3Di workflow can be automated or integrated in other applications. 

- Schematisations can be edited using Python and/or SQL (see :ref:`schematisation_scripting`).
- The 3Di API can be used for all interaction with online 3Di resources, like uploading schematisation revisions, creating 3Di models, running simulations and downloading results
- The Python package threedigrid can be used for advanced results analysis in Python
- The Python package threedidepth can be used to create water depth and water level rasters from raw 3Di results.
- The Lizard API can be used to interact with the 3Di Scenario Archive, e.g. download stored and post-processed simulation results.

The 3Di user interfaces (3Di Live, 3Di Management, and 3Di Modeller Interface) all use these packages under the hood; everything you can do in these interfaces can also be done programatically with the libraries mentioned above.


.. toctree::
   :maxdepth: 1

   j_schematisation_scripting
   j_api
   j_threedigrid
   j_threedidepth
   j_fews_3di_integrations
   j_lizard_api