# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:48:00 2020

@author: paulc
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from pylab import rcParams
rcParams['figure.figsize']=30,30

dataset = pd.read_csv("infoAlumnos.csv", header=None)
cleanup_data = {2:{"M":0,"F":1},
                3:{"LA PAZ":0, "PANDO":1,"ORURO":2,"POTOSI":3,"COCHABAMBA":4,
                                "SANTA CRUZ":5,"BENI":6}}
dataset.replace(cleanup_data, inplace=True)

X = dataset.drop([0,1,4],axis=1)
y= dataset[4]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train, y_train)
plot_tree(classifier,filled=True)

plt.show()

y_pred = classifier.predict(X_test)
print(y_pred)


