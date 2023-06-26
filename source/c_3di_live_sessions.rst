.. _3di_live_sessions:

Sessions
========

To start or follow a 3Di Live session, open your browser and go to https://3di.live and log in with your username and password. If you do not have a 3Di account yet, or do not know your username and password, please contact the :ref:`servicedesk`.

After logging in to the 3Di Live Site , the *Welcome screen* will be shown. In this screen, there are two possibilities:

* Start a new session using the :ref:`start_a_new_session` tab.
* Follow an ongoing session via the :ref:`follow_a_session` tab.

.. _start_a_new_session:

Starting a new session
----------------------

* Click *New session*. 
* If you have simulation rights for multiple organisations, use the *Billing goes to* dropdown menu to select the 
* Select the model you want to use to start a simulation with. You may type the model name in the search bar to find it.

A new session will be started. During the start up of the model tips for use of the site will be shown. It may take some time to load the model. Actual loading time dependens on the model size; for large models, this may take several minutes.

.. note::

	The number of sessions that can run simultaneously by your organisation depends on your organisation's 3Di subscription. If this limit is reached, the message "Your organization is already running X sessions" will be shown.
	
	If you organisation has a limited number of simulation hours in its subscription, the time that the session is active is subtracted from the available number of hours for the current year.
	
	When paused and inactive for too long, the session will close and say: 'This simulations is no longer active. You may start a new simulation.'



.. _follow_a_session:

Following a session
-------------------

Active sessions of your organisation can be followed. This may be a session that you started earlier (e.g. from the :ref:`3Di Modeller Interface<running-a-simulation>`), or a session that someone else in your organisation has started.

In the *Follow session* tab, Select an active session and click *Follow*. The number of followers of a session is unlimited. To leave the session, either close your browser tab, or click the *User* icon (top right) > *Leave session*. 


.. _user_menu:

User menu
^^^^^^^^^^

You can access the *User menu* by click the user icon at the top right of the screen. The user menu has the following options:

Preferences
"""""""""""

.. figure:: image/d2.8_user_menu.png 
	:alt: User menu

**Calculation speed** 
The Calculation speed is the rate at which the calculations are shown on screen. The Calculation speed is slowed down (**capped speed**) by default. This is done because the Live Site is meant to give a live insights in what is happening. If the model is too fast, it can be hard to understand the flows. 

If you want to calculate on full speed, choose the **Real-time speed** option. The model most likely will speed up in case the % on the top right of the screen was not indicating 100% already. In case the server load is at 100%, no gain will be seen in calculation speed on the Live Site.

.. _restart_session:

Restarting sessions
-------------------
Restarting the simulation resets all the calculations that have been made and reloads the simulation. If you want to save your results you will get sent back to the start screen afterwards.


.. _quit_session:

Quitting the session
--------------------

In the **User menu** you can select **quitting the simulation**, this ends the use of calculation time. If this option is not used the session remains active. One of the following scenario's might apply:

- time out after being inactive is set to 30 minute for a running simulation
- time out after being inactive is set to 5 minute for a paused simulation
- leaving the session via a tab will close the simulation after 30 minutes

You can:

- **Quit, don't store results**
- **Quit, store results**


.. _store_results:

Storing results
---------------

Results can be stored by clicking **User menu**, then clicking **Quit Simulation** and then **Quit, Store Results**. There are two options:

- Download results directly via the browser
- Store them to the Lizard platform (see https://docs.lizard.net/a_lizard.html) 

Stored (raw) results can also be downloaded using the"3Di Models and Simulations" in the 3Di Modeller Interface, see: :ref:`mi_download_res`. Note that these raw results are only available for 7 days.

The options in Lizard storage are as follows:

- raw data and logging
- basic processed results
- arrival time map
- damage estimation (NL only)

The **Basic processed results** option includes the following derivations from simulation results for Lizard users:

.. figure:: image/d3.9_store_results.png
    :alt: Storing results

- Water level - temporal
- Water depth - temporal
- Maximum flow velocity
- Maximum rate of rise
- Maximum water depth
- Flood hazard rating

The **Damage estimation** option uses a module called *WaterSchadeSchatter* (currently only available in The Netherlands)
which provides two products derived from the maximum water depth.

- Damage estimation map
- Damage estimation table
