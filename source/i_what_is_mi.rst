.. _mi_what_is:

What is the Modeller Interface
================================

The 3Di Modeller Interface is the 3Di desktop application. It makes it easy for expert modellers and hydrologists to build and edit 3Di models, run simulations and analyse simulation results to understand water systems and assess flood risks or other hydrological phenomena.

This video shows the workflow from start to finish of the modelling process:

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Uvjf4s77vr0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*Demo of the modelling process* 

For an overview of the interface and its components visit the :ref:`mi_overview` page. For more detailed information on the modelling workflow, visit the :ref:`workflow` page. There are also multiple tutorials available on how to work with the 3Di Modeller Interface. A good starting point is the :ref:`Workflow Tutorial <tutorial1_workflow>`.


This user manual is structured along the common workflow:

* :doc:`f_3di_instruments_and_downloads`
* :doc:`i_overview_user_interface`
* :doc:`i_create_new_schematisation`
* :doc:`i_loading_schematisations`
* :doc:`i_editing_schematisations`
* :doc:`i_checking_schematisations`
* :doc:`i_uploading_and_downloading_schematisations`
* :doc:`i_running_a_simulation`
* :doc:`i_downloading_results`
* :doc:`i_analyzing_results`


Technical setup
----------------
The Modeller Interface is a customized version of QGIS, shipped with several pre-installed plugins and settings. It uses the latest Long Term Release version of QGIS. All components of the 3Di Modeller Interface are installed when running the installer (.exe file). It includes the following:

3Di plugins
^^^^^^^^^^^

- *3Di Schematisation Editor* for editing schematisations

- *3Di Models and Simulations* for interaction with the 3Di API: uploading and downloading schematisations, starting and stopping simulations, downloading results.

- *3Di Toolbox* for analysing simulation results

- *3Di Customisations* takes care of the user interface customization: the user interface is simplified, some colors are different and the application name, logo and splash screen are changed.

Third party plugins
^^^^^^^^^^^^^^^^^^^

The 3Di Modeller Interface also includes some plugins that were developed by other companies or individuals. These plugins were not made  specifically for 3Di, but are very useful for 3Di modellers. These are:

- Profile tool

- Value tool

- Serval

- Quick Map Services

All these plugins are installed in a QGIS user profile folder that also contains all QGIS settings. Some of these have been pre-configured for you, such as the user interface language, number notations, and Python macro settings.


Difference between 3Di Modeller Interface and QGIS
------------------------------------------------------
There is no difference between the 3Di Modeller Interface and the Long Term Release version of QGIS. It is simply QGIS, but expanded with extra functionalities.

We have chosen QGIS as our supporting platform because of the following reasons:

- It enables seamless integration of 3Di-specific tasks with advanced GIS functionality

- QGIS comes with hundreds of powerful GIS processing tools

- It offers an extensive amount of styling options

- It has a highly customizable interface

- The option of building your own scripts, expressions, graphical models and plugins to interact with 3Di

- The fact that it is an open source platform