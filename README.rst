3Di documentation
=================

Let's try to do it with restructuredtext/sphinx!

The released documentation is at https://docs.3di.live/ .

The latest version of master is at https://docs.staging.3di.live/, you can use
this for checking if the documentation is OK to be released.

Commits are automatically tested on "travis":
https://travis-ci.com/nens/threedi-docs/, this makes sure all images are there
and that there are no missing files. Travis also uploads the
documentation. You can check the progress at:

- https://artifacts.lizard.net/overview/threedi-docs-staging/ (master builds)

- https://artifacts.lizard.net/overview/threedi-docs-production/ (tag builds,
  so releases).


Local setup
-----------

If you can run docker, you're in luck. One-time setup::

  $ docker-compose build

And then every time you want to re-generate your documentation::

  $ docker-compose up

If you're not so lucky, you'll need to pip-install sphinx (``pip install -r
requirements.txt``, preferably in a virtualenv) and you need latex (see the
`Dockerfile` for the short list of packages that we install).


Special commands
----------------

If the sphinx documentation tells you about a makefile: you can run those
commands from within docker, too. For example::

  $ docker-compose run builder make latexpdf


Images
------

Images should be lowercase. If you've added an image, please run this command
to be sure::

  $ docker-compose run builder python3 fix-uppercase-lowercase.py


Some sphinx/restructuredtext notes
----------------------------------

You'll need to learn a bit of restructuredtext:
http://www.sphinx-doc.org/en/stable/rest.html

Special stuff, cross-references, indices etc:
http://www.sphinx-doc.org/en/stable/markup/index.html

Math support ("it is all LaTeX"):
http://www.sphinx-doc.org/en/stable/ext/math.html


Any questions: ask Reinout.


Some commands needed for the OSGEO4W Shell with sphinx
------------------------------------------------------

From the git directory run the following commands::

    pip install sphinx
    sphinx-build threedi-docs\source build

You will recieve some warnings, check them. You are not able to evaluate LateX
formulas this way.


Making a release
----------------

Only released versions are shown on docs.3di.lizard.net. To make a release,
install zest.releaser::

  $ pip install zest.releaser

(It is also installed inside the docker, but your git credentials won't work
in there.)

Make a release by running::

  $ fullrelease

You can normally answer all the questions with <enter>.
