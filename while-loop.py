#### lab 8 trabajo com bucles


import random

print("Bienvenido adivine un numero!")
print("Las reglas son simple. Yo pienso un numero y tu las adivinas")

numero = random.randint(1,10)

isGuessRigth = False

while isGuessRigth != True:
    guess = int(input("Adivina un numero del 1 al 10:"))
    
    if guess == numero:
        print("Bien, adivinaste el numero")
        isGuessRigth = True
        
    else:
        print("El numero no es correcto, intenta de nuevo")