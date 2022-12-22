.. _inflow:

Inflow
======

In addition to direct rainfall on 2D cells, rainfall-runoff processes can also be included in the model using '0D inflow'. A Horton-based rainfall-runoff model calculates how much water flows from each surface into the 1D network.

There are two methods for incorporating inflow in a 3Di schematisation: using 'surfaces', a versatile method that gives you complete freedom in setting the inflow model parameters for each surface, and using 'impervious surfaces', with predefined parameters that follow the Dutch "NWRW" inflow model, common in urban drainage modelling in the Netherlands.

0D inflow can be combined with direct rainfall on 2D cells (0D-1D-2D model) or be used with 1D only (0D-1D model). It is also possible to use 0D inflow without having a 1D network, by mapping the inflow surfaces to embedded nodes (0D-2D model).

How is inflow calculated?
-------------------------
The runoff from each surface calculated by the 3Di 0D inflow model is Hortonian infiltration excess overland flow, that relates the runoff (:math:`R`) to precipitation (:math:`P`) and infiltration (:math:`I`):

.. math::
    :label: horton_runoff
    `R = P - I`

The precipitation is calculated as the precipitation at the location of the connection node to which the surface is mapped, multiplied by the surface area.

However, there is a delay between the accumulation of water on the surface (ponding) and the production of runoff. The runoff at time t :math:`Q_t` is a function of the water volume :math:`V` of water stored at the surface and outflow delay constant :math:`k_q`.

.. math::
    :label: outflow_delay
    `Q_t = k_q V_t`

The infiltration rate decays over time, and then recovers again after the rainfall event. This is described by the modified Horton infiltration equation:

.. math::
   :label: horton_infiltration
    `f_t = \frac{f_0}{1+k_d(t-1)} + \frac{f_c}{1+kt} + \frac{f_r}{1+k_r t}`


| In which:
| :math:`f_t` is the infiltration rate at time :math:`t`
| :math:`f_0` is the initial (maximum) infiltration rate
| :math:`f_c` is the equilibrium (minimum) infiltration rate that is reached once the soil has been saturated
| :math:`k_d` is the decay constant that governs how quickly the infiltration rate decreases
| :math:`k_r` is the recovery constant that governs how quickly the infiltration rate recovers

The figure below givens an overview of these parameters.

.. figure:: image/surface_runoff_parameters.png
   :alt: Parameters used to calculate runoff in the 3Di 0D inflow model

   Parameters used to calculate runoff in the 3Di 0D inflow model



Schematisation of 0D inflow
---------------------------
- In the `Global settings` table, the parameter use_0d_inflow must be set to 1 (for 'impervious surface' 0D inflow) or 2 (for using 'surface' 0D inflow). If you do not want to use 0D inflow, set it to 0.
- Add polygon features to either the `Surface` or `Impervious surface` layers. The feature attributes describe the rainfall-runoff process for each surface. These parameters are explained in more detail below.
- Map each surface to a connection node by adding a line feature to the `Surface map` or `Impervious surface map`. Draw a line from the (impervious) surface polygon to the connection node. By default, the `Percentage` is 100, meaning that 100% of the runoff produced by the mapped surface is added to the volume of the target connection node.
- If you want, you can also divide the runoff from a surface over several connection nodes. Draw (impervious) surface map lines from the same (impervious) surface polygon to several connection nodes. The `Percentage` attribute of the (impervious) surface map feature determines how the runoff is distributed over the different connection nodes. E.g. if you map as surface to 3 connection nodes, you may want to set the percentages to 25%, 25% and 50%.
- Pay attention to the total storage that is available in the target node in relation to the area of the (impervious) surface. The total storage of the node is the sum of the storage in the connection node (storage area multiplied by the difference between bottom and drain level) and half of the volume of all connected pipes, channels and/or culverts. If the total storage in the node is very small relative to the amount inflow that is expected, the water level in the node will rise very quickly, which may lead to unexpected behaviour.

Parameters for 'surface' inflow
-------------------------------

If you are using 'surfaces', you have full freedom to set the inflow parameters that characterize the inflow of a surface. The relevant parameters are set in three different layers. The table below shows in which layer you can set these parameters.

.. list-table:: Parameters when using 'surface' inflow
   :widths: 30 30 30 30 30
   :header-rows: 1

   * - Layer
     - Parameter
     - Type
     - Unit
     - Description
   * - Surface
     - area
     - decimal number
     - m\ :sup:`2`
     - The area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * -
     - surface_parameters_id
     - integer
     - N/A
     - Reference to the row in the `Surface parameters` table that is to be used for this surface
   * - Surface map
     - connection_node_id
     - integer
     - N/A
     - Reference to the connection node to which the inflow from the referenced `Surface` should be mapped
   * -
     - percentage
     - decimal number
     - N/A
     - Percentage of the runoff produced by the referenced `Surface` that should flow to the referenced connection_node
   * -
     - surface_id
     - integer
     - N/A
     - Reference to the `Surface` feature to be mapped
   * - Surface parameters
     - infiltration
     - boolean
     - N/A
     - Switch infiltration on (1) or off (0)
   * -
     - infiltration_decay_constant
     - decimal number
     - h\ :sup:`-1`
     - infiltration decay constant :math:`k_d`
   * -
     - infiltration_recovery_constant
     - decimal number
     - h\ :sup:`-1`
     - infiltration recovery constant :math:`k_r`
   * -
     - max_infiltration_capacity
     - decimal number
     - mm/h
     - initial (maximum) infiltration rate :math:`f_0`
   * -
     - min_infiltration_capacity
     - decimal number
     - mm/h
     - equilibrium (minimum) infiltration rate :math:`f_c`
   * -
     - outflow_delay
     - decimal number
     - min\ :sup:`-1`
     - outflow delay constant :math:`k_q`
   * -
     - surface_layer_thickness
     - decimal number
     - mm
     - storage on the surface

Parameters for 'impervious surface' inflow (Dutch NWRW model)
-------------------------------------------------------------
If you are using 'impervious surfaces', the inflow parameters are predefined for your convenience, in accordance to the Dutch NWRW model for sewerage inflow. The relevant parameters are set in three different layers. The table below shows in which layer you can set each of these parameters.

.. list-table:: Parameters when using 'surface' inflow
   :widths: 30 30 30 30 30
   :header-rows: 1

   * - Layer
     - Parameter
     - Type
     - Unit
     - Description
   * - Impervious surface
     - area
     - decimal number
     - m\ :sup:`2`
     - The area that is used to calculate the precipitation input to the inflow model. The area of the feature's geometry is not used for this.
   * -
     - surface_class
     - text
     - N/A
     - Type of surface. See the table below for the available options and inflow parameters associated with each option.
   * -
     - surface_inclination
     - text
     - N/A
     - Surface slope type. See the table below for the available options and inflow parameters associated with each option.
   * - Impervious surface map
     - connection_node_id
     - integer
     - N/A
     - Reference to the connection node to which the inflow from the referenced `Impervious surface` should be mapped
   * -
     - percentage
     - decimal number
     - N/A
     - Percentage of the runoff produced by the referenced `Impervious surface` that should flow to the referenced connection_node
   * -
     - surface_id
     - integer
     - N/A
     - Reference to the `Impervious surface` feature to be mapped

The parametrisation for the impervious surface types is fixed. It uses the following parameters:

.. list-table:: Parameters Impervious Surface
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