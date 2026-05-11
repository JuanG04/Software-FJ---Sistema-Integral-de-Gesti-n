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