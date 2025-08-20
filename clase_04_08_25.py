#Contar vocales
#Escribe una función que reciba una palabra y cuente cuántas vocales tiene.
print("2.5 Contar vocales")
def contar_vocales(palabra): #amigo
    vocales = ['a', 'e', 'i', 'o', 'u']
    num_vocales = 0
    for letra in palabra:
        #letra = a
        #letra = m
        #letra = i
        if(letra in vocales):
            num_vocales += 1
    return num_vocales

palabra = input("Dame una palabra\n")
print(f"La palabra {palabra} tiene {contar_vocales(palabra)} vocales\n")

#------------------------------------------------------------------------------------------------------------------------
#Palabra al revés
#Crea una función que reciba un string y devuelva la palabra invertida (sin usar slicing).
print("3.1 Palabra al revés")
palabra = input("Dame una palabra a invertir\n")
def invierte_palabra(palabra): #casa = 4 -> ['c', 'a', 's', 'a']
                               #              0    1    2    3
    palabra_invertida = ''
    for indice in range(len(palabra) - 1, -1, -1):
        print(f"indice: {indice}")
        print(f"letra: {palabra[indice]}")
        palabra_invertida += palabra[indice] #asac
    return palabra_invertida

resultado = invierte_palabra(palabra)
print(f"Tu palabra {palabra} invertida es {resultado}")

#------------------------------------------------------------------------------------------------------------------------
#Número primo
#Verifica si un número es primo usando un ciclo.
print("3.2 Número primo")
numero = int((input("Dame un número para verificar si es primo o no\n"))) 
def numero_primo(numero): #7
    if(numero < 1):
        return "no es primo"
    
    i = 1
    while(i <= numero): #i = 1, numero = 7 -> primera vuelta
        if(numero % i == 0): #División exacta
            if(not(i == 1 or numero == i)):
                return "no es primo"
        i += 1
    return 'es primo'

print(f"El número {numero} {numero_primo(numero)}\n")

#------------------------------------------------------------------------------------------------------------------------
import random
#Adivina el número
#Juego donde el usuario debe adivinar un número entre 1 y 10. Usa while.
print("3.3 Adivina el número")
def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    num = int(input("Dame un número\n"))
    while numero_aleatorio != num:
        print("\nNúmero incorrecto, intenta otra vez")
        num = int(input("Dame un número\n"))
    print(f"Felicidades, adivinaste el número {numero_aleatorio}")

adivina_numero()

#------------------------------------------------------------------------------------------------------------------------
#Contar letras y dígitos
#Escribe una función que cuente cuántas letras y cuántos números hay en un string.
print("3.4 Contar letras y dígitos")
palabra = input("Dame una palabra y yo te diré cuantas letras y cuantos números tiene\n")
def cuenta_letras_y_numeros(palabra):
    letras, numeros = 0, 0
    for letra in palabra: #copito2569
        try:
            int(letra)
        except:
            letras += 1
        else:
            numeros += 1
    return (letras, numeros)

letras, numeros = cuenta_letras_y_numeros(palabra)
print(f"Tu palabra {palabra} tiene {letras} letras y {numeros} numeros\n")

#------------------------------------------------------------------------------------------------------------------------
#Lista de múltiplos
#Escribe una función que devuelva una lista con los múltiplos de 3 hasta n.
print("3.5 Lista de múltiplos")
n = int(input("Hasta qué número quieres generar múltiplos\n"))
def multiplos(n): 
    mult = []
    for i in range(n):
        mult.append(i * 3)
    return mult

print(f"Los múltiplos de 3, de 0 a {n} son {multiplos(n)}")

#------------------------------------------------------------------------------------------------------------------------
#Conversión de temperatura
#Función que convierta Celsius a Fahrenheit o viceversa según parámetro.
print("4.1 Conversión de temperatura")
def convertir_temperatura(temp_type, temp):
    if temp_type in ['celsius', 'fahrenheit']:
        if(temp_type == 'celsius'): #El usuario dio temperatura en fahrenheit
            return (temp - 32) * 5/9
        else: #El usuario dio la temperatura en celsius
            return (temp * 9/5) + 32
    else: 
        raise ValueError("Escala de temperatura inválida")

temp_type = input("¿Qué escala de temperatura quieres obtener? (celsius, fahrenheit)\n")
temp = float(input("Dame la temperatura a convertir\n"))
print(f"Tu temperatura en {temp_type} es {convertir_temperatura(temp_type, temp)}\n")

#------------------------------------------------------------------------------------------------------------------------
#Calculadora
#Función que reciba dos números y una operación (+, -, *, /) y devuelva el resultado.
print("4.5 Calculadora")
def calculadora(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        raise ValueError("Operador no soportado")

num1 = float(input("Dame un número\n"))
num2 = float(input("Dame otro número\n"))
operacion = input("¿Qué operación deseas? (+, -, *, /)\n")
print(f"El resultado de {num1} {operacion} {num2} = {calculadora(num1, num2, operacion)}")