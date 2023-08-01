import squad
g = squad.Gestor()
def pedir():
    tropa = input("Digite el nombre de la tropa: ")
    salud = int(input("Digite la cantidad de Salud: "))
    ataque = int(input("Digite la cantidad de Ataque : "))
    defensa = int(input("Digite la cantidad de Defensa: "))
    alcance = int(input("Digite la cantidad de Alcance: "))
    return tropa,salud,ataque,defensa,alcance

while True:
    print("""\n
1.Para Digitar la tropa
2.Mostrar el escuadron
3.Borrar Tropa
4.SALIR
Su opcion?: """,end="")
    try:
        opcion = int(input())
    except:
        print("\nError.... Dato NO valido!")
        continue
    else:
        if(opcion == 4):
            g.save()
            print("\n----------> Gracias por Utilizar el Programa <----------")
            break
        elif(opcion < 0 or opcion > 4):
            print("\nError.... Dato NO valido!")
            continue
    if(opcion == 1):
        while True:
            try:
                name,life,attack,defense,alcance = pedir()
            except:
                print("\nError.... Dato NO valido!")
                continue
            else:
                break
        g.add(squad.Personaje(name,life,attack,defense,alcance))
    elif(opcion == 2):
        g.view()
    elif(opcion == 3):
        g.erase(input("Digite el nombre de la tropa a eliminar: "))
    
