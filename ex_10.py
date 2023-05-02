import re

# serie = (2,3,4,5,6,7)  # alts: tuple(range(2,8)) | [2,3,4,5,6,7] | list(range(2,8))
sum_product = 0

while True:  # validate run input
    run_no_vd = input("Ingrese su run sin puntos ni dígito verificador: ")
    # regex input with 2 to 8 digits, no dots, no start with 0
    if re.match("^[1-9]\d{1,7}$", run_no_vd):
        break
    else:
        print("Ingrese run válido, de 2 a 8 dígitos. No puede empezar con 0")

# alt: rev_run = run_no_vd[::-1]   class str
rev_run = reversed(run_no_vd)  # class reverse, is iterable
print(rev_run)
for i, value in enumerate(rev_run):  # Obs: value is a string
    sum_product += ((i % 6) + 2) * int(value)
    # alt with serie --> sum_product += serie[i % 6] * int(value)

vd = 11 - (sum_product % 11)

if vd == 10:
    vd = "K"
elif vd == 11:
    vd = 0

print(f"Su dígito verificador es: {vd}")

# For testing purposes
# '18021997' vd= 8
# '12345678' vd= 5
# 20.247.667-8
# 8.919.403-2
# 22.652.004-K
# 6.740.379-7
# 23.504.156-1
# 8.713.020-7
# 20.799.809-5
