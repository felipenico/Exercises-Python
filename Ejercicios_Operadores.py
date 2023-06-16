#Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

n1 = float(input("Digite un numero: "))
n2 = float(input("Digite otro numero: "))
print("Los numeros son iguales?: ",(n1 == n2))
print("Los numeros son Diferentes?: ",(n1 != n2))
print("n1 es mayor que n2?: ",(n1 > n2))
print("n2 es mayor o igual que n1?: ",(n2 >= n1))

# Un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
while True:
    try:
        numero_usuario = int(input("Digite un numero entero del 1 al 9: "))
    except ValueError:
        print("Error.. Clase de dato NO valida!")
    else:
        if(numero_usuario >= 1 and numero_usuario <= 9):
            break
        else:
            print("Tienes que digitar un numero entero del 1 al 9")
numero_usuario *= 9
numero_magico *= numero_usuario
print(numero_magico)
