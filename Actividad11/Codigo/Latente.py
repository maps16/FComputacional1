import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

Pi = 0         # Nacimientos Diarios
Del = 0.0001   # Muertes Naturales %  (Por dia)
Bet = 0.0095   # Transmision       %  (Por dia)
Zet = 0.0001   # Removidos         %  (Por dia)
Alf = 0.0001   # Destruidos        %  (Por dia)
Rho = 0.05     # Infected          %  (Por dia)

#Sistema de Ecuaciones Diferenciales 
def f(y, t):
    Si = y[0]
    Zi = y[1]
    Ri = y[2]
    Ii = y[3]
    # Modelo
    f0 = Pi - Bet*Si*Zi - Del*Si                #Si
    f1 = Rho*Ii + Zet*Ri - Alf*Si*Zi            #Zi
    f2 = Del*Si + Del*Ii + Alf*Si*Zi - Zet*Ri   #Ri
    f3 = Bet*Si*Zi -Rho*Ii - Del*Ii             #Ii
    
    return [f0, f1, f2, f3]

S0 = 500.                        # Poblacion Inicial
Z0 = 0.                          # Zombie Inicial
R0 = 0.                          # Muertos Inicial
I0 = 1.                          # Infectados Inicial
y0 = [S0, Z0, R0, I0]            # Condiciones Iniciales
t  = np.linspace(0., 30., 1000)  # Tiempo

# Solucion E.D.
soln = odeint(f, y0, t)
S = soln[:, 0]
Z = soln[:, 1]
R = soln[:, 2]
I = soln[:, 3]
# Grafica
plt.figure()
plt.ylim(0,600)
plt.grid(True)
plt.plot(t, S, label='Vivos')
plt.plot(t, Z, label='Zombies')
plt.xlabel('Tiempo')
plt.ylabel('Poblacion')
plt.title('Apocalipsis Zombie - Modelo Latente.')
plt.legend(loc="best")