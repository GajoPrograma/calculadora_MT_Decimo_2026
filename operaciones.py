"""operaciones.py
Funciones aritméticas usadas por main.py
No borrar este archivo — implementa las operaciones que espera la calculadora.
"""

import math


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta a - b."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación a * b."""
    return a * b


def dividir(a, b):
    """Devuelve la división a / b. Si b es 0, lanza ZeroDivisionError."""
    return a / b


def potenciacion(a, b):
    """Devuelve a elevado a la b (a ** b)."""
    return a ** b


def radicacion(a, b):
    """Devuelve la raíz de grado b de a.
    Calcula a ** (1/b). Lanza ValueError si b es 0.
    """
    if b == 0:
        raise ValueError("Índice de radicación no puede ser 0")
    # Soporta raíces de números negativos cuando el índice es impar
    if a < 0 and int(b) % 2 == 1:
        return - (abs(a) ** (1.0 / b))
    return a ** (1.0 / b)


def porcentaje(a, b):
    """Interpreta b como porcentaje aplicado a a: (a * b) / 100.
    Ejemplo: porcentaje(200, 10) -> 20
    """
    return (a * b) / 100.0


def logaritmacion(a, base):
    """Devuelve el logaritmo de a en la base `base`.
    Usa math.log(a, base). Lanza ValueError para valores no válidos.
    """
    if a <= 0:
        raise ValueError("El argumento del logaritmo debe ser mayor que 0")
    if base <= 0 or base == 1:
        raise ValueError("La base del logaritmo debe ser positiva y distinta de 1")
    return math.log(a, base)
