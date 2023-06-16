#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

while True:
    print("""Que opcion deseas realizar?:
    1.Suma de dos numeros
    2.Resta de dos numeros(el primero menos el segundo)
    3.Multiplicacion de dos numeros
    4.SALIR""")
    try:
        opcion = int(input("Digite su opcion: "))
    except ValueError:
        print("Error... Clase de Dato NO valida!")
        continue
    else:
        if(opcion == 4):
            print("---> Gracias por haber utilizado la calculadora <---")
            break
        if(opcion > 4):
            print("\nComando desconocido...")
            print("Intentelo de nuevo...\n")
            continue
    n1 = float(input("Digite un numero: "))
    n2 = float(input("Digite otro numero: "))
    if(opcion == 1):
        print("La suma de los dos numero es:",n1 + n2)
    elif(opcion == 2):
        print("La resta de los dos numeros es:",n1 - n2)
    elif(opcion == 3):
        print("La multiplicacion de los dos numeros es:",n1 * n2)

#Realiza un programa que lea un número impar por teclado. 
#Si el usuario no introduce un número impar, 
#debe repetirse el proceso hasta que lo introduzca correctamente.

numero_impar = int(input("Digite un numero impar: "))
while(numero_impar % 2 == 0):
    numero_impar = int(input("Digite un numero impar: "))
else:
    print("--> Gracias por haber digitado un numero impar <-- que fue",numero_impar)

#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
sumatoria = 0
for i,n in enumerate(range(0,101,2)):
    sumatoria += n
print(sumatoria)

print(sum(range(0,101,2)))

#Realiza un programa que pida al usuario cuantos números quiere introducir. 
#Luego lee todos los números y realiza una media aritmética:
numeros = int(input("Digite cuantos numeros quiere introducir: "))
i = 0
sumatoria = 0
while(i < numeros):
    n = float(input("Digite el numero: "))
    sumatoria += n
    i += 1
print("Se han introducido",numeros,"números que en total han sumado",sumatoria,"y la media es",sumatoria/numeros)

#Con numeros aleatorios

from random import *
def aleatorio(x = 0):
    c = 0
    l = []
    while (c < x):
        nale = randrange(0,51)
        if(nale in l):
            continue
        else:
            c += 1
            l.append(nale)
    return l
while True:
    try:
        numeros = float(input("Cuantos numeros quiere?: "))
    except ValueError:
        print("\nError... Clase de dato NO valido!\n")
    else:
        numeros = round(numeros)
        break
listale = aleatorio(numeros)
print(listale)
media = (sum(listale))/numeros
print(f"Se han introducido {numeros} números que en total han sumado {sum(listale)} y la media es {media:.3f}")


#Realiza un programa que pida al usuario un número entero del 0 al 9,
#  y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
numeros = [1, 3, 6, 9]
entero = float(input("Digite un numero entero del 0 al 9: "))
while(entero < 0 or entero > 9):
    entero = float(input("Digite un numero entero del 0 al 9: "))
if(entero in numeros):
    print("El numero",entero,"se encuentra en la lista")
else:
    print("El numero",entero,"NO se encuentra en la lista")


#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
#pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista3 = []

for n in lista_1:
    if(n in lista_2 and n not in lista3):
        lista3.append(n)
print(lista3)