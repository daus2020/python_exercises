import re  # for validate run input (exercise 10)

# from rich.console import Console
# console = Console()


# option 1:
def average_mark():
    # Sol. alt. 1
    # print("Promedio de dos notas")
    # theory, practice = input(
    #     "Ingrese nota de 'Teoría' y luego la de 'Práctica' separadas por un espacio y luego enter: "
    # ).split()
    # average = (float(theory) + float(practice)) / 2

    # Sol. alt.2 accept more marks
    while True:
        my_marks = input(
            "Ingrese notas (1.0 a 7.0), separadas por un espacio y luego enter: "
        ).split()
        if my_marks 

    # list comprehension    alt. --> marks = list(map(float, my_marks))
    marks = [float(item) for item in my_marks]
    average = sum(marks) / len(marks)

    # Sol. alt. 3 accept more marks & incl. validation
    # marks = []
    # while True:
    #     # my_mark = input("Ingrese nota (1.0 a 7.0): ")
    #     my_mark = float(input("Ingrese nota (1.0 a 7.0): "))
    #     if (my_mark >= 1) and (my_mark <= 7):
    #         # alt if (my_mark >= 1) and (my_mark <= 7):
    #         marks.append(float(my_mark))
    #         add_mark = input("Desea agregar otra nota: sí (enter) - no (n)")
    #         if add_mark == "n":
    #             break
    #     else:
    #         print("Nota fuera de rango (1.0 a 7.0). Intente nuevamente.")
    # average = sum(marks) / len(marks)
    # print("Notas: ", *marks, sep="  ")
    print("\n===========================")
    print("           Resumen")
    print(f"Promedio de notas: {average:.1f}")
    # print(f"Promedio de notas: {sum(marks)/len(marks):.1f}")
    if average >= 4:
        print(f"Situación: Alumno aprobado.")
    else:
        print(f"Situación: Alumno reprobado.")
    print("\n")


# option 2:
def celcius_farenheit():
    celcius = input("Ingrese temperatura en grados Celcius (°C): ")
    farenheit = float(celcius) * 1.8 + 32
    print(
        f"{celcius} grados Celcius (°C) equivalen a {farenheit} grados Fahrenheit (°F)"
    )
    print("\n")


# option 3:
def imc():
    my_kg = float(input("Ingrese su peso en kilogramos: "))
    my_height = float(input("Ingrese su altura en metros: "))
    imc = my_kg / (my_height**2)
    print(f"Su índice de masa corporal (imc) es de: {round(imc,2)}")
    print("\n")


# option 4:
def number_length():
    my_number = input("Ingrese un número: ")
    print(f"El número {my_number} tiene {len(my_number)} dígitos.")
    print("\n")


# option 5:
def even_numbers_between():
    num_a = int(input("Ingrese primer número entero: "))
    num_b = int(input("Ingrese segundo número entero: "))

    between_qty = abs(num_a - num_b) - 1

    if between_qty < 1:  # could be 0 or -1
        print(f"Entre {num_a} y {num_b} no hay números.")
    else:
        mini = min(num_a, num_b)
        maxi = max(num_a, num_b)

        count_even_between, sum_even_between = 0, 0

        for item in range(mini + 1, maxi):
            print(item)
            if item % 2 == 0:  # alt --> if not(i % 2):
                sum_even_between += item
                count_even_between += 1

        print(
            f"Entre {mini} y {maxi} hay {maxi - mini -1} números, siendo {count_even_between} de ellos pares."
        )
        print(f"La suma de los pares es de {sum_even_between}.")
        print("\n")


# option 6:
def multiplication_table():
    times_table = input("Ingrese un número para obtener su tabla de multiplicación: ")
    print(f"\033[4mTabla de multiplicación de {times_table}\033[0m")
    for i in range(1, 11):
        print(f"        {i} x {times_table} = {int(i) * int(times_table)}")

    print("\n")


# option 7:
def skip_number():
    num_1to19 = input("Dame un numero del 1 al 19 ==> ")
    for item in range(1, 20):
        if item == int(num_1to19):
            continue
        print(f"{item}-- ", end="")
    print("", end="\n")
    print("Terminé")
    print("\n")


# option 8:
def is_word_in_txt():
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
    print("\n")


# option 9:
def base_height_draw():
    altura = input("Ingrese altura del rectángulo: ")
    base = input("Ingrese base del rectángulo: ")

    for x in range(int(altura)):
        for y in range(int(base)):
            print("*", end="")
        print("")
    print("Fin de programa")
    print("\n")


# option 10:
def my_vd():
    sum_product = 0

    while True:  # validate run input
        run_no_vd = input("Ingrese su run sin puntos ni dígito verificador: ")
        # regex input with 2 to 8 digits, no dots, no start with 0
        if re.match("^[1-9]\d{1,7}$", run_no_vd):
            break
        else:
            print("Ingrese run válido, de 2 a 8 dígitos. No puede empezar con 0")

    rev_run = reversed(run_no_vd)
    for i, value in enumerate(rev_run):
        sum_product += ((i % 6) + 2) * int(value)

    vd = 11 - (sum_product % 11)

    if vd == 10:
        vd = "K"
    elif vd == 11:
        vd = 0

    print(f"Su dígito verificador es: {vd}")
    print("\n")


def menu():
    print("                         \033[4mMENU\033[0m")
    print("  1 > Promedio de notas y mensaje si aprobó o reprobó")
    print("  2 > Grados Celcius a Farenheit")
    print("  3 > Cálculo del imc")
    print("  4 > Cuántos dígitos tiene el entero ingresado")
    print(
        "  5 > Dos números enteros, imprimir números entre ellos,\n      cantidad de números, cantidad pares y suma de pares "
    )
    print("  6 > Tabla de multiplicar de número introducido")
    print("  7 > Imprimir números del 1 al 19 saltando el ingresado")
    print("  8 > Confirmar si cadena ingresada está en el texto")
    print("  9 > Solicitud base y altura de rectángulo y dibujarlo")
    print(" 10 > Ingresar run sin puntos ni dv, imprimir dv")
    print(" 11 > Salir")


def get_option():
    while True:
        menu()
        options = tuple(range(1, 12))
        my_option = int(input("Ingrese una opción del 1 al 10: "))

        if my_option in options:
            break
        else:
            print("Opción ingresada no válida (1 al 10). Intente nuevamente")

    return my_option


while True:
    option = get_option()
    print("\n")
    match option:
        case 1:
            average_mark()
        case 2:
            celcius_farenheit()
        case 3:
            imc()
        case 4:
            number_length()
        case 5:
            even_numbers_between()
        case 6:
            multiplication_table()
        case 7:
            skip_number()
        case 8:
            is_word_in_txt()
        case 9:
            base_height_draw()
        case 10:
            my_vd()
        case 11:
            exit()
