## README - Gestor de Tareas con Prioridades y Dependencias

### Descripción

Este programa en Python permite gestionar tareas. Puedes:

* Añadir tareas con una prioridad (1 es la más alta).
* Establecer dependencias entre tareas (una tarea depende de que otras se completen primero).
* Ver todas las tareas y su estado.
* Marcar tareas como completadas.
* Ver cuál es la siguiente tarea disponible más prioritaria.
* Ejecutar un caso de prueba automático.

### Conceptos clave

* **Prioridad**: Número entero. A menor número, mayor prioridad.
* **Dependencias**: Lista de nombres de otras tareas que deben completarse antes.
* **Tareas completadas**: Se guardan en un conjunto (`set`).

### Funciones principales

* `agregar_tarea(nombre, prioridad, dependencias)`: Añade una nueva tarea.
* `mostrar_tareas()`: Muestra todas las tareas con su información.
* `tarea_mayor_prioridad()`: Muestra la tarea disponible más prioritaria.
* `completar_tarea()`: Permite marcar una tarea como completada.
* `prueba_caso_de_uso()`: Ejecuta un ejemplo automático con tareas y acciones.
* `menu()`: Muestra un menú interactivo para usar el programa desde la consola.

### Cómo usar

1. Ejecuta el archivo Python.
2. Usa el menú que aparece para:

   * Añadir tareas
   * Ver tareas
   * Ver la siguiente tarea disponible
   * Marcar tareas como completadas
   * Probar el caso automático


### Ejemplo

Si se ejecuta la prueba automática (opción 5 del menú), se puede ver un resultado como este:

```
Tarea 'Tarea1' añadida...
Tarea 'Tarea2' añadida...
La siguiente tarea más prioritaria es: 'Tarea1'
Marcando 'Tarea1' como completada...
Nueva tarea con mayor prioridad disponible: 'Tarea4'
```


