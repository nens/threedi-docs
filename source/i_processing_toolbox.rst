.. COMMENT: This replaces "i_plugin_toolbox" 

.. _3di_processing_toolbox:

3Di Processing Toolbox
======================
The 3Di Processing Toolbox is an addition to the Processing Toolbox that is native for QGIS. It is a collection of different 3Di tools that can be used for various purposes. The 3Di Processing Toolbox is pre-installed in the Modeller Interface. You can find it by going to 'Processing' in the menubar and select 'Toolbox'. Alteratively, you can click |processing_toolbox_icon| in the attributes toolbar (or use the keyboard shortcut CTRL + ALT + T).


.. |processing_toolbox_icon| image:: /image/pictogram_processing_toolbox.png
	

Overview of the 3Di Processing Toolbox
--------------------------------------

.. figure:: image/i_3di_processing_toolbox.png 
	:alt: Toolbox Window
	:align: right
	:scale: 30% 
	
Most tools in the 3Di Processing Toolbox have built-in documentation to help you on your way.

**Computational Grid** 

	* **Computational grid from gridadmin.h5 file** generates the computational grid from a gridadmin.h5 file. *Note:* The :ref:`3di_results_manager` uses the same algorithm to visualise the computational grid.
	* **Computational grid from schematisation** generates the computational grid from a Spatialite.
	* **Detect leaking obstacles in DEM** detects obstacles such as dikes or elevated roads in the dem that are 'missed' by 3Di because they do not cover the entire edge of a calculation cell.
	* **Detect leaking obstacles in DEM (discharge threshold)** detects obstacles such as dikes or elevated roads in the dem that are 'missed' by 3Di because they do not cover the entire edge of a calculation cell. Additionally, you can add a cumulative discharge (the discharge threshold) to only look for 'leaks' with cumulative discharges of over 10 m\ :sup:`3`.

**Dry weather flow** 

	* **DWF Calculator** calculates the dry weather flow on connection nodes for a given schematisation and simulation settings. Produces a formatted csv that can be used as a 1D Lateral in simulations.

**Post-process results**

	* **Cross-sectional discharge** can be used to determine the total flow that passes a certain line. Any layer consisting of line-features can be used for this, e.g. the obstacles.
	* **Maximum water depth/level raster** can be used to create a raster with the maximum water depth/level over all timesteps. Because 3Di calculates using the volumes in a grid, calculating the water depth is done by interpolating the water levels and subtracting the DEM from the interpolated result. Additionally, you can generate the non-interpolated water level or depth raster. The resulting file can be stored in the temp folder of the Modeller Interface, or stored in any folder specified by the user. The resolution of the resulting map is equal to the resolution of the DEM. Please make sure to use the correct gridadmin file (downloaded with each simulation) with the corresponding DEM. 
	* **Water depth/level raster** works similar to determining the maximum water depth/level raster, with the difference being that you determine the water depth/level at a certain timestep (e.g. at the end of the rainfall event). Additionally, you can export the rasters for multiple timesteps in batch. For more information on how to generate water depth/level maps in batch we refer to the `QGIS documentation <https://docs.qgis.org/3.16/en/docs/user_manual/processing/modeler.html>`_.
	
	Use the :ref:`3di_results_manager` to analyse results in detail.

**Schematisation**

   * **Check Schematisation** checks the validity of your schematisation.
   * **Guess Indicators** estimates the correct values for pipe friction, manhole indicator and manhole area (only for NULL fields) with the overall option to only fill NULL fields.
   * **Import GWSW HydX** processing algorithm to import data in the format of the Dutch "Gegevenswoordenboek Stedelijk Water (GWSW)". For more information about GWSW HydX see `Stichting RIONED <https://www.riool.net/applicaties/gegevenswoordenboek-stedelijk-water/modulaire-opbouw-van-het-gwsw/gwsw-hyd>`_.
   * **Import Sufhyd** processing algorithm to import data in the format of a SUF-HYD.
   * **Migrate Spatialite** updates an old database schema to the current version


.. VRAAG: wat doet migrate spatialite? -> nog beter uitleggen.
