Choose calculation point distance
---------------------------------

When 3Di generates a computational grid from the schematisation, a calculation node is created for every connection node, plus at a regular interval along the channel, pipe or culvert. This is explained in more detail in the section :ref:`techref_calculation_point_distance`. Several considerations can be taken into account when choosing the right calculation point distance.

Scale of flow dynamics
^^^^^^^^^^^^^^^^^^^^^^

The calculation point distance relates to the scale at which you want to capture the dynamics of flow. I.e., if a channel has a uniform cross section along its entire length and the river bed is straight, the discharge and flow velocity is unlikely to vary between sections of the channel. In such a case, adding in-between calculation nodes will not affect the simulated water levels, flow velocities and discharges. If there are relevant changes in the cross-section or river bed, or there are other reasons to expect changes in the flow (e.g. a transition from sub-critical to (super) critical flow), you will need to have sufficient calculation points on the channel. The distance between these calculation points should match the scale at which you expect this variation to happen.

Another consideration is at which scale the flow dynamics are relevant for your modelling objective. If the modelling objective is to test the backwater curve of a waterway against the applicable norms, you will probably want to know very exactly how the water level and flow velocity varies in the channel. On the other hand, if you build a model for urban water management, you may want to include the open water to which the sewer overflows are connected. It is important that the water level in these waterways is in the right range, so you know when and to what extent the sewer outflow is impeded by the external water level. However, the exact flow dynamics within those channels are not important, so a large calculation point distance will suffice.

Exchange between 1D and 2D
^^^^^^^^^^^^^^^^^^^^^^^^^^

If the channel is part of a 1D2D schematisation and has a *(double) connected* calculation type, you will also need to consider the exchange with the 2D domain. This exchange is only possible at calculation points. A general guideline is to match the 1D and 2D resolutions, i.e., if the computational cell size is 40 x 40 m, a 1D calculation point distance of 40 m would be suitable.

Pipes can also be given a *connected* calculation type, in combination with a calculation point distance that is smaller than the length of the pipe. In this way, the pipe can exchange with 2D cells it crosses. This can be used as a way to schematise gullies.