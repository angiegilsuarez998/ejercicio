
# app.py


"""
Programa principal: menú y orquestación de operaciones.
Opciones:
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
"""

from pruebaservicios import (
    agregar_producto, mostrar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, calcular_estadisticas
)
from pruebaarchivos import guardar_csv, cargar_csv

def pedir_numero(prompt, tipo=float, minimo=None, permitir_vacio=False):
    """
    Utilidad para pedir y validar números.
    tipo: float o int
    minimo: si no es None valida >= minimo
    permitir_vacio: si True, retorna None si usuario presiona Enter
    """
    while True:
        entrada = input(prompt).strip()
        if permitir_vacio and entrada == "":
            return None
        try:
            if tipo == int:
                valor = int(float(entrada))  # acepta "10.0"
            else:
                valor = tipo(entrada)
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue
        if minimo is not None and valor < minimo:
            print(f"El valor debe ser >= {minimo}.")
            continue
        return valor


def menu_principal():
    inventario = []
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione una opción (1-9): ").strip()
        if opcion not in [str(i) for i in range(1, 10)]:
            print("Opción inválida. Ingrese un número entre 1 y 9.")
            continue

        if opcion == "1":
            # Agregar
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            precio = pedir_numero("Precio: ", tipo=float, minimo=0)
            cantidad = pedir_numero("Cantidad: ", tipo=int, minimo=0)
            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado/actualizado correctamente.")

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ").strip()
            if not nombre:
                print("Nombre vacío.")
                continue
            p = buscar_producto(inventario, nombre)
            if p:
                print(f"Producto encontrado: {p}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ").strip()
            if not nombre:
                print("Nombre vacío.")
                continue
            nuevo_precio = pedir_numero("Nuevo precio (Enter para no cambiar): ", tipo=float, minimo=0, permitir_vacio=True)
            nueva_cantidad = pedir_numero("Nueva cantidad (Enter para no cambiar): ", tipo=int, minimo=0, permitir_vacio=True)
            exito = actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            if exito:
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ").strip()
            if not nombre:
                print("Nombre vacío.")
                continue
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            print("\n--- Estadísticas ---")
            print(f"Unidades totales: {stats['unidades_totales']}")
            print(f"Valor total inventario: {stats['valor_total']:.2f}")
            pmc = stats["producto_mas_caro"]
            pms = stats["producto_mayor_stock"]
            if pmc[0]:
                print(f"Producto más caro: {pmc[0]} - Precio: {pmc[1]:.2f}")
            else:
                print("Producto más caro: N/A")
            if pms[0]:
                print(f"Producto con mayor stock: {pms[0]} - Cantidad: {pms[1]}")
            else:
                print("Producto con mayor stock: N/A")

        elif opcion == "7":
            ruta = input("Ruta donde guardar CSV (ej: datos/inventario.csv): ").strip()
            if not ruta:
                print("Ruta vacía. Cancelado.")
                continue
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta del CSV a cargar (ej: datos/inventario.csv): ").strip()
            if not ruta:
                print("Ruta vacía. Cancelado.")
                continue
            productos_cargados, filas_invalidas = cargar_csv(ruta)

            if not productos_cargados and filas_invalidas == 0:
                # Esto puede indicar error en header o archivo no encontrado; cargar_csv ya informó.
                continue

            # Mostrar resumen de lo que se cargó
            print(f"Se encontraron {len(productos_cargados)} productos válidos en el archivo.")
            if filas_invalidas:
                print(f"{filas_invalidas} filas inválidas fueron omitidas durante la carga.")

            # Preguntar sobrescribir o fusionar
            while True:
                resp = input("¿Sobrescribir inventario actual? (S/N): ").strip().lower()
                if resp not in ("s", "n"):
                    print("Respuesta inválida. Ingrese 'S' o 'N'.")
                    continue
                if resp == "s":
                    inventario = productos_cargados
                    accion = "sobrescrito"
                else:
                    # Fusionar: si nombre existe -> sumar cantidad; si precio difiere -> actualizar al nuevo
                    for pc in productos_cargados:
                        existente = buscar_producto(inventario, pc["nombre"])
                        if existente:
                            existente["cantidad"] += pc["cantidad"]
                            if existente["precio"] != pc["precio"]:
                                existente["precio"] = pc["precio"]
                        else:
                            inventario.append(pc)
                    accion = "fusionado"
                break

            print(f"Inventario {accion}. Productos añadidos/actualizados: {len(productos_cargados)}. Filas inválidas: {filas_invalidas}.")

        elif opcion == "9":
            print("Saliendo. ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_principal()
