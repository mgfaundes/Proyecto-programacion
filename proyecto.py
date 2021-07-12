import os
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
datos = None
archivo = None
def bienvenida():
    print("Bienvenido al organizador de datos COVID-19")

def abrirdatos():
	aux=open("CasosNuevosSinSintomas_T.csv","r")
	archivo=aux.readlines()
	archivo = "".join(archivo)
	archivo = archivo.replace(",",";")
	datos = open("Database.csv", "w")
	datos.write(archivo)
	aux2 = open("Database.csv", "r")
	datos = aux2.readlines()
	return datos

def abrirdatos2():
	aux=open("ResidenciasSanitarias_T.csv","r")
	archivo=aux.readlines()
	archivo = "".join(archivo)
	archivo = archivo.replace(",",";")
	datos2 = open("Database2.csv", "w")
	datos2.write(archivo)
	aux2 = open("Database2.csv", "r")
	datos2 = aux2.readlines()
	return datos2

def mostrardatos():
	for i in datos:
		i=i.split(";")
		aux=""
		for j in i:
			aux=aux+j+"\t"
		print(aux)

datos = abrirdatos()
datos2 = abrirdatos2()
mostrardatos()



'''
plt.plot([1, 2, 3, 4])
plt.ylabel("ejemplo")
plt.show()
'''

