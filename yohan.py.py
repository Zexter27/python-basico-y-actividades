import math

numero = input("Ingrese un número: ")
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

num = input("Ingrese un número entero: ")
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

for i in range(1, 11):
    print(i)

n = input("Ingrese un número N: ")
suma = 0
for i in range(1, n):
    suma += i
print("La suma es:", suma)

contador = 1
while contador < 10:
    print(contador)
contador = contador + 1

positivos = 0
num = 1
while num != 0:
    num = input("Ingrese un número: ")
    if num > 0:
        positivos = positivos + 1
print("Cantidad de positivos:", positivos)

tabla = input("Ingrese un número para la tabla: ")
for i in range(1, 11):
    print(tabla, "x", i, "=", tabla * i)

suma = 0
num = 0
while num >= 0:
    num = input("Ingrese un número: ")
    if num > 0:
        suma = suma + num
print("Suma de positivos:", suma)

palabra = input("Ingrese una palabra: ")
vocales = 0
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales = vocales + 1
print("Cantidad de vocales:", vocales)

inicio = input("Ingrese el inicio: ")
fin = input("Ingrese el fin: ")
for num in range(inicio, fin):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        print(num)

num = input("Ingrese un número para raíz cuadrada: ")
if num >= 0:
    print("Raíz cuadrada:", math.sqrt(num))
else:
    print("Error, número negativo")

base = input("Ingrese la base: ")
altura = input("Ingrese la altura: ")
if base > 0 and altura > 0:
    area = (base * altura) / 2
    print("Área del triángulo:", area)
else:
    print("Datos inválidos")

grados = input("Ingrese grados: ")
if grados > 360:
    print("El ángulo supera una vuelta")
print("En radianes:", math.radians(grados))

decimal = input("Ingrese un número decimal: ")
print("Ceil:", math.ceil(decimal))
print("Floor:", math.floor(decimal))
print("Absoluto:", math.fabs(decimal))

limite = input("Ingrese límite: ")
for n in range(limite):
    print(3 ^ n)

for i in range(1, 10):
    print("Raíz de", i, "=", round(math.sqrt(i), 2))

n = input("Ingrese un número: ")
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        print("No es primo")
        break
    else:
        print("Es primo")

total = 0
for i in range(1, 5):
    total += math.factorial(i)
print("Suma factoriales:", total)

x = int(input("Ingrese x: "))
print((x + 6)/(3*x))

x = int(input("Ingrese x: "))
print((4*x - 8)/(2*x))

x = int(input("Ingrese x: "))
print(5*x**2 + 10*x / 5*x)

x = int(input("Ingrese x: "))
print(9*x**2 - 3*x / 3*x)

x = int(input("Ingrese x: "))
print((2*x**2 + 6*x + 4)/2*x)
