.. _saved_states:

Saved states
============

A simulation can be initialized using a saved state. A saved state is a snapshot of the complete flow condition of the model at a specific moment in time. It contains the volumes and water levels, flow velocities and discharges of all nodes and flowlines, and any other variable or parameter value that is needed to continue the simulation from that moment in time in the exact same way. It is thus a much more elaborate way to initialize the model than :ref:`initial_water_levels`.


A saved state can be used to reduce the computational time needed to let the computational core find a balanced situation, make consistent scenario comparisons, or, in operational water management, continue from a previous simulation when e.g. updated rain forecasts become available.

Creating saved states
---------------------

Saved states can be created during the simulation in several ways:

1. At a specific moment in time in seconds since the start of the simulation.

2. At the end of the simulation.

3. When the flow has become stationary, i.e., no longer changes over time. The flow hardly ever becomes 100% stationary in all parts of the model, so a threshold has to be defined for this in terms of the maximum change in water levels and/or flow velocities. For example: if the water level change threshold is set to 0.0000001, a saved state is created when the water levels in all computational nodes changes less than the 0.0000001 [m] within one time step.

Multiple saved states can be created during one simulation.

Saved states are saved for a 3Di model. If a new 3Di model is created, the saved state will be lost.

Using saved states
------------------

When starting a simulation, and one or more saved states are available for the 3Di model, the saved state can be selected as *Initial saved state*. Saved states cannot be used in combination with initial water levels.