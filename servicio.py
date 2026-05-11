from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):
        return self.costo_base * horas

    def descripcion(self):
        return "Reserva de sala"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):
        return self.costo_base * dias

    def descripcion(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):

    def calcular_costo(self, sesiones=1):
        return self.costo_base * sesiones

    def descripcion(self):
        return "Asesoría especializada"