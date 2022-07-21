.. _tutorial1_workflow:

Tutorial 1: Workflow of creating a 3Di Schematisation and a 3Di Model
===============================================================
Since :ref:`klondike_release`, when the Klondike release took place, the complete workflow of creating a schematisation and 3Di Model takes place within the Modeller Interface.
This tutorial will guide you through this workflow.
We will use a simple model of the Laugharne and Pendine Burrows in the United Kingdom. The burrows enclose a 
flat area of reclaimed salt marshes that are currently used as farmland. Whilst this tutorial represents a 
real-world area, it is important to keep in mind that the model is greatly simplified for the purpose of this 
tutorial. 

Requirements
------------

* Having the 3Di Modeller Interface, or a custom QGIS with the Models and Simulations plugin, installed. Check out the :ref:`3di_instruments_and_downloads` if you do not have the most recent version installed.

* Having access to the 3Di :ref:`management_portal`.

* Having a copy of the Digital Elevation Map (DEM) for the Burrows area saved locally, which can be downloaded `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-01.zip>`_.


Creating a Schematisation
-------------------------
A schematisation basically exist of a Spatialite and rasters. A spatialite is a database with a .sqlite extension, which contains the settings and feature data of your schematisation. 
To create a new schematisation:

#) Open your Modeller Interface and click on the 3Di Models and Simulations icon (|modelsSimulations|). You should now see the Models and Simulations plugin panel.

#) Click the New button (|newschematisation|) and fill in a **unique** schematisation name, such as 'Burrows_tut1_<yourname>', optionally one or more tags, and select an organisation. The schematisation will be saved on name of this selected organisation. Since we are creating a schematisation from scratch, the Create new Spatialite option should be selected for the Spatialite option. 

#) Click next twice.

#) Fill in the folowing values as schematisation settings:


.. note::
    Select the downloaded DEM for the Digital elevation model field.

.. figure:: image/tut1_schem_settings.png
    :scale: 75%

    The settings for your new schematisation.


The schematisation will be saved in your Modeller interface root folder, under the folder with your new schematisation name > work in progress > schematisation.
Here you will find your sqlite file and a raster folder with, in this case, only a .tif file of your DEM.
The schematisation should also be selected in your 3Di Models and Simulations Plugin.

Adding the schematisation to your QGIS project
----------------------------------------------
In order to upload the new schematisation to the management screens, the sqlite has to be loaded into your Modeller Interface.
This can be done by clicking the 'Select 3Di results' button (|addresults|) and selecting the sqlite at the above mentioned file location.

.. note::
    Please note that, so far, your schematisation only contains the minimum required information to be uploaded to the management screens.
    Now that your sqlite has been imported to your modeller interface, your schematisation can be extender. This, however, falls outside the scope of this tutorial.



Uploading the Schematisation
----------------------------
Follow these steps to upload the schematisation to the management screens:

#) Press the upload button (|upload|) in the Models and Simulations plugin.

#) Click on 'New Upload' in the window that has popped up and click 'Next'.

#) Press the 'Check Schematisation' button, which controls whether your spatialite and Rasters are valid to upload. During this tutorial, this should give no warnings nor errors.

#) Continue by going to the next screen. Here you have to fill in a commit message. "First commit" is the conventional way of describing the first commit of a new schematisation. Later on, when you want to upload newer versions of your schematisation (so-called Revisions), it is a good-practice to enter detailed information about the changes that you have made.

#) The default settings of this window are to upload the Schematisation and process it to generate a 3Di Model. Select UPLOAD ONLY if you do not need a 3Di Model.

#) Once the progress bar is complete, your schematisation should be visible in the management screens. If you selected UPLOAD AND PROCESS, the newly generated 3Di Model can be found in both the management screens and the 3Di Livesite.



.. |modelsSimulations| image:: /image/modelsandsimulations.PNG
    :scale: 90%

.. |newschematisation| image:: /image/newschematisation.PNG
    :scale: 90%

.. |addresults| image:: /image/addresults.PNG

.. |upload| image:: /image/tut1upload.PNG
    :scale: 90%