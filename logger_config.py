# Importamos esta librería de logging para registrar diversos errores del sistema
import logging

# Configuración del archivo en el cual se guardarán los errores
logging.basicConfig(
    filename="logs.txt",
    # Solo se registrarán errores de tipo ERROR o superiores
    level=logging.ERROR,
    # Formato que tendrán los mensajes guardados en el log
    format="%(asctime)s - %(levelname)s - %(message)s"
)
