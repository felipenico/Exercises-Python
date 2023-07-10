from math import sqrt
class PuntoCartesiano:
    def __init__(self,X = 0,Y = 0):
        self.X = X;
        self.Y = Y;

    #redefinir el metodo str
    def __str__(self):
        return f"({self.X},{self.Y})"
    
    def queCuadrante(self):
        if(self.X > 0 and self.Y > 0):#Pertenece al primer Cuadrante
            print(f"El Punto ({self.X},{self.Y}) pertenece al Primer Cuadrante")
        elif(self.X < 0 and self.Y > 0 ):#Segundo cuadrante
            print(f"El Punto ({self.X},{self.Y}) pertenece al Segundo Cuadrante")
        elif(self.X < 0 and self.Y < 0):#Tercer cuadrante
            print(f"El Punto ({self.X},{self.Y}) pertenece al Tercer Cuadrante")
        elif(self.X > 0 and self.Y < 0):#Cuarto cuadrante
            print(f"El Punto ({self.X},{self.Y}) pertenece al Cuarto Cuadrante")
        else:
            print(f"Las Coordenadas del Punto({self.X},{self.Y}) es el Origen del Sistema de Coordenadas")

    def madeVector(self,p):
        rX = self.X - p.X
        rY = self.Y - p.Y
        print(f"El vector resultante de los Puntos ({self.X},{self.Y}) y ({p.X},{p.Y}) es: ({rX},{rY})")
    
    def distan(self,p):
        print(f"La Distancia entre los Puntos ({self.X},{self.Y}) y ({p.X},{p.Y}) es: {sqrt(((self.X - p.X)**2) + ((self.Y - p.Y)**2)):.4f}")


