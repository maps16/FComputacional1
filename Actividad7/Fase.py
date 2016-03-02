import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definiendo las cosntantes de la Ec. Diferencial
g = 9.81
l = 1.0
b = 0.0 #Pendulo simple por lo tanto sin friccion
c = g/l
angulo= 0
Vangular= 0.9

X_f1 =np.array([2.0*np.pi, 2.0*np.pi])

#Definicion de la ecuacion diderencial del pendulo

def p (y, t, b, c):
    theta, omega = y
    dy_dt = [omega,-b*omega -c*np.sin(theta)]
    return dy_dt

#Definiendo condiciones iniciales

y0 = [angulo, Vangular]
t = np.linspace(-0.0*np.pi,2.0*np.pi,501) #Para generar la sollucion

#Resolver la Ec. Diferencial

sol = odeint(p, y0, t, args=(b,c))

#Graficacion de la solucion.
#plt.figure(1)
#plt.plot(t, sol[:, 0], 'b', label='theta(t)')
#plt.plot(t, sol[:, 1], 'g', label='omega(t)')
#plt.legend(loc='best')
#plt.xlim(0.0,2.0*np.pi )
#plt.xlabel('t')
#plt.grid()


values  =np.linspace(-1.0*np.pi, 1.0*np.pi,50)                # position of X0 between X_f0 and X_f1
vcolors = plt.cm.autumn_r(np.linspace(0.3, 1., len(values)))  # colors for each trajectory

plt.figure(2)

#-------------------------------------------------------
# plot trajectories
for v, col in zip(values, vcolors):
    y0 = v * X_f1                               # starting point   
    X = odeint(p, y0, t, args=(b,c))         # we don't need infodict here
    plt.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( y0[0], y0[1]) )

#-------------------------------------------------------
# define a grid and compute direction at each point
#ymax = plt.ylim(ymin=0)[1]                        # get axis limits
#xmax = plt.xlim(xmin=0)[1]
nb_points   = 100

x = np.linspace(-2.0*np.pi, 2.0*np.pi, nb_points)
y = np.linspace(-12, 12, nb_points)

X1 , Y1  =np.meshgrid(x, y)                       # create a grid
DX1, DY1 = p([X1, Y1],t,b,c)                      # compute growth rate on the gridt
M = (np.hypot(DX1, DY1))                           # Norm of the growth rate
M[ M == 0] = 1.                                 # Avoid zero division errors
DX1 /= M                                        # Normalize each arrows
DY1 /= M

#-------------------------------------------------------
# Drow direction fields, using matplotlib 's quiver function
# I choose to plot normalized arrows and to use colors to give information on
# the growth speed
plt.title('Trajectories and direction fields')
Q = plt.quiver(X1, Y1, DX1, DX1, M, pivot='mid', cmap=plt.cm.jet)
plt.xlabel('Number of rabbits')
plt.ylabel('Number of foxes')
#plt.legend(loc="best")
plt.grid()
plt.xlim(-2.0*np.pi,2.0*np.pi)
plt.ylim(-12,12)
#f2.savefig('rabbits_and_foxes_2.png')

plt.show()
