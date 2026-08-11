import math

def sumar(sumando, sumando2):
    resultado = sumando + sumando2
    return resultado

def restar(minuendo, sustrayendo):
    resultado = minuendo - sustrayendo
    return resultado

def multiplicar(factor, factor2):
    resultado = factor * factor2
    return resultado

def dividir(dividendo, divisor):
    if divisor == 0:
        return "Error: División por cero"
    resultado = dividendo / divisor
    return resultado

def radicacion(radicando, indice):
    if indice == 0:
        return "Error: El índice no puede ser cero"
    resultado = radicando ** (1 / indice)
    return resultado

def potenciacion(base, exponente):
    resultado = base ** exponente
    return resultado

def logaritmacion(numero, base=10):
    if numero <= 0:
        return "Error: El número debe ser mayor que cero"
    if base <= 0 or base == 1:
        return "Error: Base inválida"
    resultado = math.log(numero, base)
    return resultado

def porcentaje(cantidad_base, tasa):
    resultado = cantidad_base * (tasa / 100)
    return resultado
