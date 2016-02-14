#importando librerias
import matplotlib.pyplot as plt
import numpy as np

#Obtencion de datos
datos = np.loadtxt('TNY.txt')

#Separacion de los datos para un mejor manejo
x = datos[:,0]
y = datos[:,1] 

#Grafica de puntos de los datos
plt.plot(x,y,'bo')

#Aplicando regresion lineal
m,b = np.polyfit(x,y,1)
xr = np.polyval([m,b],x)

#Graficar el ajuste lineal
plt.plot(x,xr,'r')
plt.show()
    
