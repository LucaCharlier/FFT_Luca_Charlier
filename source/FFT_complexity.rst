.. _FFT_complexity.rst:

Algorithme de FFT et complexité de calcul
#########################################

Après la seconde guerre mondiale, il n'est pas nécessaire de rappeller l'essort de la bombe atomique, créant un clivage entre l'est et l'ouest. Pour désamorcer le conflit, on émit l'idée d'interdire des tests supplémentaires de bombes. Pour s'assurer du bon suivi du traité il est nécessaire de pouvoir le vérifier. Ces vérifications sont néanmoins difficiles lors de tests sous-terrains. Lorsqu'une bombre nucléaire explose sous le sol, elle produit des vibrations qui peuvent être enregistrés par des sismographes (en particulier les ondes de la Tsar Bomba, explosée en nouvelle-Zemble en 1961, firent deux fois le tour de la terre avant de devenir imperceptibles). La principale difficulté néanmoins consiste à justement différencier ces vibrations des ondes sismiques. Avec une transformée de Fourier, ceci n'est pas un problème, puisque les fréquences des ondes sont différentes. On peut d'ailleurs aussi trouver l'intensité et la profondeur de l'explosion.

Toutefois, l'algorithme consistant à calculer les :math:`\hat{f}(n)` un à un est très inefficace. En 1960, pour un million de fréquences, la durée de calcul était d'approximativement 3 ans, soit 1 billions de calculs.

garwin and tukey -> 35 minutes


DFT (précision, espacement)

nombre de ponts -> nombre e fréquences


n^2 calculs

se superposent (mêmes valeurs) Seulement Nlog_2(N)

cooley -> papaer 

Gauss

image compression

radar, sonar, crystal, wifi, 5g