# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## 📌 Descripción

Este proyecto consiste en el desarrollo de un sistema integral en Python orientado a objetos para la empresa **Software FJ**, el cual permite la gestión de clientes, servicios y reservas sin el uso de bases de datos.

El sistema está diseñado bajo los principios de la Programación Orientada a Objetos (POO), implementando:

- Abstracción
- Herencia
- Polimorfismo
- Encapsulación
- Manejo avanzado de excepciones
- Registro de errores mediante logs

---

## 🎯 Objetivo general

Desarrollar un sistema robusto, modular y funcional que permita gestionar clientes, servicios y reservas, garantizando estabilidad mediante el manejo de excepciones y validaciones de datos.

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Manejo de excepciones (try/except)
- Archivos de texto para logs
- Git y GitHub

---

## 🧩 Estructura del proyecto

Software FJ/
│
├── main.py
├── cliente.py
├── servicio.py
├── reserva.py
├── excepciones.py
├── logger_config.py
├── logs.txt
└── README.md

---

## 🏗️ Funcionalidades del sistema

### 👤 Gestión de clientes
- Registro de clientes
- Validación de nombre y correo electrónico
- Encapsulación de datos

### 🛎️ Gestión de servicios
- Reserva de salas
- Alquiler de equipos
- Asesorías especializadas
- Implementación de herencia y polimorfismo

### 📅 Gestión de reservas
- Creación de reservas
- Confirmación de reservas
- Cancelación de reservas
- Validación de duración y datos

### ⚠️ Manejo de errores
- Excepciones personalizadas
- Uso de try / except / else / finally
- Continuidad del sistema ante errores
- Registro de errores en logs.txt

---

## 🧪 Ejecución del proyecto

Para ejecutar el sistema, usar el siguiente comando en terminal:

```bash
python main.py