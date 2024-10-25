#Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla si es par o impar.
num_usuario = int(input("Introduzca un número entero "))
if num_usuario % 2 == 0:
    print(f"el número {num_usuario} es par")
else:
    print(f"El número {num_usuario} es impar")
    