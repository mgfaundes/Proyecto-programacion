import os
import time
import matplotlib.pyplot as plt
archivo = None
def bienvenida():
    print("Bienvenido al organizador de datos COVID-19")
    print("Tiene descargada la database (Y/N) \n")

def abrirdatos():
	aux=open("CasosNuevosSinSintomas.csv","r")
	archivo=aux.readlines()
	return archivo

def abrirdata2():
    aux = open("CasosNuevosSinSintomas_std.csv","r")
    archivo2 = aux.readlines()
    return archivo2

def abrirdata3():
    aux = open("CasosNuevosSinSintomas_T.csv","r")
    archivo3 = aux.readlines()
    return archivo3

def mostrardatos(archivo):
	for i in archivo:
		i=i.split(",")
		aux=""
		for j in i:
			aux=aux+j+"\t"
		print(aux)



plt.plot([1, 2, 3, 4])
plt.ylabel("ejemplo")
plt.show()

archivo = abrirdatos()
mostrardatos(archivo)