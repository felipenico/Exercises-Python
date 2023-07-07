#https://www.youtube.com/watch?v=ocTilOz-xx4
#1  De dos números, saber cual es el mayor.
a = float(input("Digite un numero: "))
b = float(input("Digite otro numero: "))
if a > b:
    print(f"El numero mayor entre {a} y {b} es {a}")
else:
    print(f"El numero mayor entre {a} y {b} es {b}")
#2 Crea una variable númerica y si esta entre 0 y 10, mostrar un mensaje indicandolo.
c = 25
if c >= 0 and c <= 10:
    print(f"El numero {c} esta entre 0 y 10")
elif(c >= 11 and c <= 20):
    print(f"El numero {c} esta entre 11 y 20")
elif(c >= 21 and c <= 30):
    print(f"El numero {c} esta entre 21 y 30")

else:
    print("El numero que acabo de digitar se encuentra fuera del rango de 0 a 30")
#3 Añadir al anterior ejercicio, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.