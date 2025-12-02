"""evaluación final módulo 3, Daniel Cifuentes.
---------------------------------------------------------
Objetivo

En esta actividad, desarrollarás una aplicación de línea de comandos que permitirá gestionar tareas de manera sencilla. Con este proyecto, aplicarás conocimientos fundamentales de Python, incluyendo el uso de estructuras de datos, funciones, control de flujo y módulos.

Contexto

Imagina que eres un desarrollador que necesita una herramienta ligera para organizar sus pendientes diarios desde la terminal. No quieres depender de aplicaciones externas ni de herramientas visuales avanzadas, sino algo simple y funcional que puedas ejecutar en cualquier sistema con Python instalado.

Para ello, construirás una aplicación que permita al usuario agregar tareas, verlas, marcarlas como completadas y eliminarlas. Además, las tareas deberán guardarse en un archivo para que no se pierdan cuando se cierre el programa.

Requisitos del Proyecto

1. Menú interactivo

* La aplicación debe mostrar un menú en la consola con opciones numéricas para que el usuario pueda elegir qué acción realizar.

2. Operaciones básicas:

* Agregar una nueva tarea.

* Listar todas las tareas con un indicador de estado (Pendiente o Completada).

* Marcar una tarea como completada.

* Eliminar una tarea.

* Salir del programa.

3. Estructuras de datos

* Utilizar diccionarios para representar cada tarea.

* Usar una lista para almacenar todas las tareas.

4. Funciones
* Dividir el código en funciones reutilizables para cada operación.

5. Validaciones y manejo de errores

* Evitar errores al ingresar opciones no válidas.

* Manejar archivos de manera segura para evitar pérdidas de datos.

Ejemplo de Uso

Cuando el usuario ejecute el programa, verá un menú como el siguiente:

--- Gestor de Tareas ---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir

Elige una opción:
Al seleccionar una opción se ejecuta el código detrás de esa opción volvemos al menu hasta que el usuario seleccione Salir.
"""

tareas = [] #Para probar con lista vacía, me daba problemas en marcar tareas y eliminar, ya lo solucioné.

#Paraprobar con una lista:
tareas = [
    {"Número": 1, "Tarea": "Revisar correos", "Estado": "Pendiente"},
    {"Número": 2, "Tarea": "Preparar informe", "Estado": "Completada"},
    {"Número": 3, "Tarea": "Llamar al cliente", "Estado": "Pendiente"},
    {"Número": 4, "Tarea": "Actualizar base de datos", "Estado": "Pendiente"},
    {"Número": 5, "Tarea": "Reunión equipo", "Estado": "Pendiente"},
    {"Número": 6, "Tarea": "Enviar cotización", "Estado": "Completada"},
    {"Número": 7, "Tarea": "Revisar presupuesto", "Estado": "Pendiente"},
    {"Número": 8, "Tarea": "Documentar procesos", "Estado": "Pendiente"},
] 

############ FUNCIONES #############

#0.1  FUNCIÓN DE VALIDACIÓN
"""(Dado que se interactúa varias veces con consola, y que las opciones que
se pueden ingresar son limitadas, hice una función de validación que pueda
ser reutilizada)"""

def validacion(minimo, maximo): #El rango es variable para poder ser reutilizada en distintas partes del código
    if maximo == 0: 
      return #para no ejecutar en caso de que no haya lista y que continúe el código.
    validador = 0
    while validador != 1:
        valor = input(f"Selecciona la opción (números del {minimo} al {maximo}): ")

        if valor.isdigit():
            numero = int(valor)
            if minimo <= numero <= maximo:
                validador = 1
            else:
                print("El número no es una opción valida. Intente nuevamente.")
        else:
            print("Entrada inválida. Intente nuevamente.")

    print(f"Ha seleccionado la opción: {numero}")
    return numero #La función retorna el número validado para avanzar a la siguiente línea de código

#0.2 MENÚ
#(por cuestiones de orden, hice el menú como función)
def menu():
  print("\n#####GESTOR DE TAREAS#####")
  print("1. Agregar tarea")
  print("2. Ver tareas")
  print("3. Marcar tarea como completada")
  print("4. Eliminar tarea")
  print("5. Salir")
  print("----------------------------")

#1. FUNCIÓN AGREGAR TAREA
def agregarTarea(lista, estado="Pendiente"):
    tarea = input("Ingresa el nombre de la nueva tarea: ")

    if not lista: 
        nuevo_numero = 1
    else:
        max_numero = max(elem["Número"] for elem in lista)
        nuevo_numero = max_numero + 1

    nuevo_elemento = {
        "Número": nuevo_numero,
        "Tarea": tarea,
        "Estado": estado
    }

    lista.append(nuevo_elemento)
    print(f"La tarea '{tarea}' ha sido agregada con éxito.")
    print("---------------------------- \n")

#2. FUNCIÓN VER TAREAS
#(Esta función se reciclará en más opciones además de la propia)
def verTareas(lista):
  for elem in lista:
    print(f"{elem['Número']}.- {elem['Tarea']} - Estado: {elem['Estado']}")
  print("---------------------------- \n")
  return len(lista) #Devuelve el len, que será utilizado como rango máximo en algunas validaciones

#3. FUNCIÓN MARCAR TAREA COMO COMPLETADA
#(Aquí decidí hacer posible también la opción inversa)
def marcarTarea(lista, numero_marcado):
  if not lista:
    print("No hay tareas para marcar como completadas.") #Para continuar en caso de que no haya lista
  else:
      if lista[numero_marcado - 1]["Estado"] == "Pendiente":
        lista[numero_marcado - 1]["Estado"] = "Completada"
      else:
        lista[numero_marcado - 1]["Estado"] = "Pendiente"
      print(f"Se ha actualizado el estado de la tarea '{lista[numero_marcado-1]['Tarea']}' a '{lista[numero_marcado-1]['Estado']}' ")
      print("----------------------------\n")

#4. FUNCIÓN ELIMINAR TAREA
def eliminarTarea(lista, numero_a_eliminar):
    if not lista:
        print("No hay tareas para eliminar.") #Para continuar en caso de que no haya lista
        return
    i = 0
    # Buscar y eliminar el elemento con el número seleccionado
    while i < len(lista):
        if lista[i]["Número"] == numero_a_eliminar:
            elemento_eliminado = lista[i]
            del lista[i]
            break
        i += 1

    # Reasignar los números
    i = 0
    while i < len(lista):
        lista[i]["Número"] = i + 1
        i += 1
    print(f"La tarea '{elemento_eliminado['Número']}.- {elemento_eliminado['Tarea']}' ha sido eliminada con éxito.")
    print("----------------------------\n")

#APP
numero = 0 #Inicialización
while numero != 5: #El menú sólo finalizará si se escoge la opción salir
  menu()
  numero = validacion(1,5)
  if numero == 1:
    print("\n#####AGREGAR TAREA#####")
    print("Listado actual de tareas:")
    verTareas(tareas)
    agregarTarea(tareas)
    print("---Lista actualizada:---")
    verTareas(tareas)
  elif numero == 2:
    print("\n#####VER TAREAS#####")
    verTareas(tareas)
  elif numero == 3:
    print("\n#####CAMBIAR ESTADO DE TAREA#####")
    maximo = verTareas(tareas)
    numero_marcado = validacion(1,maximo)
    marcarTarea(tareas, numero_marcado)
    print("---Lista actualizada:---")
    verTareas(tareas)
  elif numero == 4:
    print("\n#####ELIMINAR TAREA#####")
    maximo = verTareas(tareas)
    numero_eliminar = validacion(1,maximo)
    tarea_eliminada = eliminarTarea(tareas, numero_eliminar)
    print("---Lista actualizada:---")
    verTareas(tareas)
  elif numero == 5:
    print("\n#####FIN DEL PROGRAMA#####")
    print("La app ha finalizado correctamente.")
    print("----------------------------")