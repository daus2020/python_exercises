txt = "Hola cómo estás?"
# txt = input("Ingrese Texto: ")
letters = input("Ingrese palabra o cadena a buscar: ")

search_type = input("Busca una palabra exacta NO seguida de ,.!?(opción 1), palabra con o sin acento mayúscula minúscula, o una cadena exacta le puede seguir un signos gramáticos (,.!?) (enter) o una cadena (ignora min, may, acentos)")

my_split = txt.split()

print(search_type)
# if letters in my_split:
if (letters in txt) and search_type != "1":
# if letters in (txt and my_split):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto")
elif (letters in txt) and (letters in my_split):
    print(f"La cadena '{letters}' se encuentra en el texto")
elif search_type != "1":
    print(f"La cadena '{letters}' no se encuentra en el texto")
else:
    print(f"La palabra '{letters}' no se encuentra en el texto")