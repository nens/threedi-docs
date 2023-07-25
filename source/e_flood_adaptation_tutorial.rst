Tutorial 5: Flood Adaptation measures
======================================

Introduction
-------------
Welcome to the tutorial for adding flood adaptation measures in your 3Di model during the simulation. In this tutorial, you will learn to work with the flood barrier tool and the raster editor tool in the 3Di live site. We will start with a spatialite database file (.sqlite) that is already filled in with a schematisation and a digital elevation model (DEM) raster. This file will be used to create your own version of the model in the modeller interface, which you will upload to the 3Di live site. After this you force discharge in a river, analyse the flood that this forcing causes and add adaptation measures to your 3Di model.


Learning objectives
--------------------
You will learn the following in this tutorial:

* Re-practice the workflow of creating a model from a sqlite.  
* Creating a template from a schematisation.
* Adding a flood barrier during a simulation. 
* Edit the raster of a model during a simulation. 


Preparation
-----------
Before you get started:

* Make sure you have a 3Di account. Please contact the :ref:`servicedesk` if you need help with this.
* Install the 3Di Modeller Interface installed, see :ref:`3di_instruments_and_downloads`.
* Download the dataset for this tutorial `here <https://nens.lizard.net/media/3di-tutorials/3di-tutorial-03.zip>`_.

Download the Taf dataset , which contains a digital elevation model (DEM) of Strand, which is a town in South Africa called dem_2m_LPB.tif and a spatialite database of the schematisation.

.. TODO: aan deze dataset komen!

.. Hier gebleven

Creating a new schematisation
-----------------------------
As we are building a schematisation from scratch, the workflow explained in Tutorial 1 will be used to initialize a new schematisation. If you haven't followed this tutorial yet, please do so before continuing this tutorial.
a.	Download the sqlite (link)
b.	Create a new schematisation from the spatialite in the modeller interface
Validate and upload your Schematisation to Generate a 3Di Model
Following the basic workflow (explained in Tutorial 1), we are now checking the Schematisation, uploading the schematisation to the 3Di Management screens and generate a 3Di model by:
1.	Pressing the Upload button in the Models & Simulations plugin.
2.	Clicking the New Upload button, followed by the Next button.
3.	Clicking the Check Schematisation button. This should result in no errors. If you did get a warning or error, please thoroughly check the preceding steps. Otherwise, click Next.
4.	Select Upload for the Spatialite and Terrain Model, fill in a commit message such as “Barrier Tutorial  <name>”, select UPLOAD AND PROCESS and click the Start Upload button.
After waiting for about 2 minutes, you should see the following window:
