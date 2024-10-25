#Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
#hasta que el usuario escriba “salir” que terminará.
# Programa que muestra el eco de todo lo que el usuario introduzca hasta que escriba "salir"
while True:
    frase_usuario = input("Escriba algo: ")
    if frase_usuario.lower() == "salir":
        print("Hasta luego")
        break
    else:
        print(frase_usuario)
        