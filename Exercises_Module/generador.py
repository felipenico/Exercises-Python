from math import *
from random import *
def leer_numero(ini,fin,mensaje):
    while True:
        try:#Evitar otro tipo de dato
            numero = int(input(mensaje))
        except:#ValueError
            print("Error.. Tipo de Dato NO Valido")
            continue
        else:
            if(numero >= ini and numero <= fin):
                return numero
            else:
                print(f"Error.. Digite un numero entre los valores [{ini}-{fin}]")
                continue

def generador():
    numeros = leer_numero(1,20,"¿Cuantos numeros quieres generar?[1-20]: ")
    modo = leer_numero(1,3,"¿Como quieres redondear los numeros?\n[1]Al alza\n[2]A la baja\n[3]Normal: ")
    lista = []
    i = 0

    while(i < numeros):
        u = uniform(1,101)
        print(f"Numero generado: {u}")
        if(modo == 1):
            u = ceil(u)
        elif(modo == 2):
            u = floor(u)
        else:
            u = round(u)
        print(f"Numero redondeado: {u}")
        if(u not in lista):
            lista.append(u)
        else:
            continue
        i += 1
    return lista

print(generador())
            




