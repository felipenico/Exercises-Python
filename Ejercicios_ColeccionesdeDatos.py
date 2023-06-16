#Realiza un programa que siga las siguientes instrucciones:

#Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#Crea un conjunto llamado administradores con los administradores Juan y Marta.
#Borra al administrador Juan del conjunto de administradores.
#Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

usuarios = {'Marta','David','Elvira','Juan','Marcos'}
administradores = {'Juan','Marta'}

administradores.remove('Juan')
administradores.add('Marcos')

for usuario in usuarios:
    if(usuario in administradores):
        print(usuario,'es un administrador')
    else:
        print(usuario,'no es un administrador')


#Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones: *

#El caballero tiene el doble de vida y defensa que un guerrero.
#El guerrero tiene el doble de ataque y alcance que un caballero.
#El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
#Muestra como quedan las propiedades de los tres personajes.

caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

# Completa el ejercicio aquí
caballero['vida'] += 2
caballero['defensa'] += 2
guerrero['ataque'] += 2
guerrero['alcance'] += 2
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = 1
arquero['alcance'] = guerrero['alcance'] * 2 
personajes = [caballero,guerrero,arquero]
for cuadrilla in personajes:
    print(cuadrilla)

#Durante la planificación de un proyecto se han acordado una lista de tareas. 
# Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

#¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]
from collections import deque
tareas.sort()
tareas_ordenadas = deque()
for tarea in tareas:
    tareas_ordenadas.append(tarea[1])
#print(tareas_ordenadas)


print("==> Tareas Ordenadas <==")
for tareas in tareas_ordenadas:
    print(tareas)