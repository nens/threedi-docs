.. _mi_technical_setup:

Technical setup
----------------
The 3Di Modeller Interface is a customized version of QGIS, shipped with several pre-installed plugins and settings. It uses the latest Long Term Release version of QGIS. All components of the 3Di Modeller Interface are installed when running the installer (.exe file). It consists of the latest Long-Term Release (LTR) of QGIS, 3Di-specific plugins, third-party plugins, and some preconfigured settings.

.. _mi_3di_plugins:

3Di plugins
^^^^^^^^^^^

The following 3Di-specific plugins are included in the 3Di Modeller Interface. If any user interface component that the documentation refers to is missing, you most probably need to activate the plugin that provides the component: *Main menu* > *Plugins* > *Manage and Install Plugins...* > Check the box of the plugin that you need. 



- *3Di Models and Simulations* takes care of all communication with the 3Di API, performing tasks like creating new schematisations, uploading and downloading schematisation revisions, starting simulations, and downloading simulation results. It provides two user interface components: the 3Di Models & Simulations panel, and the 3Di Models & Simulations settings dialog.

.. note:: 
   The first time you use the 3Di Models and Simulations plugin, you need to :ref:`fill in some settings <setting_up_models_and_simulations>`.

- *3Di Schematisation Editor* allows you to view and edit schematisations. Its functionalities are provided through two user interface components: the 3Di Schematisation Editor toolbar, and the processing algorithms in the 3Di Schematisation Editor section of the Processing Toolbox. Note that a great deal of what this plugin does is integrated with QGIS features, such as attribute forms with special features, automatically setting snapping options, et cetera. The 3Di Schematisation Editor also provides a number of expressions, available in the expression builder.

- *3Di Results Analysis* provides all the tooling required for visualising and analysing computational grids and simulation results. Its features are available through the 3Di Results Analysis toolbar and the processing algorithms in the 3Di section of the Processing Toolbox. 

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no difference between the 3Di Modeller Interface and the Long Term Release version of QGIS. It is simply QGIS, but expanded with extra functionalities.

We have chosen QGIS as our supporting platform because of the following reasons:

- It enables seamless integration of 3Di-specific tasks with advanced GIS functionality

- QGIS comes with hundreds of powerful GIS processing tools

- It offers an extensive amount of styling options

- It has a highly customizable interface

- The option of building your own scripts, expressions, graphical models and plugins to interact with 3Di

- The fact that it is an open source platform

