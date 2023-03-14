## RETO FINAL DE PROGRAMACION
## ENCONTRAR NUMEROS PRIMOS


def es_primo(n): ## detecta si es primo
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nprimo = [] 
for i in range(1, 251): # se evalua el rango
    if es_primo(i):
        nprimo.append(i)


with open("results.txt", "w") as archivo: ## se escribe en el archivo
    archivo.write("numeros primos entre 1 y 250:\n")
    for p in nprimo:
        archivo.write(str(p) + "\n")
        print (str(p) )

print("Los numeros primos  se grabaran en  el archivo results.txt")