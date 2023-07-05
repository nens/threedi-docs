.. _howto_use_inflow:

Use rainfall-runoff in 1D models
================================

In models with 1D elements, rainfall-runoff processes can be included using '0D inflow', i.e. inflow from a surface with a specified area and hydrological parameters that determine how much runoff flows into the 1D network. 

See :ref:`0d_inflow` for an explanation of how 0D inflow is calculated, and for the information you need to choose between using :ref:`surface` or :ref:`impervious_surface`.
 
See :ref:`inflow_objects` for an overview of the schematisation objects used.

This section explains how to use 0D inflow in a model.

Schematisation
--------------

- In the `Global settings` table, the parameter use_0d_inflow must be set to 1 (for 'impervious surface' 0D inflow) or 2 (for using 'surface' 0D inflow). If you do not want to use 0D inflow, set it to 0.

- If you are using *Surface* inflow, add a record to the :ref:`surface_parameters` table.

- Add polygon features to either the :ref:`surface` or :ref:`impervious_surface` layers. The feature attributes describe the rainfall-runoff process for each surface. If you are using *Surface* inflow, set the *surface_parameters_id* to refer to the parameter set you want to use for this surface.

- Map each surface to a connection node by adding a line feature to the :ref:`surface_map` or :ref:`impervious_surface_map`. Draw a line from the (impervious) surface polygon to the connection node. By default, the *Percentage* is 100, meaning that 100% of the runoff produced by the mapped surface is added to the volume of the target connection node.

- If you want, you can also divide the runoff from a surface over several connection nodes. Draw (impervious) surface map lines from the same (impervious) surface polygon to several connection nodes. The `Percentage` attribute of the (impervious) surface map feature determines how the runoff is distributed over the different connection nodes. E.g. if you map as surface to 3 connection nodes, you may want to set the percentages to 25%, 25% and 50%.

.. note::
	Pay attention to the total storage that is available in the target node in relation to the area of the (impervious) surface. The total storage of the node is the sum of the storage in the connection node (storage area multiplied by the difference between bottom and drain level) and half of the volume of all connected pipes, channels and/or culverts. If the total storage in the node is very small relative to the amount inflow that is expected, the water level in the node will rise very quickly, which may lead to unexpected behaviour.

Combining 0D inflow with 2D rain
--------------------------------

Combining 0D inflow with and 2D rain can be useful in several cases, for example:

- Detailed urban water management models that use 0D inflow for the flow of water from roofs to the sewerage and 2D surface for rainfall and discharge over roads

- Large open water systems in which a small area is modeled in detail while upstream catchments are lumped in 0D inflow.

An explanation of how this can be used is given in :ref:`combine_0d_2d_rain`.


Simulation
----------

After taking the steps described above, a 3Di model can be generated from the schematisation. Any rain that is forced on the model during the simulation will be used to calculate the runoff from the surfaces. It will be added to the volume of the calculation node to which it is mapped as lateral discharge.