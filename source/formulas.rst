Formulas
========

I've currently set it up so that images are generated. These are usable in the
PDF output. The javascript formulas are not.

See http://www.sphinx-doc.org/en/stable/ext/math.html for instructions.

You can have inline formulas, like :math:`F = m * a`.

And you can have more elaborate formulas. You can link to them (see the
:doc:`introduction`):


.. math::
   :label: example_formula

   25 = 2 * x^2 + 3 * y + 20


Example from the documentation:

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}
