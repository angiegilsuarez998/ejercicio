import math
from datetime import date

def doble(n): return n * 2
def es_par(n): return n % 2 == 0
def area_circulo(r): return math.pi * r ** 2
def hoy(): return date.today().isoformat()
