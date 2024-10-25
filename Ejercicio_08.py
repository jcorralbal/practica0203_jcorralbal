#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 
#al 10.
for tabla in range(0,11):
    print("La tabla del 10 es: ")
    for numeros in range (0, 11):
        multiplicacion = tabla * numeros 
        print(f"{tabla} x {numeros} = {multiplicacion}")
