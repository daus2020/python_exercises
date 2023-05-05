# Find verification digit (vd) of chilean run
import re


# tt = tuple(range(2,8))
# print(tt)

# serie = [2,3,4,5,6,7]
# multiply_list = []

# run_no_vd = input("Ingrese su run sin puntos ni dígito verificador: ")

# reverse input
# rev_run = reversed(run_no_vd)
# print(rev_run)
# rev_run = run_no_vd[::-1]

# for i in rev_run:
# # for i in range(len(rev_run)):
#   res = int(serie[i % 6]) * rev_run[i]
#   # res = serie[int(i) % 6] * rev_run[i]
#   # res = int(serie[i % 6]) * int(rev_run[i])
#   multiply_list.append(res)

# total = sum(multiply_list)

# apply_mod11 = total % 11
# vd = 11 - apply_mod11

# if vd == 10:
#   vd = 'K'
# elif vd == 11:
#   vd = 0

# print(f"Su dígito verificador es: {vd}")


# '18021997' # 8
# '12345678' # 5
# 20.247.667-8
# 8.919.403-2
# 22.652.004-K
# 6.740.379-7
# 23.504.156-1
# 8.713.020-7
# 20.799.809-5

# for i, value in enumerate(range(3, 8)):
#     print(f"{i} - {value}")

# my_input = input("Enter integer or float number: ")
# if float(my_input) in range(3, 8):
#     print(f"My number {my_input} is in the range {range(3, 8)}")

# my_list = ["c", "j", "w", ""]


# paises_y_capitales = {
#     "Japon": "Tokio",
#     "Inglaterra": "Londres",
#     "Francia": "Paris",
#     "Alemania": "Berlin",
# }

# # keys = paises_y_capitales.keys()
# values = paises_y_capitales.values()

# for i, value in values:
#     print(f"{paises_y_capitales[i]} - {value}")


# def mean(the_list):
#     res = sum(the_list) / len(the_list)
#     return res


# my_list = [5, 7]
# result = mean(my_list)
# print(result)
# a, b = input("Enter a two value: ").split()
# print("Value of a: ", a)
# print("Value of b: ", b)

# theory, practice = input(
#     "Ingrese nota de 'Teoría' y luego la de 'Práctica' separadas por un espacio y luego enter: "
# ).split()
# mean = (float(theory) + float(practice)) / 2
# print(mean)


# a = float(input("Enter a number: "))
# print(a)
# print(type(a))
# def foo(p1, *p2):
#     print(p1)
#     print(p2)


# def bar(p1, **p2):
#     print(p1)
#     print(p2)


# foo(1, 2, 3, 4, 5)
# bar(1, a=2, b=3)


# my_list = input(
#     "Ingrese nota de 'Teoría' y luego la de 'Práctica' separadas por un espacio y luego enter: "
# ).split()
# print(my_list)
# print(type(my_list))


# def average(string_list):
#     return sum(string_list) / len(string_list)


# my_marks = input(
#     "Ingrese nota de 'Teoría' y luego la de 'Práctica' separadas por un espacio y luego enter: "
# ).split()
# # my_marks = ["3", "4", "5"]
# # print(my_marks)
# marks = list(map(float, my_marks))
# # marks = [int(s) for s in my_marks.split(", ")]
# # print(marks)

# mean = average(marks)
# print(mean)

while True:
    my_marks = input(
        "Ingrese notas (1.0 a 7.0), separadas por un espacio y una vez ingresadas, digite enter: "
    ).split()
    print(my_marks)
    # validate marks are only digits
    if not (re.match("^[\d.]+$", "".join(my_marks))):
        # if not (re.match("^[\d ]+$", "".join(my_marks))):
        print(
            "Debe ingresar sólo números que estén en el rango de 1.0 a 7.0. Intente nuevamente."
        )
    else:
        # marks: list comprehension  alt.--> marks = list(map(float, my_marks))
        marks = [float(item) for item in my_marks]
        # Validation if marks in range and at least one mark entered.
        if all(1 <= item <= 7 for item in marks) and marks:
            break
        elif marks:
            no_valid_marks = [
                float(item) for item in my_marks if not (1 <= float(item) <= 7)
            ]
            print(no_valid_marks)
            print(
                f"Ingresó {no_valid_marks}, valor(es) que no está(n) entre 1.0 y 7.0, inclusive. Intente nuevamente."
            )
        else:
            print("Debe ingresar notas")

average = sum(marks) / len(marks)
print(average)


# if re.match("^[0-9 ]+$", myString):
#     print ("Only numbers and Spaces")
