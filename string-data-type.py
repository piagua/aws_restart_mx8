myString = " esto es un string"
print(myString)
print(type(myString))
print(myString + "esto es un tipo "+ str(type(myString)))

mensaje = " hola"
mensaje += " \nSoy Esteban"
mensaje += "\n escribo asi"


#input recibe un string y se puede mostrar un valor para pedirlo

nombre = input ("Cual es tu nombre? ")

mensaje += nombre
print(mensaje)