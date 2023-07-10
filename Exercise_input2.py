#Crea un script llamado tabla.py que realice las siguientes tareas:

#Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
#1. El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
#2. En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
#3. El script contendrá un bucle for que itere el número de veces del primer argumento.
#4. Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
#5. Dentro del segundo for ejecuta una instrucción ** print(" * ", end='')**, (end='' evita el salto de línea).
#6. Ejecuta el código y observa el resultado.

import sys
# print(sys.argv)
if (len(sys.argv) == 3):
    f = int(sys.argv[1])
    c = int(sys.argv[2])
    if((f >= 1 and f <= 9) and (c >= 1 and c <= 9)):
        print(f,c)
        for filas in range(f):
            for columnas in range(c):
                print("*",end = " ")
            print()

    else:
        print("Numeros mal digitados..., recuerde digitar numeros del 1 al 9")
        print("Por favor digite en tabla.py asi: \"Digite un numero1\" \"Digite otro numero\"")
else:
    print("Error al Digitar...")
    print("Por favor digite en tabla.py asi: \"Digite un numero1\" \"Digite otro numero\"")