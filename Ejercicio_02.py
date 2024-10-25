#Escribir un programa que pida al usuario dos números y muestre por pantalla
#su división. Si el divisor es cero el programa debe mostrar un error.
print("A continuación introduzca un dividendo y un divisor")
n = int(input("Introduzca su dividendo: "))
m = int(input("Introduzca su divisor: "))
if m == 0:
        print("No puedes dividir entre cero")
else:     
        print(n/m)
        