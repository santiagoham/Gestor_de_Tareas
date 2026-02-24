
from tareas import agregar_tarea, listar_tareas, marcar_completada, eliminar_tarea # Importo las funciones desde tareas.py
from rich import print # Importo "rich" con la finalidad de que el programa sea más estético


# Función para que aparezca el menú, donde se le pide al usuario que elija una opción
def mostrar_menu():
    print("\n[deep_sky_blue2]Menú del Gestor de Tareas[/deep_sky_blue2]")
    print("1. Agregar tarea")
    print("2. Lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción ingresando el número de la misma: ")

    if opcion == "1":
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = input("Qué grado de prioridad tiene su tarea? Alta, media, o baja?: ").lower()

        if prioridad not in ["alta", "media", "baja"]:
            print("[red1]Prioridad inválida. Intente nuevamente.[/red1]")
        else:
            agregar_tarea(titulo, descripcion, prioridad)

    elif opcion == "2":
        listar_tareas()

    elif opcion == "3":
        try:
            id_tarea = int(input("Ingrese el ID de la tarea para marcarla como completada: "))
            marcar_completada(id_tarea)
        except ValueError:
            print("[red1]ID inválido. Intente nuevamente.[/red1]")

    elif opcion == "4":
        try:
            id_tarea = int(input("Ingrese el ID de la tarea que desea eliminar: "))
            eliminar_tarea(id_tarea)
        except ValueError:
            print("[red1]ID inválido. Intente nuevamente.[/red1]")

    elif opcion == "5":
        print("[dark_cyan]Programa finalizado.[/dark_cyan]")
        break

    else:
        print("[red1]Opción inválida. Por favor, elija una opción del 1 al 5.[/red1]")