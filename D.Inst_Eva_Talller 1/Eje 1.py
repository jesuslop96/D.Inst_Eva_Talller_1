Palabra = input("Ingrese una palabra o frase:").lower()

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for caracter in Palabra:
    if caracter in vocales:
        vocales[caracter] += 1

for vocal, conteo in vocales.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.")