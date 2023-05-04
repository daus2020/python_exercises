txt = "Hola cómo estás?"
# txt = input("Ingrese Texto: ")
letters = input("Ingrese palabra o cadena a buscar: ")

print("Opciones de búsqueda")
print(
    "1 > Palabra/cadena exacta (case sensitive), puede estar seguida de cualquier caracter ('',.!?etc.)"
)
print(
    "2 > Palabra/cadena exacta (case sensitive), puede estar seguida sólo de espacio(s) o nada"
)
print(
    "3 > Palabra/cadena con o sin acento  (case sensitive), puede estar seguida de cualquier caracter"
)
print(
    "4 > Palabra/cadena indistintamente mayúscula/minúscula (case insensitive), respetando acentos"
)
print(
    "5 > Palabra/cadena indistintamente mayúscula/minúscula (case insensitive),  con o sin acento"
)
search_option = input("Seleccione su opción de búsqueda: ")

my_split = txt.split()

first_string = "áéíóú"
second_string = "aeiou"

txt_trans = txt.maketrans(first_string, second_string)
txt_no_accents = txt.translate(txt_trans)
txt_lower_no_accents = txt_no_accents.lower()
letters_trans = letters.maketrans(first_string, second_string)
letters_no_accents = letters.translate(letters_trans)
letters_lower_no_accents = letters_no_accents.lower()

txt_lower = txt.lower()
letters_lower = letters.lower()

if (letters in txt) and (search_option == "1"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto")
elif (letters in txt) and (letters in my_split) and search_option == "2":
    print(f"La cadena '{letters}' se encuentra en el texto 53")
elif (letters_no_accents in txt_no_accents) and (search_option == "3"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto")
elif (letters_lower in txt_lower) and (search_option == "4"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto")
# elif (letters in txt_lower_no_accents) and (search_option == "5"):
elif (letters_lower_no_accents in txt_lower_no_accents) and (search_option == "5"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto")
else:
    print(f"La palabra '{letters}' no se encuentra en el texto")
