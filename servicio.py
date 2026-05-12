# Definición de servicios base y servicios concretos con cálculo de costo.
from abc import ABC, abstractmethod


class Servicio(ABC):
# Clase abstracta que representa un servicio genérico.
    # Define la interfaz que deben implementar las subclases.
    def __init__(self, nombre, costo_base):
         # Constructor que inicializa el nombre del servicio y su costo base.
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        # Método abstracto para calcular el costo del servicio.
        # Las subclases deben implementar esta lógica (por ejemplo, por horas, días o sesiones).
        pass
        
    @abstractmethod
    def descripcion(self):
         # Método abstracto que debe devolver una descripción textual del servicio.
        pass


class ReservaSala(Servicio):
     # Servicio concreto para la reserva de una sala.

    def calcular_costo(self, horas=1):
        # Calcula el costo según el número de horas.
        # Parámetros:
        #   horas (int): número de horas de reserva (por defecto 1).
        # Retorna:
        #   float/int: costo total = costo_base * horas
        return self.costo_base * horas

    def descripcion(self):
        # Devuelve una breve descripción del servicio.
        return "Reserva de sala"


class AlquilerEquipo(Servicio):
     # Servicio concreto para el alquiler de equipos.

        def calcular_costo(self, dias=1):
            # Calcula el costo según el número de días.
        # Parámetros:
        #   dias (int): número de días de alquiler (por defecto 1).
        # Retorna:
        #   float/int: costo total = costo_base * dias
            return self.costo_base * dias
    
        def descripcion(self):
            # Devuelve una breve descripción del servicio.
            return "Alquiler de equipos"


class Asesoria(Servicio):
       # Servicio concreto para asesorías o consultorías.

    def calcular_costo(self, sesiones=1):
        # Calcula el costo según el número de sesiones.
        # Parámetros:
        #   sesiones (int): número de sesiones (por defecto 1).
        # Retorna:
        #   float/int: costo total = costo_base * sesiones
        return self.costo_base * sesiones

    def descripcion(self):
         # Devuelve una breve descripción del servicio.
        return "Asesoría especializada"