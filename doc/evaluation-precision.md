#Méthodes d'évaluation de la performance d'un classifieur

Ce court résumé s'inspire d'un document de niveau M2, disponible à l'adresse suivante : http://clement.chatelain.free.fr/docs/STAGE_M2_OUFELLA.pdf

##Évaluation scalaire

On s'intéresse ici aux métriques scalaires permettant d'évaluer la performance d'un classifieur.

####1. Taux de bonne classification

On distingue ici deux variantes :

* Le __taux de bonne classification simple__, ou sans coût, qui correspond au rapport du nombre de bonnes prédictions sur le nombre d'observations dans la base.

  __Avantages__ : simplicité de calcul, résultat scalaire d'interprétation évidente

  __Inconvénients__ : risque de ne pas prendre en compte la distribution des classes (e.g. si la base contient 99% d'observations positives, un classifieur prédisant toujours positivement aura un *taux de bonne classification* de 99%, ce qui n'est dans la majorité des cas pas représentatif de la performance réelle que l'on mesure)

* Le __taux de bonne classification avec coût__, qui prend cette fois en compte la distribution des classes (notamment si une classe est sous/sur-représentée), et peut inclure des coûts pour chaque type de prédiction.

  __Avantages__ : résulte immédiatement du taux précédent, mais en étant plus représentatif des performances réelles du classifieur

  __Inconvénients__ : nécessite la connaissance a priori des coûts de chaque prédiction (ce qui en pratique n'est jamais le cas)

####2. Précision, Rappel et F-mesure

* __Précision__ : rapport du nombre de "vrais positifs" (*__TP__*) sur le nombre de prédictions positives (*__TP+FP__*)

* __Rappel__ : rapport du nombre de "vrais positifs" (*__TP__*) sur le nombre de labels positifs dans la base (*__TP+FN__*)

  Ces deux mesures sont en pratique exploitées directement dans le cadre de __recherche documentaire__ (*information retrieval*). Plus d'informations [ici](http://fr.wikipedia.org/wiki/Pr%C3%A9cision_et_rappel).
  
* __F-mesure__ : fonction d'un paramètre *beta* (souvent fixé à 1 lorsque l'on ne souhaite pas favoriser la précision ou le rappel), qui se présente sous la forme d'une "moyenne géométrique" des deux scores précédents.

  En pratique, la __mesure F1__ est souvent utilisée pour calibrer les paramètres de classifieurs de par sa généralité plus grande que les taux de bonne classification.
  
  Néanmoins, il est à noter deux __inconvénients__ : elle ne permet pas de *différencier les erreurs*, et reste *sensible à la distribution des classes*.
  
  Qui plus est, il faudra s'efforcer d'adapter le problème, car ces trois métriques sont spécifiques à des problèmes de classification binaire (et nous travaillons sur des problèmes multi-classes).
  
####3. Courbe ROC

*(à compléter)*


