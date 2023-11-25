from tkinter import *
from tkinter import filedialog as FileDialog
root = Tk()
root.title("Contador")
#variables Var
resulVar = StringVar()
ruta = ""
contador = 0
#acciones
def guardar():
    global ruta        
    fichero = FileDialog.asksaveasfile(title="Guardar Contador",mode="w+",defaultextension=".txt",
                                       initialdir="C:\\Users\\Felipe Niño Cortes\\Documents\\Repositorios GitHub\\Repository Python\\Tkinter")
                                       #aplicar la doble diagonal invertida para aplicar la ruta inicial
    ruta = fichero.name
    if ruta is not None:
        contenido = resulVar.get()
        with open(ruta,"w+") as fichero:
            fichero.write(contenido)
        resulVar.set("")

def abrir():
    global ruta
    resulVar.set("")
    ruta = FileDialog.askopenfilename(title="Abrir Fichero",filetypes=(("Fichero de texto",".txt"),))
    if ruta != "": 
        with open(ruta,"r") as admin:
            contenido = admin.read()
            resulVar.set(contenido)
def nuevo():
    global ruta
    ruta = ""
    resulVar.set("0")

def incrementar():
    contenido = int(resulVar.get())
    contenido += 1
    resulVar.set(contenido)
def decrementar():
    contenido = int(resulVar.get())
    contenido -= 1
    resulVar.set(contenido)

menubar = Menu()
root.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command = nuevo)
filemenu.add_command(label="Save As",command = guardar)
filemenu.add_command(label="Open file",command = abrir)

menubar.add_cascade(label = "File",menu=filemenu)

#label1 = Label(root,text = "Seleccione la operacion:")
#label1.grid(row=0,column=0,sticky="w",padx=3,pady=1)
#label1.config(bg = "blue",fg="#fff",font=("Console",12))

Button(root,text = "Incrementar",command=incrementar).grid(row=2,column=0,padx=3,pady=3)
Button(root,text = "Decrementar",command=decrementar).grid(row=2,column=1,padx=3,pady=3)

resul = Label(root,text="Contador: ",font=("Console",11))
resul.grid(row=3,column=0,sticky="w")
entradaResul = Entry(root,justify="center",textvariable=resulVar,state="disabled")
entradaResul.grid(row=3,column=1,padx=3,pady=3)

root.mainloop()