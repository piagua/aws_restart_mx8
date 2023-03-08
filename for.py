students = ["Esteban", "Sandra","yomero"]

for student in students:
    if student == "Sandra":
        print("adios")
        continue
    print("Hola", student)
    
    
### range con un solo argumento va de 0 hasta n
### rnage con 2 argumentos va de n1 a n2
### range con 3 argumentos va de ni a n2 con saltos de n3

for i in range(2,10,3):
    print(i)
    
    
## imprimir numeros pares de cero a 100    
    
for i in range(0,101,2):
    print(i)