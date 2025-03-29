.. _hydrological_processes_objects:

Hydrological process objects
============================

Objects in this category contain the settings that govern a range of hydrological processes.

* :ref:`hp_initial_conditions`
* :ref:`hp_interception`
* :ref:`hp_interflow`
* :ref:`hp_groundwater`
* :ref:`hp_simple_infiltration`
* :ref:`hp_2d_vegetation_drag`

.. _hp_initial_conditions:

Initial conditions
------------------

Defines the (ground)water levels at the start of the simulation. This is stored in the simulation template, not in the 3Di model itself.

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

initial_conditions

Attributes
^^^^^^^^^^

.. list-table:: Initial conditions attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Initial water level
     - initial_water_level
     - decimal number
     - Yes
     - m MSL
     - Initial 2D surface water level. This global value is superseded in case an initial water level file is provided.
   * - Initial water level file
     - initial_water_level_file
     - text
     - No
     - m MSL
     - Name of the initial 2D surface water level file. This supersedes the global *Initial water level*.
   * - Initial water level aggregation
     - initial_water_level_aggregation
     - integer
     - Yes
     - \-
     - Choose between: *0: Max*, *1: Min*, or *2: Average*.
   * - Initial groundwater level
     - Initial_groundwater_level
     - Decimal number
     - No
     - m MSL
     - Initial groundwater level. This global value is superseded in case an initial groundwater level file is provided. See :ref:`groundwater` for more details.
   * - Initial groundwater level file
     - initial_groundwater_level_file
     - Text
     - No
     - m MSL
     - Name of the initial groundwater level file. This supersedes the global initial groundwater level.
   * - Initial groundwater level aggregation
     - initial_groundwater_level_aggregation
     - integer
     - Only when using an initial groundwater level file
     - \-
     - Choose between: *0: Max*, *1: Min*, or *2: Average*. See :ref:`groundwater` for more details.

.. _hp_interception:

Interception
------------

Defines :ref:`interception`. This is stored in the 3Di model (:ref:`subgrid_tables`).

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

interception

Attributes
^^^^^^^^^^

.. list-table:: Interception attributes
   :widths: 6 4 4 2 4 30
   :header-rows: 1

   * - Attribute alias
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - integer
     - Yes
     - \-
     - Unique identifier
   * - Interception
     - interception
     - Decimal number
     - No
     - m
     - Maximum interception volume/m:sup:`2`. This global value is superseded in case an interception file is provided.
   * - Interception file
     - interception_file
     - Text
     - No
     - m
     - Name of interception file. Supersedes global interception value.

.. _hp_interflow:

Interflow
---------

Defines :ref:`interflow`, which can be used to schematise porous medium flow below the surface.

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

interflow

Attributes
^^^^^^^^^^

.. list-table:: Interflow attributes
   :widths: 20 20 15 10 10 40 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
   * - Interflow type
     - interflow_type
     - Integer
     - Yes
     - \-
     - Choose between: (0) No interflow, (1) Local deepest point scaled porosity, (2) Global deepest point scaled porosity, (3) Local deepest point constant porosity, (4) Global deepest point constant porosity.
   * - Impervious layer elevation
     - impervious_layer_elevation
     - decimal number
     - Yes
     - m
     - Depth of impervious layer below lowest pixel. Value has to be greater than 0.
     - Impervious layer
   * - Porosity
     - porosity
     - decimal number
     - Yes
     - \-
     - Porosity value of the interflow layer. It should be a value between 0 and 1. This global value is superseded in case a porosity file is provided.
   * - Porosity file
     - porosity_file
     - Text
     - Yes
     - \-
     - Name of the porosity file. This supersedes any global porosity value.
   * - Porosity layer thickness
     - porosity_layer_thickness
     - decimal number
     - Only if using interflow type *(1) Local deepest point scaled porosity* or *(2) Global deepest point scaled porosity*.
     - m
     - Thickness of the porosity layer relative to the DEM.
   * - Hydraulic conductivity
     - hydraulic_conductivity
     - decimal number
     - Yes
     - m/d
     - Hydraulic conductivity value. This global value is superseded in case a hydraulic conductivity file is provided.
   * - Hydraulic conductivity file
     - hydraulic_conductivity_file
     - text
     - No
     - m/day
     - Name of the hydraulic conductivity file. This supersedes any global hydraulic conductivity value.

.. _hp_groundwater:

Groundwater
-----------

Defines :ref:`groundwater`.

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

groundwater

Attributes
^^^^^^^^^^

.. list-table:: Groundwater attributes
   :widths: 20 20 15 10 10 40 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
   * - Impervious layer level
     - Impervious_layer_level
     - Decimal number
     - Yes
     - m MSL
     - Level of the impervious layer that acts as the bottom (and thus boundary) of the groundwater layer.
   * - Impervious layer level file
     - Impervious_layer_level_file
     - Text
     - No
     - m MSL
     - Name of the impervious layer level file
   * - Impervious layer level aggregation
     - Impervious_layer_level_aggregation
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Phreatic storage capacity
     - phreatic_storage_capacity
     - Decimal number
     - Yes
     - \-
     - The potential storage in the saturated zone (= porosity). The phreatic storage capacity is described by a value between 0 and 1.
   * - Phreatic storage capacity file
     - phreatic_storage_capacity_file
     - Text
     - No
     - \-
     - Name of the phreatic storage capacity file.
   * - Phreatic storage capacity aggregation
     - phreatic_storage_capacity_aggregation
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Hydraulic conductivity
     - hydraulic_conductivity
     - Decimal number
     - Yes
     - m/d
     - Darcy coefficient.
   * - Hydraulic conductivity file
     - hydraulic_conductivity_file
     - Text
     - No
     - m/day
     - Name of the groundwater hydraulic conductivity file
   * - Hydraulic conductivity aggregation
     - hydraulic_conductivity_aggregation
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Initial infiltration rate
     - initial_infiltration_rate
     - Decimal number
     - Yes
     - mm/day
     - The initial infiltration rate for Horton-based infiltration. For more information, see :ref:`grwhortoninfiltration`.
   * - Initial infiltration rate file
     - initial_infiltration_rate_file
     - Text
     - No
     - mm/day
     - Name of the initial infiltration rate file
   * - Initial infiltration rate type
     - initial_infiltration_rate_type
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Equilibrium infiltration rate
     - equilibrium_infiltration_rate
     - Decimal number
     - No
     - mm/day
     - The equilibrium infiltration rate for Horton-based infiltration. For more information, see :ref:`grwhortoninfiltration`.
   * - Equilibrium infiltration rate file
     - equilibrium_infiltration_rate_file
     - Text
     - No
     - mm/day
     - Name of equilibrium infiltration rate file. For more information, see :ref:`grwhortoninfiltration`.
   * - Equilibrium infiltration rate aggregation
     - equilibrium_infiltration_rate_aggregation
     - Integer
     - Yes
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Infiltration decay period
     - infiltration_decay_period
     - Decimal number
     - Yes
     - days
     - Period in which the infiltration rate decays to an equilibrium for Horton-based infiltration.
   * - Infiltration decay period file
     - infiltration_decay_period_file
     - Text
     - No
     - days
     - Name of the infiltration decay period file.
   * - Infiltration decay period aggregation
     - infiltration_decay_period_aggregation
     - Integer
     - No
     - \-
     - Choose between: *0: Maximum*, *1: Minimum*, and *2: Average*.
   * - Leakage
     - leakage
     - Decimal number
     - Yes
     - mm/day
     - The bottom boundary condition (constant in time) that describes the leakage to or seepage from deeper groundwater layers.
   * - Leakage file
     - leakage_file
     - Text
     - No
     - mm/day
     - Name of the leakage file.

.. _hp_simple_infiltration:

Simple infiltration
-------------------

Defines :ref:`simpleinfiltration`. 

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

simple_infiltration

Attributes
^^^^^^^^^^

.. list-table:: Simple infiltration attributes
   :widths: 20 20 15 10 10 40 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
   * - Infiltration rate
     - infiltration_rate
     - Decimal number
     - Yes
     - mm/d
     - Infiltration rate.  This global value is superseded in case an infiltration rate file is provided.
   * - Infiltration rate file
     - infiltration_rate_file
     - Text
     - No
     - mm/d
     - Name of the infiltration rate file. This supersedes the global infiltration rate.
   * - Infiltration surface option
     - infiltration_surface_option
     - Integer
     - Yes
     - \-
     - Sets how the infiltration works in 2D cells. Choose between *0: Whole surface when raining* (only wet pixels when dry), *1: Always whole surface*, *2: Only wet surface*.
   * - Max. infiltration volume
     - max_infiltration_volume
     - Decimal number
     - No
     - m
     - Maximum infiltration volume (m:sup:`3`/m:sup:`2`). Once this volume has been reached in a cell, there will be no more infiltration in that cell. This global value is superseded in case a maximum infiltration volume file is provided.
   * - Max. infiltration volume file
     - max_infiltration_volume_file
     - Text
     - No
     - m
     - Name of the maximum infiltration volume file. This superseeds the global maximum infiltration volume.

.. _hp_2d_vegetation_drag:

2D Vegetation drag
------------------

The *vegetation drag* table contains the input parameters that are used for 2D flow with vegetation. For an in-depth explanation of how 2D flow with vegetation is calculated by 3Di, see :ref:`flow_with_vegetation`. For more information on using vegetation in your 3Di model and choosing the right parameter values, see :ref:`How to model vegetation<a_how_to_vegetation>`.

Vegetation drag can only be used with friction type 'Chézy', because the vegetation formulation (initially introduced by :cite:p:`Baptist2007`) uses Chézy. 

Raster files can be provided to spatially vary a parameter. If provided, they supersede the global value. If the raster value contains NoData values where the DEM does have data, the global parameter value will be used as fallback value. Raster files need to be stored in a folder called *rasters*, in the same folder as the schematisation geopackage.

This table can contain only one row.

Layer name
^^^^^^^^^^

vegetation_drag_2d

Attributes
^^^^^^^^^^

.. list-table:: Simple infiltration attributes
   :widths: 20 20 15 10 10 40 20
   :header-rows: 1

   * - Attribute
     - Field name
     - Type
     - Mandatory
     - Units
     - Description
   * - ID
     - id
     - Integer
     - Yes
     - \-
     - Unique identifier.
   * - Vegetation height
     - vegetation_height
     - Decimal number
     - Yes
     - m
     - Height of the vegetation, i.e. the length of the plant stems. This global value is superseded in case a vegetation height file is provided.
   * - Vegetation height file
     - vegetation_height_file
     - Text
     - No
     - m
     - Name of the vegetation height file. This supersedes any global vegetation height.
   * - Vegetation stem count
     - vegetation_stem_count
     - Integer
     - Yes
     - #/m\ :sup:`2`
     - Density of plant stems. This global value is superseded in case a vegetation stem count file is provided.
   * - Vegetation stem count file
     - vegetation_stem_count_file
     - Text
     - No
     - #/m\ :sup:`2`
     - Name of the vegetation stem count file. This supersedes any global vegetation stem count.
   * - Vegetation stem diameter
     - vegetation_stem_diameter
     - Decimal number
     - Yes
     - m
     - Mean diameter of plant stems. This global value is superseded in case a vegetation stem diameter file is provided.
   * - Vegetation stem diameter file
     - vegetation_stem_diameter_file
     - Text
     - No
     - m
     - Name of the vegetation stem diameter file. This supersedes any global vegetation stem diameter value.
   * - Vegetation drag coefficient
     - vegetation_drag_coefficient
     - Decimal number
     - Yes
     - \-
     - Coefficient to linearly scale the drag that vegetation exerts on the water. The drag resulting from vegetation is different for each situation. A large share of this variation is captured by choosing the correct values for vegetation height, stem count, and stem diameter. The drag coefficient can be used to account for the other factors that affect the drag. The drag coefficient can also be used as a calibration parameter. This global value is superseded in case a vegetation drag coefficient file is provided.
   * - Vegetation drag coefficient file
     - vegetation_drag_coefficient_file
     - Text
     - No
     - \-
     - Name of the vegetation drag coefficient file. This supersedes any global vegetation drag coefficient.
