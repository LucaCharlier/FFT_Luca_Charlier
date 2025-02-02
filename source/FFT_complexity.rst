.. _FFT_complexity.rst:

Algorithme de FFT et complexité de calcul
#########################################

Il n'est pas nécessaire de rappeller l'essort de la bombe atomique d'après la seconde guerre mondiale, créant un clivage entre l'est et l'ouest. Pour désamorcer le conflit, on émit l'idée d'interdire des tests supplémentaires de bombes. Pour s'assurer du bon suivi du traité il est nécessaire de pouvoir le vérifier. Ces vérifications sont néanmoins difficiles lors de tests sous-terrains. Lorsqu'une bombre nucléaire explose sous le sol, elle produit des vibrations qui peuvent être enregistrés par des sismographes (en particulier les ondes de la Tsar Bomba, explosée en nouvelle-Zemble en 1961, firent deux fois le tour de la terre avant de devenir imperceptibles). La principale difficulté néanmoins consiste à justement différencier ces vibrations des ondes sismiques. Avec une transformée de Fourier, ceci n'est pas un problème, puisque les fréquences des ondes sont différentes. On peut d'ailleurs aussi trouver l'intensité et la profondeur de l'explosion.

Toutefois, l'algorithme consistant à calculer les :math:`\hat{f}(n)` un à un est très inefficace. En 1960, pour un million de fréquences, la durée de calcul était d'approximativement 3 ans, soit 1 billion de calculs.

Bien que publié trop tardivement, un algorithme plus efficace fut (re)découvert par Tukey, qui après avoir contacté Cooley, publia un `article <https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/S0025-5718-1965-0178586-1.pdf>`_ avec lui. 

..  admonition:: FFT selon Cooley-Tukey

    En reprenant la définition de la DFT (Discret Fourier Transform), et en séparant les indices pairs (:math:`E`) et impairs (:math:`O`) nous écrivons:

    ..  math::

        X_n = \underbrace{\sum^{\frac{N}{2}-1}_{k=0} x_{2^k}e^{-2ink}}_{E_n} + e^{-in} \underbrace{\sum^{\frac{N}{2}-1}_{k=0} x_{2k+1}e^{-2ink}}_{O_n} =: E_n + e^{-in}O_n

    Intuitivement, les harmoniques paires et impaires se coupent respectivement entre elles de façon prévisible. Puisque :math:`e^{-2ink} = e^{-2in(N/2 + k)}`, il est possible de parvenir à montrer que

    ..  math::
        X_{n+\frac{N}{2}} = E_n - e^{-in}O_n
    
    Ainsi,

    ..  math::

        \begin{cases}

        X_n = E_n + e^{-in}O_n\\
        X_{n+\frac{N}{2}} = E_n - e^{-in}O_n

        \end{cases}

    Cette réécriture est intéressante car elle permet de réutiliser les résultats obtenus une première fois pour l'autre moitiée des fréquences. De plus, puisque 

    ..  math::

        E_n = \sum^{\frac{N}{2}-1}_{k=0} x_{2k}e^{-2ink},

    il s'agit à nouveau d'une DFT, tout comme :math:`O_k`, de longueur de :math:`N/2` points. Ainsi l'algorithme peut être réutilisé récursivement, avec une quantité de données diminuant progressivement. C'est le `Divide and Conquer` .

    En divisant progressivement la longueur des intervalles considérés, il ne faut plus que procéder :math:`\log_2(N)` fois le calcul d'air sur :math:`N` fréquences, d'où la complexité de :math:`\mathcal{O}(n\log_2(n))`.

La FFT permet alors d'effectuer les mêmes calculs en un peu moins de 35 minutes. Si cet algorithme avait été (re)découvert plus tôt, peut-être y aurait-il moins d'armes nucléaires sur terre.

La vidéo suivante permet une compréhension intuitive de l'algorithme de FFT: 

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/watch?v=nmgFG7PUHfo" frameborder="0" allowfullscreen></iframe>


Implémentation Python
=====================

Nous allons à présent implémenter l'algorithme en python. Nous souhaitons partir d'un ensemble :math:`A = \{a_0, a_1, a_2, \dots, a_n\}, \log_2(n) \in \mathbb{N}` de points pour arriver à un ensemble :math:`Y = \{A_0, A_1, A_2, \dots, A_n\}` qui contient le spectre de :math:`A`.

Nous utilisons de plus la fonction `complex` qui permet le calcul de valeurs imaginaires.


..  literalinclude:: scripts/factorial.py
    :linenos:
    :emphasize-lines: 9,10,11,12,15,16

Les lignes 5 à 8 préparent la transformée. On y place de plus une condition d'arrêt, lorsque nous avons décomposé toutes les listes à un seul point, donc de longueur 1.

Les lignes 9 et 10 séparent les éléments pairs des éléments impairs.

Les lignes 10 et 12 constituent le coeur de l'algorithme. On y place la récursion, en demandant d'aller récupérer les valeurs de :math:`Y` pour un ensemble moitié moins grand (calcul de la transformée de Fourier de :math:`E_n \text{ et } O_n`).

Finalement, on additionne les différents :math:`E_n \text{ et } O_n` pour chaque fréquence :math:`n` afin d'en obtenir le spectre.

