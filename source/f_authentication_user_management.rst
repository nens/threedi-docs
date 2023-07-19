.. _f_authentication_user_management:

Authentication and user management
==================================

.. _a_singing_up:

Signing up
--------------

New users require an invitation to create a 3Di account. Users with a 'manager' role within an organisation are able to :ref:`send invitations <a_user_management>`.
If you do not know whom to contact, please contact our :ref:`servicedesk` at servicedesk@nelen-schuurmans.nl.

If you have received an email from either a manager within the organisation or the servicedesk:

#) Open the invitation link in the email. 

#) Click on 'Sign up' and fill in the required fields. **Please use the same email as the invitation was sent to.** Using another email will not work.

#) Check your email for the required verification code.

#) You should now be redirected to the API root. This means you have created a 3Di account and have access to the organisation.

.. note::
   If you see a **403 error** after openining the invitation email, please try to open the url in an **incognito** window before reaching out to the Servicedesk.

.. _a_singing_in:

Signing in
----------
Users can login in either the Modeller Interface, 3Di Live, the Management Screens and the API.
Except for the Modeller Interface, all 3Di components will redirect you to the following login screen:


.. figure:: /image/a_login.png
   :alt: The login screen

   The login screen.


If you do not have an account yet, please read  ':ref:`a_singing_up`' first. 
If you do have an account, you can either log in by using your company account or by using your credentials, in case your company is listed on the left part of the login screen. Loging in via your company account is the preferred option.
Existing users should use the same method as they used when signing in for the first time.

.. warning::
   Due to our authentication update in May 2022 it might occur that you cannot log in anymore. Please use the ':ref:`a_singing_up`' guide to create a new account.

.. tip::
    Do you want to add your company to the list to centralise the user accounts
    of your organisation? Please contact our support office
    (servicedesk@nelen-schuurmans.nl) for the options.

.. _a_user_management:

User management
---------------


.. figure:: /image/a_usermanagement1.png
   :alt: The User Management interface.

   The User Management interface.


Users can be managed in the User Management interface. This interface can be reached via https://api.3di.live/management/users/.
The example above shows the list of users in the example organisation '3Di Test', with for each user options for 4 roles. These role are desribed as: 

* A **Viewer**, who can only *read* data and *follow* simulations
* A **Simulation runner**, who can *read* data and *run* simulations
* An **Creator**, who can *read* data and can *add*, *change* or *delete* schematisations and 3Di models
* A **Manager**, who can *manage* other roles in the organisation. A manager can not read or write data by default. This role should be appointed separately. 

The User Management interface gives you an overview of all users in your organisation. As manager you can distribute the roles to all users within the organisation.
This is done by clicking the '+' next to the user and choose the roles you want to assign tot the user. Click “Save” to save the changes.
If you are Manager of multiple organisations you can switch between organisations by using the selection menu next to your username.  

   
.. note::
    A manager role is required to access the User Management interface.
    If you wish to obtain one for your organisation, please contact the application manager within your organisation or our :ref:`servicedesk` at servicedesk@nelen-schuurmans.nl.
	

**Adding a new user**

You can add a new user by clicking the “NEW USER” icon in the upper right corner. This will lead you to the screen to add a new user.


.. figure:: /image/a_usermanagement2.png
   :alt: The interface for adding a user.

   The interface for adding a user.
   

By default the new user is granted a 'Viewer' role. At least one role is required when inviting a new user.  
Press the 'Save' button to finish the invitation process, which results in an invitation email sent to the (new) user. An existing user can use the invitation link to accept the invitation. 
A new user can create an account by using the :ref:`a_singing_up` guide. When accepted, the user will appear in the User Management overview.


.. note::
   * The invitation email might end up in your spam folder. 
   * Deselecting all roles will remove the user from the organisation, but will not delete the account of the user.
   * You cannot remove your own manager role.	


	

Authorisation
-------------

Within 3Di the data governance structure is set up per organisation. Users within the same organisation can see all models that are build under their organisation. 
Sharing models with external users is also possible. The two options are:

- External users get access to the 3Di subscription of the organisation. By handing out Viewer and Simulation runner roles, the user can access and run the models.
- Allow External users Viewer priveleges. This enables them to download the 3Di Models, so they can use their own subscription of their organisation to run simulations.


.. _personal_api_key:

Personal API Key
-----------------

When you login via your browser, your browser receives a session cookie.
All subsequent requests to the API are authenticated with that session cookie.

Authenticating to the REST API outside of a browser is done by attaching a
Personal API Key to *every* request. You can attach a Personal API Key to 
a request by using HTTP Basic Authentication with password = {your api key}.
The username needs to be fixed to ``__key__`` (with double underscores on both
sides of the word "key").

Almost all applications or script languages support HTTP Basic Authentication.

Generate a Personal API key at https://management.3di.live/personal_api_keys.
It is considered best practise to generate one Personal API Key per application
or script, so that you can selectively revoke keys in case they are compromised.