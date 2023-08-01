import POO.motors
listaVehiculos = []
#ruedas,cilindrada,velocidad,carga,color,tipo = 0,0,0,0,"",""
def pedir():
    color = input("Digite el Color del Coche: ")
    ruedas = int(input("Digite el numero de ruedas: "))
    velocidad = int(input("Digite la velocidad: "))
    cilindrada = int(input("Digite el cilindraje: "))
    return color,ruedas,velocidad,cilindrada

while True:
    print("""\
1.Quiere agregar un Coche?
2.Quiere agregar una Camioneta?
3.Quiere Agregar una Bicicleta?
4.Quiere Agregar una Motocicleta?
5.Mostrar Vehiculos?
6.SALIR
Su opcion?: """,end = "")
    try:
        opcion = int(input())
    except: 
        print("\nError.... Dato NO valido!")
        continue
    else:
        if(opcion == 6):
            print("\n----------> Gracias por Utilizar el Programa <----------")
            break
        if(opcion < 0 or opcion > 6):
            print("\nError.... Dato NO valido!")
            continue 
    if(opcion == 1):
        while True:
            try:
                color,ruedas,velocidad,cilindrada = pedir()
            except:
                print("\nError.... Dato NO valido!")
                continue
            else:
                break
        listaVehiculos.append(POO.motors.Coche(color,ruedas,velocidad,cilindrada))
    elif(opcion == 2):
        while True:
            try:
                color,ruedas,velocidad,cilindrada = pedir()
                carga= int(input("Digite la carga: "))
            except:
                print("\nError.... Dato NO valido!")
                continue
            else:
                break
        listaVehiculos.append(POO.motors.Camioneta(color,ruedas,velocidad,cilindrada,carga))
    elif(opcion == 3):
        
        while True:
            try:
                color = input("Digite el Color de la Bicicleta: ")
                ruedas = int(input("Digite el numero de ruedas: "))
                tipo = input("Digite el tipo de Bicicleta: ")
            except:
                print("\nError.... Dato NO valido!")
                continue
            else:
                break
        listaVehiculos.append(POO.motors.Bicicleta(color,ruedas,tipo))
    elif(opcion == 4):
        while True:
            try:
                color,ruedas,velocidad,cilindrada = pedir()
                tipo = input("Digite el tipo de Motocicleta: ")
            except:
                print("\nError.... Dato NO valido!")
                continue
            else:
                break
        listaVehiculos.append(POO.motors.Motocicleta(color,ruedas,velocidad,cilindrada,tipo))
    elif(opcion == 5):
        print("\n Se pueden consultar los vehiculos segun el numero de Ruedas,por favor digite 2 o 4")
        try:
            ruedas = int(input("Digite el Numero de ruedas: "))
        except:
            print("\nError.... Dato NO valido!")
            continue
        else:
            POO.motors.catalogo(listaVehiculos,ruedas)

