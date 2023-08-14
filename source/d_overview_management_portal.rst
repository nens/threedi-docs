.. _management_screens_manual:

Overview 3Di Management
=======================

To use 3Di Management, open your browser and go to https://management.3di.live and log in with your username and password. If you do not have a 3Di account yet, or do not know your username and password, please contact the :ref:`servicedesk`.

After logging in to 3Di Management, there are several possibilities:

* :ref:`3di_management_schematisations`
* :ref:`3di_management_models`
* :ref:`3di_management_api_key`
* :ref:`3di_management_users`
* :ref:`3di_management_simulations`
* :ref:`3di_management_live_status`

.. figure:: image/b_managementportal.png
   :alt: 3Di Management homepage
   :scale: 60%

   The homepage of 3Di Management.

In the top right, you can change organisations if you have access to multiple organisations. 
You can log out by clicking *<your user name>* > *Logout* in the top right.


.. _3di_management_schematisations:

Schematisations
===============
If you click the *Schematisations* tile in the overview, you will see a list of all :ref:`schematisations <schematisation>` within your organization. This list of schematisations can be exported to an Excel file.

You can find a specific schematisation by searching its Name, Tag, or Creator using the search bar. Once you locate the desired schematisation, you can click on its name to open the detailed view. In this detailed view, you have the following options:

- View all information related to the :ref:`threedimodel`.
- Verify the IDs.
- Select a different revision.
- Review the history of simulations conducted with this schematisation.
- Download the SQLite file and rasters.
- Generate or regenerate a 3Di model and track its progress.
- Delete the schematisation, its revisions, associated models (note: all revisions must be deleted first), and simulation templates.
- Explore the simulation templates connected to the schematisation.


.. _3di_management_models:

Models
======
When you click the *Models* tile in the overview, you will be presented with a list of all :ref:`models <threedimodel>` associated with your organization.

These models can be visualized on the map within the map view. Furthermore, the list of models can be exported to an Excel file, which can prove useful if you intend to manage your 3Di models more efficiently."

.. _3di_management_api_key:

Personal API Key
================
When you click the *Personal API Key* tile in the overview, you will be presented with a list of all the Personal API keys associated with your organisation. You have the ability to *Revoke* keys that are no longer in use. If you need to generate a new Personal API Key, follow these steps:

1. Click *+New Item*.
2. Provide a name for the key.
3. Click *Submit*.
4. Once submitted, you can copy the generated key for your use.


.. _3di_management_users:

Users
=====
When you click the *Users* tile in the overview, you will access a list of all the users associated with your organisation along with their respective roles:

- *Viewer*: This role is capable of reading data and monitoring simulations.
- *Simulation Runner*: This role has the authority to read data and execute simulations.
- *Creator*: Users with this role possess the ability to read data and make modifications such as adding, altering, or removing schematizations and 3Di models.
- *Manager*: Users holding this role are empowered to manage users by performing tasks such as addition, modification, or removal.

.. _3di_management_simulations:

Simulations
===========
When you click the *Simulations* tile within the overview, you will be presented with a comprehensive list of all :ref:`simulations <simulation_and_simulation_templates>` associated with your organisation. This list provides insights into various aspects of the simulations:

- *Name*: This denotes the name of the simulation.
- *Model*: It reveals the name of the corresponding schematization.
- *User*: This field displays the user responsible for initiating the simulation.
- *Status*: Here, you can discern the simulation's status (finished/crashed).
- *Type*: This indicates the platform used for conducting the simulation (live/api).
- *Tags*: Tags assigned to the simulation for categorization.
- *Started*: The date when the simulation was initiated (dd/mm/yyyy).
- *Length*: The duration of the simulation.
- *Project*: The project to which the simulation is associated.

To locate a specific simulation, you can perform a search based on the Simulation name, Model name, or Username using the search bar. You also have the option to fine-tune your search using the checkboxes beneath the search bar:

- *Only show my own simulations*: This filters the list to display simulations executed by you.
- *Only API simulations*: This narrows down the list to show simulations executed through the Modeller Interface.
- *Only live site simulations*: This displays simulations conducted via 3Di live.
- *Hide crashed simulations*: This excludes simulations that experienced crashes.

Once you find the desired simulation, clicking on its *Name* will open an overview. Within this overview, you have the following capabilities:

- Download the simulation results.
- Navigate to the corresponding model for which the simulation was conducted.
- View the initial conditions and events of the simulation.
- Save the simulation as a template for future use.



.. _3di_management_live_status:

Live status
===========
When you click on the *Live status* tile in the overview, you will be presented with an overview containing the following information:

- The current number of licenses being utilized by your organization.
- The count of simulations that are currently queued.
- The number of simulations that are actively running at the moment.
- Simulations that have completed while you were browsing this page.