.. _apicalculations:

API & Scripts
================

3Di has a completely API based setup. An API is an Application Programming Interface, and it enables software applications to talk with one another. The API is the connection between our user interfaces and the calculation core. Next to that, it is also possible as a user to interact with the API directly. This is for more advanced users, familiar  with programming languages. The benefit of directly using the 3Di API is:

- Batch calculating
- Automated testruns & results checking 
- Run 3Di in an operational setting 
- Use Jupyter Notebooks to run, download en analyze 3Di simulations
- Use other applications 


.. figure:: image/d_api_3di_ecosystem.png
    :alt: 3Di Eco system

The current production API of 3Di is v3. For previous versions of the API check this section :ref:`api_v1`

We support two versions of our API:

* API v3: stable
* API v1: deprecated

There is also a seperate API, which we call the Result API.

The API V1 is deprecated and will disappear in the near future.

.. _api_v3:

API v3
-------------

API v3 is available here: https://api.3di.live/v3.0/swagger/

Here you can find `the API documentation <https://api.3di.live/v3.0/docs/>`_.
We also created a webinar that takes you through the API functionalities. Here you can find `the webinar <https://attendee.gotowebinar.com/recording/1129052614373219341/>`_.

Here you can find a more `detailed technical overview <https://nens.github.io/threedi-openapi-client/usage/>`_  of our API.


.. note::
    To use the API v3 with a model created earlier with API v1, you need to re-run inpy for your model. After that it will appear in both API v1 and v3. Find out how to re-run `inpy <https://docs.3di.live/d_threedi_versioning.html#rerun_inpy>`_.

[add] examples, link to notebooks of Valerie

[add] a little history of our API (refer to v1) explain there is no v2

.. _api_v1:


API v1
-------------


With the API you can request simulations without having to access the 3Di web portal and follow your simulation. It is ideal for making various calibration runs. Also, it allows you to use several types of external forcing not available through the web portal and save and use states or restart files.

Visit https://3di.lizard.net/api/v1/calculation/start/ for all options.

Using POSTMAN

The first step is to install POSTMAN as an extension on Google Chrome.

Then take the following steps:

1. Log-in using a POSTMAN account. This account is not linked to 3Di.

.. figure:: image/d_postman_login.png
   :alt: Postman Login

   Postman Login

2. Select POST (instead of GET) left of URL

3. Enter this URL: https://3di.lizard.net/api/v1/calculation/start/

4. Select basic authorisation

.. figure:: image/d_postman2_url.png
   :alt: Postman URL

   Postman URL

5. Enter your 3Di username and password

6. Select update request

.. figure:: image/d_postman3_updaterequest.png
   :alt: Postman Update Request

   Postman Update Request

7. Click on Body 

8. Select 'raw' 

9. Select JSON from the drop-down

10. Enter the raw json body, that's the part between {} and consists of multiple lines.

11. Click Send

.. figure:: image/d_postman4_send.png
   :alt: Postman Send

   Postman Send

   
Note that postman stores your password which poses a possible security risk.

*Times*

All dates and times used in the API are based on the so-called ISO8601 standards. You can use your local times and add the off set to UTC Time. More about these standards can be found on `Wikipedia <https://en.wikipedia.org/wiki/ISO_8601>`_. In the example below:

    2016-06-22T18:00+02:00

This rainfall event will start at 18:00 hour local time.

Result API
------------

The Result API can be found `here <https://threedigrid.readthedocs.io/en/latest/>`_.

