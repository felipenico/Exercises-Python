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
    n2 = 0
    n4 = 0
    def imprimir(p):
        print("\n"+type(p).__name__)
        print(p)

    for p in vehiculos:
        if(p.ruedas != 2 and p.ruedas != 0 and p.ruedas != 4):
            print(f"No se ha encontrado ningun vehiculo con {ruedas}")
        elif(p.ruedas == ruedas):
            imprimir(p)
            n2 += 1
        elif(p.ruedas == ruedas):   
            imprimir(p)
            n4 += 1
        elif(ruedas == None):
            imprimir(p)
    if (ruedas == 2):
        print(f"Se han encontrado {n2} vehículo(s) con {ruedas} ruedas:")
    if (ruedas == 4):
        print(f"Se han encontrado {n4} vehículo(s) con {ruedas} ruedas:")

