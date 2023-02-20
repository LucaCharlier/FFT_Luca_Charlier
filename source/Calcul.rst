.. _Calcul.rst:

Calcul des transformées de Fourier
############

.. admonition:: Coefficients

    Nous définissons les coefficients comme suit:

    ..  math::

        \begin{cases}

        a_n = \frac{1}{p} \int^{p/2}_{-p/2} s(x)\cos(nx) dx\\
        b_n = \frac{1}{p} \int^{p/2}_{-p/2} s(x)\sin(nx) dx\\

        \end{cases}

    où :math:`p` est la période de la fonction. Si la fonction est apériodique, nous posons :math:`p = \infty`.

Comme annoncé précédemment, nous souhaitons procéder à une simplification des coefficients afin de n'en avoir plus qu'un pour chaque fréquence.

..  warning::

    Les détails mathématiques sont donnés, mais il n'est pas utiles de les lire pour tout comprendre. Il sera cependant nécessaire de faire confiance à la méthode.

..  admonition:: Détails mathématiques
        
    Soit :math:`s(x)` une fonction réelle. Nous posons

    ..  math::

        s(x) =  \frac{a_0}{2} + \sum^\infty_{n=1} a_n\cdot \cos(nx) + b_n\cdot \sin(nx).
    
    

    Par l'identité d'Euler nous avons

    ..  math::

        e^{inx} = \cos(nx)+ i\sin(nx)

    et donc aussi

    ..  math:: 

        \cos(nx) = \frac{e^{inx}+e{-inx}}{2} \text{ et } \sin(nx) = \frac{e^{inx}-e^{-inx}}{2}.

    En insérant dans la définition de :math:`s(x)` nous obtenons 

    ..  math::

        s(x) = \frac{a_0}{2} + \sum^\infty_{n=1} \left(\frac{a_n-ib_n}{2}\right) e^{inx}+ \sum^\infty_{n=1} \left(\frac{a_n+ib_n}{2}\right) e^{-inx}.

    Maintenant nous définissons les coefficients recherchés

    ..  math::

        c_n = \frac{1}{2}(a_n + ib_n) \text{ avec } \bar{c}_n = \frac{1}{2}(a_n-ib_n).

    Ainsi l'on peut écrire, en réindexant avec :math:`-n`

    ..  math::

        s(x) = \frac{a_0}{2} + \sum^{-\infty}_{n=-1} \bar{c}_{-n}e^{-inx} + \sum^\infty_{n=1} c_ne^{-inx}

    Nous définissons de plus

    ..  math::

        c_0 = \frac{a_0}{2} \text{ et } c_n = \bar{c}_{-n}, n = -1,-2,\dots

    Ce qui nous amène au résultat désiré

    ..  math::

        s(x) = \sum^\infty_{-\infty} c_n e^{-inx}

    A partir de :math:`c_n = \frac{1}{2}(a_n + ib_n)` on peut arriver par des méthodes similaires à 

    ..  math::

        c_n = \frac{1}{2p}\int^p_{-p} s(x)e^{inx}dx.

    En particulier pour :math:`n=0`:

    ..  math::

        c_0 = \frac{1}{2p}\int^p_{-p}s(x)dx


Pour les flemmards qui auraient pas voulu suivre la démonstration, voici le résultat final :

..  admonition:: Série exponentielle complexe 

    Nous pouvons écrire notre fonction :math:`s(x)` sous la forme:
    
    ..  math::

        s(x) = \sum^\infty_{-\infty} c_n e^{-inx}

    avec

    ..  math::
        c_n = \frac{1}{2p}\int^p_{-p} s(x)e^{inx}dx

