palabras = ["gato", "perro", "loro", "oso", "tortuga", "leon", "tigre"]

letra = input("Introduce la letra con la que deben comenzar las palabras: ").lower()

def filtrar_palabras(palabras, letra):
    return [palabra for palabra in palabras if palabra.startswith(letra)]

resultado = filtrar_palabras(palabras, letra)
print(f"Palabras que comienzan con '{letra}':", resultado)