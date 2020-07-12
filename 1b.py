# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:57:39 2020

@author: paulc
"""
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
from scipy import stats
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("infoAlumnos.csv")
vector = data.to_numpy()
nota = vector[:,4].mean()
edad = vector[:,5].mean()
print("La media de notas es: "+str(nota))
print("La media de edades es: "+str(edad))
print()
notas = vector[:,4]
edades = vector[:,5]
(notasModa, modaNotas) = np.unique(notas,return_counts=True)
(edadesModa, modaEdades) = np.unique(edades,return_counts=True)
auxNot = 0
indNot = 0
for i,val in enumerate(modaNotas):
    if(auxNot<val):
        auxNot=val
        indNot=i
auxEd = 0
indEd = 0
for i,val in enumerate(modaEdades):
    if(auxEd<val):
        auxEd=val
        indEd=i
print("La moda de notas es: "+str(notasModa[indNot]))
print("La moda de edades es: "+str(edadesModa[indEd]))
print()
desviacionNotas = vector[:,4].std()
desviacionEdades = vector[:,5].std()
print("La desviación estándar de notas es: "+str(desviacionNotas))
print("La desviación estándar de edades es: "+str(desviacionEdades))