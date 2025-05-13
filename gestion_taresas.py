import heapq

# Creamos una lista para almacenar las tareas como una cola de prioridad
tareas = []

def agregar_tarea(nombre, prioridad):
    # heapq usa min-heap, así que la prioridad más baja estará primero
    heapq.heappush(tareas, (prioridad, nombre))
    print(f"Tarea '{nombre}' con prioridad {prioridad} añadida.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        print("Tareas ordenadas por prioridad:")
        for prioridad, nombre in sorted(tareas):
            print(f" - {nombre} (Prioridad: {prioridad})")

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
                agregar_tarea(nombre, prioridad)
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
