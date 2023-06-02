.. _control:

Control Structures
==================

The possibility exists to adjust hydraulic structure parameters within the water system based on flow variables. Flow variables can be measured during the simulation by assigning measuring locations to certain calculation nodes. Based on the user-defined values for the parameters of a hydraulic structure, a controller will then operate accordingly. The measuring options, different control types and the hydraulic structure parameters to adjust are explained here. Schematically adjusting properties of hydraulic structures using some control rules can be represented as:

.. figure:: image/c_control.png
   :alt: Control structures overview

   
Measuring station
------------------

Measuring stations are locations at which a certain flow variable is monitored during the simulation. The value of this flow variable can be used to trigger an action on a structure, based on the rules defined in the type of control. The flow variable that needs to be monitored is set at the different controls. At each location multiple flow variable can be monitored if necessary.

The measurement of a flow variable can be performed at one or more locations. At each location a weight has to be allocated to the measurement. The weighted average of a group of measuring stations is used in the control of a hydraulic structure. The weights of these measurements have to add up to 1.0. When using one measuring station its weight has to be set to 1.0. At the moment measuring stations can only be defined at a connection node where the waterlevel can be monitored. Based on the waterlevel the controls be below can execute action on certain structures. 

Control types
-------------

The different types of controls are now explained. The implemented types of control are:

-	Table control

-	Memory control

.. _table_control:

Table control
-------------

The table control has a combination of flow values and action values as input. Each increment of the flow value in the input table acts as a threshold for a corresponding structure value which is set on the structure. In combination with a mathematical operators larger than and smaller than (<,>) the action will be executed when the measurement value either falls below the threshold or exceeds it. Example for table control input is:

.. list-table:: Example control table
   :widths: 40 40 
   :header-rows: 1

   * - Waterlevel [mNAP]
     - Weir crest level [mNAP]
   * - 1.2
     - 0.8
   * - 1.4
     - 0.6
   * - 1.6
     - 0.8
   * - 1.8
     - 1.0

Dependent on the mathematical operator the behavior for this control of the crest level of the control is different. For instance, when the larger than (>) operator the structure value will be 0.8 mNAP between 1.2 mNAP and 1.4 mNAP. When the smaller than (<) operator is set the structure value will be 0.8 below 1.2 mNAP. Dependent on the operator the default value of the structure will be applied at the top or bottom of the increments. For instance with the larger than operator the structure default will be applied below 1.2 mNAP.

The measurement value stems from the flow variable that is set to monitor within each control and linked to a group of measurement locations that are described above to react to this flow variable.

Memory control
--------------

The memory control has two thresholds which trigger an adjustment on a hydraulic structure. When the measured flow variable exceeds the defined upper threshold the control becomes active and adjusts the property of a structure to a new value. When the value flow variable subsequently (first the upper threshold has been exceeded) drops below the lower threshold the control becomes inactive and the property of the structure defaults back to its original value. This operation is similar to a pump with on and off thresholds.

As an extra parameter the option for inverse operation of the control can be set. In this case when the flow variable exceeds the upper threshold the control becomes inactive and was already active. After the value of the flow variable subsequently falls below the lower threshold the control becomes active again and adjusts the structure property. 

We consider a memory control on a culvert by measuring water levels with the following input parameters:

- upper threshold: 1.2 mNAP

- lower threshold: 0.8 mNAP

- adjusted structure value (action value):  0.0 (cutoff using discharge coefficient)

The control will be activated when the water level at the measuring station rises above 1.2 mNAP for the first time. Now the structure property of discharge coefficients becomes 0.0 resulting in the cutoff of flow. When the water level subsequently falls below 0.8 mNAP, the control becomes inactive and the discharge coefficients defaults back to 1.0 which was its original value. 

Adjustable hydraulic structures
-------------------------------

Different structures can be used when using a control on a structure. The list of structures with their possible properties to adjust  are:

**Weirs**

- Crest level

- Discharge coefficients (to cutoff flow at 0.0)

**Orifices**

- Crest level

- Discharge coefficients (to cutoff flow at 0.0)

**Culverts**

- Discharge coefficients (to cutoff flow at 0.0)

**Pumps**

- Pump discharge

   
