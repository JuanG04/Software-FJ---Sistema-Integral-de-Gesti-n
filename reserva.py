# Clase que gestiona las reservas de servicios para clientes.
from excepciones import ReservaInvalida


class Reserva:
    # Clase que representa una reserva de servicio para un cliente.

    def __init__(self, cliente, servicio, duracion):
        # Constructor de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"  # Estado inicial de la reserva

    def confirmar(self):
        # Confirma la reserva validando la duración.
        # Lanza:
        #   ReservaInvalida si la duración es menor o igual a cero

        if self.duracion <= 0:
            raise ReservaInvalida("Duración inválida")

        # Valida que la duración sea mayor a cero
        self.estado = "Confirmada"

    def cancelar(self):
        # Cancela la reserva cambiando su estado
        self.estado = "Cancelada"

    def mostrar_reserva(self):
        # Retorna una representación en texto de la reserva.
        # Retorna:
        #   str: información del cliente, servicio y estado

        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.descripcion()} | "
            f"Estado: {self.estado}"
        )