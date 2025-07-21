## Nivel 2 – Variables y operaciones

# Ejercicio 1: Uso de variables
# Guarda el número 10 en una variable llamada a
a = 10
# Guarda el número 5 en una variable llamada b
b = 5
# Imprime la suma de a y b
print(f"1. Suma {a + b}\n")

#--------------------------------------------------------------------------------------------
# Ejercicio 2: Más operaciones con variables
# Declara dos variables con cualquier número
c = 10 
d = 6
# Muestra en pantalla la resta, multiplicación y división de esos dos números
print(f"2. Resta {c - d}")
print(f"2. Multiplicacion {c * d}")
print(f"2. Division {c / d}\n")

#--------------------------------------------------------------------------------------------
# Ejercicio 3: Área de un triángulo
# Declara dos variables: base y altura
base = 10
altura = 5
# Calcula el área de un triángulo (base * altura / 2)
area = base * altura / 2
print(f"3. Area triángulo {area}\n")

#--------------------------------------------------------------------------------------------
## Nivel 3 – Uso de input()

# Ejercicio 4: Suma interactiva
# Pide al usuario dos números con input()
print("4. Suma interactiva")
num1 = input('Introduce un número\n')
num2 = input('Introduce otro número\n')
# Imprime la suma de esos dos números
print(f"La suma de los dos números es {int(num1) + int(num2)}\n")

#--------------------------------------------------------------------------------------------
# Ejercicio 5: Calculadora de edad futura
print("5. Calculadora de edad futura")
# Pide al usuario su edad
edad = int(input("Introduce tu edad\n"))
# Muestra cuántos años tendrá dentro de 10 años
print(f"En 10 años tendrás {edad + 10}\n")

#--------------------------------------------------------------------------------------------
# Ejercicio 6: División con input
print("6. División con input")
# Pide al usuario dos números
dividendo = input("Introduce un número a dividir\n")
divisor = input("Introduce el divisor\n")
# Muestra el resultado de dividir el primero entre el segundo
print(f"El resultado de dividir tu primer número entre el segundo es {int(dividendo) / int(divisor)}\n")

#--------------------------------------------------------------------------------------------
# Desafío extra: Conversor de grados Celsius a Fahrenheit
print("Extra. Conversor de grados Celsius a Fahrenheit")
# Pide al usuario una temperatura en grados Celsius
celsius = int(input("Dame una temperatura en Celsius\n"))
# Convierte a Fahrenheit usando la fórmula: F = C * 9/5 + 32
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura en Fahrenheit {fahrenheit}\n")


