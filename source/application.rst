.. _Application.rst:

Application
###############

L'algorithme de FFT permet une implémentation efficace des transformées de Fourrier dans de nombreux domaines. Nous allons en approfondir deux en particulier, mais notons que l'algorithme apparaît dans presque tous les domaines, essentiellement en informatique et ingénierie, mais aussi en mathématiques, où il permet par exemple la résolution d'équations différentielles ou la factorisation d'entiers. Un ami à moi, Jan Birmanns, a même mis au point un algorithme d'interpolation de courbes au moyens d'épycicles à l'aide de quaternions et de la FFT (le travail de maturité est disponible `ici <https://www.math.ch/about-sms/matura-awards/MA_JanBirmanns.pdf>`_)

Traitement de signal
==========

Dans de nombreux logiciels de traitement sonore, il est possible d'augmenter ou de baisser la hauteur d'un échantillon de son, ou alors de supprimer de bruits de fonds par exemple.

..  admonition:: Pitch Shift
    ..  figure:: figures/spectrum.gif
    :width: 80%
    :align: center

    La plus belle montagne

    auto-tuner

Compression de fichiers
==========



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