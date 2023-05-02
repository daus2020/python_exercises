# Find verification digit (vd) of chilean run
# import re


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

my_input = input("Enter integer or float number: ")
if float(my_input) in range(3, 8):
    print(f"My number {my_input} is in the range {range(3, 8)}")
