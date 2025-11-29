#ACTIVIDAD 2 


#Facturación de acomulados



import math

suma = 0
for i in range(1, 6):
    fact = math.factorial(i)
    print(f"{i}! = {fact}")
    suma += fact

print("Suma total de los factoriales:", suma)




import math

num = float(input("Ingresa un número: "))
if num > 0:
    print("La raíz cuadrada es:", math.sqrt(num))
else:
    print("Error: el número no es positivo.")

#Área de un triángulo 

base = float(input("Base: "))
altura = float(input("Altura: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print("El área del triángulo es:", area)
else:
    print("Datos no válidos, deben ser positivos.")

#conversación de grados radianes

import math

grados = float(input("Ingresa el ángulo en grados: "))
radianes = math.radians(grados)
print("El ángulo en radianes es:", radianes)

if grados > 360:
    print("El ángulo supera una vuelta completa.")



#Número redondeado


import math

num = float(input("Ingresa un número decimal: "))
print("Redondeo hacia arriba (ceil):", math.ceil(num))
print("Redondeo hacia abajo (floor):", math.floor(num))
print("Valor absoluto (fabs):", math.fabs(num))



#Potencias hasta un límite 

limite = int(input("Ingresa el límite: "))

for n in range(limite + 1):
    print(f"3^{n}={3**n}")


#Tabla de raíces cuadradas

import math

for i in range(1, 11):
    print(f"Raíz cuadrada de {i} = {round(math.sqrt(i), 2)}")


#Factorización de un número primo 

import math

num = int(input("Ingresa un número: "))

if num < 2:
    print("No es primo.")
else:
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("No es primo.")







#ACTIVIDAD 1 
#Ejercicio 1
numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#Ejercicio 2
numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Ejercicio 3

for i in range(1, 11):
    print(i)

#Ejercicio 4
N = int(input("Ingresa un número N: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print(f"La suma de los números del 1 al {N} es: {suma}")

#Ejercicio 5
contador = 1

while contador <= 10:
    print(contador)
    contador += 1

#Ejercicio 6
contador_positivos = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    if numero > 0:
        contador_positivos += 1

print(f"Cantidad de números positivos ingresados: {contador_positivos}")

#Ejercicio 7 

numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Ejercicio 8
suma = 0

while True:
    numero = float(input("Ingresa un número (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero

print(f"La suma de los números positivos ingresados es: {suma}")

#Ejercicio 9
palabra = input("Ingresa una palabra: ")
vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra '{palabra}' contiene {contador} vocal(es).")

#Ejercicio 10

inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

print(f"Números primos entre {inicio} y {fin}:")

for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

