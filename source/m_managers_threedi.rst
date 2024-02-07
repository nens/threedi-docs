:orphan:

========
Managers
========

What are the tasks of a Manager in an organization
=================================================

The role of a manager is important for managing the data of an organization.
As a manager, you grant or revoke rights for your organization.
A manager mainly has two tasks:

1. Maintaining the rights of existing users
2. Granting rights to new employees or external parties

**Maintaining rights of existing users**

The rights of users under your organization do not expire automatically.
So, it is important that you regularly check whether users still need their rights.
This can include employees leaving the organization or projects coming to an end.
Sometimes, not all rights need to be revoked, this is also possible.
It is up to you to determine how often you want to perform this check.

**Granting rights to new users**

If a user needs rights for your organization, you are responsible for granting them.
For the smooth progress of a project, it is useful to handle such requests promptly.
Granting rights also doesn't have to be a lengthy task; rights can be granted in a minute.
You can learn exactly how this works in `Inviting new users`_ and `Adjusting existing rights`_.

.. tip:: Use a bookmark to go directly to the Management page. This way, you can give a user rights in no time.

Roles and their rights
======================

**Viewer**

The basics of basics.
As a viewer, you can read data from the API of the respective organization, and you can follow simulations of others.
These users cannot start or create simulations themselves.

**Simulation Runner**

With this role, users can start simulations themselves with schematics and models provided by the organization.
This role always goes in combination with the viewer role to ensure that the user can also follow the simulation.

**Creator**

Creator rights are needed to provide new schematics and models to 3Di.
Creators can also read data from the API.
To run the provided models, the previouslty mentioned roles are necessary.

**Manager**

The manager gives and takes roles from other users.
A manager can also revoke the rights of another manager.
So, make sure to only give manager role to trusted parties.

.. tip:: In some situations, organizations arise for specific projects.
    If the data within this project falls under your organization and you want to appoint a manager for this, 
    please contact the `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_.

The management screen
=====================

The management screen offers the opportunity to manage various aspects of your organization.
This includes managing your data: schematics, scenarios, users, and more.
For complete use of these management screens, refer to the `3Di documentation <https://docs.3di.live/index.html>`_.
Only managers have access to the "Users" screen.
This is where the user management takes places, which is at the heart of this page.
In this screen, you can:

1. Invite new users.
2. Adjust existing rights.

Inviting new users
------------------

If a new user needs access to Lizard from the organization, this can be granted by the Manager.
This is done as follows:

1. Log in to the organization's portal (https://management.3di.live/).
2. Go to the user section in the management screen (https://api.3di.live/management/users/).
3. Click on `+ NEW USER` at the top right of the screen (image 1).
4. Type the user's email in the 'email' field (image 2).
5. Select the roles the user will have. For the rights associated with the roles, refer to `Roles and their rights`_.
6. Click `SAVE`.
7. Success! The invitation has been sent and will be in the new user's mailbox within 5 minutes.

.. tip:: Clicking `need help?` will also show you an overview of the roles and the rights associated with them.

.. tip:: If the email does not appear in the inbox after 5 minutes, first check your spam folder. If the invitation is not there either, you can always contact the `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_.

.. figure:: /image/m_threedi_overzicht_rechten.png
    :scale: 50%
    :alt: Overview of the 3Di management page with multiple users.

    Image 1: An overview of the user section in the management screen of 3Di.


.. figure:: /image/m_threedi_uitnodiging_rechten.png
    :scale: 50%
    :alt: Invitation screen for new users of 3Di. Enter an email and select the roles for the new user.

    Image 2: The invitation screen for new users. You select the roles by clicking on them.

Adjusting existing rights
-------------------------

In the user rights overview screen, you can manage the rights of existing users.
Here you see the following information of users who have rights for your organization:

1. Username
2. Roles
3. Email

By clicking on the plus sign next to the roles of a user, you can start adjusting the rights.
The plus button will then change to `SAVE`. Once the rights are as desired, click `SAVE` to confirm.

.. figure:: /image/m_threedi_rechten_bestaande.png


Tips
=============

.. tip:: Ensure that rights are discussed and granted at the beginning of a project.
    This prevents delays later due to someone waiting for their rights.

.. tip:: Don't forget to remove users' rights after a project is completed.
    This way, you actively maintain the user database and keep your data under control.
    However, be sure to check if any scripts are running on an API KEY of any of these users.

.. tip:: If you want to deactivate accounts, contact the `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_ for assistance.
