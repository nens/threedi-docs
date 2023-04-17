.. _a_ecosystem:

3Di Ecosystem
^^^^^^^^^^^^^

.. TODO: nog een andere naam bedenken. Ecosystem is een beetje onduidelijk.

The 3Di Ecosystem consists of the following five components:

* :ref:`The Modeller Interface <mi_what_is>`: a QGIS based environment where you can build, edit and start schematisations. The interface can also be used to analyze results.


* :ref:`The Live Site <what_is_the_live_site>`: a web application to start, pause and adjust simulations.

* :ref:`The Management screens <management_screens_what_is>`: an online overview of your schematisations, models and simulations.

* The Computational Core: a Fortran software package which handles the hydrodynamic calculations. These calculations run on specialized servers to ensure computational power. Please visit the :ref:`Physics <cons_volume>` and :ref:`Modelling Concepts <basic_modelling_concepts>` pages to read more about the science that underlies the Computational Core.

.. TODO: stukje hierboven aanpassen.

* :ref:`a_api`: an *application programming interface*, which enables other applications and user interfaces to interact with the computational core.

All components are secured by an **Authentication** and **Authorization** system. This will be discussed in the :ref:`f_authentication_user_management` section.



.. figure:: image/a_3di_ecosystem.png
   :alt: 3Di Ecosystem
   
   The 3Di Ecosystem.
