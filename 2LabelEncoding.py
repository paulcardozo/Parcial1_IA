# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:47:12 2020

@author: paulc
"""

import pandas as pd
import numpy as np

headers = ['ci','nombreCompleto','sexo','departamento','notaPromedio','edad']
data = pd.read_csv("infoAlumnos.csv",header=None,names=headers)
obj_data = data.select_dtypes(include=['object']).copy()
print(obj_data['sexo'].value_counts())
print(obj_data['departamento'].value_counts())

#creamos un diccionario para categorizar el sexo y los departamentos del país
cleanup_data = {"sexo":{"M":0,"F":1},
                "departamento":{"LA PAZ":0, "PANDO":1,"ORURO":2,"POTOSI":3,"COCHABAMBA":4,
                                "SANTA CRUZ":5,"BENI":6}}
obj_data.replace(cleanup_data, inplace=True)
print(obj_data)