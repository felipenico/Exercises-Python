"""
Crearemos un Editos de texto primitivo 
"""
from tkinter import *
from tkinter import filedialog as FileDialog
ruta = ""

def New():
    global ruta #La variable ruta ahora es global, y las lineas donde es llamada esta variable haran 
    #referencia a esta variable global.
    mensaje.set("New file")
    ruta = ""
    texto.delete(1.0,"end")#El metodo interno .delete() del widget Text() permite eliminar el texto escrito
    #en el campo de texto editable, como primer argumento indicamos 1.0 significa que empieza a borrar desde el principio
    # y como segundo argumento la palabra "end" que borre hasta el final de todo.
    #Dentro de un Text() el primer caracter siempre es un salto de linea(\n), es por ello que colocamos 1.0
    #para eliminar este salto.
    root.title("IDE")

def Open(): 
    global ruta 
    mensaje.set("Open file")
    ruta = FileDialog.askopenfilename(initialdir = '.',filetype =(("Ficheros de texto","*.txt"),),
    title = "Abrir un fichero de texto") 
    #La propiedad initialdir permite modificar el directorio inicial que se abrira, el valor '.' significa
    #que abra el directorio actual.
    #La propiedad filetype permite modificar el tipo de fichero, es decir permitir el tipo de fichero
    #que queremos utilizar, para este caso solo podremos seleccionar ficheros de extension .txt
    #La variable ruta almacenara la apertura de un fichero que se seleccione a traves de la ventana emergente

    if ruta != "":
        with open(ruta,'r') as fichero:
            contenido = fichero.read()
            texto.delete(1.0,"end")
            texto.insert("insert",contenido)
            #El metodo interno .insert() del widget Text permite insertar un texto, como primer argumento
            #indicamos la accion que haremos y como segundo argumento indicamos lo que queremos insertar 
            #al cuadro de texto editable.
        root.title(ruta + " - IDE")
def save():
    mensaje.set("Save file")
    #fichero existe 
    if ruta !=  "" :
        contenido = texto.get(1.0,"end-1c")
        #El metodo interno .get() permite obtener el texto escrito, como primer argumento indicamos
        #1.0 para que comienze desde el inicio  y como segundo argumento "end" y que vaya al final del todo
        #La expresion regular -1c permite eliminar un salto de linea que se encuentra al final del texto 
        #o cadena del marco de texto Text()
        with open(ruta,'w+') as fichero:
            fichero.write(contenido)
        mensaje.set("Save Succesful")
    else:#Fichero No existe  
        save_as()

    
def save_as():
    global ruta
    mensaje.set("Save as file")
    fichero = FileDialog.asksaveasfile(title="Save file",mode='w',defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name#Almacena la ruta del fichero, el atributo de clase(name) almacena la ruta
        contenido = texto.get(1.0,"end-1c")
        with open(ruta,'w+') as fichero:
            fichero.write(contenido)
        mensaje.set("Save as Succesful")
        texto.delete(1.0,"end")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

root = Tk()
root.title("IDE")   

#Menu Principal 
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New File",command=New)
filemenu.add_command(label="Open File",command=Open)
filemenu.add_command(label="Save",command=save)
filemenu.add_command(label="Save as",command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(menu=filemenu,label="File")

#Caja de Texto
texto = Text(root)
texto.pack(fill = "both",expand=1)
texto.config(bd=0,padx=6,pady=4,font=("Consolas",12))

#Monitor 
mensaje = StringVar()
mensaje.set("Bienvenido al IDE")
monitor = Label(root,textvariable= mensaje,justify="left")
monitor.pack(side="left")

root.mainloop()