# Import the datetime module to handle sales dates
from datetime import datetime

# =====================================================================
# Data Storage: We use nested dictionaries and lists
# =====================================================================

# Main dictionary to store products by their unique ID
products_db = {
    # The product ID is the primary key
    'P001': {
        'name': 'Laptop XPS 13',         # Product name
        'brand': 'Dell',                # Brand
        'category': 'Laptops',          # Category
        'price': 999.99,                # Unit price
        'stock': 50,                    # Quantity in stock
        'warranty_months': 12           # Warranty in months
    },
    'P002': {
        'name': 'iPhone 15',
        'brand': 'Apple',
        'category': 'Smartphones',
        'price': 799.00,
        'stock': 100,
        'warranty_months': 6
    },
    'P003': {
        'name': 'Samsung QLED TV',
        'brand': 'Samsung',
        'category': 'TVs',
        'price': 1499.50,
        'stock': 30,
        'warranty_months': 24
    },
    'P004': {
        'name': 'Sony WH-1000XM5',
        'brand': 'Sony',
        'category': 'Headphones',
        'price': 399.00,
        'stock': 75,
        'warranty_months': 12
    },
    'P005': {
        'name': 'Logitech MX Master 3S',
        'brand': 'Logitech',
        'category': 'Accessories',
        'price': 99.99,
        'stock': 200,
        'warranty_months': 3
    }
}

# List to store the sales history
sales_history = []

# =====================================================================
# Inventory Management Functions (Requirement 1 & 5)
# =====================================================================

# Function to register a new product (CREATE)
def add_product(product_id, name, brand, category, price, stock, warranty):
    # Validate that the ID does not exist to avoid overwriting
    if product_id in products_db:
        return False, f"Error: El ID de producto {product_id} ya existe."
    # Validate that numerical data are positive
    if price <= 0 or stock <= 0 or warranty < 0:
        return False, "Error: El precio y el stock deben ser positivos. La garantía puede ser cero o positiva."
        
    # Create the dictionary for the new product
    products_db[product_id] = {
        'name': name,
        'brand': brand,
        'category': category,
        'price': price,
        'stock': stock,
        'warranty_months': warranty
    }
    return True, f"Producto {name} añadido exitosamente."

# Function to view all products (READ all)
def view_products():
    # Iterate over the dictionary and print the details
    print("\n--- Inventario Actual ---")
    for prod_id, details in products_db.items():
        print(f"ID: {prod_id}, Nombre: {details['name']}, Marca: {details['brand']}, Precio: ${details['price']:.2f}, Stock: {details['stock']}, Garantía: {details['warranty_months']} meses")
    print("-------------------------\n")

# Function to update an existing product (UPDATE)
def update_product(product_id, field, value):
    # Validate that the product exists
    if product_id not in products_db:
        return False, f"Error: ID de producto {product_id} no encontrado."
        
    # Validate that the field to update is valid
    if field not in products_db[product_id]:
        return False, f"Error: El campo '{field}' no se encuentra en los detalles del producto."
        
    # Validate that numerical values are valid (Requirement 4)
    if field in ['price', 'stock', 'warranty_months']:
        try:
            value = float(value) if field == 'price' else int(value)
            if value < 0:
                 return False, f"Error: {field} debe ser un valor no negativo."
        except ValueError:
             return False, f"Error: Tipo de valor inválido para {field}."

    # Update the value in the dictionary
    products_db[product_id][field] = value
    return True, f"Producto {product_id} actualizado: {field} establecido a {value}."

# Function to delete a product (DELETE)
def delete_product(product_id):
    # Validate that the product exists before deleting
    if product_id in products_db:
        del products_db[product_id] # Delete the entry from the dictionary
        return True, f"Producto {product_id} eliminado exitosamente."
    else:
        return False, f"Error: ID de producto {product_id} no encontrado."

# =====================================================================
# Sales Registration and Consultation Functions (Requirement 2 & 5)
# =====================================================================

# Lambda function to calculate the discount based on client type (Requirement 5)
# VIP gets 10%, Regular 0%, New 5%
calculate_discount_rate = lambda client_type: 0.10 if client_type == 'VIP' else (0.05 if client_type == 'New' else 0.0)

# Function to register a sale
def register_sale(client_name, client_type, product_id, quantity):
    # Validate available stock (Requirement 2 & 4)
    if product_id not in products_db:
        return False, f"Error: ID de producto {product_id} no encontrado."
        
    product = products_db[product_id]
    if product['stock'] < quantity:
        return False, f"Error: Stock insuficiente. Solo {product['stock']} unidades disponibles."
        
    # Calculate applied discount
    discount_rate = calculate_discount_rate(client_type)
    total_price = product['price'] * quantity
    discount_amount = total_price * discount_rate
    final_price = total_price - discount_amount
    
    # Update inventory automatically (Requirement 2)
    products_db[product_id]['stock'] -= quantity
    
    # Register the sale in the history
    sale_record = {
        'client': client_name,
        'client_type': client_type,
        'product_id': product_id,
        'quantity': quantity,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # Format the current date
        'discount_applied': discount_amount,
        'total_sale': final_price,
        'brand': product['brand'],
        'price_per_unit': product['price']
    }
    sales_history.append(sale_record)
    
    return True, f"Venta registrada exitosamente. Monto total: ${final_price:.2f}."

# Function to view sales history
def view_sales_history():
    print("\n--- Historial de Ventas ---")
    if not sales_history:
        print("No hay ventas registradas aún.")
        return
        
    for sale in sales_history:
        print(f"Fecha: {sale['date']}, Cliente: {sale['client']} ({sale['client_type']}), ID Producto: {sale['product_id']}, Cantidad: {sale['quantity']}, Total: ${sale['total_sale']:.2f}")
    print("---------------------------\n")

# =====================================================================
# Reports Module Functions (Requirement 3 & 5)
# =====================================================================

# Function to generate dynamic reports
def generate_reports():
    print("\n--- Reportes Dinámicos ---")
    if not sales_history:
        print("No se pueden generar reportes. No hay datos de ventas disponibles.")
        return

    # Report 1: Top 3 best-selling products
    # We use a dictionary to count sales per product
    sales_count = {}
    for sale in sales_history:
        prod_id = sale['product_id']
        sales_count[prod_id] = sales_count.get(prod_id, 0) + sale['quantity']
    
    # Sort products by quantity sold from highest to lowest and take the top 3
    sorted_sales = sorted(sales_count.items(), key=lambda item: item[1], reverse=True) # Sort by value (quantity)
    print("\nTop 3 Productos Más Vendidos:")
    for i, (prod_id, quantity) in enumerate(sorted_sales[:3]):
        # We use the products dictionary to get the name
        prod_name = products_db.get(prod_id, {}).get('name', 'Producto Desconocido')
        print(f"{i+1}. {prod_name} (ID: {prod_id}): {quantity} unidades vendidas.")

    # Report 2: Sales grouped by brand
    sales_by_brand = {}
    for sale in sales_history:
        brand = sale['brand']
        sales_by_brand[brand] = sales_by_brand.get(brand, 0) + sale['total_sale']
        
    print("\nVentas Agrupadas por Marca (Ingreso Neto):")
    for brand, total_sales in sales_by_brand.items():
        print(f"{brand}: ${total_sales:.2f}")

    # Report 3: Gross and net income calculation
    # Gross income = original price * quantity
    # Net income = total_sale (price with discount)
    total_gross_income = sum(sale['price_per_unit'] * sale['quantity'] for sale in sales_history)
    total_net_income = sum(sale['total_sale'] for sale in sales_history)
    
    print(f"\nIngreso Bruto Total: ${total_gross_income:.2f}")
    print(f"Ingreso Neto Total (después de descuentos): ${total_net_income:.2f}")
    
    # Report 4: Inventory performance report
    print("\nInforme de Rendimiento del Inventario (Niveles de Stock Actuales):")
    # Iterate over the current inventory to show the status
    for prod_id, details in products_db.items():
        print(f"{details['name']} ({details['brand']}): {details['stock']} unidades restantes.")
        
    print("---------------------------\n")

# =====================================================================
# Interactive Console Menu and Error Handling (Requirements 4, 5, 6)
# =====================================================================

# Main function that runs the menu
def main_menu():
    # Infinite loop to keep the program running until the user decides to exit
    while True:
        print("======================================================")
        print("Sistema Integral de Gestión de Inventario y Ventas")
        print("======================================================")
        print("1. Gestionar Productos")
        print("2. Registrar Nueva Venta")
        print("3. Ver Historial de Ventas")
        print("4. Generar Reportes")
        print("5. Salir")
        
        # Error input handling for the menu option (Requirement 4)
        choice = input("Ingrese su opción: ")
        
        if choice == '1':
            product_menu() # Submenu for product management
        elif choice == '2':
            handle_register_sale() # Function that handles the sale registration logic
        elif choice == '3':
            view_sales_history()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            print("Saliendo del sistema. ¡Adiós!")
            break # Exit the main loop and terminate the program
        else:
            print("Opción inválida. Por favor ingrese un número entre 1 y 5.")

# Specific submenu for product management
def product_menu():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Ver todos los productos")
        print("2. Añadir nuevo producto")
        print("3. Actualizar detalles del producto")
        print("4. Eliminar producto")
        print("5. Volver al Menú Principal")
        
        sub_choice = input("Ingrese su opción: ")
        
        if sub_choice == '1':
            view_products()
        elif sub_choice == '2':
            # Request data from the user and handle input errors
            try:
                prod_id = input("Ingrese ID del producto (ej. P006): ")
                name = input("Ingrese Nombre: ")
                brand = input("Ingrese Marca: ")
                category = input("Ingrese Categoría: ")
                price = float(input("Ingrese Precio: "))
                stock = int(input("Ingrese Stock: "))
                warranty = int(input("Ingrese Garantía (meses): "))
                success, message = add_product(prod_id, name, brand, category, price, stock, warranty)
                print(message)
            except ValueError:
                # Capture errors if the user does not enter valid numbers
                print("Entrada inválida para precio, stock o garantía. Por favor ingrese números válidos.")
        elif sub_choice == '3':
             try:
                prod_id = input("Ingrese ID del producto a actualizar: ")
                field = input("Ingrese campo a actualizar (name, brand, category, price, stock, warranty_months): ")
                value = input(f"Ingrese nuevo valor para {field}: ")
                success, message = update_product(prod_id, field, value)
                print(message)
             except Exception as e:
                 print(f"Ocurrió un error inesperado: {e}") # General exception handling
        elif sub_choice == '4':
            prod_id = input("Ingrese ID del producto a eliminar: ")
            success, message = delete_product(prod_id)
            print(message)
        elif sub_choice == '5':
            break # Return to the main menu
        else:
            print("Opción inválida.")

# Helper function to handle the complex logic of sales registration with validations
def handle_register_sale():
    try:
        # Advanced validations: Handling input errors without stopping the program (Requirement 4)
        client_name = input("Ingrese Nombre del Cliente: ")
        client_type = input("Ingrese Tipo de Cliente (Regular, VIP, New): ")
        product_id = input("Ingrese ID del Producto vendido: ")
        quantity = int(input("Ingrese Cantidad vendida: "))
        
        success, message = register_sale(client_name, client_type, product_id, quantity)
        print(message)
    except ValueError:
        print("Entrada inválida para la cantidad. Por favor ingrese un número entero válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el registro de venta: {e}")

# Main entry point of the script
if __name__ == "__main__":
    # Ensures that the program starts by running the main menu function
    main_menu()
