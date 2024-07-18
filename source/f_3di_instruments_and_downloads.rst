.. _3di_instruments_and_downloads:

Install and update manual
=========================

.. note::

    Are you running into problems when downloading or updating the software? Please consult the :ref:`problem solving<problem_solving_3di_mi>` section. If the error and/or solution is not mentioned, please contact our :ref:`servicedesk`
	

.. _MI_installation:

Installing the 3Di Modeller Interface
---------------------------------------

To install the 3Di Modeller Interface, download the and execute the `3Di Modeller Interface Installer <https://docs.3di.live/modeller-interface-downloads/3DiModellerInterface-OSGeo4W-3.34.5-1-3-Setup-x86_64.exe>`_


.. _setting_up_models_and_simulations:

3Di Models and Simulations settings (first use)
-----------------------------------------------

When you start the 3Di Modeller Interface for the first time, you need to set two configuration settings:

* :ref:`personal_api_key` to be able to use the online functionalities of 3Di. The QGIS Password Manager stores this Personal API Key securely (encrypted).
* Working directory to store schematisations and simulation results. It is strongly recommended to use a directory on your local drive, not a shared drive.

.. note::
    If you have never used the QGIS Password Manager before, you will be asked to set a master password for the QGIS Password Manager. 
    Fill in a password and make sure you remember it. Check the box 'Store/update the master password in your Password Manager' so that you do not have to fill in the master password every time you start up QGIS. 

#) Open the 3Di Modeller Interface 
#) Click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the 3Di Models and Simulations Settings dialog.
#) The *Base API URL* default is https://api.3di.live. Change this if you want to connect to one of our other calculation centers. E.g., for Taiwan, the base API URL is https://api.3di.tw/
#) Click *Browse* and set a local working directory.
#) Click *Obtain...* to obtain your :ref:`personal_api_key`. You will be redirected to the management page where you can `create a new Personal API Key <https://management.3di.live/personal_api_keys>`_. 
#) Create a new Personal API Key by pressing the *+ NEW ITEM* button in the upper right corner.
#) Fill in a name for the new Personal API Key. Click on 'Submit' to the right.
#) You now have your own Personal API Key. Copy it.
#) Return to the 3Di Modeller Interface.
#) Click *Set…* and paste your Personal API Key. Then click *Save*.
#) You are now logged in and your name should appear next to User. You can now easily **log out** by clicking on the cross.
#) And **log in** by clicking on the arrow.

You can now use all online 3Di functionalities of the 3Di Modeller Interface. When logging in is required, the Personal API Key will be read from the QGIS Password manager and be used for logging in. 

.. |modelsSimulations| image:: /image/pictogram_modelsandsimulations.png
    :scale: 90%


.. _updating_plugin_schem_editor:

Updating the 3Di Modeller Interface
-----------------------------------

The 3Di Modeller Interface consists of two parts: QGIS and 3Di plugins. Each of these components has to be updated in a different way. The 3Di Modeller Interface is based on the long-term release (LTR) version of QGIS. The LTR is updated **annually**, in March. It is recommended to re-install the :ref:`3Di Modeller Interface<MI_installation>` every year at the end of March.

.. note:
   Updating the 3Di Modeller Interface will **not** update any plugins. QGIS plugins are installed in the *User Profile* folder, which is not removed when updating QGIS.

The :ref:`mi_3di_plugins` can be updated in the following way:

#) Start the 3Di Modeller Interface
#) If any schematisation is loaded, click *Save to Spatialite* and then *Remove 3Di model*
#) In the main menu click *Plugins* > *Manage and Install plugins*
#) At the left side, click *Installed*
#) Plugins that can be updated are shown in **bold**
#) Click the plugin name. At the bottom right, click *Upgrade plugin*
#) Updating the 3Di Results Analysis plugin requires a restart of the 3Di Modeller Interface. Do this when prompted.
#) Do **not** use *Open 3Di GeoPackage* the first time you load your schematisation after having upgraded all 3Di plugins. Use *Load from Spatialite* instead.

.. note:
   If you update a 3Di plugin, make sure to update all at once.
   
Advanced: separate installation of QGIS and 3Di plugins
-------------------------------------------------------

You can also install QGIS separately with the appropriate plugins. We only recommend this if you have specific reasons for this. Do the following:

* QGIS Standalone Installer (Long term release). `Get QGIS <http://www.qgis.org/en/site/forusers/download.html#>`_ . 

    After the installation of QGIS, set the interface language and locale to American English. This makes it easier to understand the instructions in this documentation. Some locales do not support scientific notations of numbers, these are required for very small numbers (e.g. 1e-09).

    * Go to Settings > Options > General
    * Tick the box 'Override System Locale'
    * For User Interface Translation, choose 'American English'
    * For Locale, choose 'English UnitedStates (en_US)'
    * Restart QGIS

.. note:
   The 3Di plugins are tested for the version of QGIS that is installed with the 3Di Modeller Interface installer (usually the latest Long Term Release version of QGIS). If they also work for older or newer versions of QGIS, congrats, it is your lucky day :).

* Add the 3Di plugin repository
    * In the main menu click *Plugins* > *Manage and Install plugins* > *Settings* 
    * In the section *Plugin repositories*, click *Add*
    * As details, fill in '3Di' as *Name*, and 'https://plugins.3di.live/plugins.xml' as *URL*

* Install the 3Di plugins: in the tab *All*, install the :ref:`mi_3di_plugins`. Restart QGIS when prompted.

* Enable macros
    * Make sure that *Enable macros* is set to *Always* in Settings > Options > General > Project files. 

.. note: 
    On Linux/OSX: install the following system dependencies: `python3-h5py python3-scipy python3-pyqt5.qtwebsockets`


Information for system administrators
--------------------------------------

General information
^^^^^^^^^^^^^^^^^^^^

All applications make use of https traffic over port 443 with public signed SSL/TLS certificates.
If certificate errors show, please check any security software.
One way of testing this is by visiting https://api.3di.live/v3.0/ in a browser and check the certificate.
If it is issued by R3, this is the certificate configured by us.
Any other name will point towards the security software in use.

.. _setup_modeller_interface:

3Di Modeller Interface
^^^^^^^^^^^^^^^^^^^^^^^^

The 3Di Modeller Interface is a customized version of QGIS, shipped with several pre-installed plugins and settings, see :ref:`mi_technical_setup`. Its :ref:`mi_3di_plugins` are maintained by Nelen & Schuurmans. QGIS itself and the other pre-installed plugins are not made / maintained by Nelen & Schuurmans.

Install instructions for the 3Di Modeller Interface can be found in :ref:`MI_installation`.

Because the 3Di Modeller Interface is a customized QGIS,
we refer to the QGIS documentation when you run into any issues that are not specifically related to the 3Di plugins: 

* QGIS User Manual: https://docs.qgis.org/latest/en/docs/user_manual/
* Installation section in QGIS User Manual: https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#installing-qgis

**URLs accessed by 3Di Modeller Interface**

Make sure the 3Di Modeller Interface is allowed to communicate with following URLs:

* 3Di API: https://api.3di.live/v3.0/ (each time a simulation is started from the Modeller Interface)
