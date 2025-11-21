# fruits = ["uva", "mango", "lulo", "piña", "guayaba"]

# #esta es la forma de escrbir un archivo linea por linea en un archivo que se guarda en la carpeta de raiz, un archivo .txt
# #si se neecesita en una ubicacion especifica es click derecho en la carpeta de vsc y click en relativa path este copia la ruta y luego ingresar dentro de los () para que se guarde ahi
# with open ("fruits.txt", "w") as archivo:
#     for item in fruits: #este itera en cada linea de la variable fruits y lo escribe por cada linea
#         archivo.write(f" la fruta es: {item} \n") #\n es para hacer saldo en linea como si fuera dando enter


# with open ("fuits.txt", "r") as archivo:
#     for item in fruits:
#         print(item)

#ejemplo pedir un numero y imprimir la tabla de multiplicar


# with open (f"historia_de_usurio_semana1/tabladel{Numero}.txt", "r") as file:
#     for i in Numero:
#         print(i)

# while True:
#     try:
#         Numero = int(input("Ingresa un numero: ")) 
#         with open (f"historia_de_usurio_semana1/tabladel{Numero}.txt", "w") as file:
#                 for i in range(1, 11):
#                     file.write(f"{Numero} * {i} = {Numero*i} \n")
#         break
#     except ValueError as E:
#         print(E)
#         print("ingrese un valor correcto.")


#EJERCICIOS

# Ejercicio 1: Guardar frutas
# Solicita al usuario 5 frutas y guárdalas en frutas.txt, una por línea.

# fruits=[] #se coloca una lista que se guarde 
# with open ("frutas.txt", "w") as lista:
#     for fruits in range (5): #se itera en el rango 5 que son la veces uqe va a pedir ingresar la fruta
#         lista.write(f"Fruta= {input(f"Escribe una fruta: \n")}\n") #f para que deje ingresar el input y solicitar las frutas, las{} son para que itere el mensaje pero al momento de imprimir o guardar el archivo no se imprima nuevamente el mensaje


# Ejercicio 2: Contar líneas
# Lee un archivo de texto y muestra cuántas líneas contiene.

with open("frutas.txt", "r") as file:
    lineas = file.readlines() # Lee todas las líneas y las guarda en una lista
    numero_de_lineas = len(lineas) # Cuenta los elementos de la lista
print(f"El archivo tiene {numero_de_lineas} líneas.")

# Ejercicio 3: Buscar una palabra
# Pide una palabra y muestra todas las líneas de un archivo donde aparezca.

# Definimos el nombre del archivo con el que trabajaremos
nombre_archivo = "frutas.txt" 

# Pedimos al usuario que ingrese la palabra que desea buscar
palabra_buscada = input("Introduce la palabra que deseas buscar: ")

# Abrimos el archivo en modo lectura ('r')
with open(nombre_archivo, "r") as file:
    # Leemos todas las líneas del archivo en una lista
    lineas = file.readlines()
    
    # Iteramos sobre cada línea en la lista de líneas
    for i, linea in enumerate(lineas):
        # Eliminamos los espacios en blanco al principio y final de la línea y la convertimos a minúsculas
        # para una comparación que no distinga entre mayúsculas y minúsculas.
        # Si la palabra buscada (también en minúsculas) está contenida en la línea procesada:
        if palabra_buscada.lower() in linea.strip().lower():
            # Imprimimos la línea (usamos .strip() para eliminar el salto de línea final, si es necesario,
            # aunque readlines() generalmente conserva el salto de línea al final de cada elemento de la lista).
            print(f"Línea {i+1}: {linea.strip()}") 

# Una vez finalizado el bloque 'with', el archivo se cierra automáticamente.
