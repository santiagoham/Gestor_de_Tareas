from datetime import datetime
import json
import os
from rich import print # Importo "rich" con la finalidad de que el programa sea más estético

ARCHIVO_TAREAS = "tareas.json" # Acá vamos a guardar las tareas
ARCHIVO_LOG = "registro.log" # Acá vamos a guardar los registros


# Función para escribir los logs con fecha y hora para registrar las acciones que se realizan
def registrar_log(mensaje):
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(ARCHIVO_LOG, 'a', encoding='utf-8') as f:
        f.write(f'{ahora} - {mensaje}\n')



"""Función que carga la lista de tareas guardadas en el archivo .json.
   En caso de que no exista el archivo, retorna una lista vacía.
   Notifica si ocurre algún problema."""
def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[red1]Error al cargar tareas: {e}[/red1]")
        return []



"""Función para sobreescribir la lista de tareas en el archivo .json.
   Notifica si ocure algún problema."""
def guardar_tareas(tareas):
    try:
        with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
            json.dump(tareas, f, indent=4, ensure_ascii=False) # De esta manera es mejor visualmente
    except Exception as e:
        print(f"[red1]Error al guardar tareas: {e}[/red1]")


"""Función para generar un ID único para una tarea nueva.
   En caso de no haber tareas, empieza por el 1.
   En caso de que ya haya tareas, agarra el ID más alto y le suma 1 para que no se repitan."""
def generar_id(tareas):
    if not tareas:
        return 1
    return max(t['id'] for t in tareas) + 1


"""Función para crear una nueva tarea con los datos dados y con un estado de "pendiente".
   La añade a la lista de tareas cargadas desde el archivo.
   Guarda los cambios y los registra en el log.
   Notifica al usuario cuando se agrega."""
def agregar_tarea(titulo, descripcion, prioridad):
    tareas = cargar_tareas()
    nueva_tarea = {
        "id": generar_id(tareas),
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    registrar_log(f"Tarea agregada: {nueva_tarea}")
    print("[green3]Tarea agregada con éxito.[/green3]")



"""Función para mostrar en pantalla todas las tareas cargadas.
   En caso de no haber tareas, avisa que la lista está vacía."""
def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("[gold1]No hay tareas registradas.[/gold1]")
    else:
        print("\n Lista de tareas pendientes:")
        for t in tareas:
            print(f'ID: {t["id"]} | {t["titulo"]} ({t["prioridad"]}) - {t["estado"]}')



"""Busca la tarea por su ID y cambia su estado a "completada".
   Guarda los cambios y registra la acción hecha.
   En caso de que la ID no exista, muestra un mensaje de error."""

def marcar_completada(id_tarea):
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "completada"
            guardar_tareas(tareas)
            registrar_log(f"Tarea completada: ID {id_tarea}")
            print("[green3]Tarea marcada como completada.[/green3]")
            return
    print("[red1]ID de tarea no encontrado.[/red1]")



"""Elimina la tarea que coincide con el ID proporcionado.
   Si la ID no existe, se lo informa al usuario.
   Guarda los cambios y registra la acción en el log."""
def eliminar_tarea(id_tarea):
    tareas = cargar_tareas()
    nuevas_tareas = [t for t in tareas if t["id"] != id_tarea]
    if len(nuevas_tareas) == len(tareas):
        print("[red1]ID de tarea no encontrado.[/red1]")
    else:
        guardar_tareas(nuevas_tareas)
        registrar_log(f"Tarea eliminada: ID {id_tarea}")
        print("[green3]Tarea eliminada con éxito.[/green3]")
