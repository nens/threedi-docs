3Di documentation
=================

This repository contains the source code of the 3Di documentation.

The released documentation is at https://docs.3di.live/ .

The latest version of master is at https://docs.staging.3di.live/; you can use
this for checking if the documentation is OK to be released.

Commits are automatically tested on "github actions":
https://github.com/nens/threedi-docs/actions; this makes sure all images are there
and that there are no missing files. Github Actions also uploads the
documentation. You can check the upload status at
https://artifacts.lizard.net/ if you want to make sure a release happened
(note: a full documentation build can take up to three minutes).


Local setup
-----------

If you can run docker, you're in luck. One-time setup::

  $ docker compose build

And then every time you want to re-generate your documentation::

  $ docker compose up

If you're not so lucky, you'll need to pip-install sphinx (``pip install -r
requirements.txt``, preferably in a virtualenv) and you need latex (see the
`Dockerfile` for the short list of packages that we install).


Special commands
----------------

If the sphinx documentation tells you about a makefile: you can run those
commands from within docker, too. For example, to build the pdf version::

  $ docker compose run builder make latexpdf

(The output is in ``build/pdf/3di.pdf``).


Images
------

Images should be lowercase. If you've added an image, please run this command
to be sure::

  $ docker compose run builder python3 fix-uppercase-lowercase.py


Literature & citations
----------------------

The bibliography is stored in a BibTeX file (source\literature.bib). You can edit this file with citation manager software such as Mendeley. Make sure each entry has a *citation key*. We use the first author name + year, e.g. `Volp2013` as citation key.

When the citation has been added to the .bib file, cite it in the text like this::

  For further details, see :cite:p:`Volp2013`

QGIS icons
----------

Instead of screenshotting the icons from QGIS, you can find the originals here: https://github.com/qgis/QGIS/tree/master/images/themes/default


Some sphinx/restructuredtext notes
----------------------------------

You'll need to learn a bit of restructuredtext:
http://www.sphinx-doc.org/en/stable/rest.html

Special stuff, cross-references, indices etc:
http://www.sphinx-doc.org/en/stable/markup/index.html

Math support ("it is all LaTeX"):
http://www.sphinx-doc.org/en/stable/ext/math.html

You can add TODO comments like this::

  .. todo::

     Add screenshot of the graph

These will be hidden *automatically* when rendering the released
documentation. In the staging documentation, they're visible.

Any questions: ask Reinout.


Schematisation checks list
--------------------------
A list of checks currently executed by the modelchecker is in current_schematisation_checks_table.
As new checks are added to the modelchecker, this table should be updated. When a new version of the
modelchecker is released, a pull request to update the checks table will automatically be opened in
this repository, requesting a review from the person who created the modelchecker release.


Some commands needed for the OSGEO4W Shell with sphinx
------------------------------------------------------

From the git directory run the following commands::

    pip install sphinx
    sphinx-build threedi-docs\source build

You will receive some warnings; check them. You are not able to evaluate LateX
formulas this way.


Making a release
----------------

If the release is for a new version of 3di, change ``THREEDI_RELEASE`` at the
top of ``source/conf.py``.

Only released versions are shown on docs.3di.lizard.net. To make a release,
install zest.releaser::

  $ pip install zest.releaser

(It is also installed inside the docker, but your git credentials won't work
in there.)

Make a release by running::

  $ fullrelease

You can normally answer all the questions with <enter>.
