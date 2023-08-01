#Programa que lee dos Puntos y halla la base, la altura y el area de un Rectangulo o Cuadrado.
import POO.spot
PointList = []
limite = 2

def menu():
    for i in range(limite):
        print(f"{i}.{PointList[i]}")

for n in range(limite):
    x = float(input(f"Digite la coordenada X del Punto {n + 1}: "))
    y = float(input(f"Digite la coordenada Y del Punto {n + 1}: "))
    PointList.append(POO.spot.PuntoCartesiano(x,y)) 
RoC = POO.spot.FiguraRoC(PointList[0],PointList[1])

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
        if(opcion < 0 or opcion > 4):
            print("\nError.... Dato NO valido!")
            continue      
        if(opcion == 4):
            print("\n----------> Gracias por Utilizar el Programa <----------")
            break
    menu()
    if(opcion == 2):
        RoC.alturaRoC()
    elif(opcion == 3):
        RoC.areaRoC()
    elif(opcion == 1):
        RoC.baseRoC()

        

        
