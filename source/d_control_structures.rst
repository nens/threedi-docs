Setting up Control Structures
=============================

This sections shows you how to set up a control on structures in your model. It uses a new tool from the QGIS 3Di Toolbox, so make sure you have installed a recent version of the QGIS plugin. Also, check out the workings of the controls at :ref:`control`.

Connect your model
------------------

Start by connecting to the spatialite database through QGIS [1]. Even when you have loaded your model using the *Load database* section of the plugin, you must make an extra connection with your spatialite database to be able to select the database. Open the plugin toolbox [2] and the control structures tool [3]. A screen will pop-up inwhich you can select your model [4].

.. figure:: image/d_control_structures_01.png
	:alt: Open control plugin

Measuring station
-----------------

The second tab shows to overview of the measuring stations in your model. Measuring stations are for instance connection nodes. To add a new station, select the table and id at your desired location. Then click new.

To view all available measuring stations in your model, click *view* or *view all*. 

Measuring group
---------------

Under the next tab, measuring group, you can view and add new measuring groups. The measuring group is a selection of station. Each group may consist of one or more stations station. Their combined weight must equal 1.

To add a measuring group, click new and a new pop-up will appear. Here you can load an existing group to copy it into a new group through *Load measuring group*. Or load indivudual measuring stations into the group. One control group can be used to control several sturctures.

To view all available measuring groups in your model, click *view*.

Rule
----

In the rule tab, you will create and manage your existing rules. At this moment, you are only able to implement a table controlled rule. Click *New* to open the create table control pop-up. Choose the measure variable and operator (see :ref:`table_control`). Then add the table increments with  measuring and action values. Remember that these values are not interpolated. So add sufficient increments to create a smooth transition. Finally, select the structure on which the rule applies and click save.

To view available rules in your model, click *view*. 

Control group
-------------

In the control group a measuring group and a rule are combined to create a control. You may use one measuring group for multiple controls. The rule applies to one structures and can be used only once in each group.

Add a control by clicking new and fill in the name and description of the control you are about to create. Then select the measuring group id and rule id for your first rule and click new. Add extra combinations if you wish to use multiple controls in your model. Only one control group will be active, so make sure all rules for your model are listed in one group. When your done, click *Save*.

You can define multiple groups in one spatialite database, but only one is active per model scenario (or glabal settings entry). You must therefore specify the *control group id* in the global settings for your scenario(s). This is the final step in activating the controls.