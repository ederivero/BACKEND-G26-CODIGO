# Adivinar el numero a la maquina
# Ingresar un numero del 1 al 10 
# si el numero ingresado esta fuera de este rango volver a pedirlo
# Adivinaremos el numero que la maquina escogio, si el numero que ingresamos es mayor que el numero que la maquina penso entonces imprimir "El numero es menor" y volver a pedir un numero, caso contrario imprimir "El numero es mayor" y volver a pedir un numero y si es el numero indicar que es el numero y terminar el while con un break
import random
# genera un numero aleatorio entre esos parametros
numero_a_adivinar = random.randint(1,10)
print(numero_a_adivinar)

while True:
    numero_ingresado = int(input('Ingrese un numero del 1 al 10:'))
    # Aca valido que este dentro de el rango
    if numero_ingresado < 1 or numero_ingresado > 10:
        print('Numero fuera de rango')
        continue
    
    # valido si es el numero correcto
    if numero_a_adivinar == numero_ingresado:
        print('Felicitaciones, adivinaste el numero')
        break # aca termina de manera abrupta la peticion de nuevos numeros xq ya se adivino

    # valido si el numero es mayor que el numero correro
    if numero_a_adivinar < numero_ingresado:
        print('El numero es menor')
    else:
        print('El numero es mayor')
