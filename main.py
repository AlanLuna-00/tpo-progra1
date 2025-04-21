from modules.consultas import mostrar_registro_por_patente, mostrar_ranking_tipos_vehiculo

def mostrar_menu():
    print("\n====== ESTACIONAMIENTO - CONSULTAS ======")
    print("1. Ver todos los registros")
    print("2. Filtrar por tipo de vehículo")
    print("3. Buscar por patente")
    print("4. Ver ingresos de clientes (con DNI)")
    print("5. Ver ingresos por fecha")
    print("6. Mostrar estadísticas")
    print("7. Marcar salida de un vehículo")
    print("8. Registrar ingreso de un vehículo")
    print("9. Gestión de cocheras")
    print("0. Salir")

def main():
    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("→ Mostrar todos los registros")

        elif opcion == "2":
            print("→ Filtrar por tipo de vehículo")

        elif opcion == "3":
            print("→ Buscar registros por patente")
            mostrar_registro_por_patente()

        elif opcion == "4":
            print("→ Ingresos de clientes con DNI")

        elif opcion == "5":
            print("→ Ranking sobre tipos de vehículos")
            mostrar_ranking_tipos_vehiculo()

        elif opcion == "6":
            print("→ Mostrar estadisticas")

        elif opcion == "7":
            print("→ Marcar salida de un vehiculo")

        elif opcion == "8":
            print("→ Registrar ingreso de un vehiculo")

        elif opcion == "9":
            print("→ Gestion de cocheras")

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            ejecutando = False

        else:
            print("Opción invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
