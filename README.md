# Gestor de Tareas con Prioridad

## Descripción
Aplicación de línea de comandos desarrollada en Python para la gestión de tareas con distintos niveles de prioridad (baja, media y alta).
Permite organizar actividades, registrar su estado y mantener un historial de acciones realizadas.

---

## Problema
La gestión de tareas sin una estructura clara puede generar desorganización y dificultad para priorizar actividades importantes.

---

## Solución
Esta aplicación permite registrar tareas con distintos niveles de prioridad, facilitando su organización y seguimiento, además de mantener un registro de cambios realizados.

---

## Funcionalidades principales
- Registro de tareas con nivel de prioridad  
- Visualización de tareas  
- Gestión de estado de tareas (pendiente/completada)  
- Eliminación de tareas  
- Almacenamiento persistente en formato JSON  
- Registro de acciones mediante logging  

---

## Diseño técnico
- Estructura modular del código  
- Uso de JSON como almacenamiento de datos  
- Implementación de logging para trazabilidad  
- Manejo de estado de tareas (pendiente/completada)  
- Validación de datos de entrada (prioridad)  

---

## Enfoque en datos
El sistema trabaja con datos estructurados que incluyen prioridad y estado de tareas, lo que permite su posible uso en análisis como:
- Distribución de tareas por prioridad  
- Seguimiento de tareas completadas  
- Análisis de productividad  

---

## Tecnologías utilizadas
- Python  

---

## Ejecución
```bash
pip install -r requirements.txt
python main.py
