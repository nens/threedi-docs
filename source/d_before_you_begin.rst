.. _before_you_begin:

Before You Begin
================

Before you begin consider the following.

Software
--------

To use 3Di you need these software packages:

* Recent version of Google Chrome (`Get Chrome <https://www.google.nl/chrome/browser/desktop/index.html>`_)

* QGIS 2.14 64bit (`Get QGIS <http://www.qgis.org/en/site/forusers/download.html#>`_)

* QGiS 3Di plug-in specially designed for 3Di (`Get 3Di plug-in <https://github.com/nens/threedi-qgis-plugin/wiki>`_)

* Recent version of TortoiseHG (`Get TortoiseHG <https://tortoisehg.bitbucket.io/download/index.html>`_)

After installation of TortoiseHG the program can be started by selecting the TortoiseHg Workbench program from the Windows Start menu. In a first use, activate the 'large files extension' by selecting from the File menu 'Settings' and then' Extensions' and select 'large files’. Also fill in your name. Press OK and restart TortoiseHG.

.. figure:: image/d_tortoise_extensions.png
	:scale: 75%
	:alt: Extensions

Web Portals
-----------

You can use 3Di through the following web portals:

* 3di.lizard.net to make simulations with 3Di models

* 3di.lizard.net/models to configure your model revisions

* models.lizard.net to find existing or add new repositories

* <your-organisation>.lizard.net to view and download saved simulations

.. _database-overview:

Database overview
-----------------

The database overview shows the complete overview of tables that 3Di uses in the spatialite database. You can download the complete overview of tables that 3Di uses in the spatialite database :download:`here <pdf/database-overview.pdf>`. Also, this :download:`flowchart <image/flowchart_edit_model.png>` may help you while editing your model. The following links show you the database schema's for :download:`sewerage <pdf/database-schema-sewerage.pdf>` and :download:`surface water <pdf/database-schema-surface-water.pdf>`.

Empty database
--------------

If you like to set up a new model it may be helpful to start from an empty database. Download an empty spatialite database :download:`here <other/empty.sqlite>`.