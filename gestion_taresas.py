import heapq

# Diccionario de tareas: clave = nombre, valor = (prioridad, dependencias)
tareas = {}

def agregar_tarea(nombre, prioridad, dependencias):
    if nombre in tareas:
        print("Ya existe una tarea con ese nombre.")
        return
    tareas[nombre] = (prioridad, dependencias)
    print(f"Tarea '{nombre}' añadida con prioridad {prioridad} y dependencias: {dependencias or 'ninguna'}.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        print("\nTareas ordenadas por prioridad:")
        # Ordenar por prioridad (tareas.values() devuelve tuplas (prioridad, dependencias))
        for nombre, (prioridad, dependencias) in sorted(tareas.items(), key=lambda item: item[1][0]):
            dep_str = ', '.join(dependencias) if dependencias else 'ninguna'
            print(f" - {nombre} (Prioridad: {prioridad}, Dependencias: {dep_str})")

def menu():
    while True:
        print("\n1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            try:
                prioridad = int(input("Prioridad (entero, menor es más importante): "))
                deps_input = input("Dependencias (nombres separados por coma, o dejar vacío): ")
                dependencias = [d.strip() for d in deps_input.split(',')] if deps_input else []
                # Validar dependencias existentes
                for dep in dependencias:
                    if dep and dep not in tareas:
                        print(f"Advertencia: la tarea dependiente '{dep}' aún no existe.")
                agregar_tarea(nombre, prioridad, dependencias)
            except ValueError:
                print("Por favor, introduce un número entero para la prioridad.")
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
