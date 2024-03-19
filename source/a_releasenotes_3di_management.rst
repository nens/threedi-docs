.. _release_notes_MS:

3Di Management
--------------

January 11, 2024
^^^^^^^^^^^^^^^^

- Search and filter options were added to the 3Di models overview (#1382)

- The filters that are set on pages that list models, schematisations, or simulations are now also applied when using "Export to Excel" (1184)

- On the simulation overview page, all initials and events are listed (#1327)

- You can now search for simulations by simulation ID (#239)

- Include organisation in 3Di Management URLs, so that it is easier to share URLs (#1451)

- The user interface for "add tags" has been improved (#1504)

- Bugfix: Visualise negative laterals correctly on the simulation detail page (#1389)

- Bugfix: "Run on 3Di Live" uses the wrong template is multiple templates are available for the 3Di model (#1329)

- Bugfix: Revision nr. column now correctly displays revision numbers > 99 (#1417)

- Bugfix: Wind events were not visualised correctly for long simulations in some cases (#934)


October 18, 2023
^^^^^^^^^^^^^^^^
- The simulation overview page now shows which post-processing options have been used (#814)

- You can now post-process results in Lizard for finished simulations. This option can be used if no post-processing for this simulation has been done and the raw results are still available, i.e., within 7 days after the simulation was finished. (#835, #1249, #1160)

- The "Export to Excel" option for Simulations and 3Di Models now downloads all items, not just the ones that are shown on the page (#1040)

- Simulations can now be removed from the queue (#780)

- If you do not have management rights, the *Users* button is disabled; it will now show a list of users in your organisation that have management rights when hovering over it (#852)

- You can now select multiple 3Di models, schematisations, and/or revisions and delete them all at once, including in the *Choose other revision* window on the schematisation detail page (#815, #1228)

- Schematisations can be moved to a different organisation, if you have *Creator* or *Manager* rights for the organisation that currently owns the schematisation *and* the organisation to which you want to transfer it (#234)

- Multiple improvements were made to the 3Di model overview, especially for organisations with more than 250 3Di models (#231, #227)

- The simulation ID is now shown in the simulations overview (#233)

- Bugfix: Links in *queued simulations* list were wrong, this has been fixed (#781)

- Bugfix: Schematisation detail page: not all info was updated when switching to another revision (#1158)


.. _3di_ms_release_20230921:

September 21, 2023
^^^^^^^^^^^^^^^^^^

- Redesign of the *Schematisation details* page (#741)
  - Schematisation name can be edited
  - Schematisations now have a *Description*, which can be edited. Note: in the near future, you will also be able add a schematisation-level description when creating a schematisation in the 3Di Modeller Interface.
  - Commit message can be edited
  - Tags can be edited
  - 3Di model names can be edited
  - Simulation template names can be edited
- It has become easier to delete revisions and schematisations. When a revision is deleted, its 3Di Model is also automatically deleted. When a schematisation is deleted, its revisions are also automatically deleted. 
- Added "Delete schematisation" button in the schematisation section. This deletes the schematisation, which cascades to deletion of its revisions and 3Di models.
- Make simulation name editable on simulation detail page (#792)
- Schematisation revision detail page: show available saved states (#855)
- Simulation overview page - forcings: show two decimals (#813)
- Filter live statuses by organisation (#935)
- *Export to Excel file* on the *Simulations* and *3Di Models* overview pages now exports *all* items instead of only the listed items. #1040
- Bugfix: "Has 3Di Model" column not updated after model deletion (#686)


.. _3di_ms_release_20231807:

June 18th 2023
^^^^^^^^^^^^^^

- User management is now available on 3Di management if you have Manager rights
- Vegetation rasters are now included in schematisation revision overview
- Add time zone (UTC offset) when listing start or end datetime of simulation
- "Export to Excel file" button on schematisations page now downloads all schematisation names, and shows a modal with a progress bar
- Schematisation detail page: Disable "run in 3Di Live" option if 3Di Live is not part of contract
- Schematisation list no longer shows schematisations that have no revisions, unless you explicitly choose this option
- Bugfix: On the schematisation revision detail page, Some raster download links did not work
- Bugfix: On the schematisation revision detail page, "Predefined simulation data" section had wrong contents
- Bugfix: On the schematisation revision detail page, rasters where only listed after a 3Di model had been created


March 20th 2022
^^^^^^^^^^^^^^^^^^

- improved placement of data, using the correct definition of schematisation, simulation and model
- show current number of license and how many are in use
- show max allowed number of models
- show an error message when a simulation template fails to be created
- removed graphs from levee element


November 21th 2022
^^^^^^^^^^^^^^^^^^

- See the complete commit message in the revision overview when hovering
- This overview now also shows for which revisions a 3Di model is available

.. image:: /image/management_screen_schematisation_commit_message_when_hovering.png
   :alt: You can now see the commit message when hovering.

- When clicking on a simulation template, the link now is directed to the details page of the simulation where the template was based upon. Showing the events in the simulation template.
- Added a save as template button to simulations detail page

.. image:: /image/management_screens_save_as_template.png

- Shows queued simulations:

.. image:: /image/management_screens_queued_simulations.png

- Regenerating a model that is active now gives a clear error message

.. image:: /image/management_screens_regenerating_active_model_gives_clear_error_message.png

- If a project tag is added to a simulation it will be shown


February 2022 (Klondike) v2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-	Fixed a bug where the models map page stayed empty if there were no models
-	Fixed a bug where a schematisation that has no revisions yet showed an empty page
-	Add information about the current framework version, so the user knows if the current 3Di model is up to date
-	Show model id as well as name on the models list page
-	The gridadmin.h5 file can now be downloaded from the model detail page as well as from the simulation results download
-	Simulation templates can now also be deleted
-	The information on the models list page can be exported as an Excel file
-	Generating a model can fail if the schematisation already has the maximum number; show an error message if this happens.
-	Add a column for 'latest revision' to the Schematisations table.
-	Instead of subpages, now everything is reachable from the front page


February 2022 (Klondike)
^^^^^^^^^^^^^^^^^^^^^^^^

3Di Management has been extended with a Models section. In this Models section users can:

For 3Di Models

- See an overview of Models in a list
- See an overview of Models in the map
- Per Model a detailed page is available including the location on the map, size of the Model.
- Per Model is an option to run the simulation on 3Di Live
- On the detailed Model page there is an option to run the simulation on 3Di Live
- On the detailed Model page there is an option to delete the model
- On the detailed Model page there is an option to re-generate the model from the schematisation
- A history of simulations performed with the 3Di Model
- An overview of available simulation templates. By default 1 simulation template is available for every Model. This is generated based on the spatialite. The name of the simulation template is the name in the v2_global_settings table.

For schematisations users can:

- See all available schematisations in a list.
- See past revisions of a schematisation
- Generate a 3Di Model from a schematisation or re-generate an existing model from the schematisation. Keep in mind that doing so will remove additionally generated templates


