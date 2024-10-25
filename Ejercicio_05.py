#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin,
#de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con 
#un nombre anterior a la M y los hombres con un nombre posterior a la N y 
#Slytheryn por el resto. Escribir un programa que pregunte al usuario su 
#nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (H o M): ")
if nombre == "M":
    if nombre.lower() < "m":
        casa = "Gryffindor"
    else:
        casa = "Slytheryn"
else:
    if nombre.lower() > "n":
        casa = "Gryffindor"
    else:
        casa = "Slytheryn"
print(f"Enhorabuena tu casa es {casa}: ")
