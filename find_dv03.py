# Find verification digit (vd) of chilean run
serie = '234567'
multiply_list = []

while True:
  # my_number = input("Ingrese un número entero no negativo: ")
  numbers_before_vd = input("Ingrese su run sin puntos ni dígito verificador: ")
  # preguntas:el cero es número entero? es positivo? por eso preferí 'no negativo'
  try:
    is_valid = int(numbers_before_vd)
    if is_valid < 0:
      print("Ingresó un número negativo. Intente nuevamente.")
      continue
    if len(numbers_before_vd) > 8:
      print("Ingresó un número con más de 8 dígitos. Debe tener 7 u 8. Intente nuevamente.")
      continue
    if len(numbers_before_vd) < 7:
      print("Ingresó un número con menos de 7 dígitos. Debe tener 7 u 8. Intente nuevamente.")
      continue
    break
  except ValueError:
    if numbers_before_vd[0] == "-":
      print(
        f"Ingresó {numbers_before_vd} que es negativo y no es un entero. Intente nuevamente."
      )
    else:
      print(f"Ingresó {numbers_before_vd} que no es un entero. Intente nuevamente")


# numbers_before_vd = input("Ingrese su run sin puntos ni dígito verificador: ")

rev_rut = numbers_before_vd[::-1]

print(rev_rut)

for i in range(len(rev_rut)):
  res = int(serie[i % 6]) * int(rev_rut[i])
  print(res)
  multiply_list.append(res)

total = sum(multiply_list)

apply_mod11 = total % 11
eleven_minus = 11 - apply_mod11
print(eleven_minus)

if eleven_minus == 10:
  vd = 'K'
elif eleven_minus == 11:
  vd = 0
else:
  vd = eleven_minus
  
print(f"Dígito verificador es: {vd}")
# ^[1-9]\d{6,7}$

# '18021997' # 8
# '12345678' # 5
# 20.247.667-8
# 8.919.403-2
# 22.652.004-K
# 6.740.379-7
# 23.504.156-1
# 8.713.020-7
# 20.799.809-5