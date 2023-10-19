.. _howto_clip_schematisations:

Clip a schematisation
=====================

If you have a schematisation of a large area, but you want to do a detailed study of a small part of that area, it is often beneficial to clip the study area from the schematisation. In this *How to*, we go through the steps to take to achieve this.


Create a copy of the schematisation
-----------------------------------

#. Follow :ref:`these instructions<copying_existing_schematisation>` to copy the schematisation. You do not have to upload the data yet, you will first clip what you need.
#. :ref:`Load the schematisation<load_schematisation>` in your project.


Clip the rasters
----------------

First, you will need a polygon that delineates the study area for which you want to create a smaller schematisation. If you do not have this yet, create a new polygon layer (make sure to choose the same CRS as the DEM has) and digitize the study area polygon in the new layer. If you do have such a polygon, add this layer to your project; if this layer contains multiple polygons but you want to use only one as clipping polygon, select the polygon you want to use using the *Select* tool |selectionTool|.

Now you will clip all the rasters that are part of this schematisation using this clip polygon. 

#. Open the Processing Toolbox: *Main menu* > *Processing* > *Toolbox*. The *Processing Toolbox panel* opens.
#. In the search bar of the Processing Toolbox panel, search for the processing algorithm *Clip raster by mask layer*. This algorithm is available in the *GDAL* category. Double click the algorithm.
#. Use the following input arguments:
   - Input layer: Choose the Digital Elevation Model from the dropdown menu.
   - Mask layer: Choose the clip polygon layer. If the layer contains multiple polygons and you have selected the polygon you want to use, check the option *Selected features only*
   - Assign a specified nodata value to the output bands: -9999  
   - Check the option *Match the extent of the clipped raster to the extent of the mask layer*.
   - Check the option *Keep resolution of the input raster*
   - Under *Advanced Parameters* > *Profile*, choose *High compression*
   - Clipped (mask): Save the output file in the same location as the input raster, but add "_clipped" to the file name. For example, if the DEM filename is "C:\Users\your.name\3Di\Your copied schematisation\work in progress\schematisation\rasters\dem.tif", set the output file destination to "C:\Users\your.name\3Di\Your copied schematisation\work in progress\schematisation\rasters\dem_clipped.tif"
#. Click *Run*
#. After the algorithm has completed, click *Change parameters*.
#. Change the *Input layer* to the next raster of your schematisation (e.g. Friction)
#. Change the ouput filename (algorithm argument *Clipped (mask)*) accordingly
#. Click *Run*
#. Repeat this for all the schematisation's rasters

You now need to replace the original raster files in the directory of your copied schematisation with the clipped ones. This is only possible when none of the rasters are loaded in the 3Di Modeller Interface.

#. Remove all the clipped rasters from the project
#. Remove the schematisation from the project: in the :ref:`schematisation_editor_toolbar`, click *Remove 3Di model*.
#. In the :ref:`models_simulation_panel`, click the name of the schematisation (hyperlink). Windows Explorer opens in the directory where the schematisation is stored. 
#. Browse to *work in progress* > *schematisation* > *rasters*
#. Delete all the non-clipped rasters (e.g. dem.tif)
#. Rename all the clipped rasters to their original name (e.g. from dem_clipped.tif to dem.tif)

.. note::
   If you have made any mistakes, you can use the *History* option of the *Processing Toolbox* to open the processing algorithms you have used, with the arguments you provided. Change the arguments that were wrong and run again.

Clip the 1D network
-------------------

Now you will clip all the 1D network of this schematisation, including any 0D inflow objects connected to the 1D network. You will again be using a clip polygon. 

.. note::
   You may want to use a different clip polygon for the 1D domain than the one you used for for the 2D domain. We will delete all *Connection nodes* that are outside of the clip polygon, *and all features that reference these connection nodes*. E.g. a pipe that connects a connection node *in* the clip polygon to a connection node *outside* the clip polygon will also be deleted.

Go through the following steps:

#. :ref:`Load the schematisation<load_schematisation>` in your project.
#. Open the *Select by location* tool |selectByLocation|. Use the following inputs values:
   - Select features from: Connection node
   - Where the features: Check the *disjoint* box
   - By comparing features from: Choose your clip polygon layer. If the layer contains multiple polygons and you have selected the polygon you want to use, check the option *Selected features only*
   - Click *Run*
   - Click *Close*
#. In the *Layers* panel, in the group that contains the schematisation, go the the group *1D* and click on the layer *Connection node*
#. Click the *Toggle Editing* button to start an editing session
#. Click the *Delete selected* button to delete the connection nodes that are outside of the clip polygon
#. You will get a question about *Referenced features*. Click *Delete all referenced features*
#. Save your edits and stop the editing session
#. In the :ref:`schematisation_editor_toolbar`, click *Save to Spatialite*.

Clip 2D and 1D2D schematisation objects
---------------------------------------

There may still be 2D schematisation objects (2D laterals, 2D boundary conditions, obstacles, grid refinements, or DEM average areas) or 1D2D schematisation objects (Potential breach or Exchange line) present outside of the clip polygon. Use the same approach as with the connection nodes:

#. :ref:`Load the schematisation<load_schematisation>` in your project.
#. Select any features that are *disjoint* from the clip polygon
#. Delete these features from that layer

.. note::
   Grid refinements and obstacles outside of the DEM will simply be ignored, so it is not strictly required to delete them. Other 2D objects or 1D2D objects outside of the DEM may give errors.
   
Upload the clipped schematisation as the first revision
-------------------------------------------------------

Follow :ref:`these steps<uploading_schematisation>` to upload the clipped schematisation as the first revision of the schematisation you created.

.. note::
   In the commit message for this first revision, it is probably a good idea to include the name (and/or ID) of the schematisation that this new schematisation is a copy of, and which revision. E.g. "Copy of schematisation 'Some large area' revision #23, clipped on some small area".
   
.. |selectByLocation| image:: /image/pictogram_select_by_location.png
    :scale: 90%

.. |selectionTool| image:: /image/pictogram_qgis_select_tool.png
    :scale: 90%




