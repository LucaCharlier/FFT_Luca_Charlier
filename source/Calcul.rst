.. _Calcul.rst:

Calcul des transformées de Fourier
############

.. admontion:: Coefficients

    Nous définissons les coefficients comme suit:

    ..  math::

        \begin{cases}

        a_0 = \frac{1}{p} \int^{p/2}_{-p/2} s(x) dx\\
        a_n = \frac{1}{p} \int^{p/2}_{-p/2} s(x)\cos(nx) dx\\
        b_n = \frac{1}{p} \int^{p/2}_{-p/2} s(x)\sin(nx) dx\\
        \end{cases}

Comme annoncé précédemment, nous souhaitons procéder à une simplification des coefficients afin de n'en avoir plus qu'un pour chaque fréquence.

..  warning::

    Les détails mathématiques sont donnés, mais il n'est pas utiles de les lire pour tout comprendre. Il sera cependant nécessaire de faire confiance à la méthode.

..  admonition:: Détails mathématiques
        
    Soit :math:`s(x)` une fonction réelle. Nous posons

    ..  math::

        s_N(x) = \frac{a_0}{2} + \sum^N_{n=-N} c_n\cdot e^{inx}
    
    où :math:`p` est la période de la fonction.

    Par l'identité d'Euler nous avons

    ..  math::

        e^{inx} = \cos(nx)+ i\sin(nx)

    et donc aussi
    ..  math:: 

        \cos(nx) = \frac{e^{inx}+e{-inx}}{2} \text{ et } \sin(nx) = \frac{e^{inx}-e{-inx}}{2}.

    En insérant dans la définition de :math:`s_N(x)` nous obtenons 
    ..  math::

        s_N(x) = \sum^N_{n=-N} c_n\cdot e^{inx}