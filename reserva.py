from excepciones import ReservaInvalida


class Reserva:
 """Clase que representa una reserva de servicio para un cliente."""
def __init__(self, cliente, servicio, duracion):

     """
        Inicializa una nueva reserva.
        
        Args:
            cliente: Objeto cliente que realiza la reserva
            servicio: Objeto servicio a reservar
            duracion: Duración de la reserva en unidades de tiempo
        """

self.cliente = cliente
self.servicio = servicio
self.duracion = duracion
self.estado = "Pendiente" # Estado inicial de la reserva

def confirmar(self):
    """
        Confirma la reserva después de validar que la duración sea válida.
        
        Raises:
            ReservaInvalida: Si la duración es menor o igual a cero
        """
        
if self.duracion <= 0:
      raise ReservaInvalida("Duración inválida")

# Valida que la duración sea mayor a cero

self.estado = "Confirmada"

def cancelar(self):
     """Cancela la reserva cambiando su estado a cancelada."""
self.estado = "Cancelada"

def mostrar_reserva(self):
     """
        Retorna una representación en texto de la reserva con los datos principales.
        
        Returns:
            str: Cadena formateada con cliente, servicio y estado de la reserva
        """
return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.descripcion()} | "
            f"Estado: {self.estado}"
        )