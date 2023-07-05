.. _inflow_objects:

Inflow objects
==============

.. _impervious_surface:

Impervious surface
------------------

Definition of 0D inflow surface using the Dutch NWRW system. If you are using 'impervious surfaces', the inflow parameters are predefined for your convenience, in accordance to the Dutch NWRW model for sewerage inflow.

See :ref:`0d_rain` for further details.

.. list-table:: Impervious surface attributesv
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - area
     - decimal number
     - m\ :sup:`2`
     - The area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * - surface_class
     - text
     - N/A
     - Type of surface. See the table below.
   * - surface_inclination
     - text
     - N/A
     - Surface slope type. See the table below.

The parametrisation for the impervious surface types is fixed. It uses the following parameters:

.. list-table:: Inflow model parameters for each available combination of surface class and inclination
   :widths: 30 30 30 30 30 30 30 30 30
   :header-rows: 1

   * - Surface class
     - Surface inclination
     - Outflow delay :math:`k_q` (min\ :sup:`-1`)
     - Surface storage (mm)
     - Infiltration (boolean)
     - Maximum infiltration rate :math:`f_0` (mm/h)
     - Minimum infiltration rate :math:`f_c` (mm/h)
     - Infiltration decay constant :math:`k_d` (h\ :sup:`-1`)
     - Infiltration recovery constant :math:`k_r` (h\ :sup:`-1`)
   * - gesloten verharding
     - hellend
     - 0.5
     - 0.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * -
     - vlak
     - 0.2
     - 0.5
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * -
     - vlak uitgestrekt
     - 0.1
     - 1.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - open verharding
     - hellend
     - 0.5
     - 0.0
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * -
     - vlak
     - 0.2
     - 0.5
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * -
     - vlak uitgestrekt
     - 0.1
     - 1.0
     - True
     - 2.0
     - 0.5
     - 3.0
     - 0.1
   * - dak
     - hellend
     - 0.5
     - 0.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * -
     - vlak
     - 0.2
     - 2.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * -
     - vlak uitgestrekt
     - 0.1
     - 4.0
     - False
     - 0.0
     - 0.0
     - 0.0
     - 0.0
   * - onverhard
     - hellend
     - 0.5
     - 2.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1
   * -
     - vlak
     - 0.2
     - 4.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1
   * -
     - vlak uitgestrekt
     - 0.1
     - 6.0
     - True
     - 5.0
     - 1.0
     - 3.0
     - 0.1

.. _impervious_surface_map:

Impervious surface map
----------------------

Connection between an impervious surface and its target connection node.


.. list-table:: Parameters when using 'surface' inflow
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - connection_node_id
     - integer
     - N/A
     - Reference to the connection node to which the inflow from the referenced `Impervious surface` should be mapped
   * - percentage
     - decimal number
     - N/A
     - Percentage of the runoff produced by the referenced `Impervious surface` that should flow to the referenced connection_node
   * - surface_id
     - integer
     - N/A
     - Reference to the `Impervious surface` feature to be mapped

.. _surface:

Surface
-------

Definition of 0D inflow surface using custom rainfall-runoff parameters. If you are using 'surfaces', you have full freedom to set the inflow parameters that characterize the inflow of a surface.

See :ref:`0d_rain` for further details.

.. list-table:: Surface attributes
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - area
     - decimal number
     - m\ :sup:`2`
     - The area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * - surface_parameters_id
     - integer
     - N/A
     - Reference to the row in the `Surface parameters` table that is to be used for this surface

.. _surface_map:

Surface map
-----------

Connection between a surface and its target connection node.

.. list-table:: Surface map attributes
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - connection_node_id
     - integer
     - N/A
     - Reference to the connection node to which the inflow from the referenced `Surface` should be mapped
   * - percentage
     - decimal number
     - N/A
     - Percentage of the runoff produced by the referenced `Surface` that should flow to the referenced connection_node
   * - surface_id
     - integer
     - N/A
     - Reference to the `Surface` feature to be mapped

.. _surface_parameters:

Surface parameters
------------------

Custom rainfall-runoff parameters to be used by surfaces

.. list-table:: Surface parameters
   :widths: 30 30 30 30
   :header-rows: 1

   * - Parameter
     - Type
     - Unit
     - Description
   * - infiltration
     - boolean
     - N/A
     - Switch infiltration on (1) or off (0)
   * - infiltration_decay_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration decay constant :math:`k_d`
   * - infiltration_recovery_constant
     - decimal number
     - h\ :sup:`-1`
     - Infiltration recovery constant :math:`k_r`
   * - max_infiltration_capacity
     - decimal number
     - mm/h
     - Initial (maximum) infiltration rate :math:`f_0`
   * - min_infiltration_capacity
     - decimal number
     - mm/h
     - Equilibrium (minimum) infiltration rate :math:`f_c`
   * - outflow_delay
     - decimal number
     - min\ :sup:`-1`
     - Outflow delay constant :math:`k_q`
   * - surface_layer_thickness
     - decimal number
     - mm
     - Storage on the surface
