# Diccionario de traducción inglés-español
diccionario = {
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana",
    "night": "noche",
    "cat": "gato",
    "dog": "perro",
    "tree": "árbol",
    "computer": "computadora",
    "friend": "amigo"
}

# Función para traducir una palabra de inglés a español
def traducir(palabra):
    if palabra.lower() in diccionario:
        return diccionario[palabra.lower()]
    else:
        return "Palabra no encontrada en el diccionario"

# Traducir 10 palabras de inglés a español
for _ in range(10):
    palabra_ingles = input("Ingrese una palabra en inglés: ")
    palabra_traducida = traducir(palabra_ingles)
    print(f"{palabra_ingles.capitalize()} en español es: {palabra_traducida.capitalize()}")
