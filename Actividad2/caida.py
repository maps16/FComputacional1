#Importar funcion sqtr
from math import sqrt

#Pedir al altura a usuario
h = float(input("Proporciona la altura de la torre: "))

g=9.81 #Constate de la gravedad

t=sqrt(2*h/g) #Calculo de tiempo de caida

#Impresion de Resultados
print'El tiempo de caida para una altura ',h,'m es: ', t 
