# Enunciados de ejercicios

#     Conversor de temperatura con excepciones
#     Divisor seguro con manejo de múltiples errores
#     Uso combinado de math y random
#     Fechas con datetime
#     Módulo utils_string.py con funciones de texto
#     Calculadora modular
#     Proyecto mini: Gestor de notas



import utils

def convertir_celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

try:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivale a {fahrenheit}°F")
except ValueError:
    print("Error: Debe ingresar un número válido.")
