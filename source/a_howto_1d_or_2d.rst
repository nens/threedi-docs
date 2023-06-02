When to use 1D, when to use 2D
------------------------------
Generally, 1D models run very fast, but the schematisation is a strong simplification of the real world. The 1D elements should be used for applications in which only one horizontal dimension (flow direction) is dominant over the other flow directions.

A water system consists often of small channels, ditches and pipes. These are difficult to model in 2D, and therefore they are schematised using the 1D network options in 3Di.

Some considerations for 1D elements
-----------------------------------

Every method has advantages and disadvantages. This is also true for choices considering the 1D types. It depends on the application, where the balance lies:

- considering *connected* types, the seperate dealing of the 1D and 2D domain in the same geographic area results in an overlapping volume domain. This means that the volume above a 1D channel, is counted twice.

- For embedded 1D elements, the specific handling of the 1D information is strongly related to the 2D resolution. However, there is no double counting of volume and no increase in computational cost.

- In general, use 1D models for applications that are truely 1D with respect the rest of the domain. Use it for elements that are narrow with respect to the 2D resolution and all will be fine. In those cases the advantages are great, and the disadvantages will remain small.


When to use connected
---------------------
For applications where one has an extended 2D domain including, various essential small scale features, 1D connected elements will improve the model results. Ditches, canals and manholes can be schematised using the 1D connected elements. Hereby, locally increasing the total resolution of the model.

When to use embedded
--------------------
The option to add 1D elements to the 2D domain will effectively increase your resolution and offers the possibility to take small elements into account. However, adding computational points will affect the computational effort. A middle ground could be the use of embedded 1D elements. In such case the information of the 1D elements is integrated with the information of the 2D domain. The number of computational points is not increased, but the number of velocity points is.

Using 1D vs. 2D
---------------
While modelling think of the type of 1D channel type that fits the watercourses in the study area best. For small ditches in an area without elevation, where the flow velocity is low it is sometimes useful not to use 1D channels. Digging ditches in the elevation map will probably lead to sufficient drainage and will make it possible to use bigger calculation cells.