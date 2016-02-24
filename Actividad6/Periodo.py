#LIBRERIAS
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Constantes del problema.
l = 4.0     #Longitud Del Pendulo
g = 9.81  #Gravedad
n = 500
eps= 0.001
theta_0 =np.linspace(eps, np.pi/2-eps, n)
res = [0 for i in range(n)]
err = [0 for i in range(n)]
T = [0 for i in range(n)]

#Caso de oscilaciones pequenas
T_o = 2.0 * np.pi*np.sqrt(l/g)


#Para Oscilaciones grandes

#Calculo de la integral
inte = lambda x, k : 1.0 /(np.sqrt(np.cos(x)-np.cos(k)))

for i in range(n):
    theta_00 = theta_0[i]
    res[i] , err [i] = quad(inte, 0, theta_00, args=(theta_00))

#Calculo del periodo
    T[i] = 4*np.sqrt(l/(2*g)) * res[i]

#Calculo del error
ErrorR = (T/ T_o)
x = (theta_0*180.0)/np.pi #Transformacion a Grados

#Grafica
plt.plot(x, ErrorR)
plt.xlabel("Angulo")
plt.ylabel("Error Relativo T/To")
plt.show()

