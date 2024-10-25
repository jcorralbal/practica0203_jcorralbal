#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la 
#contraseña correcta.
contraseña = "contraseña"
while True:
    contraseña_usuario = input("Introduzca la contraseña: ")
    if contraseña_usuario == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        