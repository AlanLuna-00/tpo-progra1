from modules.consultas import mostrar_registro_por_patente, mostrar_ranking_tipos_vehiculo, mostrarTodosLosRegistros

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

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido. ( 0 - 10 )")
            continue

        match opcion:
            case 1:
                print("→ Mostrar todos los registros")
                mostrarTodosLosRegistros()
            case 2:
                print("→ Filtrar por tipo de vehiculo")
            case 3:
                print("→ Buscar registros por patente")
                mostrar_registro_por_patente()
            case 4:
                print("→ Ingresos de clientes con DNI")
            case 5:
                print("→ Ranking sobre tipos de vehiculos")
                mostrar_ranking_tipos_vehiculo()
            case 6:
                print("→ Mostrar estadísticas")
            case 7:
                print("→ Marcar salida de un vehiculo")
            case 8:
                print("→ Registrar ingreso de un vehiculo")
            case 9:
                print("→ Gestion de cocheras")
            case 0:
                print("Saliendo del programa. ¡Hasta luego!")
                ejecutando = False
            case _:
                print("Opción invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
