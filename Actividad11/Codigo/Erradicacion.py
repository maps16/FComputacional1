import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

Pi  = 0        # Nacimientos Diarios
Del = 0.0001   # Muertes Naturales %  (Por dia)
Bet = 0.0055   # Transmision       %  (Por dia)
Zet = 0.0900   # Removidos         %  (Por dia)
Alf = 0.0075   # Destruidos        %  (Por dia)
k = 0.25
n=4

# solve the system dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
    # Modelo
    f0 = Pi - Bet*Si*Zi - Del*Si                  #Si
    f1 = Bet*Si*Zi + Zet*Ri - Alf*Si*Zi           #Zi
    f2 = Del*Si + Alf*Si*Zi - Zet*Ri              #Ri
    f3 = -k*n*Zi                                  #DZi
    
    return [f0, f1, f2, f3]

# initial conditions
S0 = 500.                        # Poblacion Inicial
Z0 = 0.                          # Zombie Inicial
R0 = 0.                          # Muertos Inicial
DZ0 = 0.                          # Infectados Inicial
y0 = [S0, Z0, R0, DZ0]            # Condiciones Iniciales
t  = np.linspace(0., 130., 1000)  # Tiempo

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]
I = soln[:, 3]
# plot results
plt.figure()
plt.ylim(0,500)
plt.grid(True)
plt.plot(t, S, label='Vivos')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Tiempo')
plt.ylabel('Poblacion')
plt.title('Apocalipsis Zombie - Modelo Tratamiento.')
plt.legend(loc="best")