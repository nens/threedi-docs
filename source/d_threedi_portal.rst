.. _guide_to_portal:

Guide to the 3Di Live Site
=====================================

Login
------

Follow the steps below to access the 3Di Live Site:

#) Start the internet browser (Chrome or Firefox) and go to: https://3di.live
#) Log in with your username and password.

	* Username and password can be requested via servicedesk@nelen-schuurmans.nl.


.. figure:: image/d2.1_login.png
	:scale: 50%
	:alt: Login screen
	
Welcome to 3Di
--------------

After logging in to the 3Di Live Site, the screen *Welcome screen* will show:

.. figure:: image/d2.2_login.png 
	:alt: Welcome to 3Di screen

In this screen, there are two possibilities:

* Start a new session using the :ref:`start_a_new_session` tab.
* Follow an ongoing session via the :ref:`follow_a_session` tab.

.. _follow_a_session:

Following a session
--------------------

Through the tab **Follow session** an active session of your organization can be followed. Select an active simulation and press **follow**. The number of followers of a session is not limited. To leave the session, got to the **user menu** under the user icon (top right) and press **Leave session**. 


.. _start_a_new_session:

Start a new session
--------------------

* Select the **New session** tab. 
* Select your company in the **Billing goes to:** drop down menu. 
* Select the model you want to start.

A new session will be started. During the start up of the model tips for use of the site will be shown. It may take several minutes to load the model. Actual loading time is dependent on model size, calculation grid and table step size.

.. figure:: image/d2.4_start_session.png 
	:alt: Start new session

*For each organization, the number of simultaneous sessions is limited according to the agreement (contract). If the limit is reached, the message "Your organization is already running X sessions" will show. The amount of server time used is subtracted from the time available within the agreement.*



Main session
------------

When starting or following a session, the screen in :numref:`fig_main_ses` will be loaded. The loaded model will be shown in the complete extent. At the top left you can see the name of the loaded model.


.. _fig_main_ses:

.. figure:: image/d2.6_main.png 
	:alt: Main session

	Interface main session.


1. With the **Start simulation** button, the simulation can be started and once started paused. 
2. Here the simulation run time will be indicated in hours:minutes.
3. Indicates the load of the model on the server in %.
4. The :ref:`user_menu`.
5. The Search Bar.
6. The bar from top to bottom contains: 

- point tool
- side view tool
- add a discharge point (2D)
- add a pumping point (2D)
- add rainfall
- add wind
- edit the DEM of the model

7. layer tool

For the visualization of the model elements, see the :ref:`layers_menu`.

.. _user_menu:

User menu
----------

Click the user icon at the top right of the screen to show the **User menu**. The user menu has the following options:

Preferences
"""""""""""

.. figure:: image/d2.8_user_menu.png 
	:alt: User menu

**Calculation speed** 
Calculation speed on the live site is slowed down (**capped speed**) by default in case of fast models. This is done because the live site is meant to have live insights in what is happening. If the model is too fast, it is hard to understand the flows. 
If you want to calculate on full speed, choose the **Real-time speed** option. The model most likely will speed up in case the % on the top right of the screen was not indicating 100% already. In case the server load is at 100%, no gain will be seen in calculation speed on the live site.


Help
""""
Currently sends you to https://3diwatermanagement.com/3di-start/.
For support from the help desk, visit :ref:`https://3diwatermanagement.com/3di-start/`.


Quit simulations
""""""""""""""""
:ref:`timeoutlivesite` ends the use of calculation time. And let's you save your results.

You can:

- **Quit, don't store results**
- **Quit, store results**, for more information, see: :ref:`store_results_live_site`.

*link naar results toevoegen* 

Restart simulations
"""""""""""""""""""
Restarting the simulation resets all the calculations that have been made and reloads the simulation. If you want to save your results you will get sent back to the start screen afterwards.


.. _layers_menu:

Layers menu
----------------

Click on the globe at the top right of the screen. The layers menu appears. 

If the model contains 1D-elements, they are immediately visible. Depending on which 1D elements are present in the model (and turned on in the maplayers menu, you will see:

- Breaches (shown after zooming in)
- Channels
- Culverts
- Levees
- Manholes (shown after zooming in)
- Nodes
- Sewers 
- Pump stations 
- Weirs

Colors for all these layers can be changed to reflect user preferences

In the maplayers menu the background map can be chosen:

- Topographic
- Satellite
- Dark

In the calculation section all layers are shown that indicate a results of the simulation on the map:

- Waterdepth
- Flow velocity
- Model grid 

Model rasters:

 - Digital Elevation Model. This shows the DEM that is used in the model. 

Advanced:

- Here other raster layers will be shown if present in the model:

All layers can toggled on or off by simply clicking on them in the layer menu. 


.. _timeoutlivesite:

Quitting the simulation
------------------------

In the menu under the user icon, quitting the simulation ends the use of calculation time. If this option is not used the session remains active. One of the following scenario's might apply:

- time out after being inactive is set to 30 minute for a running simulation
- time out after being inactive is set to 5 minute for a paused simulation
- leaving the session via a tab will close the simulation after 30 minutes


.. _store_results_live_site:

Saving results
--------------
*verhaal van scenario toevoegen hier*

.. _notables:

Notables
----------

- When inactive for too long, the session will close 'This simulations is no longer active. You may start a new simulation.'
- Editing of structures or DEM can only be done after *pausing* a simulation.
- In the current setup special attention to models with initial water levels in 2D and laterals. 
- Initial water level in 2D is taken into account, but only with the 'max' parameter.
- Laterals in a model are at the moment not used in the live site.
- The color scheme of the water depth can not be changed in the live site
- The language of the site will change depending on the language settings of your browser. Currently mandarin, english and dutch are supported. Please keep in mind that model elements are never translated. 
- Manholes are turned off by default. Turning them on and zooming out might cause the live site to slow down.
- Water depth is not shown in the channel nodes.