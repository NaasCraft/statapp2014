import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn import grid_search

digits = datasets.load_digits()

X = digits.images.reshape((len(digits.images), -1))
y = digits.target

possible_parameters = np.logspace(-10, 0, 10)

clf = grid_search.GridSearchCV(
        svm.SVC(C=1),
        {'C': possible_parameters},
        cv=3,
        scoring='precision',
        refit=True
    )
clf.fit(X, y)

print "final score:", metrics.f1_score(y, clf.predict(X))
