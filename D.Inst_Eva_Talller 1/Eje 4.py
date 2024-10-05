numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def suma_pares(numeros):
    suma = 0
    for numero in numeros:
        if numero % 2 == 0:  # Verifica si el número es par
            suma += numero
    return suma

resultado = suma_pares(numeros)
print("La suma de los números pares es:", resultado)