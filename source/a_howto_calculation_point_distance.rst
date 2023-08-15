Choosing the 1D resolution by setting the calculation point distance 
====================================================================

When 3Di generates a computational grid from the schematisation, a computational node is created for every connection node. Depending on the 1D resolution, extra computational nodes are added at a regular interval along the channel, pipe or culvert. A more detailed explanation about this can be found in the section :ref:`techref_calculation_point_distance`. When choosing the 1D resolution, keep the following in mind:


Scale of flow dynamics
^^^^^^^^^^^^^^^^^^^^^^
The 1D resolution (calculation point distance) relates to the scale at which the dynamics of flow are captured. If there are relevant length scales of the dynamics, accelerations or there are other reasons to expect changes in the flow, you will need to have a sufficient number of computational points on that 1D element. The distance between computational points should be smaller than the scale at which you expect such variations to play a role.


Exchange between 1D and 2D
^^^^^^^^^^^^^^^^^^^^^^^^^^
If the channel is part of a 1D2D schematisation and has a *(double) connected* :ref:`calculation type <calculation_types>`, you will also need to consider the exchange with the 2D domain. This exchange is only possible at computational points. A general guideline is to match the 1D and 2D resolutions in those areas, i.e., if the computational cell size is 40 x 40 m\ :sup:`2`\, a 1D calculation point distance of 40 m would be suitable.

Pipes can also be given a *connected* calculation type, in combination with a calculation point distance that is smaller than the length of the pipe. In this way, the pipe can exchange with 2D cells it crosses. This can be used as a way to schematise gullies.

Visit the link for more information and a visual representation of the exchange between 1D and 2D in the :ref:`channelflow` section.