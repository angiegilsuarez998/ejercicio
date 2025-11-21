# archivos.py
"""
Módulo para persistencia en CSV:
- guardar_csv(inventario, ruta, incluir_header=True)
- cargar_csv(ruta) -> (lista_productos, filas_invalidas_count)
"""

import csv
import os

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    Formato: nombre,precio,cantidad
    Parámetros:
        inventario (list)
        ruta (str)
        incluir_header (bool)
    Retorna:
        bool: True si guardó, False si no (pero no levanta excepción).
    """
    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return False

    try:
        # Asegurar directorio existe
        dirpath = os.path.dirname(ruta)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], f"{p['precio']:.2f}", p["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
        return True
    except PermissionError:
        print("Error: permiso denegado al intentar escribir el archivo. Verifique permisos y vuelva a intentar.")
        return False
    except OSError as e:
        print(f"Error de sistema al guardar el archivo: {e}")
        return False


def cargar_csv(ruta):
    """
    Carga productos desde un CSV y valida su formato.
    Reglas:
        - Encabezado exacto (nombre,precio,cantidad) (case-insensitive, espacios tolerados)
        - Cada fila 3 columnas
        - precio -> float >= 0, cantidad -> int >= 0
    Parámetros:
        ruta (str)
    Retorna:
        (productos, filas_invalidas_count)
        productos: lista de dicts con la estructura del inventario
    Maneja FileNotFoundError y errores de decodificación y retorno de fila inválidas.
    """
    productos = []
    filas_invalidas = 0
    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",")
            try:
                header = next(reader)
            except StopIteration:
                print("El archivo está vacío.")
                return [], 0

            # Normalizar header: quitar espacios y pasar a minúsculas
            header_norm = [h.strip().lower() for h in header]
            if header_norm != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido. Se esperaba: nombre,precio,cantidad")
                return [], 0

            for i, fila in enumerate(reader, start=2):  # start=2 porque la línea 1 es el header
                # Validar número de columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                nombre_raw, precio_raw, cantidad_raw = fila
                nombre = nombre_raw.strip()
                try:
                    precio = float(precio_raw.strip())
                    cantidad = int(float(cantidad_raw.strip()))  # permite "10.0" como int
                except ValueError:
                    filas_invalidas += 1
                    continue

                if precio < 0 or cantidad < 0:
                    filas_invalidas += 1
                    continue

                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
        return productos, filas_invalidas
    except FileNotFoundError:
        print(f"Error: archivo no encontrado: {ruta}")
        return [], 0
    except UnicodeDecodeError:
        print("Error: no se pudo decodificar el archivo (posible codificación incorrecta).")
        return [], 0
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return [], 0
