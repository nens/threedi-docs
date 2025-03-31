.. _howto_convert_to_1d2d:

Add 1D elements to a 2D model
=============================

1D elements can be added to any 2D model in a few simple steps. First, you need to change some :ref:`model_settings`, :ref:`numerical_settings`, and :ref:`physical_settings`. Then you add the 1D elements to the schematisation and upload it as a new revision. The 3Di model that is created from this revision will include the 1D elements.

Model settings to be changed
----------------------------

To make the required changes to the model settings, :ref:`load your schematisations<load_schematisation>` and open the *Model settings* attribute table.

- In the tab *Processes*, check the option *Use 1D flow*

- In the tab *General*, set *Calculation point distance 1D* to 1000. Specify the calculation point distance for each individual 1D element; this global value will then be ignored.

- In the tab *Advanced* set *Max angle advection 1D* to 1.570795 radians.

- In the tab *General* set *Table step size 1D* to 0.01. It is recommended to make this value much smaller than the smallest 1D cross section in the schematisation.

Numerical settings to be changed
--------------------------------

Open the *Numerical settings* attribute table.

- In the tab *Matrix solver*, set *Use nested Newton* to the correct value (depends on whether the 1D elements you are going to add will have open or closed cross-sections).
- Still in the tab *Matrix*, set *Convergence criterion for conjugate gradient method* to "7: For 1D and 2D flow"

- In the tab *Slope limiters*, switch the *Limiter water level gradient 1D* on. 

- In the tab *Misc*, the *Pump implicit ratio* should normally be set to 1, unless you want to study exactly when the pump switches on or off.

Physical settings to be changed
-------------------------------

- Set *Use advection 1D* to *3: Combined momentum and energy conservative scheme* 

Adding 1D elements
------------------

After having set these settings, you can start adding 1D features. See :ref:`edit_schematisation` for more information.

You can also add 1D elements outside of the 2D domain. Set their :ref:`exchange type<calculation_types>` to *isolated* and connect them to a schematisation object (e.g. a channel) that does overlap with the 2D domain and has a *connected* or *embedded* exchange type.
