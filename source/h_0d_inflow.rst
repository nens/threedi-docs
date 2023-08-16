.. Deze tekst hierheen verplaats van a_howto_combine_0d_rain. 
 De tekst moet nog wel verbeterd worden maar het lijkt mij logisch dat er een kopje 0D inflow onder het kopje flow bestaat.

.. _0d_inflow:

0D inflow
=========

0D inflow is a module in 3Di that computes the amount of rain that falls on a surface and arrives in the 1D network. These surfaces represent (urban) elements, which are coupled to the sewerage system. For example buildings, or more distant roads which are included in the 1D domain only. The type of surface determines whether there is volume stored, infiltrated or delayed in flowing to the 1D network. In short, the 0D inflow module computes the rainfall volume (area x rainfall_intensity x delta t) for each time step for each impervious area or surface area. 

The impervious surfaces table uses the Dutch NWRW model. In this model, a surface is defined by certain characteristics. It can be for example sloping or flat, paved or unpaved etc. These characteristics are translated to hydrological parameters like storage and delay of inflow. These are translated into a discharge hydrograph which is added as a lateral inflow to the sewerage system. The surface table works similar to the impervious surface table but differs because you have to specify all the hydrological parameters of the surface yourself (i.e. infiltration, outflow delay, storage). For more information on 0D rainfall: :ref:`0d_rain`.

.. figure:: image/d_panden.png
   :alt: impervious_surfaces_for_0D_inflow
     
   Impervious surfaces which facilitate the 0D inflow.