##Questions posées et quelques réponses


#### Décrire le problème d'apprentissage statistique lié aux datasets MNIST, CIFAR10 et CIFAR100

* __MNIST dataset__

> The MNIST database (Mixed National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems.
>
> -- From Wikipedia.

_Objectif_ : Etre capable de déterminer quel chiffre correspond à une image de caractère manuscrit. Il s'agit d'un problème de classification (output discret à 10 valeurs possibles).

_Application(s) potentielle(s)_ : Transcription de texte manuscrit (pour l'instant limité aux chiffres), par exemple pris en photo depuis un téléphone ou un document scanné.

_Critères de performance utilisables_ : Chaque caractère n'étant pas plus important que les autres, un [F1-score](http://fr.wikipedia.org/wiki/Pr%C3%A9cision_et_rappel) (pondérant également précision et rappel) devrait être judicieux.

* __CIFAR10 & CIFAR100 dataset__

> The CIFAR-10 and CIFAR-100 are labeled subsets of the 80 million tiny images dataset. They were collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

#### Quels sont les algorithmes de classification qui permettent de traiter ce problème ?

#### Quelle méthodologie permet de tester la performance des algorithmes sur un jeu de données ?

#### Pourquoi les statisticiens utilisent souvent un ensemble d'apprentissage et un ensemble de test ?

#### Comment calibrer les paramètres à choisir ?

#### Qu'est-ce que l'overfitting ? L'underfitting ? Une fois que le meilleur algorithme trouvé (avec les bons paramètres), comment savoir si pour augmenter les performances, il faut de meilleurs "features" (par exemple utiliser une vectorisation différent des images, une meilleure résolution, etc) ou alors plus d'images (augmenter la taille jeu de données) ?

#### Une fois que vous avez choisi et calibré un algorithme, comment lui soumettre une nouvelle image ? Par exemple une image d'un chiffre que vous avez dessiné au stylo puis pris en photo avec votre téléphone portable ?

#### [Une fois que vous aurez répondu à plusieurs des questions ci-dessus] Si vous deviez rapidement vous confronter à un nouveau jeu de données de classification, comment choisir un algorithme rapidement en écrivant le moins de code possible ?