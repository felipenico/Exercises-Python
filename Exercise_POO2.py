#Programa que lee dos Puntos y halla la base, la altura y el area de un Rectangulo o Cuadrado.
import spot
PointList = []
limite = 2

def menu():
    for i in range(limite):
        print(f"{i}.{PointList[i]}\n")

for n in range(limite):
    x = float(input(f"Digite la coordenada X del Punto {n + 1}: "))
    y = float(input(f"Digite la coordenada Y del Punto {n + 1}: "))
    PointList.append(spot.PuntoCartesiano(x,y)) 
RoC = spot.FiguraRoC(PointList[0],PointList[1])

while True:
    print("""\n1.Si quiere saber la Base?
2.Si quiere saber la Altura?
3.Si quiere saber el Area?
4.Salir
Su opcion:""",end = " ")
    try:
        opcion = round(int(input()))
    except:
        print("\nError.... Dato NO valido!")
        continue
    else:
        if(opcion < 0):
            print("\nError.... Dato NO valido!")
            continue      
        if(opcion == 4):
            print("\n----------> Gracias por Utilizar el Programa <----------")
            break
        elif(opcion > 4):
            print("\nError.... Dato NO valido!")
            continue
    menu()
    if(opcion == 2):
        RoC.alturaRoC()
    elif(opcion == 3):
        RoC.areaRoC()
    elif(opcion == 1):
        RoC.baseRoC()

        

        
