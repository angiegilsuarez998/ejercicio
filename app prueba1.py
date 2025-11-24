# app.py
from modulo_inventario import (
    agregar_producto, actualizar_producto, eliminar_producto, listar_productos,
    registrar_venta, listar_ventas, top_3_productos, ventas_por_autor, calcular_ingresos
)

# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu():
    print("\n=== SISTEMA DE INVENTARIO Y VENTAS ===")
    print("1. Listar productos")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Registrar venta")
    print("6. Listar ventas")
    print("7. Reporte: Top 3 productos más vendidos")
    print("8. Reporte: Ventas por autor")
    print("9. Reporte: Ingresos del sistema")
    print("0. Salir")

# 🔽 Este bloque muestra el menú principal al usuario.


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                print("\n--- Lista de Productos ---")
                for pid, data in listar_productos().items():
                    print(pid, data)

            elif opcion == "2":
                print("\n--- Agregar Producto ---")
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))

                nuevo_id = agregar_producto(titulo, autor, categoria, precio, stock)
                print(f"Producto agregado con ID: {nuevo_id}")

            elif opcion == "3":
                print("\n--- Actualizar Producto ---")
                pid = int(input("ID del producto: "))
                campo = input("Campo a actualizar (titulo, autor, categoria, precio, stock): ")
                valor = input("Nuevo valor: ")

                if campo in ["precio", "stock"]:
                    valor = float(valor) if campo == "precio" else int(valor)

                actualizar_producto(pid, campo, valor)
                print("Producto actualizado correctamente.")

            elif opcion == "4":
                pid = int(input("ID del producto a eliminar: "))
                eliminar_producto(pid)
                print("Producto eliminado.")

            elif opcion == "5":
                print("\n--- Registrar Venta ---")
                cliente = input("Cliente: ")
                pid = int(input("ID del producto: "))
                cantidad = int(input("Cantidad: "))
                descuento = float(input("Descuento (%): "))

                venta = registrar_venta(cliente, pid, cantidad, descuento)
                print("Venta registrada:", venta)

            elif opcion == "6":
                print("\n--- Ventas Registradas ---")
                for v in listar_ventas():
                    print(v)

            elif opcion == "7":
                print("\n--- TOP 3 PRODUCTOS ---")
                print(top_3_productos())

            elif opcion == "8":
                print("\n--- VENTAS POR AUTOR ---")
                print(ventas_por_autor())

            elif opcion == "9":
                print("\n--- INGRESOS ---")
                bruto, neto = calcular_ingresos()
                print(f"Ingreso bruto: {bruto}")
                print(f"Ingreso neto: {neto}")

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print(f"Error: {e}")

# 🔽 Este bloque ejecuta todas las funciones dependiendo del número que elija el usuario.


# ============================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()

# 🔽 Este bloque permite ejecutar el programa desde la terminal.