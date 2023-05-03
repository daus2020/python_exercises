# from unidecode import unidecode
import re

txt = "María se casó con José!"
letters = input("Ingrese cadena de letras: ")

letters_in_txt = re.search(letters, txt)
print(letters_in_txt)

# uni = unidecode(letters)
# print(uni)


if letters_in_txt:
    print(f"La cadena '{letters}' está en el texto: '{txt}'")
else:
    print(f"La cadena '{letters}' no está en el texto: '{txt}'")

# my_regex = r""
#   letters = sys.argv[1]
# my_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"

# if re.search(my_regex, subject, re.IGNORECASE):
#     etc.
