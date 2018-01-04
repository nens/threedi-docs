State files
===========

During a 3Di calculation the user can choose to save a state of a 3Di simulation. This state can be used in future calculations as a starting point. The state file contains a snapshot of the volume and flow conditions throughout the model.

Saving states is typically done for one of two reasons:

1.       Creating a stable model situation to use for future calculations

2.       Saving a model situation to continue calculating from in operational setup, typically known as “warm state”

Choices in saving a state file
------------------------------

3Di allows the user to choose when to save a state file. There are three options currently provided for the user. A state can be written at:

1.       A specific moment in date and time; This option lets the user dictate the exact date and time to save the state file.

2.       The end of the simulation; When this option is chosen, the simulation will run until the indicated end of simulation is reached. Just before stopping the simulation, the state of the model is saved.

3.       The moment that the model is “stable” to conditions specified by the user; Choosing to save the model when it is “stable”, requires the user to also choose a condition of the model is should meet. This condition depends on both: variable(s) to monitor and corresponding threshold value(s). Only when this condition is met, the state is saved. The variables that can be monitored are water level (s1) and flow velocity (u1) For example: the user can choose to save a model when: “variable” s1 in all calculation nodes, changes less than “threshold” 0.001 [m] within one calculation time step.

Saving state files
------------------

Currently, state files can only be saved when calculating via the API. In the API POST we can use the parameter *save_states*. When a calculation is started with the parameter save_states, the response will contain at least a *status*, *organization_id*, *subgrid_id* and a *save_state_id*. The *save_state_id* is a unique id that corresponds to the exact version of the model and the version of the calculation core and will not by applicable when either one is updated. When saving a state, we can also give a description to help identify the situation of the state we have saved.

Finding and removing state files
--------------------------------

To use a saved state file, the user will need to find the unique id to reference to. The *save_state_id* is returned when starting a calculation, but can also be found via a user interface or API.

To find the id in the user interface, go to 3Di.lizard.net/models, search for the repository and continue to the specific model it was saved to. There will be a column named “Nr of saved states” which has a number you can click on. The resulting page will list the state files that are available to use for that specific model, the description that was provided when saving the calculation and the moment at which the state file was written. It is important to note that there is a column “available” which indicates whether the file can be used already, or if you still need to wait for it to become usable. Here the option is also present to remove the saved states via a button.

To find the saved states via the API you can navigate to: 3di.lizard.net/api/v1/threedimodelsavedstates/ The page listing all the state files also contains instructions on how to delete them via API.

Using state files
-----------------

To use a saved state to start a calculation with, the user should choose the parameter *used_saved_state* and provide the unique id. The calculation will start by reading the values for all variables from the saved state file and ignore initial conditions that were set in the model schematization.
