"""""""""""""""""""""

Managers rechten 3Di
"""""""""""""""""""""

Wat zijn de taken die vallen op een Manager van een organisatie
===============================================================

De rol van manager is belangrijk voor het beheer van de data van een organisatie.
Als manager verleent u rechten voor uw organisatie, of neemt u deze af.
Een manager heeft voornamelijk twee taken:

1. Het onderhouden van de rechten van bestaande gebruikers
2. Het verlenen van rechten aan nieuwe medewerkers of externe partijen

**Onderhouden rechten van bestaande gebruikers**

De rechten van gebruikers die onder uw organisatie vallen vervallen niet automatisch.
Het is dus van belang dat u met enige regelmaat controleert of gebruikers hun rechten nog nodig hebben.
Dit kan dan gaan om werknemers die de organisatie verlaten, maar ook om een project wat af loopt.
Soms hoeven niet alle rechten afgenomen te worden, ook dit is mogelijk.
Het is aan u om te bepalen hoe vaak u dit wil controleren.

**Verlenen rechten nieuwe gebruikers**

Als een gebruiker rechten nodig heeft voor uw organisatie bent u hiervoor verantwoordelijk.
Voor het spoedig verloop van een project is het handig om dit soort verzoeken met enige spoed af te handelen.
Het verlenen van rechten hoeft ook geen langdradige klus te zijn, met een minuut zijn de rechten al verleend.
Hoe dit exact in zijn werk gaat leest u in `Een extern of nieuwe projectmedewerker rechten geven tot de organisatie.`_.

.. tip:: Gebruik een bookmark om direct naar de Management-pagina te komen. Op deze manier kan je binnen no-time een gebruiker rechten geven.


Welke rechten zijn er te verdelen en wanneer is dit nodig?
==========================================================

**Viewer**

De basis van de basis. 
Als viewer kan je data lezen vanuit de API van de desbetreffende organisatie, en je kan simulaties van andere volgen. 
Deze gebruikers kunnen zelf geen simulaties starten of maken.

**Simulation Runner**

Met deze rol kunnen gebruikers zelf simulaties starten met schematisaties en modellen die aangeleverd zijn vanuit de organisatie.
Deze rol gaat altijd in combinatie met de viewer rol om te zorgen dat de gebruiker de simulatie ook kan volgen.


**Creator**

De creator rechten zijn nodig om nieuwe schematisaties en modellen aan te leveren aan 3Di. 
Creator's kunnen ook data lezen in de API.
Om de aangeleverde modellen te draaien zijn de voorgaande rechten nodig.
 
**Manager**

De manager geeft en neemt rechten van andere. 
Een manager kan ook de rechten van een andere manager afnemen. 
Zorg dus dat u alleen vertrouwde partijen managers rechten geeft.

.. tip:: In sommige situaties ontstaant organisaties voor specifieke projecten. 
    Als de data binnen dit project onder uw organisatie valt en u wilt hiervoor een manager aanstellen, 
    neem dan contact op met de `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_.


Het managementscherm
====================

Het managementscherm bied de mogelijkheid om verschillende aspecten van je organisatie te beheren.
Denk hierbij aan het beheren van uw data: schematisaties, scenario's, gebruikers en meer. 
Voor het complete gebruik van deze managementschermen kunt u terecht op de `3Di documentatie <https://docs.3di.live/index.html>`_.
Belangrijkste is in dit geval het "User Management".
Alleen managers hebben toegang tot het "Users" scherm.
Het is in dit scherm dat u:

1. Nieuwe gebruikers kunt uitnodigen.
2. Bestaande rechten kunt aanpassen.


Nieuwe gebruikers uitnodigen
----------------------------

Als een nieuwe gebruiker toegang tot Lizard nodig heeft vanuit de organisatie kunnen deze verleend worden door de Manager.
Dit gebeurt als volgt:

1. U logt in op het portaal van de organisatie (https://management.3di.live/).
2. Ga naar het gebruikersgedeelte in het managementscherm (https://api.3di.live/management/users/).
3. Klik op `+ NEW USER` rechts boven in het scherm (afbeelding 1).
4. Type het e-mail van de gebruiker in de 'e-mail' balk (afbeelding 2).
5. Selecteer de rollen die de gebruiker krijgt. Voor de rechten die aan de rollen gekoppeld zitten kunt terug vallen op `rechten <Welke rechten zijn er te verdelen en wanneer is dit nodig?>`_.
6. Klik op `SAVE`.
7. Het is gelukt! De uitnoding is verstuurd en zal binnen 5 minuten in de mailbox van de nieuwe gebruiker belanden.

.. tip:: Als u `need help?` klikt krijgt u ook een overzicht van de rollen en de daaraan gekoppelde rechten te zien. 

.. tip:: Wanneer de e-mail niet in de inbox verschijnt na 5 minuten, controleer dan eerst uw spam. Mocht de uitnodiging hier ook niet zijn, dan kunt u altijd de `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_ benaderen.

.. figure:: /images/threedi/threedi_overzicht_rechten.png
    :scale: 50%
    :alt: Overview of the 3Di management page with multiple users.

    Afbeelding 1: Een overzicht van het gebruikersgedeelte in het managementscherm van 3Di.


.. figure:: /images/threedi/threedi_uitnodiging_rechten.png
    :scale: 50%
    :alt: Invitation screen for new users of 3Di. Enter an e-mail and select the roles for the new user.

    Afbeelding 2: Het uitnodigingscherm voor nieuwe gebruikers. U selecteert de rollen door er op te klikken.


Bestaande rechten aanpassen
---------------------------

In het gebruikersrechten overzicht scherm kunt u de rechten van bestaande gebruikers beheren.
U ziet hier de volgende informatie van gebruikers die rechten hebben voor uw organisatie:

1. Gebruikersnaam / Username
2. Rollen / Roles
3. Email

Door op het plusje achter de rollen van een gebruiker te klikken kunt u de rechten gaan aanpassen.
De plus knop veranderd dan ook in `SAVE`. Zodra de rechten naar wens zijn klikt u op `SAVE` om dit te bevestigen.

.. figure:: /images/threedi/threedi_rechten_bestaande.png


Tips
=============

.. tip:: Zorg dat direct aan het begin van een project rechten worden besproken en verleend.
    Dit voorkomt dat er later vertraging plaats vindt doordat iemand moet wachten op zijn rechten.

.. tip:: Vergeet na het afsluiten van een project niet de rechten van gebruikers niet te verwijderen.
    Op deze manier houd u actief de gebruikersdatabase bij en is uw data onder uw controle.
    Controleer hierbij wel of er geen scripts draaien op een API KEY van een van deze gebruikers.

.. tip:: Mocht u accounts willen deactiveren, neem dat contact op met de `servicedesk <mailto:servicedesk@nelen-schuurmans.nl>`_