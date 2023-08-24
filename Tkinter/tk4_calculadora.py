'''
Primer Programa en Tkinter
'''
from tkinter import *

def sumar():
    resul.set( float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    resul.set(float(n1.get()) - float(n2.get()))
    borrar()

def multi():
    resul.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n2.set("")
    n1.set("")

root = Tk()
n1 = StringVar()# Inicializa un Objeto de la Clase StringVar
n2 = StringVar()#tenemos que convertir estas variables de StringVar a float para manipularlas   
resul = StringVar()
'''
Con la propiedad textvariable podemos obtener lo que se escribe en un campo de texto editable,
almacenarlo para despues operar con el 

El metodo interno .get() permite obtener el valor almacenado en el Objeto de la Clase StringVar()
(en este caso n1,n2 y resul) que pasamos como valor a la propiedad textvariable en la Clase Entry, 

Cada Widget ocupara una fila
'''
Label(root,text="Ingrese un numero:").grid(row = 0,column = 0,sticky="W",pady = 5)
Entry(root,justify="center",textvariable = n1).grid(row = 0 , column = 1,padx= 5,pady = 5)
Label(root,text="Ingrese un numero:").grid(row = 1,column = 0,sticky="W")
Entry(root,justify="center",textvariable=n2).grid(row = 1, column = 1)

Label(root,text="Resultado:").grid(row = 2,column = 0,sticky="W",pady = 5)
Entry(root,justify="center",textvariable=resul,state="disabled").grid(row = 2,column = 1,pady = 5)

Button(root,text="Sumar",command=sumar).grid(row=3,column=0,padx= 5,pady = 5)
Button(root,text = "Restar",command=restar).grid(row = 3,column=1,padx = 1,pady = 5)
Button(root,text = "Multiplicar",command=multi).grid(row = 3,column=2,padx = 1,pady = 5)

#Finalmente bucle de la aplicacion 
root.mainloop()