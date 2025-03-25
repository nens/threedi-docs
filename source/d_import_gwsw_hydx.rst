.. _import_gwsw_hydx:

Import GWSW HydX
^^^^^^^^^^^^^^^^

The Urban Water Data Dictionary ('GegevensWoordenboek Stedelijk Water' or GWSW in Dutch) is an open standard for the unambiguous exchange and disclosure of data in urban water management. More information can be found on the `GWSW website <https://data.gwsw.nl/>`_.

The tool can be accessed by :ref:`activating the 3Di Processing Toolbox <3di_processing_toolbox>` > clicking '3Di' in the toolbox > 'Schematisation' > 'Import GWSW HydX'. 

You can use this processing algorithm to import a previously downloaded local dataset, or download a dataset directly from the server.

**Parameters:**

* **Target 3Di Schematisation**: Geopackage (*.gpkg) file that contains the layers required by 3Di. Imported data will be added to any data already contained in the 3Di schematisation geopackage.
* **GWSW HydX directory (local)**: Use this option if you have already downloaded a GWSW HydX dataset to a local directory.
* **GWSW dataset name (online)**: Use this option if you want to download a GWSW HydX dataset.
* **Destination directory for GWSW HydX dataset download**: If you have chosen to download a GWSW HydX dataset, this is the directory it will be downloaded to.

A log file will be created in the same directory as the Target 3Di Schematisation. Please check this log file after the import has completed.  
