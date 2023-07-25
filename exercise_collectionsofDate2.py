#un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

#En este otro:

#Un día que el viento soplaba con fuerza...
#- Mira como se mueve aquella banderola -dijo un monje.
#- Lo que se mueve es el viento -respondió otro monje.
#- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.

#Lo único prohibido es modificar directamente el texto

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
texto = texto.split("#")
texto[0] = texto[0] + "..."
for i,n in enumerate(texto):
    texto[i] = n.capitalize()
    if(i > 0):
        texto[i] = "- " + texto[i] + "."
    print(texto[i])
#texto = "\n- ".join(texto)

#2) Crea una función tratar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

#Borrar los elementos duplicados
#Ordenar la lista de mayor a menor
#Eliminar todos los números impares
#Realizar una suma de todos los números que quedan
#Añadir como primer elemento de la lista la suma realizada
#Devolver la lista modificada
#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
copy_list = lista[:]
def tratar(clista):
    #1.)
    clista = list(set(lista))
    #2.)
    clista.sort(reverse = True)
    #3.)
    for i in range(0,len(clista))[::-1]:
        if((clista[i] % 2) != 0):
            clista.remove(clista[i])
    #4.)
    clista.insert(0,sum(clista))
    return clista

copy_list = tratar(copy_list)
print("\nLa suma de sus elementos da como resultado el primer elemento?:",copy_list[0] == sum(copy_list[1:]))