
#https://github.com/daveshb/riwipython/blob/main/modulo1/semana1/Taller1.md
#https://github.com/Riwi-io-Medellin/Python_Fundamentals/blob/main/02_variable_types/variable_types.md

# la f es para poder colocar variable y un print al mismo tiempo. habilita utiliza {} para colocar las variables e imprimir
# if es un si condicional 
# el "entonces" es :
# el "int" es para convertir un numero en un entero para que funcionen las condicionales
#todo input debe ser texto



# print("hola mundo")

# name = input("ingrese su nombre:")
# age = int(input("ingrese su edad:"))


# name_age = f"su nombre es {name} y su edad es {age} años" #este es tipo variable en vez de print

# print(name_age)
# print(f"su nombre es {name} su edad es {age} años")


# if age > 17 :
#     print(f"{name} es mayor de edad")

# else:
#     print(f"{name} es menor de edad")


# #condicionales
# #si es menor de 10, el color es azul
# # si es mayor que 10, el color es gris
# # si es mayor de 40, el color es negro

# value = 41

# if value < 10:
#     print(f"el color es azul")
    
# elif value >= 10 and value < 40:
#     print("el color es gris")
    
# else:
#     print("el color es negro")

# #se usa para rango que es star, stop y step (que hace salto en el conteo)
# for i in range(1,100,2): 
#     print("hola")


# entrada = ""

# while entrada != "x": #pide la x para salir del ciclo
#     print("sigue adentro")
#     entrada = input("ingrese x para salir: ")

# #hacer un contador
# iterador = 0
# while iterador < 5:
#     print("El iterador es: ", iterador)
#     # iterador += 1 #metodo mas corto, le suma el 1 y lo asigna
#     iterador = iterador + 1

# # Python permite agregar un bloque else a un while.
# # Este se ejecuta solo cuando el ciclo termina sin usar break.

# intentosPermitidos = 3 #variable para intentos de ingreso de contraseña, realmente son 
# intentos = 0

# contraseñaCorrecta = "python123"
# contraseñaUsuario = ""

# while contraseñaUsuario != contraseñaCorrecta:
#     contraseñaUsuario = input("Introduce la contraseña: ")
#     intentos += 1 #suma de uno en uno y cuando llegue a 3 quema las posibilidades
#     print(intentos)

#     if contraseñaUsuario == contraseñaCorrecta: #se iguala con la contraseña correcta para que no solo salga la erronea
#         print("contraseña correcta")
#         print("Bienvenido al programa")
#         break #se debe colocar para que no siga con el otro if.

#     if intentosPermitidos == intentos: #cuando los intentos lo igualan por la suma
#         print("intente en una hora")
#         break #se cierra el bucle de la contraseña


# else:
#     print("¡Contraseña correcta!") #ejecuta otro codigo si el while tiene un error o deja de funcionar

#FUNCION
#una funcion es un bloque de codigo reutilizable, se busca que las funciones cumplan un objetivo.
# def saludar(aqui van lo parametros que quiero en la funcion o a la variablae (lista)) #def siempre se coloca, en parentesis se puede colocar las variables
# print(f"saludar")

# x = 10
# def showmain():
#     x = 20
#     print(x)

# showmain()
# print(x)
    #se imprimen las 2 varibles de x ya que una esta dentro de la funcion y la otra esta fuera

# nums = [23, 22, 10, 100]
# animals = ["cat", "dog", "horse", "elephant"]

# def showFirstAndLast(cosas):
#     first = cosas[0] #variable que define que va a imprimir de las listas anteriores
#     last = cosas[3]
#     return first , last #lo que hace retornar las informacion que estan en la varible

# num1, num2 = showFirstAndLast(nums)
# animal1, animal2 = showFirstAndLast(animals)

# print(num1, num2) 
# print(animal1, animal2)


#funcion lambda, son funciones abreviadas, ya que no necesita una declaración return y puede aceptar múltiples argumentos, pero solo contiene una única expresión. 
# # Función que suma dos números
# suma = lambda x, y: x + y
# print(suma(5, 3))  # Salida: 8

# # Función para invertir una cadena de texto
# invertir = lambda s: s[::-1]
# print(invertir("hola"))  # Salida: aloh


# # Usar lambda con la función sorted()
# lista = [(1, 'uno'), (3, 'tres'), (2, 'dos')]
# lista_ordenada = sorted(lista, key=lambda item: item[0])
# print(lista_ordenada)  # Salida: [(1, 'uno'), (2, 'dos'), (3, 'tres')]
 #lambda Función anónima en Python que se define sin usar el def, y se utiliza para escribir pequeñas funciones en una sola línea.


#LISTAS
#se define por [] y se separan por ,
# Crear una lista
# frutas = ["manzana", "plátano", "cereza"]

# # Acceder a elementos por índice
# print(frutas[0])  # Salida: manzana

# # Añadir un elemento
# frutas.append("naranja")
# print(frutas)  # Salida: ['manzana', 'plátano', 'cereza', 'naranja']

# # Eliminar un elemento
# frutas.remove("plátano")
# print(frutas)  # Salida: ['manzana', 'cereza', 'naranja']


#METODO = funciones


# frutas = ["manzana", "plátano", "cereza"]
# frutas.append("mandarina") #se coloca el nombre de la lista y cada que se agrega un metodo es con "."
# #se hace para agregar nuevos elemenos en la lista
# print(frutas)


# Numbers = ["1", "4", "2", "3", "5", "7", "6", "8"]
# Numbers.sort() #metodo para organizar numeros
# print(Numbers)


#funcion lambda
# Una función lambda en Python es una función anónima, es decir, una función que no tiene nombre y que se usa normalmente para realizar operaciones simples y rápidas.
# Se define con la palabra clave lambda.
# Ejemplo 1: Función que suma dos números
# Con def (función normal):
# def sumar(a, b):
#     return a + b

# print(sumar(5, 3))  # Salida: 8

# Con lambda (función anónima):
# sumar = lambda a, b: a + b
# print(sumar(5, 3))  # Salida: 8

#diccionario
# colecciones de pares clave-valor que permiten almacenar y 
# acceder a datos de manera eficiente usando una clave única. 
# Se crean con llaves {} y cada par clave-valor se separa con dos puntos :,
# mientras que los pares se separan con comas. Las claves deben ser inmutables 
# (como cadenas o tuplas), mientras que los valores pueden ser de cualquier tipo de dato. 
# mi_diccionario = {
#       'nombre': 'Ana',
#       'edad': 30,
#       'ciudad': 'Madrid'
#     }

# # Acceso a los valores
# # Se accede a los valores utilizando la clave correspondiente entre corchetes. 

# print(mi_diccionario['nombre']) # Salida: Ana

# # También puedes acceder a elementos anidados, como en el 
# # siguiente ejemplo donde se accede a un elemento de una lista dentro del diccionario: 

# datos = {
#   'lenguajes': ['Python', 'Ruby'],
#   ' Tabs or Spaces': 'Tabs'
# }
# print(datos['lenguajes'][0]) # Salida: Python

# # crear diccionarios con listas y que el usuario pueda agregar los datos

# coders = [] 
# print(coders)

# amaount = int(input("Cuantos users va a agregar: "))

# while amaount != 0 : #se utiliza el while para la variabla amaount para que vuelva a iniciar el ciclo y volver a ingresar los datos del otro coder.
#     name = input("Ingresa el nombre: ")
#     lastName = input("Ingresa el apellido: ")
#     age = input("Ingresa el edad: ")
#     email = input("Ingresa el correo: ")

#     coder = { #se habre el diccionario se colocan las variables la cuales el usuario registra
#         "nombre": name,
#         "apellido": lastName,
#         "edad": age,
#         "correo": email
#     }
#     amaount -=1 #se coloca para que el ciclo while deje de preguntar despues que el usuario ingrese los datos de todos los coders que dijo que iba a ingresar inicialmente.
#     coders.append(coder) #se utiliza para agregar un elemento final a la lista
#     print(f"te faltan {amaount} usuario por ingresar") #se coloca print para que cada vez que ingrese un usuario salga las veces que le reste.


# print(coders)

