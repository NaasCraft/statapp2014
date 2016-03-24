### Réseaux de neurones

#### Jeu de données utilisé

On utilisera le set de _digits_ manuscrits accessible via la fonction [load_digits](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html).

__Code :__

```python
from sklearn.datasets import load_digits
digits = load_digits()
```

#### Fonction de scoring

On aura plusieurs possibilités : exploiter des fonctions de scoring utilisables en [_classification binaire_](http://en.wikipedia.org/wiki/Binary_classification), par exemple les scores de [précision et rappel](http://en.wikipedia.org/wiki/Precision_and_recall), ou d'autres types de fonctions/métriques utilisées pour les [problèmes de classification plus généraux](http://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics).

#### Validation croisée

__Rappel__ : [Cross validation (statistics)](http://en.wikipedia.org/wiki/Cross-validation_(statistics))

* Description des différents types de validation croisée
	* KFold
	* Stratified KFold
	* Leave-P-Out
	* ShuffleSplit

* Dans GridSearchCV, ...

* Calibrage de la valeur de K dans la validation croisée __KFold__.

* Un exemple de code "à la main"

```python
a_la_main = sklearn.datasets.load_aLaMain()
```

#### Mesures de performance

* Gestion des paramètres

* Autres points de réglage : notion de [learning curve](http://scikit-learn.org/stable/modules/learning_curve.html#learning-curve)

#### _"Confusion Matrix"_

... Késako ?