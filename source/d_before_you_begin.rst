.. _before_you_begin:

Before You Begin
================

The tutorials below are aimed at giving you some examples on how to use, modify or create your 3Di models. They show you how to create different types of models for different purposes or add elements to existing models. The first tutorials aim to give you an introduction to 3Di as well explaining some basic steps. They therefore explain the steps and reasons behind them quite extensively. The later tutorials assume you have sufficient knowledge about 3Di and modelling in general. They are less extensive and can be used as cheat sheets for performing different tasks.

All tutorials assume you have some knowledge of 3Di and have access to QGIS, the 3Di QGIS plugin, Google Chrome and TortoiseHG. They also assume that your organization has uploaded one or more 3Di models for use in the 3Di portal. For a complete overview of the software required, check the software section.

Before you begin consider the following.

.. _software:

Software
--------

To use 3Di you need these software packages:

* Recent version of Google Chrome (`Get Chrome <https://www.google.nl/chrome/browser/desktop/index.html>`_)

* The `Modeller Interface <https://docs.3di.lizard.net/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.4.13-1-Setup-x86_64.exe>`_ or install QGIS with the appropriate plugins. For more details on how to do this see :ref:`plugin_installation`

* Recent version of TortoiseHG (`Get TortoiseHG <https://tortoisehg.bitbucket.io/download/index.html>`_)

    After installation of TortoiseHG the program can be started by selecting the TortoiseHg Workbench program from the Windows Start menu. In a first use, activate the 'large files extension' by selecting from the File menu 'Settings' and then' Extensions' and select 'large files’. Also fill in your name. Press OK and restart TortoiseHG.

.. figure:: image/d_tortoise_extensions.png
	:scale: 75%
	:alt: Extensions
..

    Tortoise also has a built-in encrypted password manager, allowing you to push and pull revisions without being prompted for your username and    password each time. To enable the password manager:

    * Open TortoiseHg Workbench
    * Go to File > Settings > Extensions
    * Check the box 'mercurial_keyring'.
    * Restart TortoiseHg Workbench
    * Now you still have to enable the password manager for each repository you clone, see :ref:`download-repository`



Web Portals
-----------

* checkout https://3diwatermanagement.com/3di-start/ for a up-to-date overview of all available 3Di portals

* <your-organisation>.lizard.net to view and download saved simulations



.. _database-overview:

Database overview
-----------------

The database overview shows the complete overview of tables that 3Di uses in the spatialite database. You can download the complete overview of tables that 3Di uses in the spatialite database :download:`here <pdf/database-overview.pdf>`. Also, this :download:`flowchart <image/flowchart_edit_model.png>` may help you while editing your model. The following links show you the database schema's for :download:`sewerage <pdf/database-schema-sewerage.pdf>` and :download:`surface water <pdf/database-schema-surface-water.pdf>`.

.. _empty_database:

Empty database
--------------

If you like to set up a new model it may be helpful to start from an empty database. Download an empty spatialite database :download:`here <other/empty.sqlite>`.

Please be aware not to add any columns to existing tables in the spatialite as they may interfere with future migrations.