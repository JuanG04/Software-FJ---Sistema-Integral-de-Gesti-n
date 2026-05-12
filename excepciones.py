# Esta excepción se llega a usar cuando un servicio no llega a estar disponible
class ServicioNoDisponible(Exception):
    pass


# Esta excepción aparece cuando una reserva tiene datos los cuales son incorrectos
class ReservaInvalida(Exception):
    pass
