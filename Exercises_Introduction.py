#*A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota media. El problema es que cada nota tiene un valor porcentual: *
#
#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
#Desarrolla un programa para calcular perfectamente la nota final.
nota_1 = 10
nota_2 = 7
nota_3 = 4
nota_final = (nota_1*0.15) + (nota_2*0.35) + (nota_3*0.5)
print(f"{nota_final:.2f}")

# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, 
#es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. 
#¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
matriz[1][-1] = sum(matriz[1][:3])
matriz[-1][-1] = sum(matriz[-1][:3])
print(matriz)

#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
#Al parecer contiene el nombre de un alumno y la nota de un exámen. 
#¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:

#Nombre Apellido ha sacado un Nota de nota.

cadena = "zeréP nauJ,01"
cadena = cadena[::-1]
print(cadena[3:] + " ha sacado un " + cadena[:2] + ' de nota.')