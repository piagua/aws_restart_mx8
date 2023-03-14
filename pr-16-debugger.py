name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")


import pdb

def suma(a, b):
    resultado = a + b
    pdb.set_trace()  # Insertar un punto de interrupción
    return resultado

print(suma(2, 3))