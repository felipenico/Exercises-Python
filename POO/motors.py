class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):# \Quita el espacio vacio al imprimir 
        return """Color: {}\nRuedas:{}\n""".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + "Velocidad: {}km/h\nCilindraje: {}cc\n".format(self.velocidad, self.cilindrada)
    
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)#llamando al constructor de Clase de nuestra SuperClase
        self.carga = carga

    def __str__(self):
        return super().__str__() + f"Carga: {self.carga}kg\n"

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f"Tipo: {self.tipo}\n"
    
class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "Velocidad: {}km/h\nCilindrada: {}cc\n".format(self.velocidad,self.cilindrada)

def catalogo(vehiculos,ruedas = None):
    n = 0
    def imprimir(p):
        print("\n"+type(p).__name__)
        print(p)
    if (ruedas == None):
        for i in vehiculos:
            imprimir(i)
    elif(ruedas != 2 and ruedas != 4):
        print(f"No se ha encontrado ningun vehiculo con {ruedas}")
        return
    for p in vehiculos:
        if(p.ruedas == ruedas):#2
            imprimir(p)
            n += 1
        #elif(ruedas == None):
         #   imprimir(p)
    print(f"Se han encontrado {n} vehículo(s) con {ruedas} ruedas")
