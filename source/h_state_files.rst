.. _state_files:

State files
===========

During a 3Di computation, the user can choose to save a state of a 3Di simulation. This state can be used in future simulations as an initial condition. The state file contains a snapshot complete flow condition of the model.

A save state assists the user in:

1. A correct initial condition, for speeding up simulations and consistent scenario comparisons. 

2. Defining a “warm state” in a operational setting. It allows the computations to continue a simulation from a previous run.

Choices in saving a state file
------------------------------

3Di allows the user to choose when to save a state and thereby generating a state-file. The three options for defining a state-file are:

1. A specific moment in time. The user dictates an exact date and time to save the state file.

2.       The end of the simulation. For this option, the simulation will run until the indicated end of simulation is reached. At the end of the simulation, the flow variables of the model are saved.

3.       The moment that the flow is stationary, c.q. the flow does not change in time. The “stable” condition is defined by the user. The user indicates the maximum change in water levels and/or flow velocities. For example: the user saves the flow state when the water level in all computational nodes, changes less than  the “threshold” 0.0000001 [m] within one time step.

Saving state files
------------------

Currently, state files can only be saved when the simulation is run via the API. In the API POST use the parameter *save_states*. When a simulation is started with the parameter save_states, the response will contain at least a *status*, *organization_id*, *subgrid_id* and a *save_state_id*. The *save_state_id* is a unique id that corresponds to the exact version of the model and the version of the computational core. This state will be deprecated when either one is updated. This means that after a new 3Di Release, a new state file should be made. It is recommended the add a description to the saved state, although it is optional. 

Finding and removing state files
--------------------------------

A simulation is initialized with a state file, by referring to the unique id of the state file. The *save_state_id* can be found via the user interface or the API.

The save_state_id can be found in the repository of the specific model via the user interface at `user interface <http://www.3Di.lizard.net/models>`_ . There is a column named “Nr of saved states”. By clicking on that number, the resulting page lists the state files that are available to use for that specific model. It also shows the description if it was provided. Note the column “available”. It indicates whether the file can be used. It might take some time before it becomes available. From this page saved states can also be removed.

To find the saved states via the API you can navigate to: `API <https://3di.lizard.net/api/v1/threedimodelsavedstates/>`_
This page lists all the state files and it also contains instructions on how to use and remove them via API.

.. TODO: Deze websites bestaan niet! waar staan nu de saved states? (3di.lizard.net bestaat niet)

Using state files
-----------------

To use a saved state for initializing a simulation, the user chooses the parameter *use_saved_state* and provides the unique save_state_id. The simulation will ignore the initial conditions that were defined in the model schematization and uses the state instead.
