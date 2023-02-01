Pour s'amuser
###############

Sous-titre
==========

sous-sous-titre
-------------

..  admonition:: Message
    salut

..  warning::
    attention

..  error::
    fais gaffe

..  note::
    salut

petit tableau
=============

.. csv-table:: Table Title
   :file-path: CSV file path and name
   :widths: 30, 70
   :header-rows: 1

   Prénom, nom
   Guido, Van Rossum
   Alan, Turing,
   Ada, Lovelace

images
======

..  figure:: figures/Moleson
    :width: 80%
    :align: center

    La plus belle montagne

mathématiques
=============

On peut mettre des formules dans le texte :math:`\sin^2(x)+\cos^2(x)`

..  math::
    \begin{equation}
    \frac{1}{p_i} \neq 1
    \end{equation}

..  raw:: latex
    \begin{equation}
    \frac{1}{p_i} \neq 1
    \end{equation}


Inclure du code
==============

..  literalinclude:: scripts/factorial.py
    :linenos:
    :emphasize-lines: 1