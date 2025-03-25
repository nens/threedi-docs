.. _load_schematisation:

Loading a schematisation
========================

You can load a :ref:`schematisation revision<revision>` with the :ref:`schematisation_editor_toolbar`:

#. Click *Add schematisation* |add_schematisation| 
#. Select the schematisation you want to load from your 3Di Working Directory
#. Click *Load*

Your schematisation should now be loaded and you should be able to view all the elements in the *Layers panel*.

.. Note:: 
    If your schematisation database does not have the newest database schema version, it will automatically be migrated so that it is compatible with all the latest features.

.. |add_schematisation| image:: /image/add_schematisation.svg
	:scale: 25%


.. _multiplestyles:

Multiple styles per layer
-------------------------

All layers have multiple predefined styles. These can be helpful to quickly visualise the needed information on the map. 

To switch between stylings:

#. In the *Layer panel*, right-click the layer you are interested in. 
#. Hold your mouse over *Styles* and the multiple styles will be shown. 
#. Click the style you want to use. The style with the dot next to it is the active style. 

To see the details of how the labels and the symbology of the styles are calculated, open the properties dialog: right-click the layer > *Properties* > *Style* and have a look at the categories *Symbology* and *Labels*. Alternatively, open the *Layer styling* panel (*Main menu* > *View* > *Panels* > *Layer styling*)

