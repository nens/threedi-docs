.. _logging:

Log files
=========


.. _flow_summary:

Flow summary
------------

File name: flow_summary.log

This file provides a full water balance of the entire model domain for the entire simulation duration. It is recommended to always check this file after the simulation has finished.

The maximum volume error is also included in the volume balance; large volume errors are an indication that there may be something wrong with the schematisation. What constitutes a large volume error depends on the size of the model and the type of forcing that is used. By frequently inspecting the flow summary, an expert judgement can be trained to judge wether the volume error is normal. In very general terms, volume errors above 10 m³ are somewhat large; if the volume error is more than 1.000 m³, there is almost certainly something wrong with the schematisation.   

Iteration
---------

File name: iteration.log

This file contains logging from the computional core from any moment when it needs more iterations to solve the matrix than expected.

Matrix
------

File name: matrix.log

This file contains log entries in case the 3Di computional core has had a hard time to find a solution for a specific time step. This file should normally be empty.

Scheduler
---------

File name: scheduler.log

This file contains all the log output of the scheduler, i.e. the component that manages all action, forcings and events during the simulation.

Simulation
----------

File name: simulation.log

This file contains general logging from the 3Di computational core.

Time step reduction
-------------------

File name: timestep_reduction.log

This file contains information for every simulation time step when timestep reduction was applied by the 3Di computational core. This is useful when you want to optimize the calculation speed of your model.

Water balance
-------------

File name: water_balance.csv

This file gives a cumulative water balance for the entire model domain, for each output time step.
