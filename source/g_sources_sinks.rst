.. _sources_sinks:

Source and Sink terms
========================

Mass conservation is one of the two fundamental laws to which a 3Di simulation is bounded. This is locally, per computational cell valid and globally in the simulation domain. There are various scenarios possible to add and extract water to a simulations. Some of these are linked in 3Di to specific physical processes, others are more generic in order to give some freedom to the users.

Here, laterals, surface sources and sinks and leakage will be discussed. They all act as sources and sinks, but differ in their application. However, they share two major characteristics; i) water can always be added ii) there can never be water extracted which is not there. These characteristics seem trivial, but especially the second one is computationally not always trivial. 3Di will limit the extraction in case of very limited water levels. Therefore, just before the cell will become dry, the extraction discharge will be less, than the users input. This, to guarantee stability and capture reality better [#footnote_publication]_. This is valid for all types of sources and sinks that are discussed in this section.

.. [#footnote_publication] A Surface-Subsurface Model; balancing speed, accuracy and reality, Stelling and Volp (to be published)

.. toctree::
   :maxdepth: 2
   :caption: Various types of sources and sinks
   :name: various_sources_sinks

   g_rainfall
   g_infiltration
   g_laterals
   g_surface_sources_sinks
   g_leakage
   g_inflow

.. TODO: file not found: b_boundary_conditions
