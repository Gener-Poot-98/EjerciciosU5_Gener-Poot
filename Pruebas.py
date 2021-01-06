#Pruebas de asignación
contador = 0
factorial = contador

#Pruebas de operaciones aritméticas básicas
contador = contador + 1
suma = 2.7 + 3
resta = 5 - contador
multiplicacion = suma * 5
division = multiplicacion / 2

#Pruebas de expresiones booleanas básicas
contador == suma
contador != factorial
resta < suma
resta <= multiplicacion
suma > resta
multiplicacion >= division

#Pruebas de formulas complejas del tipo c = a op ( b op d)
factorial = 9 * (2 + suma)
resultado = (multiplicacion - 5) / 2

#Pruebas de encabezados de estructuras de control

#Estructura IF
compra = 80
if compra <= 100: 
    print ("Pago en efectivo")
elif compra > 100 and compra < 300: 
    print ("Pago con tarjeta de débito")
else: 
    print ("Pago con tarjeta de crédito")

#ESTRUCTURA WHILE
anio = 2005
while anio <= 2012: 
    print ("Informes del Año"), str(anio) 
    anio += 1

#ESTRUCTURA FOR
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio'] 
for nombre in mi_lista: 
    print (nombre)

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo') 
for color in mi_tupla: 
    print (color)

for anio in range(2001, 2013): 
    print ("Informes del Año"), str(anio)