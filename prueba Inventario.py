# modulo_inventario.py
"""
Módulo central de gestión de inventario y ventas.
Incluye manejo de productos, ventas, reportes y validaciones.
"""

# ============================================================
# ESTRUCTURAS DE DATOS
# ============================================================

productos = {
    1: {"titulo": "Python 101", "autor": "Mike Dane", "categoria": "Programación", "precio": 45.0, "stock": 10},
    2: {"titulo": "Deep Learning Básico", "autor": "Ian Goodfellow", "categoria": "IA", "precio": 60.0, "stock": 7},
    3: {"titulo": "Código Limpio", "autor": "Robert C. Martin", "categoria": "Programación", "precio": 50.0, "stock": 5},
    4: {"titulo": "El Programador Pragmático", "autor": "Andrew Hunt", "categoria": "Programación", "precio": 55.0, "stock": 4},
    5: {"titulo": "Manual de Ciencia de Datos", "autor": "Jake VanderPlas", "categoria": "Datos", "precio": 70.0, "stock": 6},
}

ventas = []  
# Cada venta almacena: cliente, producto, cantidad, descuento y total final

# 🔽 Este bloque define los datos base: 5 productos precargados y la lista de ventas.


# ============================================================
# VALIDACIONES
# ============================================================

def validar_numero_positivo(valor, nombre_campo):
    if not isinstance(valor, (int, float)) or valor <= 0:
        raise ValueError(f"{nombre_campo} debe ser un número positivo.")


def validar_stock(id_producto, cantidad):
    if id_producto not in productos:
        raise ValueError("El producto no existe.")
    if productos[id_producto]["stock"] < cantidad:
        raise ValueError("Stock insuficiente.")

# 🔽 Este bloque valida datos: números positivos y stock disponible antes de vender.


# ============================================================
# GESTIÓN DE PRODUCTOS
# ============================================================

def agregar_producto(titulo, autor, categoria, precio, stock):
    validar_numero_positivo(precio, "Precio")
    validar_numero_positivo(stock, "Stock")

    nuevo_id = max(productos.keys()) + 1
    productos[nuevo_id] = {
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    return nuevo_id


def actualizar_producto(id_producto, campo, nuevo_valor):
    if id_producto not in productos:
        raise ValueError("Producto no encontrado.")

    if campo in ["precio", "stock"]:
        validar_numero_positivo(nuevo_valor, campo)

    productos[id_producto][campo] = nuevo_valor
    return True


def eliminar_producto(id_producto):
    if id_producto not in productos:
        raise ValueError("Producto no encontrado.")

    del productos[id_producto]
    return True


def listar_productos():
    return productos

# 🔽 Este bloque incluye funciones CRUD: agregar, actualizar, eliminar y listar productos.


# ============================================================
# GESTIÓN DE VENTAS
# ============================================================

def registrar_venta(cliente, id_producto, cantidad, descuento=0.0):
    validar_numero_positivo(cantidad, "Cantidad")
    validar_stock(id_producto, cantidad)

    precio = productos[id_producto]["precio"]
    subtotal = precio * cantidad
    monto_descuento = subtotal * (descuento / 100)
    total = subtotal - monto_descuento

    productos[id_producto]["stock"] -= cantidad

    venta = {
        "cliente": cliente,
        "producto": id_producto,
        "cantidad": cantidad,
        "descuento": descuento,
        "total": total
    }

    ventas.append(venta)
    return venta


def listar_ventas():
    return ventas

# 🔽 Este bloque registra una venta, actualiza stock y devuelve la información completada.


# ============================================================
# REPORTES
# ============================================================

def top_3_productos():
    conteo = {}

    for venta in ventas:
        pid = venta["producto"]
        conteo[pid] = conteo.get(pid, 0) + venta["cantidad"]

    ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    return ordenados[:3]


def ventas_por_autor():
    totales = {}

    for venta in ventas:
        pid = venta["producto"]
        autor = productos[pid]["autor"]
        totales[autor] = totales.get(autor, 0) + venta["total"]

    return totales


def calcular_ingresos():
    ingreso_bruto = sum(venta["cantidad"] * productos[venta["producto"]]["precio"] for venta in ventas)
    ingreso_neto = sum(venta["total"] for venta in ventas)
    return ingreso_bruto, ingreso_neto

# 🔽 Este bloque genera reportes: top 3 productos, ventas por autor y total de ingresos.