from modules.consultas import mostrar_registro_por_patente, mostrar_ranking_tipos_vehiculo, mostrarTodosLosRegistros, \
    filtrar_por_tipo_vehiculo, mostrarPorDni, ver_estacionamiento, mostrar_estadisticas, mostrar_estado_caja, \
    mostrar_gastos_por_cliente
from modules.registros import agregar_estacionado, egresar_vehiculo, registrar_movimiento


def mostrar_menu():
    """
    Muestra un menú interactivo con opciones para acceder a distintas funciones de la aplicación.
    """

    print("\n====== ESTACIONAMIENTO - CONSULTAS ======")
    print("1. Ver todos los registros")
    print("2. Filtrar por tipo de vehículo")
    print("3. Buscar por patente")
    print("4. Ver ingresos de clientes (con DNI)")
    print("5. Ver ranking de tipos de vehículos")
    print("6. Mostrar estadísticas del estacionamiento")
    print("7. Marcar salida de un vehículo")
    print("8. Registrar ingreso de un vehículo")
    print("9. Vista del estacionamiento")
    print("10. Registrar movimiento de caja")
    print("11. Ver estado de caja")
    print("12. Ver gastos por cliente")
    print("0. Salir")


def main():
    """
    Esta es la funcion principal que contiene el ciclo principal de mostrar_menu() para la seleccion de las opcione
    y tambien las llamadas a sus respectivas funcionalidades por caso.
    """

    ejecutando = True

    while ejecutando:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido. ( 0 - 9 )")
            continue

        try:
            match opcion:
                case 1:
                    print("→ Mostrar todos los registros")
                    mostrarTodosLosRegistros()
                case 2:
                    print("→ Filtrar por tipo de vehiculo")
                    filtrar_por_tipo_vehiculo()
                case 3:
                    print("→ Buscar registros por patente")
                    mostrar_registro_por_patente()
                case 4:
                    print("→ Ingresos de clientes con DNI")
                    mostrarPorDni()
                case 5:
                    print("→ Ranking sobre tipos de vehiculos")
                    mostrar_ranking_tipos_vehiculo()
                case 6:
                    print("→ Estadisticas del estacionamiento")
                    mostrar_estadisticas()
                case 7:
                    print("→ Marcar salida de un vehiculo")
                    egresar_vehiculo()
                case 8:
                    print("→ Registrar ingreso de un vehiculo")
                    agregar_estacionado()
                case 9:
                    print("→ Vista del estacionamiento")
                    ver_estacionamiento()
                case 10:
                    print("→ Registrar salida de dinero")
                    registrar_movimiento()
                case 11:
                    print("→ Ver estado de caja")
                    mostrar_estado_caja()
                case 12:
                    print("→ Ver gastos por cliente")
                    mostrar_gastos_por_cliente()
                case 0:
                    print("Saliendo del programa. ¡Hasta luego!")
                    ejecutando = False
                case _:
                    print("Opción invalida. Intente nuevamente.")
        except (FileNotFoundError, ValueError, RuntimeError) as e:
            print(str(e))
        except KeyboardInterrupt:
            print("\nInterrupción del usuario. Saliendo del programa.")
            ejecutando = False


if __name__ == "__main__":          
    main()
