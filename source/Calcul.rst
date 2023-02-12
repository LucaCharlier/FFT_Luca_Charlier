.. _Calcul.rst:

Calcul des transformées de Fourier
############

Comme annoncé précédemment, nous souhaitons procéder à une simplification des coefficients afin de n'en avoir plus qu'un pour chaque fréquence.

..  warning::

    Les détails mathématiques sont donnés, mais il n'est pas utiles de les lire pour tout comprendre. Il sera cependant nécessaire de faire confiance à la méthode.

..  admonition:: Détails mathématiques
        
    Soit :math:`s(x)` une fonction réelle. Nous posons

    ..  math::

        s_N(x) = \sum^N_{n=-N} c_n\cdot e^{i2\pi n x/p}
    
    où :math:`p` est la période de la fonction.
    

