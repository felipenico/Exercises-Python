#Le preguntamos al Usuario si digitara un incremento o decremento en el contador 
#y lo almacenamos en el fichero 
from io import open
try :
    with open("contador.txt","r") as fichero:
        i = int(fichero.read())
        print(i)
except FileNotFoundError:#Exception as iden
    #print(type(iden).__name__)
    with open("contador.txt","w") as fichero:
        print("hola")
        i = 0
        fichero.write(str(i))  
while True:
    print("""\n
inc -> Digite inc para Incrementar el Contador
dec -> Digite dec para Decrementar el Contador
3.SALIR""")
    print("Su opcion?: ",end = "")
    opcion = input("")
    if(opcion == "inc"):
        i += 1
    elif(opcion == "dec"):
        i -= 1
    elif(opcion == "3"):
        print("\n----------> Gracias por Utilizarinc el Programa <----------")
        break
    with open("contador.txt","w") as fichero:
        fichero.write(str(i))
    print(i)
    

