# serie = [2,3,4,5,6,7]
dni_multiply_serie = []
serie_string = '234567'
numbers_before_vd = '12345678'
# rut_no_dots_no_vd = '12345678'

rev_rut = numbers_before_vd[::-1]
aa = 0 % 6 # 0
bb = 1 % 6 # 1
cc = 2 % 6 # 2
dd = 3 % 6 # 3
ee = 4 % 6 # 5
ff = 5 % 6 # 1
gg = 6 % 6  # 0
hh = 7 % 6  # 0

print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(gg)
print(hh)
print(rev_rut)
print(type(rev_rut))
print(int(rev_rut))
print(type(int(rev_rut)))

n_loops = len(numbers_before_vd)
print(n_loops)

res = int(serie_string[0]) * int(rev_rut[0])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[1]) * int(rev_rut[1])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[2]) * int(rev_rut[2])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[3]) * int(rev_rut[3])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[4]) * int(rev_rut[4])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[5]) * int(rev_rut[5])
print(res)
dni_multiply_serie.append(res) 
res = int(serie_string[0]) * int(rev_rut[6])
print(res)
dni_multiply_serie.append(res) 
# res = int(serie_string[1]) * int(rev_rut[7])
# print(res)
# dni_multiply_serie.append(res) 
print(dni_multiply_serie)

total = sum(dni_multiply_serie)
print(total)

apply_mod11 = total % 11
print(apply_mod11)
eleven_minus = 11 - apply_mod11
print(eleven_minus)

if eleven_minus == 10:
  dv = 'k'
elif eleven_minus == 11:
  dv = 0
else:
  dv = eleven_minus
  
print(f"Dígito verificador es: {dv}")