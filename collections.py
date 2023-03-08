##LISTAS


# Secuecia
# posiciones
# 0,1,2,3
# Permite repetidos
# posiciones represntadas en indices
# si uso indicadores negativos se accede de atras para adelante desde 1


fruits = ["grape","Apple", "Coco"]

print(fruits)
fruits[0] = True
print (f"Fruits es {type(fruits)} el primer elemento es {type(fruits[0])}")

print(" el indice de Coco es ", fruits.index("Coco"))


#### TUPLA

#es imputable

colors = ("Blue", "Red", "Yellow")
print (colors)

## DICCIONARIO
#key, value

students = ["Esteban", "otro", "yo mero"]
notas = [100,78,34]

print(students,notas)


## RECORDS
records = {"Esteban":300, "otro":90, "yomero":90}

print(records)