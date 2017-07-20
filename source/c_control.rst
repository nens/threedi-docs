Adjustable hydraulic structures
===============================

The possibility exists to adjust hydraulic structure parameters within the water system based on flow variables. Flow variables can be measured during the simulation by assigning measuring stations to certain calculation nodes. Based on the user-defined values for the parameters of a hydraulic structure, a controller will then operate accordingly. The measuring options and the hydraulic structure parameters to adjust are explained here.

**Timed Controller**

One of the methods to adjust parameters of a hydraulic structure is time-dependent adjustments. By providing a time interval in which a controller is active the hydraulic structure will be operated. An example of such a controller is a weir adjustment for maintaining winter and summer level in a canal system.

**Simple condition controller**

Based on a simple condition for flow variables in the water system a hydraulic can be controlled. When a threshold is exceeded the parameters of hydraulic are adjusted and once the condition is no longer exceeded the structure parameters are set back to their original values. This type of condition based controller can be combined with a timed control. During the combination the condition based controller will only be active within the given time interval of the timed controller. 

**Adjustable hydraulic structures**

The following parameters can be adjusted:

* Weirs
   -- Crest level
   
   -- Discharge coeffients (seperately for both directions)
   
   -- Occlusion (Cutting off flow entirely)
* Orifices
   -- Crest level
   
   -- Discharge coeffients (seperately for both directions)
   
   -- Occlusion (Cutting off flow entirely)
* Culverts
   -- Discharge coeffients (seperately for both directions)
   
   -- Occlusion (Cutting off flow entirely)
* Pumps
   -- Pump discharge

**Measuring stations**

At the moment, measuring stations can only be applied to connection nodes. At these locations the water levels can be measured to trigger a control on a hydraulic structure. 


**Example**