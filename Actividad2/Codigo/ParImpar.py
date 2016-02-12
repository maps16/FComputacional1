
print 'Ingrese dos numeros enteros, un par y un impar'

m = int(input('Ingrese primer numero entero: '))
n = int(input('Ingrese segundo numero entero: '))

while (m+n)%2==0:
    print 'Uno debe ser impar y el otro par, vuelva a intentar'
    m = int(input('Ingrese primer numero entero: '))
    n = int(input('Ingrese segundo numero entero: '))

print 'Los numeros escogidos son ',m,'y ',n
