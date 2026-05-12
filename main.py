import logging

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import ReservaInvalida

import logger_config


def ejecutar_operaciones():

    operaciones = []

    print("\n===== SOFTWARE FJ =====\n")

    # OPERACIÓN 1
    try:
        cliente1 = Cliente("Juan", "juan@gmail.com")
        operaciones.append(cliente1.mostrar_datos())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 2
    try:
        cliente2 = Cliente("", "correo")

    except Exception as e:
        logging.error(e)
        print("Error cliente 2:", e)

    # OPERACIÓN 3
    try:
        cliente3 = Cliente("Miguel Perez", "miguelP@gmail.com")
        operaciones.append(cliente3.mostrar_datos())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 4
    try:
        sala = ReservaSala("Sala VIP", 100)

        reserva1 = Reserva(cliente1, sala, 2)
        reserva1.confirmar()

        operaciones.append(reserva1.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 5
    try:
        equipo = AlquilerEquipo("Laptop", 50)

        reserva2 = Reserva(cliente1, equipo, -1)
        reserva2.confirmar()

    except ReservaInvalida as e:
        logging.error(e)
        print("Error reserva:", e)

    # OPERACIÓN 6
    try:
        asesoria = Asesoria("Python", 80)

        reserva3 = Reserva(cliente3, asesoria, 3)
        reserva3.confirmar()

        operaciones.append(reserva3.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 7
    try:
        cliente4 = Cliente("Pedro", "pedrogmail.com")

    except Exception as e:
        logging.error(e)
        print("Error cliente 4:", e)

    # OPERACIÓN 8
    try:
        reserva4 = Reserva(cliente1, sala, 5)
        reserva4.cancelar()

        operaciones.append(reserva4.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 9
    try:
        reserva5 = Reserva(cliente3, equipo, 1)
        reserva5.confirmar()

        operaciones.append(reserva5.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 10
    try:
        cliente5 = Cliente("Miguel Asencio", "miguelasencio@gmail.com")
        operaciones.append(cliente5.mostrar_datos())

    except Exception as e:
        logging.error(e)

    finally:
        print("\nSistema ejecutado correctamente.\n")

    return operaciones


resultado = ejecutar_operaciones()

print("===== OPERACIONES REALIZADAS =====\n")

for op in resultado:
    print(op)
    
import logging

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import ReservaInvalida

import logger_config  # Configuración del logger (se asume que inicializa logging)


def ejecutar_operaciones():
    """
    Ejecuta una serie de operaciones de ejemplo sobre clientes y reservas,
    capturando errores y registrándolos. Devuelve una lista con las
    representaciones (strings) de las operaciones realizadas exitosamente.
    """

    operaciones = []  # Lista donde se guardarán los resultados de operaciones exitosas

    print("\n===== SOFTWARE FJ =====\n")

    # OPERACIÓN 1: Crear cliente válido y mostrar sus datos
    try:
        cliente1 = Cliente("Juan", "juan@gmail.com")
        operaciones.append(cliente1.mostrar_datos())  # Añadimos la representación del cliente

    except Exception as e:
        # Si ocurre cualquier excepción al crear o mostrar el cliente, se registra el error
        logging.error(e)

    # OPERACIÓN 2: Intentar crear cliente inválido (nombre vacío, email inválido)
    try:
        cliente2 = Cliente("", "correo")

    except Exception as e:
        # Se captura la excepción específica de validación y se registra
        logging.error(e)
        print("Error cliente 2:", e)

    # OPERACIÓN 3: Crear otro cliente válido y mostrar sus datos
    try:
        cliente3 = Cliente("Miguel Perez", "miguelP@gmail.com")
        operaciones.append(cliente3.mostrar_datos())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 4: Reservar una sala y confirmar la reserva
    try:
        sala = ReservaSala("Sala VIP", 100)  # Creación de un servicio tipo sala  reserva1 = Reserva(cliente1, sala, 2)  # Reserva para cliente1 por 2 unidades (p. ej. horas)
        reserva1.confirmar()  # Confirma la reserva (cambia su estado)

        operaciones.append(reserva1.mostrar_reserva())  # Añade la info de la reserva confirmada

    except Exception as e:
        # Errores posibles: cliente1 no existe, validación de reserva, errores internos, etc.
        logging.error(e)

    # OPERACIÓN 5: Intentar alquilar un equipo con duración negativa -> excepción esperada
    try:
        equipo = AlquilerEquipo("Laptop", 50)

        reserva2 = Reserva(cliente1, equipo, -1)  # Duración inválida (-1)
        reserva2.confirmar()

    except ReservaInvalida as e:
        # Se captura la excepción específica de reserva inválida y se muestra/registran los detalles
        logging.error(e)
        print("Error reserva:", e)

    # OPERACIÓN 6: Solicitar una asesoría y confirmar la reserva
    try:
        asesoria = Asesoria("Python", 80)

        reserva3 = Reserva(cliente3, asesoria, 3)
        reserva3.confirmar()

        operaciones.append(reserva3.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 7: Intentar crear cliente con email mal formado -> se espera excepción
    try:
        cliente4 = Cliente("Pedro", "pedrogmail.com")

    except Exception as e:
        logging.error(e)
        print("Error cliente 4:", e)

    # OPERACIÓN 8: Crear y cancelar una reserva existente
    try:
        reserva4 = Reserva(cliente1, sala, 5)
        reserva4.cancelar()  # Cancela la reserva en lugar de confirmarla

        operaciones.append(reserva4.mostrar_reserva())  # Se añade la representación de la reserva cancelada

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 9: Reservar un equipo correctamente y confirmarlo
    try:
        reserva5 = Reserva(cliente3, equipo, 1)
        reserva5.confirmar()

        operaciones.append(reserva5.mostrar_reserva())

    except Exception as e:
        logging.error(e)

    # OPERACIÓN 10: Crear otro cliente válido y añadir sus datos a las operaciones
    try:
        cliente5 = Cliente("Miguel Asencio", "miguelasencio@gmail.com")
        operaciones.append(cliente5.mostrar_datos())

    except Exception as e:
        logging.error(e)

    finally:
        # Este bloque se ejecuta siempre, haya error o no en las operaciones anteriores.
        print("\nSistema ejecutado correctamente.\n")  return operaciones  # Devuelve la lista con los resultados de las operaciones exitosas


# Llamada principal: ejecuta las operaciones y las imprime por pantalla
resultado = ejecutar_operaciones()

print("===== OPERACIONES REALIZADAS =====\n")

for op in resultado:
    print(op)