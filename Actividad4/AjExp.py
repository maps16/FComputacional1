# -*- coding: utf-8 -*-
#importando librerias
import matplotlib.pyplot as plt
import numpy as np
from scipy import  optimize 

#Obtencion de datos
datos = np.loadtxt('PvsA.txt')

#Separacion de los datos para un mejor manejo
x1 = datos[:,0]
y1 = datos[:,1] 

#Definiendo la forma de la función a ajustar
#y=c*e^(-a*x)+b
def f(x,a,b,c):
    return c * np.exp(-a * x) + b

#Generando Estimación
y2 = y1 + 0.2 * np.random.normal(size=len(x1))

#Optimizacion de la curva
popt, pcov = optimize.curve_fit(f,x1,y2)

#Genero datos y grafico

plt.plot(x1, y1, "go", x1, f(x1, *popt), "b-")

#Propiedades de la Grafica
plt.grid()
plt.legend()
plt.title("Atmospheric pressure vs. altitude")
plt.xlabel("Altitude")
plt.ylabel("Pressure")

plt.show()
