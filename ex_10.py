import re

serie = (2,3,4,5,6,7)  # alts: tuple(range(2,8)) | [2,3,4,5,6,7] | list(range(2,8))
total_sum = 0

while True:  # validate run input
  run_no_vd = input("Ingrese su run sin puntos ni dígito verificador: ")
  # regex input with 2 to 8 digits, no dots, no start with 0
  if re.match("^[1-9]\d{1,7}$", run_no_vd):
    break
  else:
    print("Ingrese run válido, de 2 a 8 dígitos. No debe empezar con 0")

# alt: rev_run = run_no_vd[::-1]
rev_run = reversed(run_no_vd)
print(rev_run)
for i, value in enumerate(rev_run):  # value is a string
  total_sum += serie[i % 6] * int(value)

vd = 11 - (total_sum % 11)

if vd == 10:
  vd = 'K'
elif vd == 11:
  vd = 0
  
print(f"Su dígito verificador es: {vd}")


# '18021997' # 8
# '12345678' # 5
# 20.247.667-8
# 8.919.403-2
# 22.652.004-K
# 6.740.379-7
# 23.504.156-1
# 8.713.020-7
# 20.799.809-5