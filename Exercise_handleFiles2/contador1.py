#Utilizamos la entrada del script para incrementar o decrementar el valor del contador 
#por tanto procura escribir en la entrada del script lo siguiente:[ruta_del_directorio "inc o dec"]
from io import open
import sys
with open("contador1.txt","a+") as fic:
    fic.seek(0)
    reader = fic.read()
    if(len(reader) == 0):
        reader = "0"
        fic.write(reader)
    i = int(reader[-1])#len(reader) - 1
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "inc"):
            i += 1
        elif(sys.argv[1] == "dec"):
            i -= 1
        print(i)
        if(i >= 0):
            fic.write(str(i))
        

    
