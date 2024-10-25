#Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla un triángulo rectángulo como el de más abajo, de altura el 
#número introducido.
#*
#**
#***
#****
#*****
num_usuario = int(input("Introduzca un número entero: "))
for asterisco in range(1, num_usuario + 1):
    print('*' * asterisco)
    