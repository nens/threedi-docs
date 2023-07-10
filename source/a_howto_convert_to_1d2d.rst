.. _howto_convert_to_1d2d:

Add 1D elements to a 2D model
=============================

1D elements can be added to any 2D model in a few simple steps. First, you need to change some :ref:`global_settings` and :ref:`numerical_settings`. Then you add the 1D elements to the schematisation and upload it as a new revision. The 3Di model that is created from this revision will include the 1D elements.

Global settings to be changed
-----------------------------

To make the required changes to the global settings, :ref:`load your schematisations<load_schematisation>` and open the *Global settings* attribute table.

- In the tab *General*, check the option *Use 1D flow*

- In the tab *Extra options 1D*, check if the settings have the correct values

	.. csv-table:: Global settings for models with 1D elements
		:name: inf_settings
		:header: "Setting", "Attribute name", "Suggested value", "Comments"

		"Advection 1D", "advection_1d", "1", "In most cases, you will want to include the effect of advective forces on flow in the 1D domain"
		"Calculation point distance", "dist_calc_points", "1000", "Specify the calculation point distance for each individual 1D element; this global value will then be ignored."
		"Manhole storage area", "manhole_storage_area", "NULL", "Relevant only for sewerage models without 2D"
		"Max angle advection 1D", "max_angle_advection_1d", "1.570795", "Advection is not relevant when the angle is more then 90 degrees"
		"Table step size 1D", "table_step_size_1d", "0.01", "Recommended to make this value much smaller than the smallest 1D cross section in the schematisation"

Numerical settings to be changed
--------------------------------

Open the *Numerical settings* attribute table.

- In the tab *Limiters*, switch the *limiter_grad_1d* on (set it to 1). 

- In the tab *Matrix*, set *use_of_nested_newton* to the correct value (depends on what if the 1D elements you are going to add will have open or closed cross-sections).

- Still in the tab *Matrix*, set *max_degree* to "7: for 1D and 2D flow"

- If you are going to use pumps, the *pump_implicit_ratio* (*Miscellaneous* tab) should normally be set to 1, unless you want to study exactly when the pump switches on or off.

- The *preissmann_slot* (*Miscellaneous* tab) should normally not be used, i.e. set it to 0.

Adding 1D elements
------------------

After having set the global and numerical settings, you can start adding 1D features. See :ref:`edit_schematisation` for more information.

