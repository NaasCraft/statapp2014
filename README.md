#### TODO File

Aller sur : https://docs.google.com/document/d/1dkMmiM5ekHwP7ofpPG57kDBSJb4GQu1BNhqqrrJeuYs/edit?usp=sharing

#### Deadlines

- rendu du rapport de mi-parcours: 24/02/2015 (3-4 pages)
- rendu du rapport final: 25/05/2015 (30 pages hors annexes + 4 pages note de synthèse)
- soutenance: mi-mai à mi-juin 2015

#### Challenge

Trouver l'erreur de méthodologie dans
https://github.com/pierroweb/statapp2014/blob/master/pierre-examples/trouver-lerreur.py

Pourquoi le score affiché à la fin ne reflète pas le score que l'on obtiendrait sur de nouvelles images photographiés demain avec votre téléphone portable ?

#### Pour chacun des algorithmes que vous vous êtes répartis...

1. Vous mettre d'accord sur un jeu de données commun, petit. (par exemple  http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html qui est bien plus petit que MNIST et plus facile à manipuler.)
2. Choisir une fonction de score (precision, F1, recall, ROC, ...). Décrire une situation réelle où cette fonction de score est adaptée (filtrer images pornographiques sur une app, faire des diagnostics de sida ou de grossesse, etc.) et expliquer pourquoi cette fonction de score est adaptée ici. http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
3. 
4. Comprendre les nuances entre différents types de validation croisée, par exemple en étudiant celles proposés par sklearn (KFold, Stratified KFold, Leave-P-out, ShuffleSplit, ...) Quel est la validation croisée utilisée par défaut dans GridSearchCV ? Quel compromis devez-vous faire (qu'est ce l'avantage de KFold avec K=2, avec K=100 ? le désavantage ? Quel K offre un bon compromis ?)
5. Vous devez être capable de coder un type de validation croisée à la main, avec des boucles pythons.
6. Faire jouer les paramètres et essayer de trouver les paramètres qui donnent le meilleur score.
7. Pour améliorer les perf, avez-vous besoin de plus d'examples, ou de plus de features ? http://scikit-learn.org/stable/modules/learning_curve.html#learning-curve ; Comment (et à quel coût) rendre ces courbes plus lisses ?
8. Comment choisir le range de paramètres à tester ? Pourquoi pour le paramètre $C$ en SVM, on utilise souvent une échelle log ? Qu'en est-il des autres paramètres pour d'autres algos (question difficile!) ? Dessiner des courbes de performances en fonction des paramètres des algorithmes.
9. QU'est ce que la "confusion matrix" ? Est-ce qu'il est possible de l'interprêter pour le jeu de données que vous avez choisi ?
10. Envoyer régulièrement les codes que vous produisez dans Git. Pour l'instant chacun peut créer un répertoire avec le nom de l'algorithme qu'il étudie pour éviter les conflits.
11. Jeter un coup d'oeil là http://git-scm.com/doc et là http://scikit-learn.org/stable/tutorial/ ; il y a quelques bons réflexes à prendre



#### Consignes pour commencer

Comme expliqué lors de notre entretien, ce projet de statapp est "à la carte", avec une première partie qu'il faut absolutement comprendre et maitriser. Répondre à ces questions en jouant avec le dataset MNIST et sklearn vous permettra de comprendre déjà beaucoup de choses, et ensuite nous pourrons explorer d'autres choses plus sexy (calcul sur un cloud distant, jeux de donnée plus gros, convolututional nets).

- Décrire le problème d'apprentissage statistique lié aux datasets MNIST, CIFAR10 et CIFAT100.
- Quels sont les algorithmes de classification qui permettent de traiter ce problème ?
- Quelle méthodologie permet de tester la performance les algorithmes sur un jeu de données ?
- Pourquoi les statisticiens utilisent souvent un ensemble d'apprentissage et un ensemble de test ?
- Comment calibrer les paramètres à choisir ?
- Qu'est-ce que l'overfitting ? L'underfitting ? Une fois que le meilleur algorithme trouvé (avec les bons paramètres), comment savoir si pour augmenter les performances, il faut de meilleurs "features" (par exemple utiliser une vectorisation différent des images, une meilleure résolution, etc) ou alors plus d'images (augmenter la taille jeu de données) ?
- Une fois que vous avez choisi et calibré un algorithme, comment lui soumettre une nouvelle image ? Par exemple une image d'un chiffre que vous avez dessiné au stylo puis pris en photo avec votre téléphone portable ?
- [Une fois que vous aurez répondu à plusieurs des questions ci-dessus] Si vous deviez rapidement vous confronter à un nouveau jeu de données de classification, comment choisir un algorithme rapidement en écrivant le moins de code possible ?

#### Documentation

https://github.com/pierroweb/statapp2014/tree/master/doc

N'hésitez pas à documenter ce que vous faîtes au fur et à mesure dans ce dossier.
Cela profitera aux autres et vous sera très utile pour le rapport final
