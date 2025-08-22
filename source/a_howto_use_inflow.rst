.. _howto_use_inflow:

Use rainfall-runoff (0D inflow) in 1D models
============================================

Rain typically falls directly onto surfaces before finding its way into the sewerage system. However, in urban areas, a substantial portion of the rain lands on buildings. This rainwater can either flow into the sewerage system through rain pipes or be retained, a phenomenon known as 0D inflow.

For a detailed understanding of how 0D inflow is computed, see :ref:`0d_rain`. Additionally, refer to :ref:`inflow_objects` for an overview of the relevant schematisation objects.


Schematisation
--------------

How to add 0D inflow to a schematisation:

- In the :ref:`simulation_template_settings`, *Use 0D inflow* be set to *True*.

- Define hydrological parameters for the types of surfaces you want to use in the :ref:`surface_parameters` layer.

- Add polygon features to the :ref:`surface` layer. The feature attributes describe the rainfall-runoff process for each surface. Set the *Surface parameters ID* to refer to the parameter set you want to use for each surface.

- Map each surface to a connection node by adding a line feature to the :ref:`surface_map`. Draw a line from the surface polygon to the connection node. By default, the *Percentage* is 100, meaning that 100% of the runoff produced by the mapped surface is added to the volume of the target connection node.

- If you want, you can also divide the runoff from a surface over several connection nodes. Draw :ref:`surface_map` lines from the same :ref:`surface` to several connection nodes. The *Percentage* attribute of the :ref:`surface_map` feature determines how the runoff is distributed over the different connection nodes. E.g. if you map a surface to three connection nodes, you may want to set the percentages to 25%, 25% and 50%.

.. note::
    Pay attention to the total storage that is available in the target node in relation to the area of the surface. The total storage of the node is the sum of the storage in the connection node (storage area multiplied by the difference between bottom and exchange level) and half of the volume of all connected pipes, channels and/or culverts. If the total storage in the node is very small relative to the amount of inflow that is expected, the water level in the node will rise very quickly, which may lead to unexpected behaviour.

Combining 0D inflow with 2D rain
--------------------------------

Combining 0D inflow with 2D rain can be useful in several cases, for example:

- Detailed urban water management models that use 0D inflow for the flow of water from roofs to the sewerage and 2D surface for rainfall and surface flow over roads

- Large open water systems in which a small area is modelled in detail while upstream catchments are lumped in 0D inflow.

An explanation of how this can be used is given in :ref:`combine_0d_2d_rain`.

Simulation
----------

After taking the steps described above, a 3Di model can be generated from the schematisation. Any rain that is forced on the model during the simulation will be used to calculate the runoff from the surfaces. It will be added to the volume of the calculation node to which it is mapped as lateral discharge.