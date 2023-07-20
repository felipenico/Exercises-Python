#Leer de un fichero de texto.txt lo almacenado en el, convertirlo en un diccionario y 
#imprimirlo de manera visual al cliente
from io import open
with open("personas.txt","r",encoding="utf8") as fichero:
    reader = fichero.readlines()
    personas = []
    for fila in reader:
        l = fila.replace("\n","").split(";")
        personas.append({"id":l[0],"nombre":l[1],"apellido":l[2],"nacimiento":l[3]})
    #for id,name,ape,born in personas:
    #    per.append({"id":id,"nombre":name,"apellido":ape,"nacimiento":born})
    for c in personas:
        print(f"[{c['id']}] - {c['nombre']} {c['apellido']} ({c['nacimiento']})")
        