# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:51:51 2020

@author: paulc
"""

  
# list of elements to calculate mean 
n_num = [[4860120,"CARDOZO LAUREL CARLOS PAUL","M","LA PAZ",63,23],
[1239845, "MOLLEJAS RAMIREZ MANUEL","M","LA PAZ",52,24],
[65123788,"ARTEAGA PEREZ ANDREA CARLA","F","LA PAZ",60,22],
[5643721, "SALINAS PATZI VICTORIA ADRIANA","F","PANDO",77,23],
[9808032, "VARGAS GARNICA MIGUEL ANGEL","M","ORURO",65,24],
[6789101, "HERRERA CHAMBI JHOSELIN SELENE","F","POTOSI",47,25],
[2367277, "CARDOZO FLORES CARLOS PAUL","M","LA PAZ",75,27],
[7231567, "CASTRO RAMIREZ SARA REBECA","F","LA PAZ",77,23],
[1256728, "ORDONEZ SILVA JOAQUIN","M","LA PAZ",76,25],
[8776766, "VARGAS RAMIREZ DOUGLAS JOEL","M","COCHABAMBA",78,24],
[5467281, "FERNANDEZ MAVRICH DANIELA ALEJANDRA","F","COCHABAMBA",72,22],
[3781920, "MERIDA ALVAREZ PATRICIA","F","SANTA CRUZ",82,26],
[67342876,"LIZARRAGA QUISPE GUSTAVO ARIEL","M","LA PAZ",67,26],
[5621717, "VILLARROEL ARZE DANIELA ALEJANDRA","F","SANTA CRUZ",81,23],
[43516177,"DELGADO SILVA VALERIA PATRICIA","F","LA PAZ",91,22],
[8776364, "DURAN MOLINA JESSIVA IVANA","F","BENI",72,25],
[4767672, "ARIAS ROBLES SERGIO","M","LA PAZ",52,23],
[1234552, "ABREGO ROBLES AUGUSTO MANUEL","M","SANTA CRUZ",77,24],
[3617289, "MANRIQUEZ SALCEDO DANIELA VALENTINA","F","ORURO",49,25],
[84912398,"LOPEZ FERNANDEZ EDITH","F","LA PAZ",39,24],
[7323567, "MEDINA ANDRADE DANIELA ALEJANDRA","F","LA PAZ",77,24],
[8564721, "SALINAS MENEGAT JEAN CARLO","M","BENI",53,25],
[4782361, "CARDOZO PEDRAJA MIGUEL ANGEL","M","SANTA CRUZ",42,26]]
n = len(n_num) 

meansumNota=0
meansumEdad=0
for x in n_num:
    meansumNota+=x[4]
    meansumEdad+=x[5]

meanNota = meansumNota / n 
meanEdad = meansumEdad / n 

varNota = 0
varEdad = 0
for x in n_num:
    varNota+=(x[4]-meanNota)**2
    varEdad+=(x[5]-meanEdad)**2

stdNota  = (varNota/(n))**(1/2)  # standard deviation
stdEdad  = (varEdad/(n))**(1/2)  # standard deviation
  
print("El promedio de notas de la lista es: " + str(meanNota)) 
print("la media o premdio es la tendencia central entre las notas que tenemos como datos")
print("")
print("La desviación estándar de notas de la lista es: " + str(stdNota)) 
print("La desviación estándar de notas nos muestra en cuántos puntos puede variar las notas del promedio")
print("")
print("El promedio de edades de la lista es: " + str(meanEdad)) 
print("la media o premdio es la tendencia central entre las edades que tenemos como datos")
print("")
print("La desviación estándar de edades de la lista es: " + str(stdEdad)) 
print("La desviación estándar de edades nos muestra en cuántos años puede variar las edades del promedio")