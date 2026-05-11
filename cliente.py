# Clase la cual representa un cliente del sistema de gestión de reservas
class Cliente:

    def __init__(self, nombre, correo):
 # El Constructor de la clase Cliente

        # Validación del nombre: este no puede estar vacío      
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

         # Validación del correo: este debe de llegar a contener '@'
        if "@" not in correo:
            raise ValueError("Correo inválido")

        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        # Retorna el nombre del cliente
        return self.__nombre

    def get_correo(self):
        # Retorna el correo del cliente
        return self.__correo

    def mostrar_datos(self):
        # Retorna los datos del cliente en un formato el cual sea legible
        return f"{self.__nombre} - {self.__correo}"
