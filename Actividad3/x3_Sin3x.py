import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Generando datos
x01 = np.random.random(12)
x1 = 4.0*x01-2.0
y1 = (x1*x1*x1)*(np.sin(3.0*x1))


#Graficar los puntos aleatorios x y los f(x)=Sin(2x)
plt.plot(x1, y1, 'o', label='Data')

#Punto para interpolar
x = np.linspace(min(x1),max(x1),200)

#Opciones para interp1d
opc = ('linear', 'quadratic', 'cubic')

for o in opc:
    f = interp1d(x1, y1, kind=o)
    plt.plot(x, f(x), label=o)

#Mostrar la grafica
plt.legend(loc='best')
plt.show()