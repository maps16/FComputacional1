import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definiendo las constantes de la Ec. Diferencial
g = 9.81
l = 1.0
b = 0.0 #Pendulo simple por lo tanto sin friccion
c = g/l

#Codiciones Iniciales
X_f1 =np.array([-4.0*np.pi,4.0*np.pi])
X_f2 =np.array([-2.0*np.pi,-0.0*np.pi]) #Completar Diagrama
t = np.linspace(-0.0*np.pi,5.0*np.pi,500) #Para generar la solucion

#Definicion de la ecuacion diderencial del pendulo
def p (y, t, b, c):
    theta, omega = y
    dy_dt = [omega,-b*omega -c*np.sin(theta)]
    return dy_dt

#Defininedo Color y Numero
values  =np.linspace(-1.0,1.0,100) # position of X0 between X_f0 and X_f1
vcolors = plt.cm.Greys(np.linspace(0.5,1.0,len(values))) #Color Trayectoria
#=====================================
# Trayectoria
for v, col in zip(values, vcolors):
    y0 = v * X_f1                               # Punto de Inicio   
    X = odeint(p, y0, t, args=(b,c))         
    plt.plot( X[:,0], X[:,1], color=col, label='X0=(%.f, %.f)'%(y0[0],y0[1]))

# Trayectoria          #Completar el diagrama fase
for v, col in zip(values, vcolors):
    y1 = v * X_f2                               # Punto de Inicio   
    X1 = odeint(p, y1, t, args=(b,c))           
    plt.plot( X1[:,0], X1[:,1], color=col, label='X0=(%.f, %.f)'%(y1[0],y1[1]))
#=====================================
#Graficar
plt.title('Trayectorias y direcciones')
plt.xlabel('Angulo')
plt.ylabel('Velocidad Angular')
plt.grid()
plt.xlim(-2.0*np.pi,2.0*np.pi)
plt.ylim(-10,10)

plt.show()