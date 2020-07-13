# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:35:55 2020

@author: paulc
"""
import pandas as pd
import matplotlib.pyplot as plt

headers = ['ci','nombreCompleto','sexo','departamento','notaPromedio','edad']
data = pd.read_csv("infoAlumnos.csv",header=None,names=headers)

#creamos un diccionario para categorizar el sexo y los departamentos del país
cleanup_data = {"sexo":{"M":0,"F":1},
                "departamento":{"LA PAZ":0, "PANDO":1,"ORURO":2,"POTOSI":3,"COCHABAMBA":4,
                                "SANTA CRUZ":5,"BENI":6}}
data.replace(cleanup_data, inplace=True)
print(data.corr(method="pearson"))

plt.matshow(data.corr())
#Para hallar y visualizar la correlación por ejemplo entre edad y nota
plt.plot(data["notaPromedio"],data["edad"],"ro")
plt.ylabel("Edad")
plt.xlabel("Nota Promedio")