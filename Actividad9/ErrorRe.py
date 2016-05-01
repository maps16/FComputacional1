# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pylab as plt

#Parametros
g,l,n = 9.81 , 1.0 , 5000
RadGrad = 180.0 / np.pi
eps = 0.001

#Definir una serie de valores
thetaI = np.linspace(eps, np.pi-eps,n)

#Arrays
Int = [0 for i in range(n)]
IntI = [0 for i in range(n)]
Perio = [0 for i in range(n)]
Sin = [0 for i in range(n)]
Err = [0 for i in range(n)]

#Aprox Angulos pequeños
PerioTeo = 2.*np.pi*np.sqrt(l/g)
 
#Calculo Error Rel
# m terminos
m = 10
for i in range(0,m):
    for j in range(0,n):
        facto0 = float(math.factorial(2.*(i)))
        facto1 = float((2.**i * math.factorial(i))**2.)
        Sin [j] = np.sin(thetaI[j]/2.)**(2.*(i))
        Int [j] = ((facto0/facto1)**2.)*Sin[j]
        IntI[j] = IntI[j] +Int[j]
        Perio[j] = 2.*np.pi*np.sqrt(l/g)*IntI[j]
        Err [j] =  Perio[j]/PerioTeo