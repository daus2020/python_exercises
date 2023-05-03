txt = "Hola cómo estás"
# txt = "Hola cómo estás."
# txt = "Hola cómo estás?"
# txt = input("Ingrese Texto: ")
letters = input("Ingrese palabra o cadena a buscar: ")

search_type = input(
    " 1 >Busca una palabra exacta (case sensitive), puede estar seguida de ,.!?(opción 1), 2 > palabra con o sin acento, 3 > Indistinto mayúscula minúscula, 4 > Indistinto may/min -  acento/sin acento"
)

my_split = txt.split()
print(my_split)

# no_accents =

print(search_type)
# if letters in my_split:
if (letters in txt) and search_type != "1":
    # if letters in (txt and my_split):
    print(f"La cadena/palabra '{letters}' se encuentra en el texto 17")
elif (letters in txt) and (letters in my_split):
    print(f"La cadena '{letters}' se encuentra en el texto 19")
elif search_type != "1":
    print(f"La cadena '{letters}' no se encuentra en el texto 21")
else:
    print(f"La palabra '{letters}' no se encuentra en el texto 23")
