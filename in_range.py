# option 1:
def average_mark():
    print("Average Mark")
    marks = []
    while True:
        my_mark = input("Ingrese nota (1.0 a 7.0): ")
        # my_mark = float(input("Ingrese nota (1.0 a 7.0): "))
        if float(my_mark) >= 1 and float(my_mark) <= 7:
            marks.append(float(my_mark))
            add_mark = input("Desea agregar otra nota: sí (enter) - no (n)")
            if add_mark == "n":
                break
        else:
            print("Nota fuera de rango (1.0 a 7.0). Intente nuevamente.")
    average = sum(marks) / len(marks)
    print("\n================================================================")
    print("             Resumen")
    print("Notas: ", *marks, sep="  ")
    print(f"Promedio de notas: {average:.1f}")
    # print(f"Promedio de notas: {sum(marks)/len(marks):.1f}")
    if average >= 4:
        print(f"Situación: Alumno aprobado.")
    else:
        print(f"Situación: Alumno reprobado.")


# option 2:
def celcius_farenheit():
    print("Option 2")


# option 3:
def imc():
    print("Option 3")


# option 4:
def number_length():
    print("Option 4")


# option 5:
def even_numbers_between():
    print("Option 5")


# option 6:
def multiplication_table():
    print("Option 6")


# option 7:
def skip_number():
    print("Option 7")


# option 8:
def is_word_in_txt():
    print("Option 8")


# option 9:
def base_height_draw():
    print("Option 9")


# option 10:
def my_vd():
    print("Option 10")


def menu():
    print("                 \033[4mMENU\033[0m")
    print(" 1 > Promedio de notas y mensaje si aprobó o reprobó")
    print(" 2 > Grados Celcius a Farenheit")
    print(" 3 > Cálculo del imc")
    print(" 4 > Cuántos dígitos tiene el entero ingresado")
    print(
        " 5 > Dos números enteros, imprimir números entre ellos,\n     cantidad de números, cantidad pares y suma de pares "
    )
    print(" 6 > Tabla de multiplicar de número introducido")
    print(" 7 > Imprimir números del 1 al 19 saltando el ingresado")
    print(" 8 > Confirmar si cadena ingresada está en el texto")
    print(" 9 > Solicitud base y altura de rectángulo y dibujarlo")
    print("10 > Ingresar run sin puntos ni dv, imprimir dv")


def get_option():
    # not_valid = True

    while True:
        # while not_valid:
        menu()
        options = tuple(range(1, 11))
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
# options_request()

get_option()
print(my_option)
