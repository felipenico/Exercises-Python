import spot
PointList = []
opciones = []
while(True):
    try:
        limite = int(input("Cuanto Puntos quiere generar?: "))
    except:
        print("\nDato no valido.. Escriba un numero mayor a cero")
    else:
        if(limite > 0):
            print("\nGracias por escribir su numero")
            break
        else:
            print("\nDato No valido...")

for n in range(limite):
    x = float(input(f"Digite la coordenada X del Punto {n}: "))
    y = float(input(f"Digite la coordenada Y del Punto {n}: "))
    PointList.append(spot.PuntoCartesiano(x,y)) 
while True:
    print("""\n1. Si quiere saber el Cuadrante de una Coordenada?
2.Si quiere saber el vector entre dos puntos?
3.Si quiere saber la distancia entre dos puntos?
4.Salir
Su opcion:""",end = " ")
    try:
        opcion = round(int(input()))
    except:
        print("\nError.... Dato NO valido!")
        continue
    else:
        if(opcion == 4):
            print("\n----------> Gracias por Utilizar el Programa <----------")
            break
        elif(opcion > 4):
            print("\nError.... Dato NO valido!")
            continue
        elif(opcion == 1):
            for i in range(limite):
                print(f"{i}.{PointList[i]}")
            print("Su opcion?:",end = " ")
            o = int(input())
            PointList[o].queCuadrante()
            continue
    for i in range(limite):
        print(f"{i}.{PointList[i]}")
    for j in range(2):
        print("Su opcion?:",end = " ")
        opciones.append(int(input()))
    if(opcion == 2):
        PointList[opciones[0]].madeVector(PointList[opciones[1]])
        opciones = []
    elif(opcion == 3):
        PointList[opciones[0]].distan(PointList[opciones[1]])
        opciones = []
        
    

