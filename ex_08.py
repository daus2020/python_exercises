txt = "Hola cómo estás."
# txt = "Hola cómo estás."
# txt = "Hola cómo estás?"
# txt = input("Ingrese Texto: ")
letters = input("Ingrese palabra o cadena a buscar: ")

print("Opciones de búsqueda")
print(
    "1 > Palabra/cadena exacta (case sensitive), puede estar seguida de cualquier caracter ('',.!?etc.)"
)
print(
    "2 > Palabra/cadena exacta (case sensitive), puede estar seguida sólo de espacio(s) o nada"
)
print("3 > Palabra/cadena con o sin acento  (case sensitive)")
print(
    "4 > Palabra/cadena indistintamente mayúscula/minúscula (case insensitive), respetando acentos"
)
print(
    "5 > Palabra/cadena indistintamente mayúscula/minúscula (case insensitive),  con o sin acento"
)
search_option = input("Seleccione su opción de búsqueda: ")
# search_type = input(
#     " 1 >Busca una palabra exacta (case sensitive), puede estar seguida de ,.!?(opción 1), 2 > palabra con o sin acento, 3 > Indistinto mayúscula minúscula, 4 > Indistinto may/min -  acento/sin acento"
# )

my_split = txt.split()
print(f"my_split 27 -> {my_split}")

first_string = "áéíóú"
second_string = "aeiou"

txt_trans = txt.maketrans(first_string, second_string)
txt_no_accents = txt.translate(txt_trans)
txt_lower_no_accents = txt_no_accents.lower()
print(f"txt_no_accents 35 -> {txt_no_accents}")
letters_trans = letters.maketrans(first_string, second_string)
letters_no_accents = letters.translate(letters_trans)
letters_lower_no_accents = letters_no_accents.lower()
print(f"letters_no_accents 31 -> {letters_no_accents}")
print(f"letters_lower_no_accents 32 -> {letters_lower_no_accents}")

txt_lower = txt.lower()
letters_lower = letters.lower()
print(f"txt_lower 44 -> {txt_lower}")
print(f"letters_lower 45 -> {letters_lower}")

print(search_option)
# if letters in my_split:
if (letters in txt) and (search_option == "1"):
    # if letters in (txt and my_split):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto 51")
elif (letters in txt) and (letters in my_split) and search_option == "2":
    print(f"La cadena '{letters}' se encuentra en el texto 53")
elif (letters_no_accents in txt_no_accents) and (search_option == "3"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto 55")
elif (letters_lower in txt_lower) and (search_option == "4"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto 57")
# elif (letters in txt_lower_no_accents) and (search_option == "5"):
elif (letters_lower_no_accents in txt_lower_no_accents) and (search_option == "5"):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto 60")
else:
    print(f"La palabra '{letters}' no se encuentra en el texto")
