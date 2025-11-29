# ====================== TAREA 1 ======================

# Ejercicio 1 — Número positivo o negativonum = int(input('Ingrese un número: '))
if num > 0:
    print('El número es positivo')
elif num < 0:
    print('El número es negativo')
else:
    print('El número es cero')

print('='*40)

# Ejercicio 2 — Número par o impar
n = int(input('Ingrese un número entero: '))
if n % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')

print('='*40)

# Ejercicio 3 — Mostrar números del 1 al 10
for i in range(1, 11):
    print(i)

print('='*40)

# Ejercicio 4 — Suma de números del 1 al N
N = int(input('Ingrese N: '))
suma = 0
for i in range(1, N + 1):
    suma += i
print(f'La suma es: {suma}')

print('='*40)

# Ejercicio 5 — Contador con while
i = 1
while i <= 10:
    print(i)
    i += 1

print('='*40)

# Ejercicio 6 — Contar números positivos
cont = 0
num = int(input('Ingrese un número (0 para terminar): '))
while num != 0:
    if num > 0:
        cont += 1
    num = int(input('Ingrese otro número (0 para terminar): '))
print(f'Se ingresaron {cont} números positivos')

print('='*40)

# Ejercicio 7 — Tabla de multiplicar
num = int(input('Ingrese un número para su tabla de multiplicar: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

print('='*40)

# Ejercicio 8 — Suma de números positivos
suma = 0
num = int(input('Ingrese un número (negativo para terminar): '))
while num >= 0:
    suma += num
    num = int(input('Ingrese otro número (negativo para terminar): '))
print(f'La suma de los números positivos es {suma}')

print('='*40)

# Ejercicio 9 — Contar vocales en una palabra
palabra = input('Ingrese una palabra: ')
vocales = 'aeiouAEIOU'
cont = 0
for letra in palabra:
    if letra in vocales:
        cont += 1
print(f'La palabra contiene {cont} vocales')

print('='*40)

# Ejercicio 10 — Números primos en un rango
inicio = int(input('Ingrese el inicio del rango: '))
fin = int(input('Ingrese el fin del rango: '))
for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

print('='*80)


# ====================== TAREA 2 ======================

import math    

num = int(input('Ingrese el número al cual sacará raíz cuadrada :'))
if num >= 0:
    raiz = math.sqrt(num)
    print(raiz)
else:
    print('No puede ser negativo')

print('='*40)

base = int(input('Ingrese la base :'))
altura = int(input('Ingrese la altura :'))
if base <= 0:
    print('La base no es válida')
if altura <= 0:
    print('La altura no es válida')
else:
    area = (base*altura)/2
    print(f'El área del triángulo es {area}')

print('='*40)

angulo = int(input('Ingrese el ángulo en grados :'))
if angulo > 360:
    print('El ángulo supera una vuelta completa')
else:
    radian = math.radians(angulo)
    print(f'{angulo}° en radianes es {radian}')    

print('='*40)

n = float(input('Ingrese un número decimal :'))
print(f'{n} redondeado hacia arriba -> {math.ceil(n)}')
print(f'{n} redondeado hacia abajo -> {math.floor(n)}')
print(f'valor absoluto de {n} -> {math.fabs(n)}')

print('='*40)

limite = int(input('Ingrese el límite :'))
for i in range(limite + 1):
    print(f'3**{i} = {3**i}')

print('='*40)

for i in range(1, 11):
    print(f'{round(math.sqrt(i), 2)}')

print('='*40)

e = int(input('Ingrese un número entero :'))
r = math.sqrt(e)
r = int(r)
primo = True
if e <= 1:
    primo = False
elif e == 2:
    primo = True
elif e > 2 and e % 2 == 0:
    primo = False
else:        
    for i in range(3, r, 2):
        if e % i == 0:
            primo = False
            break
if primo:
    print(f'El número {e} es primo')
else:
    print(f'El número {e} no es primo')

print('='*40)

suma = 0
for i in range(1, 6):
    facto = math.factorial(i)
    print({facto})
    suma += facto
print(f'La suma total de los factoriales es -> {suma}')    

print('='*80)


# ====================== TAREA 3 ======================

import sympy as sp
from sympy import symbols, simplify
x = symbols('x')

fra = (x + 6)/(3*x)
sim = simplify(fra)
print(f'La fracción simplificada es {sim}')

print('='*40)

frac = (4*x - 8)/(2*x)
print(f'La fraccion algebraica simplificada -> {simplify(frac)}')

print('='*50)

print(f'(5x² + 10x)/(5x) simplificada -> {simplify((5*x**2 + 10*x)/(5*x))}')
print('='*50)

print(f'(9x² - 3x)/(3x) simplificada -> {simplify((9*x**2 - 3*x)/(3*x))}')
print('='*66)

print(f'(2x² + 6x + 4)/(2x) simplificada -> {simplify((2*x**2 + 6*x + 4)/(2*x))}')
