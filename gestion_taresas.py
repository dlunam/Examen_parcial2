# Gestor de tareas con prioridades, dependencias y caso de prueba

tareas = {}
completadas = set()

def agregar_tarea(nombre, prioridad, dependencias):
    if nombre in tareas:
        print("⚠️ Ya existe una tarea con ese nombre.")
        return
    tareas[nombre] = (prioridad, dependencias)
    print(f"✅ Tarea '{nombre}' añadida con prioridad {prioridad} y dependencias: {dependencias or 'ninguna'}.")

def mostrar_tareas():
    if not tareas:
        print("📭 No hay tareas.")
    else:
        print("\n📋 Tareas ordenadas por prioridad:")
        for nombre, (prioridad, dependencias) in sorted(tareas.items(), key=lambda item: item[1][0]):
            dep_str = ', '.join(dependencias) if dependencias else 'ninguna'
            estado = "✅ completada" if nombre in completadas else "⏳ pendiente"
            print(f" - {nombre} (Prioridad: {prioridad}, Dependencias: {dep_str}, Estado: {estado})")

def tarea_mayor_prioridad():
    candidatas = [
        (prioridad, nombre)
        for nombre, (prioridad, dependencias) in tareas.items()
        if nombre not in completadas and all(dep in completadas for dep in dependencias)
    ]
    if not candidatas:
        print("🚫 No hay tareas disponibles sin dependencias pendientes.")
    else:
        prioridad, nombre = min(candidatas)
        print(f"🔝 La siguiente tarea más prioritaria es: '{nombre}' (Prioridad: {prioridad})")

def completar_tarea():
    nombre = input("🔧 Nombre de la tarea a marcar como completada: ")
    if nombre in tareas and nombre not in completadas:
        completadas.add(nombre)
        print(f"✅ Tarea '{nombre}' marcada como completada.")
    elif nombre in completadas:
        print("⚠️ Esa tarea ya está completada.")
    else:
        print("❌ Tarea no encontrada.")

def prueba_caso_de_uso():
    print("\n🎬 --- Ejecutando caso de prueba ---")
    tareas.clear()
    completadas.clear()

    agregar_tarea("Tarea1", 1, [])
    agregar_tarea("Tarea2", 2, ["Tarea1"])
    agregar_tarea("Tarea3", 3, ["Tarea2"])
    agregar_tarea("Tarea4", 2, [])

    print("\n📋 Tareas actuales:")
    mostrar_tareas()

    print("\n🔍 Tarea con mayor prioridad disponible:")
    tarea_mayor_prioridad()

    print("\n✅ Marcando 'Tarea1' como completada...")
    completadas.add("Tarea1")

    print("\n🔍 Nueva tarea con mayor prioridad disponible:")
    tarea_mayor_prioridad()

def menu():
    while True:
        print("\n==== MENÚ ====")
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Mostrar siguiente tarea prioritaria sin dependencias pendientes")
        print("4. Marcar tarea como completada")
        print("5. Ejecutar caso de prueba")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("📝 Nombre de la tarea: ")
            try:
                prioridad = int(input("🔢 Prioridad (entero, menor es más importante): "))
                deps_input = input("🔗 Dependencias (nombres separados por coma, o dejar vacío): ")
                dependencias = [d.strip() for d in deps_input.split(',')] if deps_input else []
                agregar_tarea(nombre, prioridad, dependencias)
            except ValueError:
                print("⚠️ Por favor, introduce un número entero para la prioridad.")
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            tarea_mayor_prioridad()
        elif opcion == "4":
            completar_tarea()
        elif opcion == "5":
            prueba_caso_de_uso()
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
