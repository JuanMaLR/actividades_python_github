# import random
# # Nivel 1: Muy fácil (Repaso de variables, tipos y operaciones)
# # 1. Suma de dos números
# # Escribe una función que reciba dos números y regrese su suma.
# def suma(a, b):
#     return a + b

# print(f"1.1. Suma de dos números 5 y 7 = {suma(5, 7)}\n")

# # 2. Número par o impar
# # Escribe una función que reciba un número entero y devuelva si es par o impar.
# def par_o_impar(a):
#     return "par" if a % 2 == 0 else 'impar'

# print("1.2. Número par o impar")
# print(f"20 es {par_o_impar(20)}")
# print(f"17 es {par_o_impar(17)}\n")

# # 3. Mayor de dos números
# # Pide dos números al usuario y muestra cuál es mayor (o si son iguales).
# print("1.3. Mayor de dos números")
# a = int(input("Dame un número\n"))
# b = int(input("Dame otro número\n"))
# if (a > b): 
#     print(f"{a} es mayor")
# elif (b > a):
#     print(f"{b} es mayor")
# else:
#     print(f"{a} y {b} son iguales")

# # 4. Tipo de dato
# # Dado un valor cualquiera, imprime su tipo usando type().
# print("\n1.4. Tipo de dato")
# print(f"Tipo de 5 es {type(5)}")
# print(f"Tipo de True es {type(True)}")
# print(f"Tipo de 'hola' es {type('hola')}")
# print(f"Tipo de [1, 2, 3] es {type([1, 2, 3])}\n")

# # 5. Multiplicar los primeros 10 números
# # Usa un for para multiplicar del 1 al 10 y mostrar el resultado.
# print("1.5. Multiplicar los primeros 10 números")
# valor = 1
# for i in range(1, 11):
#     valor *= i
# print(f"El resultado de multiplicar los números del 1 al 10 es {valor}\n")

# #------------------------------------------------------------------------------------------
# # Nivel 2: Fácil con condicionales y ciclos
# # 1. Contador hacia atrás
# # Usa un while para contar del 10 al 1.
# print("2.1 Contador hacia atrás")
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
# i = 0

# # 2. Suma de números del 1 al N
# # Crea una función que reciba un número n y devuelva la suma del 1 al n.
# print("\n2.2 Suma de números del 1 al N")
# def suma_de_numeros(n):
#     val = 0
#     for i in range(1, n + 1):
#         print(i)
#         val += i
#     return val

# print(f"La suma del 1 a 6 es {suma_de_numeros(6)}\n")

# # 3. Tabla de multiplicar
# # Muestra la tabla de multiplicar del número que el usuario indique.
# print(f"2.3 Tabla de multiplicar de los primeros 10 números")
# n = int(input("Dime de qué número quieres su tabla de multiplicar?\n"))
# for i in range(1, 11):
#     print(f"{i} x {n} = {i*n}")

# # 4. Validación de edad
# # Pide una edad y muestra si la persona es menor de edad, mayor de edad o adulto mayor.
# print("\n2.4 Validación de edad")
# edad = int(input("Cuál es tu edad?\n"))
# if edad < 18:
#     print("Eres menor de edad")
# elif edad >= 18 and edad < 60:
#     print("Eres mayor de edad")
# else:
#     print("Eres adulto mayor")

# # 5. Contar vocales
# # Escribe una función que reciba una palabra y cuente cuántas vocales tiene.
# print("\n2.5 Contar vocales")
# def contar_vocales(palabra):
#     vocales = ['a', 'e', 'i', 'o', 'u']
#     num_vocales = 0
#     for letra in palabra:
#         if(letra in vocales):
#             num_vocales += 1
#     return num_vocales

# word = input("Dame una palabra\n")
# print(f"La palabra {word} tiene {contar_vocales(word)} vocales\n")

# #------------------------------------------------------------------------------------------
# # Nivel 3: Uso de lógica, operadores y ciclos anidados
# # 1. Palabra al revés
# # Crea una función que reciba un string y devuelva la palabra invertida (sin usar slicing).
# print("\n3.1 Palabra al revés")
# word = input("Dame una palabra a invertir\n")
# def invierte_palabra(palabra):
#     palabra_invertida = ''
#     for letra in range(len(palabra) - 1, -1, -1):
#         palabra_invertida += palabra[letra]
#     return palabra_invertida

# print(f"Tu palabra {word} invertida es {invierte_palabra(word)}\n")

# # 2. Número primo
# # Verifica si un número es primo usando un ciclo.
# print("\n3.2 Número primo")
# def numero_primo(numero):
#     if(numero < 1):
#         return "no es primo"
    
#     i = 1
#     while(i <= numero):
#         if(numero % i == 0):
#             if(not (numero == i or i == 1)):
#                 return 'no es primo'
#         i += 1
    
#     return 'es primo'

# num = int(input("Dame un número para verificar si es primo o no\n"))
# print(f"El numero {num} {numero_primo(num)}\n")

# # 3. Adivina el número
# # Juego donde el usuario debe adivinar un número entre 1 y 10. Usa while.
# def adivina_numero():
#     random_integer = random.randint(1, 10)
#     num = int(input("¿Cuál crees que es el número?\n"))
#     while(random_integer != num):
#         print("\nNúmero incorrecto, intenta nuevamente")
#         num = int(input("¿Cuál crees que es el número?\n"))

#     print(f"Felicidades, adivinaste el número {random_integer}")


# print("3.3 Adivina el número")
# adivina_numero()

# # 4. Contar letras y dígitos
# # Escribe una función que cuente cuántas letras y cuántos números hay en un string.
# def cuenta_letras_y_numeros(palabra):
#     letras = 0
#     numeros = 0
#     for letra in palabra:
#         try: 
#             int(letra)
#         except:
#             letras += 1
#         else:
#             numeros += 1
    
#     return (letras, numeros)


# print("3.4 Contar letras y dígitos")
# palabra = input("Dame una palabra y yo te diré cuantas letras y cuantos números tiene\n")
# letras, numeros = cuenta_letras_y_numeros(palabra)
# print(f"Tu palabra {palabra} tiene {letras} letras y {numeros} numeros\n")

# # 5. Lista de múltiplos
# # Escribe una función que devuelva una lista con los múltiplos de 3 hasta n.
# def multiplos(n):
#     mult = []
#     for i in range(0, n + 1):
#         mult.append(i * 3)

#     return mult

# print("3.5 Lista de múltiplos")
# n = int(input("Hasta qué número quieres generar múltiplos?\n"))
# print(f"Los múltiplos de 3 de 0 a {n} son {multiplos(n)}\n")

# #------------------------------------------------------------------------------------------
# # Nivel 4: Intermedio básico (uso combinado de todo lo anterior)
# # 1. Conversión de temperatura
# # Función que convierta Celsius a Fahrenheit o viceversa según parámetro.
# def convert_temp(temp_type, temp):
#     if(temp_type in ['celsius', 'fahrenheit']):
#         if(temp_type == "celsius"):
#             return (temp - 32) * 5/9
#         else:
#             return (temp * 9/5) + 32
#     else:
#         raise ValueError("Escala de temperatura indicada inválida")

# print("4.1 Conversión de temperatura")
# temp_type = input("Qué escala de temperatura quieres obtener (celsius, fahrenheit)?\n")
# temp = float(input("Dame tu temperatura a convertir\n"))
# print(f"Tu temperatura en {temp_type} es {convert_temp(temp_type, temp)}\n")

# # 2. Palíndromo
# # Escribe una función que verifique si una palabra es palíndromo.
# def palindromo(word):
#     i = len(word) - 1
#     for letra in word:
#         if(letra != word[i]):
#             return "no es palíndromo"
#         i -= 1

#     return "es palíndromo"


# print("4.2 Palíndromo")
# palabra = input("Dame una palabra o frase para verificar si es palíndromo o no\n")
# formatted_word = str.lower(palabra).replace(' ', '')
# print(f"Tu palabra {palabra} {palindromo(formatted_word)}\n")

# # 3. Días de la semana
# # Crea un menú interactivo que muestre el nombre del día según el número (1 = lunes...).
# dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
# def menu_interactivo():
#     print("Bienvenido al menu interactivo")
#     option = input('Introduce un número del 1 al 7 para obtener el día correspondiente\n')
#     try:
#         numeric_option = int(option)
#     except:
#         raise TypeError("Input provided is not numeric")
#     if numeric_option > 0 and numeric_option < 8:
#         print(f"{option} = {dias_semana[numeric_option - 1]}")
#     else:
#         print("Opción inválida")

# print("4.3 Días de la semana")
# menu_interactivo()

# 4. Serie Fibonacci
# Escribe una función que devuelva los primeros n números de Fibonacci.

# Normal
# def fibonacci_normal(n):
#     if n <= 0:
#         print("No hay Fibonacci")
#         return
#     if n == 1:
#         print(0)
    
#     if n == 2: 
#         print(0)
#         print(1)
    
#     if n > 2:
#         print(0)
#         print(1)
#         a = 0
#         b = 1
#         res = 0
#         for i in range(2, n):
#             res = a + b
#             print(res)
#             a = b
#             b = res

# List
# def fibonacci_list(n):
#     lista = []
#     if n <= 0:
#         return
#     if n == 1:
#         lista.append(0)
    
#     if n == 2: 
#         lista.append(0)
#         lista.append(1)
    
#     if n > 2:
#         lista.append(0)
#         lista.append(1)
#         a = 0
#         b = 1
#         res = 0
#         for i in range(2, n):
#             res = a + b
#             lista.append(res)
#             a = b
#             b = res

#     return lista

# Lista optimizada
# def fibonacci_list_optimized(n):
#     lista = []
#     if n <= 0:
#         return
#     if n >= 1:
#         lista.append(0)
    
#     if n >= 2: 
#         lista.append(1)
    
#     if n > 2:
#         a = 0
#         b = 1
#         res = 0
#         i = 2
#         while i < n:
#             res = a + b
#             lista.append(res)
#             a = b
#             b = res
#             i += 1

#     return lista

# Lista optimizada 2
# def fibonacci_list_optimized_2(n):
#     lista = []
#     if n <= 0:
#         return

#     a = 0
#     b = 1    

#     for num in range(n):
#         lista.append(a)
#         res = a + b
#         a = b
#         b = res

#     return lista

# Normal optimizado
# def fibonacci_normal_optimizado(n):
#     a = 0
#     b = 1    

#     for num in range(n):
#         print(a)
#         res = a + b
#         a = b
#         b = res

# Normal optimizado versión Python
def fibonacci_normal_optimizado_python(n):
    a, b = 0, 1

    for _ in range(n):
        print(a)
        a, b = b, a + b

# Rescursivo
def fibonacci_recursivo(n):
    if n <= 0:
        return
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1

    return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)

print("4.4 Serie Fibonacci")
n = int(input("Hasta qué número deseas calcular su Fibonacci?\n"))
#fibonacci_normal(n)
#print(f"Tu lista de fibonacci es: {fibonacci_list(n)}")
#print(f"Tu lista de fibonacci es: {fibonacci_list_optimized(n)}")
#print(f"Tu lista de fibonacci es: {fibonacci_list_optimized_2(n)}")
#fibonacci_normal_optimizado(n)
# Sin recursividad para encontrar toda la lista de números Fibonacci hasta n
fibonacci_normal_optimizado_python(n)
# Con recursividad para encontrar sólo el Fibonacci de n
print(f"El valor Fibonacci de {n} es {fibonacci_recursivo(n)}")

# # 5. Calculadora
# # Función que reciba dos números y una operación (+, -, *, /) y devuelva el resultado.
# def calculadora(a, b, op):
#     if(op == "+"):
#         return a + b
#     elif(op == "-"):
#         return a - b
#     elif(op == "*"):
#         return a * b
#     elif(op == "/"):
#         return a / b
#     else:
#         raise ValueError("Operador no soportado")

# print("4.5 Calculadora")
# num1 = int(input("Dame un número\n"))
# num2 = int(input("Dame otro número\n"))
# operacion = input("¿Qué operación deseas realizar? (+, -, *, /)\n")
# print(f"El resultado de {num1} {operacion} {num2} = {calculadora(num1, num2, operacion)}")