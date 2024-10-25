#Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla un triángulo rectángulo que tenga tantas líneas como el número 
#introducido, como el triángulo de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
num_lineas = int(input("Introduce un número entero: "))
for i in range(1, num_lineas + 1):
    numero_inicial = 2 * i - 1
    linea = ''
    for j in range(numero_inicial, 0, -2):
        linea += str(j) + ' '
    print(linea.strip())
    