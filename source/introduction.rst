.. _introduction.rst:

Introduction
############

Considérons un patient insomniaque :math:`P` se rendant à l'hôpital pour effectuer une électroencéphalographie. Plusieurs électrodes seront placées sur son crâne, et après avoir passé une nuit en clinique, les médecins sauront lui trouver un remède à ses troubles du sommeil.

Le cerveau est le siège d'une intense activité électrique. On distingue plusieurs régions et niveaux d'activités différents qui produisent chacuns des fréquences électriques différentes. Ainsi, le signal final est un méli-mélo de superposition de fréquences et intensités électriques différentes : comment alors séparer les informations ?

..  figure:: figures/electro_cerveau.png
    :width: 80%
    :align: center
    
    Electroencéphalographie d'une seconde

Appelons :math:`f(t)` la fonction réelle décrivant cette courbe. Nous admettons de pouvoir décomposer notre signal avec une série de Fourier :

.. math::
  
  f(t) = \sum_{n=1}^\infty \left(a_n\cdot \cos(nt)+b_n \cdot \sin(nt)\right)

Cela signifie que la fonction :math:`f` se laisse écrire comme la superposition


