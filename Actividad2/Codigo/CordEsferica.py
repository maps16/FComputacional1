#Importar Funciones necesarias
from math import acos, atan, sqrt

x = float(input('Componente x: '))
y = float(input('Componente y: '))
z = float(input('Componente z: '))

#Calculo de las coordenadas
r = sqrt(x*x + y*y + z*z) #Norma
   #Angulos
theta = acos(z/r)
phi = atan(y/x)

print 'r= ',r 
print 'theta= ', theta
print 'phi=  ', phi




