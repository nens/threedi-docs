.. _3di_instruments_and_downloads:

Install and update manual
=========================

3Di Software requirements
---------------------------------

.. _software:

•	To be able to build, edit and run schematisations you need to install the Modeller Interface 
•	Our Live Site and Management Portal are optimized for chrome browser

.. note::

    Are you running into problems when downloading or updating the software? Please consult the 'problem solving' section and if the error and/or solution is not mentioned, please contact our support office (servicedesk@nelen-schuurmans.nl)
	

.. _MI_installation:

Installing the 3Di Modeller Interface
---------------------------------------

You can install the modeller interface simply with the download link below.

- Install the `Modeller Interface <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.28.5-1-5-Setup-x86_64.exe>`_

*last update: 10 March 2023*

The newest Modeller Interface also includes the newest versions of the 3Di plugins. If you would like, you could also upgrade the 3Di plugins from within the Modeller Interface manually. Follow the instructions of this movie to do so: `How to upgrade 3Di plugins in the Modeller Interface <https://www.youtube.com/watch?v=9XeVuZo28jw>`_.


.. _setting_up_models_and_simulations:

Setting up the 3Di Models and Simulations Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
   This step needs to be done just once.


When you start the 3Di Models & Simulations plugin for the first time, you are required to set a :ref:`personal_api_key` that will be used to log in. 
The QGIS Password Manager stores this Personal API Key securely (encrypted). 

.. note::
    If you have never used the QGIS Password Manager before, you will be asked to set a master password for the QGIS Password Manager. 
    Fill in a password and make sure you remember it. Check the box 'Store/update the master password in your Password Manager' so that you do not have to fill in the master password every time you start up QGIS. 

#) Open your Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the Models and Simulations plugin panel.
#)  Click 'Browse' and set a local working directory.
#) Click 'Obtain…' to obtain your :ref:`personal_api_key`. You will be redirected to the management page where you can `create a new Personal API Key <https://management.3di.live/personal_api_keys>`_. 
#) Create a new Personal API Key by pressing the '+NEW ITEM' button in the upper right corner.
#) Add a name for the new Personal API Key. Click on 'Submit' to the right.
#) You now have your own Personal API Key. Copy it (|Copy_button|).
#) Return to the Modeller Interface.
#) Click 'Set…' and paste your Personal API Key. Then press 'Save'.
#) You are now logged in and your name should appear after User. You can now easily **log out** by clicking on the cross.
#) And **log in** by clicking on the arrow.

You can now use all online functionalities of the 3Di Models & Simulations plugin. When logging in is required, the Personal API Key will be read from the QGIS Password manager and be used for logging in. 

.. |modelsSimulations| image:: /image/e_modelsandsimulations.png
    :scale: 90%
.. |Copy_button| image:: /image/e_copy_button.png
    :scale: 90%

.. _updating_plugin_schem_editor:

Updating the 3Di Schematisation Editor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To **update** to a newer version of the Schematisation Editor:

    #) Make sure that in Plugins > Manage and Install Plugins > Settings, the '*Show also experimental plugins*' box is checked

    #) Go to Installed plugins, click on 3Di Schematisation Editor and then '*Upgrade plugin*'




Advanced: separate installation of QGIS and appropriate plugins
----------------------------------------------------------------------

You can also install QGIS separately with the appropriate plugins. We only recommend this if you have specific reasons for this. 

- Install the Long Term Release (LTR) of QGIS, and install the 3Di toolbox and "3Di Models and Simulations" as QGIS plugins


.. _plugin_installation:

Plugin Installation
^^^^^^^^^^^^^^^^^^^^

* QGIS Standalone Installer Version 3.22 (Long term release). `Get QGIS <http://www.qgis.org/en/site/forusers/download.html#>`_ . 

    After the installation of QGIS, set the interface language and locale to American English. This makes it easier to understand the instructions in this documentation. Some locales do not support scientific notations of numbers, these are required for very small numbers (e.g. 1e-09).

    * Go to Settings > Options > General
    * Tick the box 'Override System Locale'
    * For User Interface Translation, choose 'American English'
    * For Locale, choose 'English UnitedStates (en_US)'
    * Restart QGIS

* QGiS 3Di plug-in specially designed for 3Di
	
	* 3Di Toolbox
	* 3Di Models and Simulations
	* 3Di Schematisation Editor - EXPERIMENTAL

The plugins work for:

- QGIS 3.22.x (LTR after March 2021)
- 64-bit version of QGIS (see below for more details)
- On Linux/OSX: install the following system dependencies: `python3-h5py python3-scipy python3-pyqt5.qtwebsockets`
- 3Di v2 results

To install the **3Di-Toolbox** plugin follow the steps below: 

1) Open QGIS and via the menu bar go to 'Plugins > Manage And Install Plugins'. 
2) Go to 'Settings'. 
3) Add a plugin repository
4) Fill in a name and copy the URL: https://plugins.3di.live/plugins.xml into the URL box. 
5) Go to 'All' and choose '3Di toolbox' from the list
6) Install the plugin.

.. figure:: image/d_qgispluging_pluginmanager.png
    :alt: QGIS Plugin Manager
    
.. figure:: image/d_qgispluging_pluginmanager_addlizard_repo.png
    :alt: Add Lizard repo Plugin

.. figure:: image/d_qgispluging_pluginmanager_install_toolbox.png
    :alt: Install 3Di Toolbox


To install the **3Di Models and Simulations** plugin follow the steps below: 

1) Open QGIS and via the menu bar go to 'Plugins > Manage And Install Plugins'. 
2) Go to 'Settings'. 
3) Add a plugin repository
4) Fill in a name and copy the URL: https://plugins.lizard.net/plugins.xml into the URL box. 
5) Go to 'All' and choose '"3Di Models and Simulations"' from the list
6) Install the plugin.
7) To active the panel of the"3Di Models and Simulations", choose plugins --> "3Di Models and Simulations" --> "3Di Models and Simulations". Now the panel will be available.


To install the **Schematisation Editor** plugin, follow the steps below:

1) Making sure that in the Plugins > Manage and Install Plugins > Settings the '*Show also experimental plugins*' box is checked;
2) Searching '*3Di Schematisation Editor*' in the Plugin Management Screen, and pressing the *Install Plugin* button.
3) Make sure that '*Enable macros*' is set to '*Always*' in Settings > Options > General > Project files. 


.. _plugin_settings:

Plugin settings
^^^^^^^^^^^^^^^^
To set the Base API URL:

1) Open QGIS and via the menu bar go to 'Plugins > "3Di Models and Simulations" > Settings'
2) Fill in a Base API URL. The Base API URL is in most cases https://api.3di.live. If you want to connect to our second calculation center in Taiwan, the base API URL is https://api.3di.tw/

.. deze links komen als dode links naar boven in de check, maar deze kloppen wel voor het invullen van de plugin instellingen :)



Information for system administrators
--------------------------------------

General information
^^^^^^^^^^^^^^^^^^^^

All applications make use of https traffic over port 443 with public signed SSL/TLS certificates.
If certificate errors show, please check any security software.
One way of testing this is by visiting https://api.3di.live/ in a browser and check the certificate.
If it is issued by R3, this is the certificate configured by us.
Any other name will point towards the security software in use.

.. VRAAG: deze website klopt niet. wat moet het zijn? -> aan wolf vragen. of het stukje tekst hierboven nog klopt.

.. _setup_modeller_interface:

3Di Modeller Interface
^^^^^^^^^^^^^^^^^^^^^^^^

This is a pre-configured version of QGIS (www.qgis.org), with some options switched off, different stylesheets, and some pre-installed plugins.
Two of these plugins (3Di Toolbox and "3Di Models and Simulations") are maintained by Nelen & Schuurmans.
QGIS itself and the other pre-installed plugins are not made / maintained by Nelen & Schuurmans.

Install instructions for the 3Di Modeller Interface can be found in :ref:`3di_instruments_and_downloads`.

Because the 3Di Modeller Interface is a customized QGIS,
we refer to the QGIS documentation when you run into any issues that are not specifically related to the plugins '3Di Toolbox' or '"3Di Models and Simulations"': 

* QGIS User Manual: https://docs.qgis.org/latest/en/docs/user_manual/
* Installation section in QGIS User Manual: https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#installing-qgis

**URLs accessed by 3Di Modeller Interface**

Make sure the 3Di Modeller Interface is allowed to communicate with following URLs:

* PyPI: https://pypi.org/ (only during first run after installation / update)
* 3Di API: https://api.3di.live (each time a simulation is started from the Modeller Interface)


Database
----------	

.. _database-overview:

Database overview
^^^^^^^^^^^^^^^^^^

The database overview shows the complete overview of tables that 3Di uses in the spatialite database. You can download the complete overview of tables that 3Di uses in the spatialite database :download:`here <pdf/database-overview.pdf>`. Also, this :download:`flowchart <image/flowchart_edit_model.png>` may help you while editing your model. The following links show you the database schema's for :download:`sewerage <pdf/database-schema-sewerage.pdf>` and :download:`surface water <pdf/database-schema-surface-water.pdf>`.

.. _empty_database:

Empty database
^^^^^^^^^^^^^^

If you like to set up a new model it may be helpful to start from an empty database. Download an empty spatialite database :download:`here <other/empty.sqlite>`.

Please be aware not to add any columns to existing tables in the spatialite as they may interfere with future migrations.
