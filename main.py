diccionario = {
    "vpi": "Abreviatura de Va para ahí, usado como un OK o un Dale",
    "lol": "Puede ser usada como una abreviatura de el juego league of legends, o también como abreviatura de laughing out loud",
    "cringe": "Algo que provoca vergüenza ajena"
}
while True:
    word = input("Introduce la palabra que quieras buscar:").lower()
    if word in  diccionario.keys():
        print(diccionario[word])
    else:
        print("Esa palabra no está en el diccionario!")
