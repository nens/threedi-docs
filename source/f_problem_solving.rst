.. _f_problem_solving:

FAQ and problem solving
=======================

This section will help you solve some problems or errors that may occur when using 3Di.
Some issues are due to the software, these will be summarised in the section Known Issues, including a temporary solution.
Errors related to input data or other user settings are usually covered by the schematisation checker. In rare cases however they might not catch a potential issue.

- :ref:`faq`
- :ref:`known_issues`


.. _faq:

Frequently Asked Questions
--------------------------

- My 3Di API script doesn't work anymore, what do I need to do? 

*In case this is an old script (< 2022) please check the migration workflow available* `here <https://api.3di.live/v3/docs/migrate_to_threediapi/>`_. 

- How do I edit a simulation template?

*Simulation templates cannot be edited directly. In the 3Di Modeller Interface, start a new simulation based on the template, make the desired changes, and save the simulation as a new template. When using the 3Di API, create a new simulation from the template, make the desired edits, and create a new template from the simulation.*

- Can I change infiltration in a simulation template?

*No, infiltration is part of the schematisation. You can copy a schematisation and change the infiltration file there.
An explainer on schematisations and simulation templates can be found here* :ref:`basic_modelling_concepts`

- Why is the name of my simulation template 'default'? 

*The name is being read from the v2_global_settings table in the 'name' column. If that happens to be 'default', then that is the name of your simulation template.*

- What happens if I add an extra entry in the v2_global_settings table? 

*Extra entries will be ignored.*

- I have a variant of my schematisation that I like to test, what is the best way of doing so? 

*Copy/clone the schematisation, make your changes and upload it as a new schematisation.*

- My model shows unstable behaviour, what can I do to avoid this? 

First of all, instability is not common within 3Di, but certain settings or modelling choices can cause problems for the solver. 

*We have these tips:*

#) Make sure you have fixed all errors *and warnings* that the Schematisation checker gives. 
#) Decrease your calculation time step (background information: courant number)
#) Temporarily decrease your output time step . This makes it easier to analyse what goes wrong
#) Check if there are pump stations that are pumping to another 1D-node within the same 2D-computational cell
#) Put the 'pump_implicit_ratio' in the numerical settings to 1. This makes sure that the model calculates smoothly for pump stations (see :ref:`matrixsolvers` --> pump_implicit_ratio)


.. _known_issues:

Known issues
------------

.. _problem_solving_3di_mi:

3Di Modeller Interface
^^^^^^^^^^^^^^^^^^^^^^

3Di Modeller Interface keeps freezing at every click
""""""""""""""""""""""""""""""""""""""""""""""""""""

- In some cases, the 3Di Modeller Interface becomes very slow to respond to everything. This is usually caused by a known QGIS issue with the *Browser panel*. It occurs when QGIS cannot connect to all network drives. To resolve it, hide all network drives from the browser panel, as shown in the figure below.

.. figure:: image/f_qgis_hide_from_browser.png
    :alt: How to hide network drives from the Browser panel

Interflow in the Water balance tool
"""""""""""""""""""""""""""""""""""

The *Water Balance tool* does not support interflow yet. If your simulation includes interflow, the water balance may not be complete

Changing the 3Di Working Directory
"""""""""""""""""""""""""""""""""" 

The 3Di working directory can be changed as follows:

Via the 3Di Models & Simulations plugin settings (see below). 

.. figure:: image/f_changepluginsettings1.png
    :alt: Open the settings of 3Di Models and Simulations

.. figure:: image/f_changepluginsettings2.png
    :alt: Change the working directory of 3Di Models and Simulations	

3Di Modeller Interface in other languages than English
""""""""""""""""""""""""""""""""""""""""""""""""""""""

The 3Di Modeller Interface can be used in other languages than English. What matters is that the numbers notation is set to English. There is a bug in QGIS with scientific notations and Dutch number notations which can cause unexpected behaviour. This may also apply to number locations in other locales.  
Please go to *Settings* > *Options* > *General* and set *Locale (numbers, date and currency formats)* to *en_GB*.


SSLError (HTTPSConnectionPool(host='api.3di.live', port=443): Max retries exceeded with url ...)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In some cases the 3Di Models and Simulations plugin (part of the 3Di Modeller Interface) can give a generic SSLError on a Windows system (see figure below).
To solve this issue, please contact your organisation's system administrator.
Instructions for your system administrator on how to solve this problem are given below the figure::

  Error: HTTPSConnectionPool(host='api.3di.live', port=443): Max retries exceeded with url: /v3/auth/token/ (Caused by SSLError(1, 'A failure in the SSL Library occurred (_ssl.c:1129)')))

.. figure:: image/f_ssl_error_qgis.png
    :alt: Screenshot of the error

This error is resulting from a combination of how the plugin validates SSL/TLS certificates and how Windows expects that to happen.
We are using Let's Encrypt as our certificate supplier for most of our 3Di webservices.
In September 2021 their root certificate 'DST Root CA X3' expired and was replaced by the 'ISRG Root X1' certificate.
All of the Let's Encrypt domain name certificates are issued by Intermediate Certificate 'R3'.
There are some cases where this Intermediate Certificate is still issued by 'DST Root CA X3', and this can create issues.

To solve this, please open a Microsoft Management Console (mmc.exe) and add the Certificates Snap-In for the user.

.. figure:: image/f_mmc_certificates_snapin.png
    :alt: MMC Certificates Snap-In

Open the "Intermediate Certification Authorities" and then the "Certificates" folder.
Find the 'R3' Intermdiate Certificate, and check who the issuer is.
If this is only 'DST Root CA X3', please remove it and visit https://api.3di.live/v3 with a browser.

Please contact our :ref:`servicedesk` after this fix is applied and are still receiving the error message.


3Di Live
^^^^^^^^

- If a raster has a nodatavalue of 3.4028234663852886e+38 will not be visible in 3Di Live. Setting it to -9999 will solve the issue. This can be done using QGIS tooling or the following GDAL command: ``gdalwarp -of GTiff -srcnodata 3.4028234663852886e+38 -dstnodata -9999 -co "COMPRESS=DEFLATE" dem1.tif dem2.tif``

- In rare cases the waterdepth interpolation in 3Di Live may show unexpected behaviour; it shows triangular patterns. These deviations are only visual, so the results are still correctly. 


3Di Management
^^^^^^^^^^^^^^

I can't find the 3Di Model I am looking for
"""""""""""""""""""""""""""""""""""""""""""

Please check the following:

- Do you have access to the organisation to which the 3Di model belongs

- Does the schematisation have a 3Di model? Someone may have deleted it, in which case you need to regenerate it. Go to `management.3di.live <https://management.3di.live>`_, search for your schematisation and check out the details page. 


Crashed simulations
^^^^^^^^^^^^^^^^^^^

ERROR - F - Matrix diagonal element, near zero
""""""""""""""""""""""""""""""""""""""""""""""

At one calculation point there is no storage area or the wet cross section area is near zero or even negative. This may be caused by various reasons listed below:

* Structure levels are below cross section reference levels, f.i. a culvert below the bed level. This is not possible as when water level drops below the bed level, flow through the culvert has no area to flow to. Update reference or structure levels so that they match. Reference levels can be below structure levels.

* A lateral inflow from laterals or an inflow surface is connected to a node without storage area, f.i. an pump end node or boundary node. Removes laterals or inflow from these nodes.

* Water level boundary is below structure level.

* All definition values for width and height must be positive.

* Pump start level is below pump stop level.

The error is followed by a reference to the node without any storage or link without wet cross section area. This will look something like::

    near zero, aii(nod)<1.0d-10,nod,aii(nod),su(nod)  14614   14439  0.0000E+00  0.0000E+00

The first number (14614 in this example) refers to the calculation node on which the error occurs. This number can be found using the QGIS plugin when a result of this model is available. The number can be located using the *node_results*. The id's in this table match the one given here. The second number is a link id and can be found using the *line_result* layer.

ERROR - F - Impossible line connection at calculation node:            729
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This error may occur when using embedded in combination with structures. Make sure no structure is placed entirely inside a 2D computational cell. You can only check this when you have a copy of the 2D computational grid. You can obtain this by making a purely 2D model of your DEM and grid refinement of try making one using the 'create grid' function in the QGIS processing toolbox.

Runtime Error: NetCDF: String match to name in use
""""""""""""""""""""""""""""""""""""""""""""""""""

Check the aggregation NetCDF name settings, names must be unique.


.. _current_schematisation_checks:

List of checks run by the schematisation checker on the schematisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are the checks performed by the schematisation checker.
The checks are listed in the order in which they are run.
The beta checks are for testing purposes only, and not performed in normal usage.

.. include:: i_current_schematisation_checks_table.rst