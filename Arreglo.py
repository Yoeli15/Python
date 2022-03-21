import random
from random import randint

arreglo = []
validación = False

def añadirValores(numero):
    for i in range(numero):
        valor = random.randint(1,100)
        arreglo.append(valor)
    
    print("Los números que hay en tu arreglo son:", arreglo)

def sumarArreglo(numeros):
    suma = 0
    for valor in numeros:
            suma = suma + valor

    print(f"La suma del arreglo es: {suma}")

print("Antes de realizar la suma primero vamos a elegir la cantidad de números.")
print("NOTA: No pueden ser más de 1000\n")
while validación == False:
    cantidad = int(input("¿Cuántos valores quieres para tu arreglo?: "))
    if cantidad > 1000:
        print("No pueden ser más de 1000")
        #
    else:
        añadirValores(cantidad)
        break

sumarArreglo(arreglo)
