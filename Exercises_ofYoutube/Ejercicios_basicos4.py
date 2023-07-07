#https://www.youtube.com/watch?v=h4ziC95nzQc
#Generar un rango entre 0 y 10
for n in range(0,11):
    print(f"{n}")
#Generar un número entre 5 y 10
print("Next")
print(list(range(5,11)))
#Generar un rango de 10 a 0.
print(list(range(10,-1,-1)))
#Generar un rango de 0 a 10 y de 15 a 20, incluidos el 10 y 20
print(list(range(0,11))+ list(range(11,21)))
#Generar un rango desde 0 hasta la longitud de la cadena “Hola mundo"
cadena = len("Hola mundo")
print(list(range(0,cadena)))