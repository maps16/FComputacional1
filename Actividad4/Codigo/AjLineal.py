#importando librerias
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import  leastsq

#Obtencion de datos
datos = np.loadtxt('TNY.txt')

#Separacion de los datos para un mejor manejo
x1 = datos[:,0]
y1 = datos[:,1] 

#Ajuste Lineal   

fitfunc = lambda p, x: p[0] + p[1]*x # Target function
errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
p0 = [-15., -1.] # Initial guess for the parameters
p1, success = leastsq(errfunc, p0[:], args=(x1, y1))

#Genero datos y grafico
time = np.linspace(x1.min(), x1.max(), 100)
plt.plot(x1, y1, "go", time, fitfunc(p1, time), "b-") # Plot of the data and the fit

#Propiedades de la Grafica
plt.title("Temperatura Nueva York en invierno")
plt.xlabel("Ano")
plt.ylabel("Temperatura")

plt.show()