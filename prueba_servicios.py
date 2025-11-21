# servicios.py
"""
Módulo con funciones CRUD y estadísticas para el inventario en memoria.
Cada producto es un diccionario: {"nombre": str, "precio": float, "cantidad": int}
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.
    Si el nombre ya existe, suma la cantidad y actualiza el precio al nuevo.
    Parámetros:
        inventario (list): lista de diccionarios
        nombre (str)
        precio (float)
        cantidad (int)
    Retorna:
        None
    """
    prod = buscar_producto(inventario, nombre)
    if prod:
        # Política: si existe, sumamos cantidad y actualizamos precio al nuevo
        prod["cantidad"] += cantidad
        prod["precio"] = precio
    else:
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)


def mostrar_inventario(inventario):
    """
    Imprime el inventario en formato legible.
    Parámetros:
        inventario (list)
    Retorna:
        None
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario ---")
    for i, p in enumerate(inventario, start=1):
        print(f"{i}. Nombre: {p['nombre']}, Precio: {p['precio']:.2f}, Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre (case-insensitive).
    Parámetros:
        inventario (list)
        nombre (str)
    Retorna:
        dict o None
    """
    nombre = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto existente.
    Parámetros:
        inventario (list)
        nombre (str)
        nuevo_precio (float|None)
        nueva_cantidad (int|None)
    Retorna:
        bool: True si se actualizó, False si no se encontró.
    """
    p = buscar_producto(inventario, nombre)
    if not p:
        return False
    if nuevo_precio is not None:
        p["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        p["cantidad"] = nueva_cantidad
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto por nombre.
    Parámetros:
        inventario (list)
        nombre (str)
    Retorna:
        bool: True si se eliminó, False si no se encontró.
    """
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario:
        - unidades_totales: suma de cantidades
        - valor_total: suma de precio * cantidad
        - producto_mas_caro: (nombre, precio)
        - producto_mayor_stock: (nombre, cantidad)
    Se usa una lambda opcional para subtotal.
    Parámetros:
        inventario (list)
    Retorna:
        dict con las métricas
    """
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": (None, 0.0),
            "producto_mayor_stock": (None, 0)
        }

    unidades_totales = sum(p["cantidad"] for p in inventario)
    # lambda para subtotal (opcional)
    subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }
