import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definiendo las cosntantes de la Ec. Diferencial
g = 9.81
l = 0.01
b = 1.0 #Pendulo simple por lo tanto sin friccion
c = g/l
angulo= 0
Vangular= 10


#Definicion de la ecuacion diderencial del pendulo

def p (y, t, b, c):
    theta, omega = y
    dy_dt = [omega,-b*omega -c*np.sin(theta)]
    return dy_dt

#Definiendo condiciones iniciales

y0 = [angulo, Vangular]
t = np.linspace(0,50,501) #Para generar la sollucion

#Resolver la Ec. Diferencial

sol = odeint(p, y0, t, args=(b,c))

#Graficacion de la solucion.
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
