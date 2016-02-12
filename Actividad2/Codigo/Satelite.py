#Impotar el valor de pi
from math import pi

#Definicion de constantes
G = 6.67*(10**(-11)) #Constante de gravitacion
M = 5.97*(10**(24)) #Masa de la tierra en kg
R = 6371000  #Radio de la tierra en m

#Pedir el perido al usuario
t = float(input('Proporciona el periodo del satelite (minutos)'))
#Tranformar el periodo de min -> s
T = t*60

#Calculo de la altura desde la superficie de la tierra de la orbita
H = ((G*M*T**2)/(4*pi**2))**(1./3.)-R

print 'La altura a la que orbita un satelite de periodo ', t,'minutos es de ', H,'metros'


