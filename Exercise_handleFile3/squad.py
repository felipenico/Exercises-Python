from io import open
from math import *
import pickle
class Personaje:
    Personaje = {};
    def __init__(self,nombre: str,vida:float,ataque:float,defensa:float,alcance:float):
        if(vida > 0 and ataque > 0 and defensa > 0 and alcance > 0):
            self.Personaje = {"nombre":nombre,"vida":trunc(vida),"ataque":trunc(ataque),"defensa":trunc(defensa),"alcance":trunc(alcance)}
            print("Se creo al Personaje: "+ nombre)
        else:
            print("Datos Invalidos....")
            return
    
    def __str__(self):
        return f"""Nombre -> {self.Personaje["nombre"]}:
Vida: {self.Personaje["vida"]}
Ataque: {self.Personaje["ataque"]}
Defensa: {self.Personaje["defensa"]}
Alcance: {self.Personaje["alcance"]}\n"""
        
class Gestor:
    Personajes = []
    def __init__(self):
        self.load()
        
    def add(self,c):#c hace referencia a un Objeto de la Clase Personaje
        for i,n in enumerate(self.Personajes):
            if(n.Personaje["nombre"] == c.Personaje["nombre"]):
                print("Ya existe este personaje...")
                return
        self.Personajes.append(c)
        self.save()
     
    def view(self):
        if(len(self.Personajes) == 0):
            print("No se agregado ningun Personaje")
        else:    
            for n in self.Personajes:
                print(n)
                
    def erase(self,nombre):
        for i,n in enumerate(self.Personajes):
            if(n.Personaje["nombre"] == nombre):
                print(f"Se elimino el Personaje {nombre} de la lista")
                del(self.Personajes[i])   
                self.save()
            
    
    def load(self):
        with open("personajes.pckl","ab+") as characters:
            characters.seek(0)
            try:
                self.Personajes = pickle.load(characters)
            except:
                print("El fichero esta vacio")
            finally:
                print(f"Se han cargado {len(self.Personajes)} personajes")
    
    def save(self):
        with open("personajes.pckl","wb") as characters:
            pickle.dump(self.Personajes,characters)

if(__name__ == "__main__"):
    pass