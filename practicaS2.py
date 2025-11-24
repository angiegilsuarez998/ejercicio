
# option = ""
# Inventary = []
# while option != 4:
#       print("")
#       print("MENÚ PRINCIPAL")
#       print("1.Agregar producto")
#       print("2.Mostrar inventario")
#       print("3.Calcular estadísticas")
#       print("4.Salir")
#       print("")

#       option = input("Ingresa opcion (1-4): ")

#       if option == '1':
#             amaount = int(input("Cuantos productos vas a agregar: "))
#             print("")
#         #solicitar producto
#             while amaount != 0 : 
#                 product = input("Ingrese el nombre del producto: ").strip().capitalize() #strip quita espacios #capitalize coloca primera letra en mayuscula
#                 price = float(input("enter the price of product: "))
#                 quantity = int(input("enter quantity: "))
#                 print("")
#                 print("")

#                 Compras = {  #se hace diccionario para la lista
#                          "producto" : product,
#                          "precio" : price,
#                          "cantidad" : quantity,
          
#                         }
#                 amaount -=1 #amaount se coloca para que vaya descontando de la cantidad que se ongresa a hasta llegar 0 
#                 Inventary.append(Compras) #agregar productos al final de la lista
#                 print(f"te faltan {amaount} productos por ingresar")
        
#       elif option == '2':
#               if Inventary: #se coloca para ingresar al inventrio y sacar los productos
#                      for index, item in enumerate(Inventary,1 ): #para recorrer el inventario index para recorrer y item para sacar el inventario, enumerate es para convertir el diccionario en pequeñas listas.
#                             print(f"--- Producto {index} ---")
#                             print(f"nombre: {item['producto']}")
#                             print(f"precio: {item['precio']}")
#                             print("-" * 20)
                     
#               else:
#                      print("Inventario esta vacio.")       
#                      print("")
      

#       elif option == '3':
#                 print("")
#                 print("--- CÁLCULO DE ESTADÍSTICAS ---")            
                
#                 if Inventary:
#                     # 1. Asegurarse de que el campo 'total' exista
#                    # Si la Opción 2 ya lo calcula, este paso es para seguridad.
#                    for item in Inventary:
#                        # Se recalcula el total solo si no existe o si es necesario
#                        if 'total' not in item:
#                            item['total'] = item['cantidad'] * item['precio']
                   
                   
#                    # 2. Extraer todos los valores 'total' usando
#                    # Esto crea una lista como [15.0, 40.5, 20.0, ...]
#                    totales_por_producto = [item['total'] for item in Inventary]
                   
                   
#                    # 3. Sumar todos los totales para obtener el valor total del inventario
#                    total_general_inventario = sum(totales_por_producto)
                   
                   
#                    # 4. Mostrar el resultado
#                    print(f"Número total de productos únicos en inventario: {len(Inventary)}")
#                    print("-" * 40)
#                    print(f"El VALOR TOTAL del inventario es: ${total_general_inventario:.2f}")#.2f quita decimales
#                    print("-" * 40)
                   
#                 else:
#                    print("No hay productos en el inventario para calcular estadísticas.")   


#       elif option == '4':
#                print("")
#                print("Saliendo...")      

#       else:
#               print("Digite un valor que este en el menu o valido")

# #El objetivo de la semana fue aprender a hacer listas, diccionario, a iterar y asi hacer una base de datos 


# Tarea 5 - Documentación y limpieza del código:
# Objetivo de la semana: Implementar un sistema de inventario básico usando listas de diccionarios,
# bucles while/for, y condicionales (if/elif/else). El enfoque fue la modularización del código
# en funciones para mayor legibilidad y mantenibilidad.

# Variable global para almacenar el inventario


inventario = []

def mostrar_menu():
    """Muestra el menú principal del sistema de inventario."""
    print("" + "=" * 20)
    print("      MENÚ PRINCIPAL")
    print("=" * 20)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("-" * 20)

def agregar_producto():
 
    # Se añade un bucle para permitir el ingreso de múltiples productos.
    while True:
        try:
            # Validación de entrada para asegurar que sea un número entero positivo.
            cantidad_a_agregar = int(input("¿Cuántos productos vas a agregar? (0 para cancelar): "))
            if cantidad_a_agregar < 0:
                print(" La cantidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print(" Entrada inválida. Por favor, ingresa un número entero.")
    
    # Bucle para agregar la cantidad de productos especificada
    for i in range(cantidad_a_agregar):
        print(f"Ingreso de Producto {i + 1}/{cantidad_a_agregar}")
        
        # Solicita y limpia el nombre del producto
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        
        # Bucle y validación para el precio
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print(" El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print(" Entrada inválida. Por favor, ingresa un valor numérico para el precio.")

        # Bucle y validación para la cantidad
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad < 0:
                    print(" La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print(" Entrada inválida. Por favor, ingresa un número entero para la cantidad.")

        #Almacenar como diccionario en la lista
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
        }
        inventario.append(producto)
        print(f" Producto '{nombre}' agregado al inventario.")

def mostrar_inventario():
    """
    Recorre la lista 'inventario' y muestra cada producto en un formato claro.
    Muestra un mensaje si el inventario está vacío.
    """
    # Tarea 3 - Mostrar todos los productos del inventario:
    if not inventario:
        print("Inventario vacío. No hay productos registrados.")
    else:
        print("  INVENTARIO ACTUAL")
        # Bucle for para recorrer la lista de diccionarios
        for index, item in enumerate(inventario, 1):
            # Formato de salida claro
            print(f"Producto {index}: {item['nombre']} | Precio: ${item['precio']:.2f} | Cantidad: {item['cantidad']}")
        print("-----------------------------------")


def calcular_estadisticas():
    """
    Calcula el valor total del inventario y la cantidad total de productos registrados.
    """
    # Tarea 4 - Calcular estadísticas básicas:
    if not inventario:
        print("\n No hay productos para calcular estadísticas. ---")
        return

    # Inicialización de contadores
    valor_total_inventario = 0.0
    cantidad_total_stock = 0
    
    # Bucle for para procesar cada producto
    for item in inventario:
        # Calcular el valor por producto (precio * cantidad)
        valor_por_producto = item['precio'] * item['cantidad']
        
        # Acumular el valor total del inventario
        valor_total_inventario += valor_por_producto
        
        # Acumular la cantidad total de unidades en stock
        cantidad_total_stock += item['cantidad']
        
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Productos únicos registrados: {len(inventario)}")
    print(f"Unidades totales en stock: {cantidad_total_stock}")
    print(f" Valor total del inventario: ${valor_total_inventario:.2f}")
    print("-" * 40)


def main():
    """
    Función principal que ejecuta el bucle del menú y maneja las opciones.
    """
    # Tarea 2 - Implementar un bucle para múltiples registros (bucle principal)
    # Tarea 1 - Validación de datos con condicionales
    opcion = ""
    while opcion != '4':
        mostrar_menu()
        opcion = input(" Ingresa opción (1-4): ").strip()

        if opcion == '1':
            agregar_producto()
        
        elif opcion == '2':
            mostrar_inventario()
            
        elif opcion == '3':
            calcular_estadisticas()
        
        elif opcion == '4':
            # Salida del bucle
            print("\n ¡Gracias por usar el sistema! Saliendo...")
            
        # Tarea 1 - Manejo de opción inválida
        else:
            print(f"\n Opción '{opcion}' inválida. Por favor, selecciona una opción entre 1 y 4.")

# Ejecución del programa
if __name__ == "__main__":
    main()

# Resumen de Correcciones y Mejoras

    # Modularización (Tarea 5): El código fue dividido en las funciones mostrar_menu(), agregar_producto(), mostrar_inventario(), calcular_estadisticas(), y una función principal main().

    # Comentarios (Tarea 5): Se agregaron comentarios detallados a cada función y sección del código.

    # Validación de Opciones (Tarea 1): El bloque if/elif/else dentro de main() maneja las opciones válidas e imprime un mensaje de error claro para opciones inválidas, sin salir del programa.

    # Validación de Datos (Mejora): Se añadieron bloques try-except y bucles while dentro de agregar_producto() para asegurar que precio sea un float y cantidad sea un int, además de verificar que no sean negativos.

    # Estadísticas (Tarea 4): La función calcular_estadisticas() ahora calcula y muestra el número de productos únicos (len(inventario)) y la suma total del stock (unidades en cantidad) además del valor total.